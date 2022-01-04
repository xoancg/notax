from config.settings import *
from tkinter import scrolledtext as st
from tkinter import ttk
import tkinter as tk
from mvc.controller import Controlador

# Instancia del controlador
con = Controlador.get_controller_instance()


# Probar qué pasa si sacamos el código de la función
def init_view():
    main_window = tk.Tk()
    main_window.title('Notax')
    main_window.iconbitmap(ICO)  # Configuración en config/settings.py
    # Vista(main_window)
    # main_window.mainloop()


    global frame_note

    # Inserta todos los registros de notas en la rejilla
    def list_notes():
        for note in con.get_notes():
            tree.insert('', tk.END, text=note.notebook, values=(note.title, note.content, note.content))

    # Inicio de la creación de la interfaz gráfica
    # Marco que contiene los elementos para la edición de notas
    frame_note = tk.LabelFrame(main_window, text=' EDICIÓN DE NOTAS ')
    frame_note.grid(row=0, column=0, columnspan=5, padx=20, pady=15, sticky=tk.W + tk.E)

    # Libreta a la que pertenece la nota seleccionada
    tk.Label(frame_note, text=' Libreta: ').grid(row=1, column=0, padx=20, pady=5, sticky=tk.W)
    notebook = ttk.Combobox(frame_note, values=['libreta por defecto'], width=100)
    notebook.current(0)
    notebook.grid(row=1, column=1, sticky=tk.W)
    notebook.focus()

    # Título de la nota seleccionada
    tk.Label(frame_note, text=' Título: ', justify=tk.RIGHT).grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)
    title = ttk.Entry(frame_note, width=120)
    title.grid(row=2, column=1, sticky=tk.W)

    # Etiqueta de la nota seleccionada
    tk.Label(frame_note, text=' Etiquetas: ').grid(row=3, column=0, padx=20, pady=5, sticky=tk.W)
    tag = ttk.Entry(frame_note, width=120)
    tag.grid(row=3, column=1, sticky=tk.W)
    # Las etiquetas se separarán por comas. El string del campo tag será dividido con split(',')

    # Contenido de la nota seleccionada
    tk.Label(frame_note, text=' Contenido: ').grid(row=4, column=0, padx=20, pady=50, sticky=tk.W)
    content = st.ScrolledText(frame_note, width=91, height=10)
    content.grid(row=4, column=1, sticky=tk.N + tk.S + tk.W)


    # Rejilla para mostrar la lista de notas
    frame_list = tk.LabelFrame(main_window, text=' LISTA DE NOTAS ')
    frame_list.grid(row=7, column=0, columnspan=3, padx=20, pady=15)

    tree = ttk.Treeview(frame_list, height=10, columns=("#0, #1", "#2", "#3"))
    tree.grid(row=7, column=0, columnspan=2, padx=20, pady=10)
    tree.heading("#0", text="Libreta", anchor=tk.CENTER)
    tree.heading("#1", text="Título nota", anchor=tk.CENTER)
    tree.heading("#2", text="Contenido", anchor=tk.CENTER)
    tree.heading("#3", text="Etiquetas", anchor=tk.CENTER)

    # Relleno de rejilla con lista de notas
    list_notes()

    # Scroll vertical rejilla - ¡Sin probar!
    yscrollbar = tk.Scrollbar(frame_list)
    yscrollbar.grid(row=7, column=2, sticky="nsew")
    tree.config(yscrollcommand=yscrollbar.set)

    # def save_note():
    #     notes = con.get_notes
    #     iid = tree.focus()
    #     note_selected = notes[iid]
    #     note_title = title.get()
    #     note_notebook = notebook.get()
    #     note_content = content.get()
    #     note_tag = tag.get()
    #     note_selected.notebook = note_notebook
    #     note_selected.title = note_title
    #     note_selected.content = note_content
    #     note_selected.tag = note_tag
    #     con.save_note(note_selected)
    #
    # def new_note():
    #     note_title = title.get()
    #     note_notebook = notebook.get()
    #     note_content = content.get()
    #     note_tag = tag.get()
    #     con.newNote(note_notebook, note_title, note_content, note_tag)

    # Botón para guardar cambios en la nota
    # Actualiza el registro si ya existe o crea uno nuevo si no existe previamente
    # Llama a la función que actualiza la rejilla del listado de notas
    ttk.Button(frame_note, text='GUARDAR NOTA', command=None).grid(row=5, columnspan=2, ipadx=50, pady=10)

    # Botones para crear nueva nota y borrar la nota seleccionada en la rejilla
    ttk.Button(text='NUEVA NOTA', command=None).grid(row=8, column=0, columnspan=2, ipadx=50, pady=10)
    # BORRAR elimina la nota de la base de datos + Actualiza la rejilla del listado de notas
    ttk.Button(text='BORRAR', command=None).grid(row=8, column=1, columnspan=2, ipadx=50, pady=10)
    # ttk.Button(text='LIMPIAR LISTA').grid(row=9, column=1, columnspan=2, ipadx=50, pady=10)

    # Foco en la primera fila de la rejilla al abrir la ventana - ¡Sin probar!
    item = tree.identify_row(0)
    tree.selection_set(item)
    tree.focus(item)

    # mainloop
    main_window.mainloop()


if __name__ == "__main__":
    init_view()
