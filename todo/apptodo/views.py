from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def Inicio(request):
    proyectos=Proyecto.objects.all()
    return render(request, "index.html", {})

def Proyectos(request):
    proyectos=Proyecto.objects.all()
    return render(request, "proyectos.html", {"proyectos":proyectos})

def Estados(request):  
    estados=Estado.objects.all()
    return render(request, "estados.html", {"estados":estados})

def Tareas(request, claveProyecto=''):
    proyectos=Proyecto.objects.all()
    tareas=Tarea.objects.filter(Proyecto__Clave=claveProyecto)
    return render(request, "tareas.html", {"proyectos":proyectos, "claveProyectoSeleccionado":claveProyecto, "tareas":tareas})

def CrearTareas(request, claveProyecto=''):
    if request.method == "POST":
        datos = request.POST
        estadoPorDefecto=Estado.objects.filter(PorDefecto=1)[0]
        proyectoSeleccionado=Proyecto.objects.filter(Clave=claveProyecto)[0]
        tarea = Tarea(Titulo=datos["titulo"], Contenido=datos["contenido"], Completado=0, Estado=estadoPorDefecto, Proyecto=proyectoSeleccionado)
        tarea.save()
        return Tareas(request, claveProyecto)

    proyectos=Proyecto.objects.all()
    tareas=Tarea.objects.filter(Proyecto__Clave=claveProyecto)
    return render(request, "creartareas.html", {"proyectos":proyectos, "claveProyectoSeleccionado":claveProyecto, "tareas":tareas})





##### LLEGUÉ HASTA 00:42:00 DE LA CLASE 21 #####