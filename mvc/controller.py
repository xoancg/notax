from mvc.model import init_model
from mvc.view import init_view
import mvc.view


class Controlador:
    """Clase Controlador (MVC). En conexión con las clases Modelo y Vista"""
    pass


def init_app():
    init_model()
    init_view()
    pass


if __name__ == "__main__":
    init_app()
