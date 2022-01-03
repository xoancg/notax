import peewee

from config.settings import *
from peewee import *

# Instanciación de la base de datos con activación expresa de claves foráneas (desactivadas por defecto en SQLite)
try:
    db = SqliteDatabase(DB_NAME, pragmas=DB_PRAGMAS)
    logging.info(msg=f'[OK] Fuck yeah! Database path: {DB_NAME}')
except Exception as e:
    logging.error(msg=f'[!] Database connection error! > {e}')


# DEFINICIÓN DE CLASES
class BaseModel(peewee.Model):
    """Base modelo según las buenas prácticas de Peewee. http://docs.peewee-orm.com/en/latest/peewee/models.html
    Las subclases de BaseModel heredarán la conexión a la base de datos"""

    class Meta:
        """Especificación del nombre de la base de datos mediante la variable database"""
        database = db


class Notebook(BaseModel):
    """Modelo de Libreta"""
    # idNotebook = AutoField(unique=True)
    notebook = CharField(max_length=120)

    class Meta:
        """Especificación del nombre de la tabla en la base de datos mediante la variable db_table"""
        db_table = 'notebooks'


class Tag(BaseModel):
    """Modelo de Etiqueta"""
    # idTag = AutoField(unique=True)
    tag = CharField(unique=True, max_length=120)

    class Meta:
        """Especificación del nombre de la tabla en la base de datos mediante la variable db_table"""
        db_table = 'tags'


class Note(BaseModel):
    """Modelo de Nota"""
    # idNotebook = ForeignKeyField(Notebook)
    # idNote = AutoField(unique=True)
    notebook = ForeignKeyField(Notebook)
    title = CharField(max_length=120, null=False)
    content = CharField(max_length=500, null=True)
    tag = ManyToManyField(Tag)  # https://docs.peewee-orm.com/en/latest/peewee/relationships.html#manytomanyfield

    # tag = ManyToManyField(Tag, backref='notes')
    # El atributo backref se expone como una consulta Select prefiltrada (es una referencia implícita)
    # http://docs.peewee-orm.com/en/latest/peewee/relationships.html

    class Meta:
        """Especificación del nombre de la tabla en la base de datos mediante la variable db_table"""
        db_table = 'notes'


# Tabla relación Note-Tag - # https://docs.peewee-orm.com/en/latest/peewee/relationships.html#manytomanyfield
NoteTag = Note.tag.get_through_model()
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

# Listado de Query
def query_notes():
    notes = Note.select(Note.notebook, Note.title, Note.content, Note.content) \
        .join(Notebook).order_by(Notebook.notebook)
    return notes


def save_notes(notebook, title, labels, content):
    # notes = Note.save(Note.notebook, Note.title, Note.content, Note.content)
    pass



#
#
# for row in query_notes().dicts():
#     print(row)


# Inicio de la base de datos
def init_model():
    try:
        db.connect()
        db.create_tables([Notebook,
                          Note,
                          Tag]
                         )
        logging.info(msg=f'[OK] Database connection is working')
    except Exception as e:
        logging.error(msg=f'[!] Database connection error! > {e}')

    # Debug
    # Crea la libreta por defecto
    # notebook1 = Notebook.create(notebook='default name1')
    # notebook2 = Notebook.create(notebook='default name2')
    # note1 = Note.create(notebook_id=1, title="Title1", content="Contenido de la nota1")
    # note1 = Note.create(notebook_id=2, title="Title2", content="Contenido de la nota2")
    # tag1 = Tag.create(tag='etiqueta1')
    # tag2 = Tag.create(tag='etiqueta2')
    # notetag1 = NoteTag.create(note_id=1, tag_id=1)  # No funciona
    # notetag2 = NoteTag.create(note_id=2, tag_id=2)  # No funciona

    # DELETE
    # delete = Notebook.delete().where(Notebook.notebook == 'default name1')
    # delete.execute()


# Inicio del modelo desde el controlador
if __name__ == "__main__":
    init_model()
