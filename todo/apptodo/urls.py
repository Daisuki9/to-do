
from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio, name="inicio"),
    path('proyectos/', Proyectos, name="proyectos"),
    path('estados/', Estados, name="estados"),
    #path('tareas/', Tareas, name="tareas"),
    path('proyectos/<slug:claveProyecto>/', Tareas, name="proyectos"),
]
