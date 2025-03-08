from django.urls import path
# Importa la función `path` del módulo `django.urls` para definir las rutas URL.

from . import views
# Importa el módulo `views` del paquete actual (la aplicación `spa`), que contiene las vistas que se utilizarán en las rutas URL.

urlpatterns = [
    # Define una lista de rutas URL para la aplicación `spa`.

    path('', views.menu_view, name='menu'),
    # Define una ruta URL para la vista `menu_view`. Esta ruta es la raíz de la aplicación (`''`), y se accede a ella mediante el nombre 'menu'.

    path('suma/', views.suma_view, name='suma'),
    # Define una ruta URL para la vista `suma_view`. Esta ruta se accede mediante la URL 'suma/' y se puede referenciar con el nombre 'suma'.

    path('resta/', views.resta_view, name='resta'),
    # Define una ruta URL para la vista `resta_view`. Esta ruta se accede mediante la URL 'resta/' y se puede referenciar con el nombre 'resta'.

    path('palindromos/', views.palindromos_view, name='palindromos'),
    # Define una ruta URL para la vista `palindromos_view`. Esta ruta se accede mediante la URL 'palindromos/' y se puede referenciar con el nombre 'palindromos'.
]
# Cierra la lista de rutas URL.