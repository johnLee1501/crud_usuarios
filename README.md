# Crud Usuarios con Django

Este sencillo proyecto te permite realizar las operaciones básicas del crud sobre un modelo Usuario

## Algunas caracteristicas principales: 

#### -Conexión con base de datos Mysql
#### -Uso del modelo Usuario interno de Django
#### -Uso de Formularios Django
#### -Operaciones básicas de Crud utilizando vistas genéricas basadas en clases (ListView, CreateView, UpdateView, DeleteView)
#### -Uso de bootstrap y django-widget-tweaks para el diseño de los templates


## Getting Started

Estas instrucciones te proporcionarán una copia del proyecto en funcionamiento en tu máquina local con fines de desarrollo y prueba.

### Prerrequisito

Si quieres probar, necesitarás estos requisitos previos

```
Python > 3.6
```

### Instalación

Primero, clona el proyecto en tu computadora

```
git clone https://github.com/johnLee1501/crud_usuarios.git
```

luego, crea un entorno virtual para el proyecto, puedes usar virtualenvwrapper-win si tu sistema operativo es Windows

```
pip install virtualenvwrapper-win
mkvirtualenv <nombre_del_entorno>
```

después de esto, instala los paquetes en requirements.txt para asegurarte de tener todo lo necesario

```
pip install -r requirements.txt
```

finalmente configura tu servidor de base de datos Mysql, puedes hacerlo fácilmente utilizando laragon si tu sistema operativo es Windows. Ten en cuenta la siguiente configuración de settings.py, puedes modificarla de ser necesario
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crud_usuario',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
por último realiza las migraciones de tu modelo a la base de datos.
```
py manage.py makemigrations
py manage.py migrate
```

Listo! ya puedes ejecutarlo

```
py manage.py runserver
```

Ingresa a localhost:8000 y podrás listar, registrar, actualizar, y eliminar usuarios. 


## Autor

* **John Vega**

## Screenshots
Listar Usuarios
![Listar Usuarios](https://user-images.githubusercontent.com/71096926/106542767-6c6e2680-64d2-11eb-99b1-6168cdd2cd25.jpg)

Crear Usuario
![Crear Usuario](https://user-images.githubusercontent.com/71096926/106542804-7ee86000-64d2-11eb-87f8-865d236a7355.jpg)

Actualizar Usuario
![Actualizar Usuario](https://user-images.githubusercontent.com/71096926/106542819-86a80480-64d2-11eb-8aa5-b332393f8d56.jpg)

Eliminar Usuario
![Eliminar Usuario](https://user-images.githubusercontent.com/71096926/106542826-8a3b8b80-64d2-11eb-8287-3615b660ca67.jpg)
