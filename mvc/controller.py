import mvc.model as model
import mvc.view as view


class Controlador:
    """Clase Controlador (MVC). En conexión con las clases Modelo y Vista"""

    # Singleton
    controller_instance = None

    def __init__(self):
        # self.model = model.Modelo()
        # self.view = view.Vista()
        Controlador.controller_instance = self

    # Singleton. Si no existe ninguna instancia de Controlador, la crea; si existe, devuelve la instancia existente
    @staticmethod
    def get_controller_instance():
        if Controlador.controller_instance is None:
            Controlador()
        return Controlador.controller_instance

    def init_app(self):
        model.init_model()
        view.init_view()


