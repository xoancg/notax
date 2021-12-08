from config.settings import *
from tkinter import scrolledtext as st
from tkinter import ttk
import tkinter as tk


class Client:
    def __init__(self, window):
        # Atributos del constructor
        self.win = window
        self.win.title('Notax')

        global frame_note

        # Inicio de la creación de la interfaz gráfica
        # Marco que contiene los elementos para la edición de notas
        frame_note = tk.LabelFrame(self.win, text=' EDICIÓN DE NOTAS ')
        frame_note.grid(row=0, column=0, columnspan=5, padx=20, pady=15, sticky=tk.W + tk.E)

        # Libreta a la que pertenece la nota seleccionada
        tk.Label(frame_note, text=' Libreta: ').grid(row=1, column=0, padx=20, pady=5, sticky=tk.W)
        self.notebook = ttk.Combobox(frame_note, values=['libreta por defecto'], width=100)
        self.notebook.current(0)
        self.notebook.grid(row=1, column=1, sticky=tk.W)
        self.notebook.focus()

        # Título de la nota seleccionada
        tk.Label(frame_note, text=' Título: ', justify=tk.RIGHT).grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)
        self.title = ttk.Entry(frame_note, width=120)
        self.title.grid(row=2, column=1, sticky=tk.W)

        # Etiqueta de la nota seleccionada
        tk.Label(frame_note, text=' Etiquetas: ').grid(row=3, column=0, padx=20, pady=5, sticky=tk.W)
        self.tag = ttk.Entry(frame_note, width=120)
        self.tag.grid(row=3, column=1, sticky=tk.W)

        # Contenido de la nota seleccionada
        tk.Label(frame_note, text=' Contenido: ').grid(row=4, column=0, padx=20, pady=50, sticky=tk.W)
        self.content = st.ScrolledText(frame_note, width=91, height=10)
        self.content.grid(row=4, column=1, sticky=tk.N + tk.S + tk.W)

        # Botón para guardar cambios en la nota
        ttk.Button(frame_note, text='GUARDAR NOTA').grid(row=5, columnspan=2, ipadx=50, pady=10)

        # Rejilla para mostrar la lista de notas
        frame_list = tk.LabelFrame(self.win, text=' LISTA DE NOTAS ')
        frame_list.grid(row=7, column=0, columnspan=3, padx=20, pady=15)

        self.tree = ttk.Treeview(frame_list, height=10, columns=("#0, #1", "#2", "#3"))
        self.tree.grid(row=7, column=0, columnspan=2, padx=20, pady=10)
        self.tree.heading("#0", text="Libreta", anchor=tk.CENTER)
        self.tree.heading("#1", text="Título nota", anchor=tk.CENTER)
        self.tree.heading("#2", text="Contenido", anchor=tk.CENTER)
        self.tree.heading("#3", text="Etiquetas", anchor=tk.CENTER)

        # Scroll vertical rejilla - ¡Sin probar!
        yscrollbar = tk.Scrollbar(frame_list)
        yscrollbar.grid(row=7, column=2, sticky="nsew")
        self.tree.config(yscrollcommand=yscrollbar.set)

        # Botones para editar y borrar la nota seleccionada en la rejilla
        ttk.Button(text='EDITAR').grid(row=8, column=0, columnspan=2, ipadx=50, pady=10)
        ttk.Button(text='BORRAR').grid(row=8, column=1, columnspan=2, ipadx=50, pady=10)
        # ttk.Button(text='LIMPIAR LISTA').grid(row=9, column=1, columnspan=2, ipadx=50, pady=10)

        # Foco en la primera fila de la rejilla al abrir la ventana - ¡Sin probar!
        item = self.tree.identify_row(0)
        self.tree.selection_set(item)
        self.tree.focus(item)


def init_view():
    # print('init_view function')
    main_window = tk.Tk()
    main_window.iconbitmap(ICO)  # Configuración en config/settings.py
    Client(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    init_view()
