from mvc import model
from mvc import view


# CONTROLADOR (MVC)
class Controlador:
    def __init__(self):
        self.model = Modelo()
        self.view = Vista()

    def get_notebooks(self):
        notebooks = self.model.notebooks
        return self.view.list_notebooks(notebooks)

    def get_notebook_default(self):
        notebook_default = self.model.notebook_default
        return self.view.list_notebook_default(notebook_default)

    # def get_print_notebook_default(self):
    #     notebook_default = self.model.notebook_default
    #     return self.view.print_notebook_default(notebook_default)

    # def get_notes(self):
    #     notes = self.model.notes
    #     return self.view.list_notes(notes)

    def get_notes(self):
        notes = self.model.notes
        return self.view.list_notes(notes)

    # def get_note(self):
    #     #  Limpiar grid
    #     records = Client.__init__(self).tree.get_children()
    #     for element in records:
    #         Client.__init__().tree.delete()
    #
    #     #  Ejecutar consulta
    #     query = self.model.notes

    def get_tags(self):
        tags = self.model.tags
        return self.view.list_tags(tags)