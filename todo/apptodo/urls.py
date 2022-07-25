
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Inicio, name="inicio"),
    path('buscar/', Buscar, name="buscar"),
    
    # path('proyectos/', Proyectos_ver, name="proyectos"),
    # path('proyectos/nuevo/', Proyectos_nuevo, name="proyectoNuevo"),
    # path('proyectos/editar/<claveProyecto>', Proyectos_editar, name="proyectoEditar"),
    # path('proyectos/detalles/<claveProyecto>/', Proyectos_ver_detalle, name="proyectos"),
    # path('proyectos/detalles/<claveProyecto>/quitartarea/<idTarea>', Tarea_quitar, name="QuitarTarea"),
    # path('proyectos/detalles/<claveProyecto>/editartarea/<idTarea>', Tarea_editar, name="EditarTarea"),
    
    #region Proyectos
    path('proyecto/list', ProyectoList.as_view(), name="proyecto_list"),
    path(r'^(?P<pk>/d+)$', ProyectoDetail.as_view(), name="proyecto_detail"),
    path(r'^nuevo$', ProyectoCreate.as_view(), name="proyecto_create"),
    path(r'^editar/(?P<pk>/d+)$', ProyectoUpdate.as_view(), name="proyecto_update"),
    path(r'^eliminar/(?P<pk>/d+)$', ProyectoDelete.as_view(), name="proyecto_delete"),
    #endregion
    #region Tareas
    path('nuevaTarea/<idProyecto>', TareaCreate, name="tarea_create"),
    path('eliminarTarea/<idProyecto>/<idTarea>', TareaDelete, name="tarea_delete"),
    path('editarTarea/<idProyecto>/<idTarea>', TareaUpdate, name="tarea_update"),
    path('editarTarea/<idProyecto>/<idTarea>/<idEstado>', TareaUpdateEstado, name="tarea_update_estado"),
    #endregion


    path('configuraciones/', Configuraciones, name="configuraciones"),
    path('configuraciones/estados/estadopordefecto/<idEstado>/', Configuraciones_estado_por_defecto, name="estadoPorDefecto"),
    
    path('estados/crearestados/', CrearEstados, name="crearEstados"),
]
