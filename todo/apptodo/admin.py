from django.contrib import admin
from apptodo.models import *

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('Clave', 'Titulo', )

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('Titulo',)

class TareaAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'Fecha', 'Contenido', 'Completado', 'Estado', 'Proyecto')

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Tarea, TareaAdmin)