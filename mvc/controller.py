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
        """Método que devuelve el contenido de la consulta de todas las notas existentes en la base de datos"""
        return self.model.query_notes()

    def save_note(self, notebook, title, tags, content):
        """Botón GUARDAR NOTA. Elimina el registro de una nota en la base de datos y actualiza la lista de notas en
        rejilla."""
        # 1-Actualizamos el registro de la nota con el contenido de los cuatro campos
        note = model.Note(notebook=notebook, title=title, tags=tags, content=content)
        note.save()
        # 2-Actualizamos la lista de notas en rejilla
        # ¿Cómo accedemos a la función list_notes() de view.py? ¿Controlador.get_notes()?
        # 3-El contenido de la nota se mantiene visible
        pass

    def new_note(self, notebook, title, tags, content):
        """Botón NUEVA NOTA. Limpia los campos de la nota en la vista y crea un nuevo registro en la base de datos
        con todos los campos en blanco. No actualiza la lista de notas en rejilla."""
        # 1-Limpiamos los campos en blanco.
        # Controlador.empty_note()
        # 2-Creamos un nuevo registro de nota, con todos los campos en blanco
        note = model.Note(notebook=notebook, title=title, tags=tags, content=content)
        note.save()

        # Persistimos los datos. save() es un método de instancia, por lo que necesitamos crear un objeto para usarlo
        # user1 = User(username='user1', email='user1@dominio.com', active=True)
        # user1.save()

    def delete_note(self):
        """Botón BORRAR NOTA. Elimina el registro de una nota en la base de datos y actualiza la lista de notas en
        rejilla."""
        # ¿Parámetros? ¿note_id?
        # 0-Cuando el usuario selecciona una nota en rejilla, el contenido de la misma se visualiza en la parte superior
        # 1-Consultamos los valores de la instancia de la nota seleccionada en rejilla
        # note = model.Note.select().where(Note.id == <note_id>)
        # 2-Eliminamos dicha instancia con <instancia>.delete_instance()
        # note.delete_instance()
        # 3-Ponemos en blanco los cuatro campos de la nota que se visualizan en la parte superior de la vista
        # Controlador.empty_note()
        # 4-Actualizamos la lista de notas en rejilla
        # ¿Cómo accedemos a la función list_notes() de view.py? ¿Controlador.get_notes()?
        pass

        # Borrar registros. Método de instancia. Lo consultamos para poder usarlo y luego lo eliminamos
        # user = User.select().where(User.username == 'user7').get()
        # user.delete_instance()

        # Otra forma. Método de clase, por lo que podemos usarlo directamente sobre el modelo (User.id) sin instanciar
        # query = User.delete().where(User.id == 6)
        # query.execute()

    def empty_note(self):
        """Método para vaciar, sólo a nivel de vista, el contenido de los cuatro campos que componen el registro de
        una nota introduciendo strings vacíos en los mismos. Este método no afecta a ningún registro de la base de
        datos."""
        # ¿Parámetros?
        # 1-Ejecuta la función save_note() para persistir el contenido actual de la nota
        # Controlador.save_note()
        # 2-Vacía el contenido de los cuatro campos de notas, SIN crear ningún registro en la base de datos
        # (pone strings vacíos)
        pass

    # El controlador inicia el modelo y la vista
    def init_app(self):
        # import mvc.model as model
        model.init_model()
        import mvc.view as view
        view.init_view()
