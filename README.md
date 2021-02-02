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
![admin](https://user-images.githubusercontent.com/71096926/106147387-c8892180-6145-11eb-9a5a-6a2a9e231a76.jpg)
![admin_cactus_model](https://user-images.githubusercontent.com/71096926/106147466-e191d280-6145-11eb-9d8d-8517f9d373c3.jpg)
![swagger](https://user-images.githubusercontent.com/71096926/106147506-eeaec180-6145-11eb-9e34-01472e8275aa.jpg)
![swagger_post](https://user-images.githubusercontent.com/71096926/106173552-0eec7980-6162-11eb-8709-0a01971266d6.png)
