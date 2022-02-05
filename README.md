![Image text](https://github.com/xoancg/notax-main/blob/main/res/img/ui.png)
![Image text](https://github.com/xoancg/notax/blob/main/res/img/ui_draft.jpg)

## Base de datos - SQLite utilizando Peewee ORM
#### Tabla Note:
- title: str
- notebook: Notebook
- content: str
- created_date: date

#### Tabla Tag:
- name: str

#### Tabla  Notebook:
- name: str

#### Tabla NoteTag:
- note: Note
- tag: Tag

#### Relaciones entre tablas:
- Note <- Notebook (1-N:M) --- Una note pertenece a una sola notebook y una notebook contiene muchas notes
- Note - Tag (N:M-N:M) --- Una note puede tener muchas tags y una tag puede tener muchas notes

## Casos de uso
- Un usuario puede realizar las siguientes acciones:
    - Crear una nota nueva
    - Eliminar una nota existente
    - Modificar una nota existente (título, etiquetas, contenido, libreta a la que pertenece)
    - Asignar etiquetas a una nota
    - Modificar etiquetas asignadas a una nota (nombre)
    - Eliminar etiquetas asignadas a una nota
    - Crear una nueva libreta
    - Eliminar una libreta siempre y cuando no existan notas en esa libreta
    - Visualizar un listado de todas las notas existentes en la base de datos
    - Mostrar el contenido, título, libreta y etiqueta de una nota en concreto elegida por el usuario

## Funcionalidad TKinter
En la pantalla principal observaremos 2 módulos diferentes. El módulo superior se utilizará para guardar (crear/actualizar)
una nota y visualizar su contenido mientras que el módulo inferior se utilizará para visualizar todas las notas existentes
en la base de datos con la posibilidad de seleccionarlas y borrarlas además de poder indicar que se muestre su contenido.


    - Base de datos: afinar modelo con Peewee ORM  - HECHO
    - Optimización de código: buenas prácticas   - HECHO
    - Aplicar POO: encapsulación de funciones   - Las clases controller.py, view.py y model.py tienen que poder accederse a ellas desde el exterior ya que dependen unas de otras por lo que la encapsulación de funciones (declarar métodos/atributos como privados) para poder ser accedidos únicamene desde su clase y nadie del exterior) no se puede aplicar en este caso
    - Implementar MVC correctamente (u otra estructura)   - HECHO
    - Interfaz gráfica: dotar de funcionalidad (Tkinter)   - HECHO
    - Test: pruebas funcionales basadas en caja negra   - HECHO
    - Aplicación mínima 100 % funcional y, a partir de ahí, ver si implantar más cosas   - HECHO

---
https://markdown.es/sintaxis-markdown/
https://www.markdownguide.org/cheat-sheet/