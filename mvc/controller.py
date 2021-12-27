import mvc.model as model
# import mvc.view as view


class Controlador:
    """Clase Controlador (MVC). En conexión con las clases Modelo y Vista"""

    # Singleton
    controller_instance = None

    def __init__(self):
        self.model = model
        # self.view = Vista()
        Controlador.controller_instance = self

    # Singleton. Si no existe ninguna instancia de Controlador, la crea; si existe, devuelve la instancia existente
    @staticmethod
    def get_controller_instance():
        if Controlador.controller_instance is None:
            Controlador()
        return Controlador.controller_instance

    # Devuelve lista de notas
    def get_notes(self):
        return self.model.query_notes()

    # Botón nueva nota
    def save_note(self, notebook, title, labels, content):
        note = model.Note(notebook=notebook, title=title, tags=labels, content=content)
        note.save()

    # Botón Guardar nota
    def edit_note(self):
        pass

    # Borrar nota
    def delete_note(self):
        pass


    # El controlador inicia el modelo y la vista
    def init_app(self):
        # import mvc.model as model
        model.init_model()
        import mvc.view as view
        view.init_view()
