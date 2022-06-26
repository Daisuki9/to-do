
from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio),
    path('proyectos/', Proyectos),
    path('estados/', Estado),
    path('categoriadeestados/', CategoriaDeEstado),
    path('tareas/', Tarea),
]
