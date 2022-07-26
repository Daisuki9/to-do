
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Inicio, name="inicio"),
    path('buscar/', Buscar, name="buscar"),
    path('about/', About, name="about"),
    #region Sesion
    path('login', login_request, name="login"),
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    path('usuario/editar', PerfilUpdate, name="usuario_update"),
    #endregion
    #region Proyectos
    path('proyecto/list', ProyectoList.as_view(), name="proyecto_list"),
    path('proyecto/nuevo', ProyectoCreate.as_view(), name="proyecto_create"),
    path('proyecto/<pk>', ProyectoDetail.as_view(), name="proyecto_detail"),
    path('proyecto/editar/<pk>', ProyectoUpdate.as_view(), name="proyecto_update"),
    path('proyecto/eliminar/<pk>', ProyectoDelete.as_view(), name="proyecto_delete"),
    #endregion
    #region Tareas
    path('nuevaTarea/<idProyecto>', TareaCreate, name="tarea_create"),
    path('eliminarTarea/<idProyecto>/<idTarea>', TareaDelete, name="tarea_delete"),
    path('editarTarea/<idProyecto>/<idTarea>', TareaUpdate, name="tarea_update"),
    path('editarTarea/<idProyecto>/<idTarea>/<idEstado>', TareaUpdateEstado, name="tarea_update_estado"),
    #endregion
    #region Configuraciones
    path('configuraciones/', Configuraciones, name="configuraciones"),
    path('configuraciones/estado/estadopordefecto/<idEstado>/', Configuraciones_estado_por_defecto, name="estadoPorDefecto"),
    path('configuraciones/estado/nuevo/', EstadoCreate, name="estado_create"),
    #endregion
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)