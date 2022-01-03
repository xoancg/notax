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

    # Botón Guardar nota
    def save_note(self, notebook, title, tags, content):
        # 1-Actualizamos el registro de la nota con el contenido de los cuatro campos
        note = model.Note(notebook=notebook, title=title, tags=tags, content=content)
        note.save()
        # 2-Actualizamos la lista de notas en rejilla
        # (pendiente)
        pass

    # Botón nueva nota
    def new_note(self, notebook, title, tags, content):
        # 1-Limpiamos los campos en blanco
        # (pendiente)
        # 2-Creamos un nuevo registro de nota, con todos los campos en blanco
        note = model.Note(notebook=notebook, title=title, tags=tags, content=content)
        note.save()

        # Persistimos los datos. save() es un método de instancia, por lo que necesitamos crear un objeto para usarlo
        # user1 = User(username='user1', email='user1@dominio.com', active=True)
        # user1.save()

    # Borrar nota
    def delete_note(self):
        # 0-Cuando el usuario selecciona una nota en rejilla, el contenido de la misma se visualiza en la parte superior
        # 1-Consultamos los valores de la instancia de la nota seleccionada en rejilla
        # 2-Eliminamos dicha instancia con <instancia>.delete_instance()
        # 3-Ponemos en blanco los cuatro campos de la nota que se visualizan en la parte superior de la vista
        # 4-Actualizamos la lista de notas en rejilla
        pass

        # Borrar registros. Método de instancia. Lo consultamos para poder usarlo y luego lo eliminamos
        # user = User.select().where(User.username == 'user7').get()
        # user.delete_instance()

        # Otra forma. Método de clase, por lo que podemos usarlo directamente sobre el modelo (User.id) sin instanciar
        # query = User.delete().where(User.id == 6)
        # query.execute()

    def empty_note(self):
        # 1-Ejecuta la función save_note() para persistir el contenido actual de la nota
        # 2-Vacía el contenido de los cuatro campos de notas, SIN crear ningún registro en la base de datos
        pass

    # El controlador inicia el modelo y la vista
    def init_app(self):
        # import mvc.model as model
        model.init_model()
        import mvc.view as view
        view.init_view()
