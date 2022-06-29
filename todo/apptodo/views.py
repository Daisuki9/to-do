from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .forms import *

def Inicio(request):
    if request.method == "POST":
        datos = request.POST
        if str(datos["Criterio"]) == "Tareas":
            tareas=Tarea.objects.filter(Q(Titulo__icontains=datos["TextoBusqueda"]) | Q(Contenido__icontains=datos["TextoBusqueda"]))
            return render(request, "busquedatareas.html", {"tareas":tareas})
        elif str(datos["Criterio"]) == "Proyectos":
            proyectos=Proyecto.objects.filter(Titulo__contains=datos["TextoBusqueda"])
            return render(request, "busquedaproyectos.html", {"proyectos":proyectos})

    formularioVacio=BuscarProyectosYTareas()
    return render(request, "index.html", {"form":formularioVacio})

def Proyectos(request):
    proyectos=Proyecto.objects.all()
    return render(request, "proyectos.html", {"proyectos":proyectos})

def CrearProyectos(request):
    if request.method == "POST":
        datos = request.POST
        proyecto=Proyecto(Titulo=datos["Titulo"], Clave=datos["Clave"])
        proyecto.save()
        return redirect("proyectos")
        
    formularioVacio=NuevoProyecto()
    return render(request, "crearproyectos.html", {"form":formularioVacio})

def Estados(request):  
    estados=Estado.objects.all()    
    return render(request, "estados.html", {"estados":estados})

def CrearEstados(request):
    if request.method == "POST":
        datos = request.POST
        estado=Estado(Titulo=datos["Titulo"], PorDefecto=datos.get('PorDefecto', False))
        estado.save()
        return redirect("estados")
        
    formularioVacio=NuevoEstado()
    return render(request, "crearestado.html", {"form":formularioVacio})

def Tareas(request, claveProyecto=''):
    proyectos=Proyecto.objects.all()
    tareas=Tarea.objects.filter(Proyecto__Clave=claveProyecto)
    return render(request, "tareas.html", {"proyectos":proyectos, "claveProyectoSeleccionado":claveProyecto, "tareas":tareas})

def CrearTareas(request, claveProyecto=''):
    if request.method == "POST":
        datos = request.POST
        estadoPorDefecto=Estado.objects.filter(PorDefecto=1)[0]
        proyectoSeleccionado=Proyecto.objects.filter(Clave=claveProyecto)[0]
        tarea = Tarea(Titulo=datos["Titulo"], Contenido=datos["Contenido"], Completado=0, Estado=estadoPorDefecto, Proyecto=proyectoSeleccionado)
        tarea.save()
        return Tareas(request, claveProyecto)

    formularioVacio = NuevaTarea()
    proyectos=Proyecto.objects.all()
    tareas=Tarea.objects.filter(Proyecto__Clave=claveProyecto)
    return render(request, "creartareas.html", {"form":formularioVacio, "proyectos":proyectos, "claveProyectoSeleccionado":claveProyecto, "tareas":tareas})
