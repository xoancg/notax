from config.settings import *
from peewee import *

# Inicialización de la base de datos con activación expresa de claves foráneas (desactivadas por defecto en SQLite)
try:
    db = SqliteDatabase(DB_NAME, pragmas=DB_PRAGMAS)
    logging.info(msg=f'[OK] Fuck yeah! Database path: {DB_NAME}')
except Exception as e:
    logging.error(msg=f'[!] Database connection error! > {e}')


# DEFINICIÓN DE CLASES
class BaseModel(Model):
    """Base modelo según las buenas prácticas de Peewee. http://docs.peewee-orm.com/en/latest/peewee/models.html
    Las subclases de BaseModel heredarán la conexión a la base de datos"""

    class Meta:
        """Especificación del nombre de la base de datos mediante la variable database"""
        database = db


class Notebook(BaseModel):
    """Modelo de Libreta"""
    name = CharField(unique=True, max_length=120, null=False, index=True)  # PK

    class Meta:
        """Especificación del nombre de la tabla en la base de datos mediante la variable db_table"""
        db_table = 'notebooks'


class Tag(BaseModel):
    """Modelo de Etiqueta"""
    name = CharField(unique=True, max_length=120, null=False, index=True)  # PK

    class Meta:
        """Especificación del nombre de la tabla en la base de datos mediante la variable db_table"""
        db_table = 'tags'


class Note(BaseModel):
    """Modelo de Nota"""
    title = CharField(unique=True, max_length=120, null=False, index=True)  # PK
    notebook = ForeignKeyField(Notebook, backref='notes', on_delete='CASCADE', on_update='CASCADE')
    content = CharField(max_length=500, null=True)
    created_date = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    tags = ManyToManyField(Tag, backref='notes', on_delete='CASCADE', on_update='CASCADE')

    # https://docs.peewee-orm.com/en/latest/peewee/relationships.html#manytomanyfield

    # La configuración que permite "limpiar" la base de datos de libretas y etiquetas que no estén en uso:
    # Se utiliza on_delete='CASCADE' para eliminar las dependencias de los objetos creados en cascada (notebook, tag)
    # Se utiliza on_update='CASCADE' para actualizar las dependencias de los objetos en cascada (notebook, tag)

    # El atributo backref se expone como una consulta Select prefiltrada (es una referencia implícita)
    # http://docs.peewee-orm.com/en/latest/peewee/relationships.html

    class Meta:
        """Especificación del nombre de la tabla en la base de datos mediante la variable db_table"""
        db_table = 'notes'


# Tabla relación Note-Tag - # https://docs.peewee-orm.com/en/latest/peewee/relationships.html#manytomanyfield
NoteTag = Note.tags.get_through_model()


# Otra forma de representar Many-To-Many
# class NoteTag(Model):
#     """Modelo de Nota - Tag"""
#     note = ForeignKeyField(Note)
#     tag = ForeignKeyField(Tag)
#
#     class Meta:
#         """Especificación de una tabla con índice (PK) multi-columna con note/tag y del nombre de la tabla"""
#         db_table = 'note-tag'


# Hay varias formas de crear la relación muchos-a-muchos
# https://github.com/xoancg/bdpython_codigofacilito/blob/main/02-peewee/13-peewee_relacion_muchos_muchos.py
# https://docs.peewee-orm.com/en/latest/peewee/relationships.html#implementing-many-to-many


# Consultas Notebook
# notebooks = Notebook.select(Notebook.notebook).group_by(Notebook.idNotebook)
# notebooks = Notebook.select(Notebook.notebook).group_by(Notebook.idNotebook)
# notebook_default = Notebook.select(Notebook.notebook).where(Notebook.idNotebook == 1)
# notebook_default = Notebook.select(Notebook.notebook).group_by(Notebook.idNotebook)

# Consultas Note
# notes = Note.select(Note.idNotebook, Note.idNote, Note.title, Note.content).order_by(Note.idNotebook)
# notes = Note.select(Note.idNote, Note.title, Note.content, Note.idNotebook).order_by(Note.idNote)
# notes = Note.select(Note.idNote, Note.title, Note.content).join(NoteTag) # Devuelve todas las notas que tengan tag
# notes = Note.select(Note.notebook, Note.title, Note.content, Note.content).join(Notebook).order_by(Notebook.notebook)

# notes_tag = Note.select(Note.title, Note.content, Note.tag)\
#     .join(NoteTag).order_by(Note.title)

# Esta consulta devuelve todos ok por print
# for row in query_notes().dicts():
#     print(row)
# print('')
# for row in notes_tag.dicts():
#     print(row)

# for row in Note.select(Notebook.notebook, Note.title, Note.content)\
#         .join(Notebook).dicts():
#     print(row)

# Consultas Tag
# tags = Tag.select(Tag.tag)

def get_notes():
    """
    Método que devuelve todas las notas existentes en la base de datos
    :return notes: Devuelve todas las notas existentes en la base de datos
    """
    notes = Note.select(Note.notebook, Note.title, Note.content).join(Notebook).order_by(Notebook.name)
    return notes


def get_note_tags(note_name):
    """
    Coger etiquetas correspondientes a una nota
    :param note_name: Nombre de la nota (PK)
    :return: Etiquetas de una nota
    """
    note = Note.select().where(Note.title == note_name).get()
    tags = note.tags.execute()
    tags_list = ""
    for t in tags:
        tags_list += t.name + ","
    return tags_list


def delete_tag(tag_name):
    """
    Eliminar etiqueta
    :param tag_name: Nombre de la etiqueta (PK)
    """
    tag = Tag.select().where(Tag.name == tag_name).get()
    tag.delete_instance()


def save_notebook(notebook_name):
    """
    Guarda una libreta nueva no existente
    :param notebook_name: Nombre de la libreta a la que pertenece
    :return: Notebook creada
    """
    (Notebook.insert(name=notebook_name)
     .on_conflict(conflict_target=Notebook.name, update={Notebook.name: notebook_name}).execute())
    notebook = Notebook.select().where(Notebook.name == notebook_name).get()
    return notebook


def save_note(notebook_name, title, content):
    """
    Guarda una nota en la base de datos o la actualiza en caso de que ya exista
    :param notebook_name: Nombre de la libreta a la que pertenece
    :param title: Título de la nota
    :param content: Contenido de la nota
    :return: Nota creada / actualizada
    """
    # Coger el objeto de la notebook a la que pertenece la nota
    notebook = Notebook.select().where(Notebook.name == notebook_name).get()
    # Realizamos un 'insert' ya que equivale a un 'upsert', es decir, insert or update
    (Note
     .insert(title=title, notebook=notebook.id, content=content)
     .on_conflict(
        conflict_target=Note.title,
        update={Note.content: content,
                Note.notebook: notebook.id})
     .execute())
    note = Note.select().where(Note.title == title).get()
    return note


def save_tag(name):
    """
    Guarda una etiqueta en la base de datos
    :param name: Tag name
    :return: Tag creada / actualizada
    """
    # Realizamos un 'insert' ya que equivale a un 'upsert', es decir, insert or update
    (Tag.insert(name=name).on_conflict(conflict_target=Tag.name, update={Tag.name: name}).execute())
    tag = Tag.select().where(Tag.name == name).get()
    return tag


def add_tag_note(note, tag):
    """
    Añade una etiqueta a una nota
    :param note: Nota a la que añadir la etiqueta
    :param tag: Etiqueta a añadir
    """
    note.tags.add([tag])


def delete_note(
        note_name):  # Se eliminan también las etiquetas y la libreta asociadas: eliminación en cascada
    """
    Borra una nota de la base de datos
    :param note_name: Nota a eliminar (se elimina por nombre ya que es su clave primaria)
    """
    note = Note.get(Note.title == note_name).get()
    note.delete_instance()


# Inicio de la base de datos
def init_model():
    try:
        db.connect()
        db.create_tables([Notebook, Note, Tag, NoteTag])
        logging.info(msg=f'[OK] Database connection is working')
    except Exception as ex:
        logging.error(msg=f'[!] Database connection error! > {ex}')

    # Crear valores por defecto
    # Descomentar cuando se inicia la base de datos desde 0: noteboook1, notebook2, notebook3
    # notebook1 = Notebook.create(name='Notebook #1')
    # notebook1.save()
    # notebook2 = Notebook.create(name='Notebook #2')
    # notebook2.save()
    # notebook3 = Notebook.create(name='Notebook #3')
    # notebook3.save()
    #
    # Debug
    # tag1 = Tag.create(name='Etiqueta #1')
    # tag1.save()
    #
    # note1 = Note.create(notebook=notebook1.id, title="Título de la nota #1", content="Contenido de la nota #1")
    # note1.tags.add([tag1])
    # note1.save()


# Inicio del modelo desde el controlador
if __name__ == "__main__":
    init_model()
