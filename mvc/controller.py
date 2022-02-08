
import mvc.model as model


class Controlador:
    """Clase Controlador (MVC). En conexión con las clases Modelo y Vista"""

    controller_instance = None

    def __init__(self):
        self.model = model
        Controlador.controller_instance = self

    @staticmethod
    def get_controller_instance():
        """
        Singleton - Patrón de diseño de tipo creación
        Si no existe ninguna instancia de Controlador, la crea; si existe, devuelve la instancia existente
        :return: Instancia controlador
        """
        if Controlador.controller_instance is None:
            Controlador()
        return Controlador.controller_instance

    # Devuelve lista de notas
    def get_notes(self):
        """
        Método que devuelve el contenido de la consulta de todas las notas existentes en la base de datos
        :return: Todas las notas existentes en la base de datos
        """
        return self.model.get_notes()

    def get_note_tags(self, note_name):
        """
        Método que devuelve las etiquetas asociadas a una nota
        :param note_name: nombre de la nota de la que extraer sus etiquetas
        :return: Etiquetas de la nota
        """
        return self.model.get_note_tags(note_name)

    def delete_tag(self, tag_name):
        """
        Método para eliminar una etiqueta
        :param tag_name: Nombre de la etiqueta
        """
        return self.model.delete_tag(tag_name)

    def save_notebook(self, notebook_name):
        """
        Guarda una libreta nueva o la actualiza en caso de que ya exista
        :param notebook_name: Nombre de la libreta a la que pertenece
        :return: Notebook creada
        """
        return self.model.save_notebook(notebook_name=notebook_name)

    def save_note(self, notebook, title, content):
        """
        Botón GUARDAR NOTA. Elimina el registro de una nota en la base de datos y actualiza la lista de notas en
        rejilla.
        :return: Nota guardada/actualizada
        """
        # Si la nota ya existe - Se actualiza. Si no existe - Se crea con el contenido
        return self.model.save_note(notebook_name=notebook, title=title, content=content)

    def save_tag(self, tag_name):
        """
        Este método se utiliza para guardar una etiqueta
        :param tag_name: nombre de la etiqueta
        :return: Etiqueta guardada
        """
        return self.model.save_tag(name=tag_name)

    def assign_tag_note(self, note, tag):
        """
        Este método se utiliza para asignar una etiqueta a una nota y viceversa (relación many-to-many)
        :param note: Nota a utilizar en la asignación
        :param tag: Etiqueta a utilizar en la asignación
        """
        self.model.add_tag_note(note=note, tag=tag)

    def delete_note(self, note_name):
        """
        Elimina el registro de una nota en la base de datos.
        :param note_name: Nombre de la nota
        """
        # 1. Cuando el usuario selecciona una nota, el contenido de la misma se visualiza en la parte superior
        # 2. Consultamos los valores de la instancia de la nota seleccionada en rejilla
        # 3. Eliminamos dicha instancia con <instancia>.delete_instance()
        self.model.delete_note(note_name)


# El controlador inicia el modelo
if __name__ == "__main__":
    model.init_model()
