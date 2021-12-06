from config.settings import *
from os import remove
from peewee import *
import logging


def init_db():
    # INICIO DE LA APLICACIÓN
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
        # idTag = AutoField(unique=True)
        name = CharField(max_length=120)

    class Note(BaseModel):
        idNote = AutoField(unique=True)
        title = CharField(max_length=120, null=False)
        content = CharField(max_length=500, null=True)
        tags = ManyToManyField(Tag, backref='notes')
        idNotebook = ForeignKeyField(Notebook)

    NoteTag = Note.tags.get_through_model()

    # Tabla relación muchos-a-muchos entre tablas Note y Tag
    # class NoteTag(BaseModel):
    #     idNote = ForeignKeyField(Note)
    #     idTag = ForeignKeyField(Tag, on_delete='CASCADE')
    #
    #     class Meta:
    #         primary_key = CompositeKey('idNote', 'idTag')

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

    # Crea la libreta por defecto
    # notebook1 = Notebook.create(name='default name1')
    # notebook2 = Notebook.create(name='default name2')
    # tag1 = Tag.create(name='etiqueta1')
    # tag2 = Tag.create(name='etiqueta2')
    # note1 = Note.create(idNotebook=1, title="Title1", content="Contenido da nota1")
    # note2 = Note.create(idNotebook=2, title="Title2", content="Contenido da nota2")
    # # notetag1 = NoteTag.create(idNote_id=1, idTag_id=1)
    # notetag1 = NoteTag.create(note_id=1, tag_id=2)
    # note2 = Note.create(idNotebook=1, idNote=99 title="Title1", content="Contenido da nota1")

    # MODELO (MVC)
    class Modelo:
        notebooks = Notebook.select(Notebook.idNotebook, Notebook.name).group_by(Notebook.idNotebook)
        # notebooks = Notebook.select(Notebook.name).group_by(Notebook.idNotebook)
        notebook_default = Notebook.select(Notebook.name).where(Notebook.idNotebook == 1)
        # notebook_default = Notebook.select(Notebook.name).group_by(Notebook.idNotebook)
        # notes = Note.select(Note.title, Note.content).order_by(Note.idNote)
        # notes = Note.select(Note.idNotebook, Note.idNote, Note.title).order_by(Note.idNotebook)
        notes = Note.select(Note.idNotebook, Note.idNote, Note.title).order_by(Note.idNotebook)
        tags = Tag.select(Tag.name)


if __name__ == "__main__":
    init_db()

# Revisar configuración recomendada de pragma para SQLite
# https://docs.peewee-orm.com/en/latest/peewee/database.html
