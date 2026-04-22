# 📝 Notax - Gestor de Notas Simple

Notax es una aplicación de escritorio desarrollada como proyecto DAM (Desarrollo de Aplicaciones Multiplataforma) que proporciona un gestor de notas simple e intuitivo. Permite organizar notas en libretas, asignar etiquetas y gestionar contenido de forma eficiente.

![Interfaz de Notax](https://github.com/xoancg/notax-main/blob/main/res/img/ui.png)

## 🎯 Características Principales

- **Gestión de Libretas**: Crea y organiza múltiples libretas para clasificar tus notas
- **Creación de Notas**: Añade notas con título, contenido y etiquetas
- **Sistema de Etiquetas**: Asigna múltiples etiquetas a cada nota para una mejor categorización
- **Búsqueda y Filtrado**: Encuentra tus notas rápidamente por libreta, título o contenido
- **Edición y Actualización**: Modifica notas existentes de forma sencilla
- **Eliminación en Cascada**: Elimina notas y sus etiquetas asociadas automáticamente
- **Interfaz Gráfica Intuitiva**: Desarrollada con Tkinter para una experiencia de usuario fluida
- **Base de Datos Persistente**: SQLite garantiza que tus datos se guarden de forma segura

## 🏗️ Arquitectura MVC

La aplicación implementa el patrón Modelo-Vista-Controlador (MVC):

### **Modelo (mvc/model.py)**
- Define las entidades de la base de datos: `Notebook`, `Note` y `Tag`
- Implementa las operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
- Utiliza Peewee ORM para interactuar con SQLite
- Gestiona relaciones muchos-a-muchos entre notas y etiquetas

### **Vista (mvc/view.py)**
- Interfaz gráfica construida con Tkinter
- Panel de edición de notas con campos para libreta, título, etiquetas y contenido
- Tabla (Treeview) que muestra el listado de notas
- Botones para crear nueva nota, guardar, mostrar y borrar

### **Controlador (mvc/controller.py)**
- Clase `Controlador` que implementa el patrón Singleton
- Actúa como intermediario entre la Vista y el Modelo
- Métodos para gestionar notas, etiquetas y libretas

## 📋 Requisitos Previos

- **Python**: 3.9.7 o superior
- **SQLite**: 3.36.0 (incluido en Python)
- **pip** o **conda**: Gestor de paquetes Python

## 🚀 Instalación

### Opción 1: Usando pip

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/xoancg/notax.git
   cd notax
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements-pip.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python main.py
   ```

### Opción 2: Usando Conda

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/xoancg/notax.git
   cd notax
   ```

2. **Crea el entorno desde el archivo env.yaml:**
   ```bash
   conda env create -f env.yaml
   ```

3. **Activa el entorno:**
   ```bash
   conda activate notax
   ```

4. **Ejecuta la aplicación:**
   ```bash
   python main.py
   ```

## 💻 Uso

1. **Crear una Nueva Nota:**
   - Haz clic en el botón "NUEVA NOTA"
   - Selecciona o crea una libreta
   - Introduce el título, etiquetas (separadas por comas) y contenido
   - Haz clic en "GUARDAR"

2. **Ver una Nota:**
   - Selecciona una nota de la lista
   - Haz clic en "MOSTRAR" para cargar su contenido en el panel de edición

3. **Editar una Nota:**
   - Muestra la nota que deseas editar
   - Modifica el contenido
   - Haz clic en "GUARDAR"

4. **Eliminar una Nota:**
   - Selecciona la nota que deseas eliminar
   - Haz clic en "BORRAR"
   - Las etiquetas asociadas se eliminarán automáticamente

## 📁 Estructura del Proyecto

```
notax/
├── .idea/                    # Configuración de IDE (PyCharm)
├── config/                   # Configuración de la aplicación
│   └── settings.py          # Variables de configuración global
├── database/                # Almacenamiento de la base de datos SQLite
│   └── notax.db            # Archivo de base de datos
├── logs/                    # Registros de la aplicación
├── mvc/                     # Patrón Modelo-Vista-Controlador
│   ├── __init__.py
│   ├── model.py            # Modelos de datos y operaciones CRUD
│   ├── view.py             # Interfaz gráfica con Tkinter
│   └── controller.py       # Controlador central (Singleton)
├── res/                     # Recursos (imágenes, iconos)
│   └── img/
│       └── ui.png          # Captura de pantalla de la interfaz
├── main.py                  # Punto de entrada de la aplicación
├── env.yaml                # Especificación del entorno Conda
├── requirements-pip.txt     # Dependencias para pip
├── requirements-conda.txt   # Dependencias para Conda
└── README.md               # Este archivo
```

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Descripción |
|-----------|---------|------------|
| **Python** | 3.9.7 | Lenguaje de programación principal |
| **Tkinter** | Incluido | Framework para interfaz gráfica de escritorio |
| **SQLite** | 3.36.0 | Base de datos relacional embebida |
| **Peewee ORM** | 3.14.8 | Mapeador objeto-relacional para Python |
| **Certificados** | 2021.10.8 | Certificados SSL/TLS de confianza |

## 📊 Modelo de Datos

### Entidad: Notebook (Libreta)
```
- id: Identificador único (PK)
- name: Nombre de la libreta (UNIQUE, NOT NULL)
```

### Entidad: Note (Nota)
```
- id: Identificador único (PK)
- title: Título de la nota (UNIQUE, NOT NULL)
- notebook_id: Referencia a Notebook (FK, CASCADE)
- content: Contenido de la nota (máx. 500 caracteres)
- created_date: Fecha de creación (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
- tags: Relación muchos-a-muchos con Tag
```

### Entidad: Tag (Etiqueta)
```
- id: Identificador único (PK)
- name: Nombre de la etiqueta (UNIQUE, NOT NULL)
```

### Relación: Note ↔ Tag
- Relación muchos-a-muchos (Many-to-Many)
- Tabla intermedia generada automáticamente por Peewee
- Soporte para eliminación en cascada (CASCADE)

## 🔑 Características Técnicas

- **Patrón Singleton**: El controlador utiliza el patrón Singleton para garantizar una única instancia
- **ORM Peewee**: Abstracción de la base de datos con soporte para migraciones y relaciones
- **Relaciones en Cascada**: Eliminación automática de dependencias al borrar entidades
- **Interfaz Tkinter**: GUI responsive con Treeview para tabla de datos y ScrolledText para contenido
- **Logging**: Registro de eventos importante para debugging

## 📝 Notas de Desarrollo

- La base de datos se inicializa automáticamente al ejecutar la aplicación
- Las etiquetas se pueden separar por comas en el campo de etiquetas
- La aplicación está optimizada para Windows (ver configuración en `env.yaml`)
- El contenido de las notas está limitado a 500 caracteres por defecto

## 👨‍💻 Información del Autor

- **Autor**: xoancg
- **Proyecto**: DAM (Desarrollo de Aplicaciones Multiplataforma)  

## 📄 Licencia

Este proyecto es software de código abierto.

## 📞 Contacto y Contribuciones

Para reportar errores, sugerir mejoras o contribuir al proyecto, siéntete libre de abrir un issue o pull request en el repositorio.

---

**Disfruta organizando tus notas con Notax** 📚✨
