from django.urls import path
from . import views

urlpatterns = [
    path('',views.menu_view, name='menu'),
    path('suma/', views.suma_view, name='suma'),
    path('resta/', views.resta_view, name='resta'),
    path('palindromos/', views.palindromos_view, name='palindromos'),
]
