from mvc.controller import Controlador


class Libro:
    def __init__(self, nombre, contenido, autor):
        self.nombre = nombre
        self.contenido = contenido
        self.autor = autor

    def leer(self):
        for x in self.contenido.split():
            print(x)

    def addUser(self, nombre, contrasena):
        c = Controlador.get_controller_instance()
        c.addUser(nombre, contrasena)
