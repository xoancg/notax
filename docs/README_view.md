## NOTAS ARCHIVO view.py

### Clase Tkinter
El módulo tkinter es un conjunto de funciones que envuelven las implementaciones widgets Tk como clases de Python. Proporciona un conjunto de herramientas para administrar ventanas. Disponible para desarrolladores a través del paquete tkinter y sus extensiones, los módulos tkinter.tix y tkinter.ttk.

El paquete tkinter («interfaz Tk») es la interfaz por defecto de Python para el toolkit de la GUI Tk. Tanto Tk como tkinter están disponibles en la mayoría de las plataformas Unix, así como en sistemas Windows (Tk en sí no es parte de Python, es mantenido por ActiveState).

### Ttk widgets

Ttk viene con 18 widgets, doce de los cuales ya existían en tkinter: Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale, Scrollbar y Spinbox. Los otros seis son nuevos: Combobox, Notebook, Progressbar, Separator, Sizegrip y Treeview. Y todas ellas son subclases de Widget.

Para anular los widgets Tk básicos, la importación debe seguir la importación de Tk:

    from tkinter import *
    from tkinter.ttk import *

Ese código hace que varios widgets tkinter.ttk (Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale y Scrollbar) reemplacen automáticamente los widgets Tk.

Esto tiene el beneficio de usar los nuevos widgets que dan una mejor apariencia en todas las plataformas; sin embargo, el reemplazo de widgets no es completamente compatible. La principal diferencia es que las opciones de widgets como «fg», «bg» y otras relacionadas con el estilo del widget ya no están presentes en los widgets de Ttk. En su lugar, utiliza la clase **ttk.Style** para mejorar los efectos de estilo.

### Fuentes
- https://docs.python.org/es/3.8/library/tk.html
- https://docs.python.org/es/3.8/library/tkinter.html
- https://docs.python.org/es/3.8/library/tkinter.ttk.html