from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def Inicio(request):
    proyectos=Proyecto.objects.all()
    return render(request, "index.html", {"proyectos":proyectos})

def Proyectos(request):
    
    #proyectos=Proyecto.objects.all()
    #return render(request, "proyectos.html", {"proyecto":proyectos})
    return render(request, "proyectos.html", {})

def Estado(request):
    
    return render(request, "estados.html", {})

def CategoriaDeEstado(request):
    
    return render(request, "categoriadeestados.html", {})

def Tarea(request):
    
    return render(request, "tareas.html", {})
