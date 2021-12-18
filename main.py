from mvc.controller import Controlador
from mvc.Libros import Libro

c = Controlador.get_controller_instance()
c.addUser("juan", "contrasena1")
li = Libro("nom", "con", "aut")
li.addUser("pepe", "contrasena2")

for u in c.usuarios:
    print(u)

# if __name__ == '__main__':
#     controller.init_app()
