from config.settings import *
from peewee import *

# Instanciación de la base de datos con activación expresa de claves foráneas (desactivadas por defecto en SQLite)
try:
    db = SqliteDatabase(DB_NAME, pragmas=DB_PRAGMAS)
    logging.info(msg=f'[OK] Fuck yeah! Database is here: {DB_NAME}')
except Exception as e:
    logging.error(msg=f'[!] Database connection error! > {e}')


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
    tags = ManyToManyField(Tag, backref='notes')


NoteTag = Note.tags.get_through_model()


# Query
class Modelo:
    """Clase Modelo (MVC)"""
    notebooks = Notebook.select(Notebook.idNotebook, Notebook.name).group_by(Notebook.idNotebook)
    # notebooks = Notebook.select(Notebook.name).group_by(Notebook.idNotebook)
    notebook_default = Notebook.select(Notebook.name).where(Notebook.idNotebook == 1)
    # notebook_default = Notebook.select(Notebook.name).group_by(Notebook.idNotebook)
    # notes = Note.select(Note.title, Note.content).order_by(Note.idNote)
    # notes = Note.select(Note.idNotebook, Note.idNote, Note.title).order_by(Note.idNotebook)
    notes = Note.select(Note.idNotebook, Note.idNote, Note.title).order_by(Note.idNotebook)
    tags = Tag.select(Tag.name)


def init_model():
    try:
        db.connect()
        db.create_tables([Notebook,
                          Note,
                          Tag,
                          NoteTag]
                         )
        logging.info(msg=f'Database connection is working')
    except Exception as e:
        logging.error(msg=f'[!] Database connection error! > {e}')


if __name__ == "__main__":
    init_model()
