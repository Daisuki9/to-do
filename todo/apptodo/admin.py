from django.contrib import admin
from apptodo.models import *

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('Clave', 'Titulo', )
    search_fields = ('Clave', 'Titulo', )

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('Titulo',)
    def __unicode__(self):
        return self.Titulo

class TareaAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'Contenido', 'Completado', 'estado', 'proyecto')
    search_fields = ('Titulo', 'Contenido',)
    def estado(self, obj):
        return obj.Estado.Titulo
    def proyecto(self, obj):
        return obj.Proyecto.Titulo

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Tarea, TareaAdmin)