Descripción del Proyecto Django - MenuSpa

Este documento explica paso a paso cómo se creó el proyecto Django llamado "MenuSpa" con una aplicación llamada "spa".

-------------------------------------------------------------------------------

PASO 1: INSTALAR DJANGO

Asegúrate de tener Python instalado. Luego, instala Django con pip:

    pip install django

-------------------------------------------------------------------------------

PASO 2: CREAR EL PROYECTO DJANGO

Crea un nuevo proyecto llamado "MenuSpa":

    django-admin startproject MenuSpa

-------------------------------------------------------------------------------

PASO 3: NAVEGAR AL DIRECTORIO DEL PROYECTO

Cambia al directorio del proyecto:

    cd MenuSpa

-------------------------------------------------------------------------------

PASO 4: CREAR UNA APLICACIÓN DJANGO

Dentro del proyecto, crea una aplicación llamada "spa":

    python manage.py startapp spa

-------------------------------------------------------------------------------

PASO 5: REGISTRAR LA APLICACIÓN EN settings.py

Edita el archivo MenuSpa/settings.py y añade 'spa' en la lista de INSTALLED_APPS:

    INSTALLED_APPS = [
        # ... otras aplicaciones ...
        'spa',
    ]

-------------------------------------------------------------------------------

PASO 6: CONFIGURAR LAS URLs DEL PROYECTO Y DE LA APLICACIÓN

1. En el archivo MenuSpa/urls.py:

    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('spa/', include('spa.urls')),
    ]

2. Crea el archivo spa/urls.py con contenido básico:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
        # Puedes agregar más rutas aquí
    ]

-------------------------------------------------------------------------------

PASO 7: CREAR UNA VISTA BÁSICA

En spa/views.py, define una función que devuelva una plantilla:

    from django.shortcuts import render

    def index(request):
        return render(request, 'spa/menu.html')

-------------------------------------------------------------------------------

PASO 8: CREAR PLANTILLAS HTML

Crea el directorio: spa/templates/spa/

Luego agrega archivos HTML como:
- base.html
- menu.html
- palindromos.html
- resta.html
- suma.html

Ejemplo de spa/templates/spa/menu.html:

    <!DOCTYPE html>
    <html>
    <head>
        <title>Menu</title>
    </head>
    <body>
        <h1>Bienvenido al Menú</h1>
        <!-- Contenido del menú -->
    </body>
    </html>

-------------------------------------------------------------------------------

PASO 9: REALIZAR MIGRACIONES DE LA BASE DE DATOS

Ejecuta:

    python manage.py migrate

-------------------------------------------------------------------------------

PASO 10: EJECUTAR EL SERVIDOR DE DESARROLLO

Ejecuta el servidor para probar la aplicación:

    python manage.py runserver

-------------------------------------------------------------------------------

ESTRUCTURA FINAL DEL PROYECTO

Después de completar los pasos, tu estructura debe parecerse a esto:



```
MenuSpa/
├── db.sqlite3
├── manage.py
│
├── MenuSpa/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
└── spa/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    ├── static/
    └── templates/
        └── spa/
            ├── base.html
            ├── menu.html
            ├── palindromos.html
            ├── resta.html
            └── suma.html
```


-------------------------------------------------------------------------------

ARCHIVOS CLAVE

- manage.py: Utilidad de línea de comandos.
- settings.py: Configuración del proyecto.
- urls.py (proyecto): URLs principales.
- urls.py (spa): URLs específicas de la app.
- views.py: Funciones que responden a las solicitudes.
- templates/spa/: Plantillas HTML del proyecto.

-------------------------------------------------------------------------------

PARA INICIAR LA APLICACIÓN:

    python manage.py runserver

Abre tu navegador y visita: http://127.0.0.1:8000/spa/

¡Listo! El proyecto está configurado y funcionando.
