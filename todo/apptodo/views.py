from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def Base(request):
    proyectos=Proyecto.objects.all()
    return render(request, "base.html", {})

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
    tareas=Tarea.objects.all()
    return render(request, "tareas.html", {"proyectos":proyectos, "claveProyectoSeleccionado":claveProyecto, "tareas":tareas})
