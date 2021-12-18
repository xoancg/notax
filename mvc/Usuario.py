class Usuario:
    numUsuarios = 0

    def __init__(self, nombre, contrasena):
        Usuario.numUsuarios += 1
        self.nombre = nombre
        self.contrasena = contrasena
