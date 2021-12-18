from mvc.controller import Controlador

controller = Controlador.get_controller_instance()


if __name__ == '__main__':
    controller.init_app()
