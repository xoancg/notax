from config.settings import *
from tkinter import scrolledtext as st
from tkinter import ttk
import tkinter as tk
from mvc.controller import Controlador

# Inicializar instancia del controlador
con = Controlador.get_controller_instance()


def list_notes(tree):
    """
    Añade las notas existentes a la tabla
    """
    notes = con.get_notes()
    for note in notes:
        tree.insert('', tk.END, text=note.notebook.name, values=(note.title, note.content, note.created_date))


def init_view():
    global frame_note
    main_window = tk.Tk()
    main_window.title('Notax')
    main_window.iconbitmap(ICO)  # Configuración en config/settings.py

    # Inicio de la creación de la interfaz gráfica
    # Marco que contiene los elementos para la edición de notas
    frame_note = tk.LabelFrame(main_window, text=' EDICIÓN DE NOTAS ')
    frame_note.grid(row=0, column=0, columnspan=5, padx=20, pady=15, sticky=tk.W + tk.E)

    # Libreta a la que pertenece la nota seleccionada
    tk.Label(frame_note, text=' Libreta: ').grid(row=1, column=0, padx=20, pady=5, sticky=tk.W)
    notes = con.get_notes()
    all_notebooks = []
    for note in notes:
        all_notebooks.append(note.notebook.name)
    if len(all_notebooks) > 0:
        notebooks = all_notebooks
        notebook = ttk.Combobox(frame_note, values=notebooks, width=110)
        notebook.current(0)
    else:
        notebook = ttk.Combobox(frame_note, values=['Default Notebook'], width=110)
        notebook.current(0)

    notebook.grid(row=1, column=1, sticky=tk.W)
    notebook.focus()

    def restore():
        notes = con.get_notes()
        all_notebooks = []
        for note in notes:
            all_notebooks.append(note.notebook.name)
        if len(all_notebooks) > 0:
            notebooks = all_notebooks
            notebook = ttk.Combobox(frame_note, values=notebooks, width=110)
            notebook.current(0)
        else:
            notebook = ttk.Combobox(frame_note, values=['Default Notebook'], width=110)
            notebook.current(0)

    # Título de la nota seleccionada
    tk.Label(frame_note, text=' Título: ', justify=tk.RIGHT).grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)
    title = ttk.Entry(frame_note, width=114)
    title.grid(row=2, column=1, sticky=tk.W)

    # Etiqueta de la nota seleccionada
    tk.Label(frame_note, text=' Etiquetas: ').grid(row=3, column=0, padx=20, pady=5, sticky=tk.W)
    tag = ttk.Entry(frame_note, width=114)
    tag.grid(row=3, column=1, sticky=tk.W)
    # Las etiquetas se separan por comas. El string del campo tag será dividido con split(',')

    # Contenido de la nota seleccionada
    tk.Label(frame_note, text=' Contenido: ').grid(row=4, column=0, padx=20, pady=50, sticky=tk.W)
    content = st.ScrolledText(frame_note, width=91, height=10)
    content.grid(row=4, column=1, sticky=tk.N + tk.S + tk.W)

    def clear(nb):
        """
        Este método limpia los campos en el formulario de nota, donde se añaden las nuevas notas
        """
        notebook.delete(0, 'end')  # Borrar el título por defecto
        # Reasignar los valores al combobox de notebooks
        values = list(notebook["values"])
        if nb not in values:
            notebook["values"] = values + [nb]
        else:
            notebook["values"] = values
        title.delete(0, 'end')
        tag.delete(0, 'end')
        content.delete("1.0", 'end')

    def nueva_nota():
        # Limpia el formulario de edición de notas
        clear(notebook.get())

        # Quita la selección en la lista de notas (para evitar sobreescribir la nota seleccionada con la nueva nota)
        tree.selection_set()
        tree.focus()

    # NUEVA NOTA
    ttk.Button(frame_note, text='NUEVA NOTA', command=nueva_nota).grid(row=5, column=0, columnspan=2, ipadx=50, pady=10)

    def guardar():
        """
        Este método guarda/actualiza notas nuevas o ya existentes. Una vez guardadas, deja los campos limpios para crear
        una nueva nota.
        """
        # Guardar una nueva libreta si no existe
        try:
            con.save_notebook(notebook.get())
        except:
            notebook_ = notebook.get()
            print(f'La libreta "{notebook_}" ya existe en la base de datos')

        # Guardar la nota
        note = con.save_note(notebook.get(), title.get(), content.get("1.0", "end"))
        tags = tag.get().split(",")

        # Guardar las etiquetas
        for t in tags:
            # Solo guardar las tags en caso de ser nueva nota o añadir alguna nueva a una nota existente
            try:
                x = con.save_tag(t)
                con.assign_tag_note(note, x)
            except:
                print(f'La etiqueta "{t}" ya está asignada a la nota: "{note.title}"')
                # Eliminar y volver a crear las tags en caso de modificar alguna
                con.delete_tag(t)
                x = con.save_tag(t)
                con.assign_tag_note(note, x)

        # Después de guardar, borrar contenido de la pantalla
        clear(notebook.get())  # Reutilización de código --- Buenas prácticas

        # Añadir nota a la tabla
        try:  # Si la nota ya existe previamente y la estamos actualizando, borramos el registro anterior de la tabla
            tree.delete(tree.selection())  # Borrar la fila de la tabla
            tree.insert('', tk.END, text=note.notebook.name, values=(note.title, note.content, note.created_date))
        except:  # Si la nota es una nueva simplemente se inserta en la tabla
            tree.insert('', tk.END, text=note.notebook.name, values=(note.title, note.content, note.created_date))

    # GUARDAR NOTA
    ttk.Button(frame_note, text='GUARDAR', command=guardar).grid(row=6, column=0, columnspan=2, ipadx=50, pady=10)

    # Rejilla para mostrar la lista de notas
    frame_list = tk.LabelFrame(main_window, text=' LISTA DE NOTAS ')
    frame_list.grid(row=7, column=0, columnspan=3, padx=20, pady=15)

    tree = ttk.Treeview(frame_list, height=10, columns=("#1", "#2", "#"))
    tree.grid(row=7, column=0, columnspan=2, padx=20, pady=10)
    tree.heading("#0", text="Libreta", anchor=tk.CENTER)
    tree.heading("#1", text="Título", anchor=tk.CENTER)
    tree.heading("#2", text="Contenido", anchor=tk.CENTER)
    tree.heading("#3", text="Última modificación", anchor=tk.CENTER)

    # Relleno de rejilla con lista de notas
    list_notes(tree)

    # Scroll vertical rejilla
    yscrollbar = tk.Scrollbar(frame_list, command=tree.yview)
    yscrollbar.grid(row=7, column=2, sticky="nsew")
    tree.config(yscrollcommand=yscrollbar.set)

    def mostrar():
        """
        Carga el contenido en la pantalla principal de la nota seleccionada en la lista de notas
        """
        # Este método se utiliza cuando se selecciona una nota de la lista de notas se muestre el contenido
        # Coger el item seleccionado de la tabla
        for data in tree.selection():
            libreta = tree.item(data, "text")
            values = tree.item(data, "values")
            titulo_nota = values[0]
            contenido_nota = values[1]
            clear(notebook.get())  # Reutilización de código --- Buenas prácticas
            notebook.insert(0, libreta)  # Escribir el título correspondiente a la nota
            title.insert(0, titulo_nota)
            content.insert("1.0", contenido_nota)
            tags = con.get_note_tags(note_name=titulo_nota)
            tag.insert(0, tags)

    # MOSTRAR NOTA
    ttk.Button(text='MOSTRAR', command=mostrar).grid(row=8, column=0, columnspan=2, ipadx=50, pady=10)

    def borrar():
        """
        Elimina la nota de la base de datos + Actualiza la rejilla del listado de notas
        """
        mostrar()
        # Coger el item seleccionado de la tabla
        for data in tree.selection():
            # data contiene lo siguiente ->
            # {'text': note.notebook.name,
            # 'image': '',
            # 'values': [note.title, note.content, note.created_date],
            # 'open': 0,
            # 'tags': ''}
            # Podemos coger el título de la nota a borrar cogiendo la 1a posición de la key 'values' del diccionario

            values = tree.item(data, "values")
            nombre_nota = values[0]

            # Eliminamos la nota y las etiquetas asignadas a esa nota también se eliminan ya que está la opción
            # especificada de on_delete='CASCADE'
            con.delete_note(note_name=nombre_nota)

            # Se eliminan los contenidos en pantalla de la nota eliminada en caso de estar mostrada
            clear(notebook.get())  # Reutilización de código --- Buenas prácticas
            tree.delete(tree.selection())  # Borrar la fila de la tabla

        restore()

    # BORRAR
    ttk.Button(text='BORRAR', command=borrar).grid(row=8, column=1, columnspan=2, ipadx=50, pady=10)

    # Foco en la primera fila de la rejilla al abrir la ventana
    item = tree.identify_row(0)
    tree.selection_set(item)
    tree.focus(item)

    # mainloop
    main_window.mainloop()


if __name__ == "__main__":
    init_view()
