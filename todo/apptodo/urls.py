
from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio, name="inicio"),
    path('buscar/', Buscar, name="buscar"),
    path('proyectos/', Proyectos_ver, name="proyectos"),
    path('proyectos/nuevo/', Proyectos_nuevo, name="proyectoNuevo"),
    path('proyectos/detalles/<claveProyecto>/', Proyectos_ver_detalle, name="proyectos"),
    path('configuraciones/', Configuraciones, name="configuraciones"),
    path('configuraciones/estados/estadopordefecto/<idEstado>/', Configuraciones_estado_por_defecto, name="estadoPorDefecto"),

    #path('proyectos/<slug:claveProyecto>/creartarea', CrearTareas, name="crearTareas"),
    #path('tareas/', Tareas, name="tareas"),
    
    path('estados/crearestados/', CrearEstados, name="crearEstados"),
]
