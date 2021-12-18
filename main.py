from mvc.controller import Controlador

# Instancia del controlador para poder llamar al método que inicie la aplicación
controller = Controlador.get_controller_instance()


# Llamada al controlador para que éste inicie la aplicación
if __name__ == '__main__':
    controller.init_app()
