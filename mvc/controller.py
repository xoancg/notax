# from mvc.model import init_model
# from mvc.view import init_view
# import mvc.model as model
# import mvc.view as view
from mvc.Usuario import Usuario


class Controlador:
    """Clase Controlador (MVC). En conexión con las clases Modelo y Vista"""

    # Singleton
    controller_instance = None

    def __init__(self):
        # self.model = model.Modelo()
        # self.view = view.Vista()
        self.usuarios = []
        Controlador.controller_instance = self

    def addUser(self, nombre, contrasena):
        usuario = Usuario(nombre, contrasena)
        self.usuarios.append(usuario)

    # Singleton. Si no existe ninguna instancia de Controlador, la crea; si existe, devuelve la instancia existente
    @staticmethod
    def get_controller_instance():
        if Controlador.controller_instance is None:
            Controlador()
        return Controlador.controller_instance

    # def init_view(self):
    #     view.init_view()
    #
    # def init_model(self):
    #     model.init_model()

    # def get_notes(self):
    #     return self.model.notes
    pass


def init_app():
    # init_model()
    # init_view()
    pass


if __name__ == "__main__":
    init_app()
