from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .forms import *

def Inicio(request):
    
    return render(request, "index.html", {})

def Proyectos_ver(request):
    proyectos=Proyecto.objects.all()
    return render(request, "Proyectos_ver.html", {"proyectos":proyectos})

def Proyectos_ver_detalle(request, claveProyecto=''):
    if request.method == "POST":
        datos = request.POST
        estadoPorDefecto=Estado.objects.filter(PorDefecto=1)[0]
        proyectoSeleccionado=Proyecto.objects.filter(Clave=claveProyecto)[0]
        tarea = Tarea(Titulo=datos["Titulo"], Contenido=datos["Contenido"], Completado=0, Estado=estadoPorDefecto, Proyecto=proyectoSeleccionado)
        tarea.save()
    proyectos=Proyecto.objects.all()
    tareas=Tarea.objects.filter(Proyecto__Clave=claveProyecto)
    formularioVacio=NuevaTarea()
    return render(request, "Proyectos_ver_detalle.html", {"proyectos":proyectos, "claveProyectoSeleccionado":claveProyecto, "tareas":tareas, "form":formularioVacio})

def Proyectos_nuevo(request):
    if request.method == "POST":
        datos = request.POST
        clave=str(datos["Clave"]).replace(" ", "")
        proyecto=Proyecto(Titulo=datos["Titulo"], Clave=clave)
        proyecto.save()
        return redirect("proyectos")
        
    formularioVacio=NuevoProyecto()
    return render(request, "Proyectos_nuevo.html", {"form":formularioVacio})

def Buscar(request):
    if request.method == "POST":
        datos = request.POST
        if str(datos["Criterio"]) == "Tareas":
            tareas=Tarea.objects.filter(Q(Titulo__icontains=datos["TextoBusqueda"]) | Q(Contenido__icontains=datos["TextoBusqueda"]))
            return render(request, "busquedatareas.html", {"tareas":tareas})
        elif str(datos["Criterio"]) == "Proyectos":
            proyectos=Proyecto.objects.filter(Titulo__contains=datos["TextoBusqueda"])
            return render(request, "busquedaproyectos.html", {"proyectos":proyectos})

    formularioVacio=BuscarProyectosYTareas()
    return render(request, "buscar.html", {"form":formularioVacio})

def Configuraciones(request):  
    estados=Estado.objects.all()    
    return render(request, "configuraciones.html", {"estados":estados})

def Configuraciones_estado_por_defecto(request, idEstado=''):
    estado = Estado.objects.get(PorDefecto=1)
    estado.PorDefecto=0
    estado.save()
    estado = Estado.objects.get(id=int(idEstado))
    estado.PorDefecto=1
    estado.save()
    return redirect("configuraciones")





def CrearEstados(request):
    if request.method == "POST":
        datos = request.POST
        estado=Estado(Titulo=datos["Titulo"], PorDefecto=datos.get('PorDefecto', False))
        estado.save()
        return redirect("estados")
        
    formularioVacio=NuevoEstado()
    return render(request, "crearestado.html", {"form":formularioVacio})

# def CrearTareas(request, claveProyecto=''):
#     if request.method == "POST":
#         datos = request.POST
#         estadoPorDefecto=Estado.objects.filter(PorDefecto=1)[0]
#         proyectoSeleccionado=Proyecto.objects.filter(Clave=claveProyecto)[0]
#         tarea = Tarea(Titulo=datos["Titulo"], Contenido=datos["Contenido"], Completado=0, Estado=estadoPorDefecto, Proyecto=proyectoSeleccionado)
#         tarea.save()
#         return Proyectos_ver_detalle(request, claveProyecto)

#     formularioVacio = NuevaTarea()
#     proyectos=Proyecto.objects.all()
#     tareas=Tarea.objects.filter(Proyecto__Clave=claveProyecto)
#     return render(request, "creartareas.html", {"form":formularioVacio, "proyectos":proyectos, "claveProyectoSeleccionado":claveProyecto, "tareas":tareas})
