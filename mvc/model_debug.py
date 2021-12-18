from peewee import *

# Instanciación de la base de datos con activación expresa de claves foráneas (desactivadas por defecto en SQLite)
try:
    db = SqliteDatabase("debug.db", pragmas={'foreign_keys': 1, 'permanent': True})
    # logging.info(msg=f'[OK] Fuck yeah! Database path: {DB_NAME}')
except Exception as e:
    # logging.error(msg=f'[!] Database connection error! > {e}')
    pass


# DEFINICIÓN DE CLASES
class BaseModel(Model):
    """Base modelo según las buenas prácticas de Peewee. http://docs.peewee-orm.com/en/latest/peewee/models.html
    Las subclases de BaseModel heredarán la conexión a la base de datos"""

    class Meta:
        database = db


class Notebook(BaseModel):
    idNotebook = AutoField(unique=True)
    name = CharField(max_length=120, null=False)


class Tag(BaseModel):
    idTag = AutoField(unique=True)
    name = CharField(max_length=120)


class Note(BaseModel):
    idNotebook = ForeignKeyField(Notebook)
    idNote = AutoField(unique=True)
    title = CharField(max_length=120, null=False)
    content = CharField(max_length=500, null=True)
    tags = ManyToManyField(Tag, backref='notetags')
    # El atributo backref se expone como una consulta Select prefiltrada (es referencia posterior implícita)
    # http://docs.peewee-orm.com/en/latest/peewee/relationships.html


NoteTag = Note.tags.get_through_model()

try:
    db.connect()
    db.create_tables([Notebook,
                      Note,
                      Tag,
                      NoteTag]
                     )
    # logging.info(msg=f'[OK] Database connection is working')
except Exception as e:
    # logging.error(msg=f'[!] Database connection error! > {e}')
    pass


# Listado de Query
class Modelo:
    """Clase Modelo (MVC). Definición de las consultas a la base de datos"""

    # Consultas Notebook
    notebooks = Notebook.select(Notebook.idNotebook, Notebook.name).group_by(Notebook.idNotebook)
    # notebooks = Notebook.select(Notebook.name).group_by(Notebook.idNotebook)
    notebook_default = Notebook.select(Notebook.name).where(Notebook.idNotebook == 1)
    # notebook_default = Notebook.select(Notebook.name).group_by(Notebook.idNotebook)

    # Consultas Note
    # notes = Note.select(Note.idNotebook, Note.idNote, Note.title, Note.content).order_by(Note.idNotebook)
    # notes = Note.select(Note.idNote, Note.title, Note.content, Note.idNotebook).order_by(Note.idNote)
    # notes = Note.select(Note.idNote, Note.title, Note.content).join(NoteTag) # Devuelve todas las notas que tengan tag
    notes = Note.select(Note.idNote, Note.title, Note.content, Note.tags).join(Notebook)

    # Consultas Tag
    tags = Tag.select(Tag.name)


# Inicio de la base de datos
def init_model():
    pass

    # Debug
    # Crea la libreta por defecto
    # notebook1 = Notebook.create(name='default name1')
    # notebook2 = Notebook.create(name='default name2')
    # note1 = Note.create(idNotebook=1, title="Title1", content="Contenido de la nota1")
    # note2 = Note.create(idNotebook=2, title="Title2", content="Contenido de la nota2")
    # note3 = Note.create(idNotebook=1, idNote=99 title="Title3", content="Contenido da nota3")
    # tag1 = Tag.create(name='etiqueta1')
    # tag2 = Tag.create(name='etiqueta2')
    # notetag1 = NoteTag.create(note_id=1, tag_id=1)
    # notetag1 = NoteTag.create(note_id=2, tag_id=2)


# Inicio del modelo desde el controlador
if __name__ == "__main__":
    init_model()
