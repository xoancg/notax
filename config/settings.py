import logging

# Rutas de ficheros
DB_NAME = "database/notax.db"
DB_PRAGMAS = {'foreign_keys': 1, 'permanent': True}
ICO = "res/img/notax.ico"
LOG_INFO = "logs/info.log"
LOG_ERROR = "logs/error.log"

# Configuración de logging
logger = True  # True para activar logs de información y de errores
if logger:
    logging.basicConfig(filename=LOG_INFO,
                        level=logging.INFO,
                        format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                        datefmt='%H:%M:%S'
                        )
else:
    pass

# Activar/Desactivar opciones de desarrollo - MODEL.PY
deleteNotebook = False  # True para activar el borrado de LIBRETAS durante las pruebas de desarrollo
deleteTag = False  # True para activar el borrado de ETIQUETAS durante las pruebas de desarrollo
debug_db = False  # True para que se ejecuten las pruebas de la base de datos de este fichero
remove_db = False  # True para borrar el fichero de la base de datos al finalizar la ejecución del programa
untag = False  # True para activar el desetiquetado de notas durante las pruebas de desarrollo

# DB_NAME = "../database/notax.db" cuando se ejecuta model.py directamente
# DB_NAME = "database/notax.db" cuando se ejecuta la función de creación de la base de datos desde main.py
