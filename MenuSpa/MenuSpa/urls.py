"""
URL configuration for MenuSpa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# Importa el módulo `admin` de `django.contrib` para habilitar la interfaz de administración de Django.

from django.urls import path, include
# Importa las funciones `path` e `include` del módulo `django.urls` para definir las rutas URL y para incluir otras configuraciones de URL.

urlpatterns = [
    # Define una lista de rutas URL para el proyecto `MenuSpa`.

    # path('admin/', admin.site.urls),
    # Comenta la ruta URL para la interfaz de administración de Django. Si se descomenta, esta ruta permitirá acceder a la interfaz de administración en 'admin/'.

    path('', include('spa.urls')),
    # Define una ruta URL que incluye las rutas definidas en `spa.urls`. Esta ruta es la raíz del proyecto (`''`), y redirige todas las solicitudes a las rutas definidas en la aplicación `spa`.
]
# Cierra la lista de rutas URL.