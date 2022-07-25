from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import *
from .forms import *

@login_required
def Inicio(request):
    return render(request, "index.html", {})

#region Sesión

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    form=AuthenticationForm()
    return render(request, "apptodo/login.html", {"form":form})

def register_request(request):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            form.save()
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
            return redirect("login")
        return render(request, "apptodo/register.html", {"form":form})
    form=UserRegisterForm()
    return render(request, "apptodo/register.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

#endregion

#region Proyectos

class ProyectoList(LoginRequiredMixin, ListView):
    model=Proyecto
    template_name="apptodo/proyecto_list.html"

class ProyectoDetail(LoginRequiredMixin, DetailView):
    model=Proyecto
    template_name="apptodo/proyecto_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(ProyectoDetail, self).get_context_data(**kwargs)
        obj = self.get_object()
        tareasDelProyecto=Tarea.objects.filter(Proyecto__id=obj.id)
        estados=Estado.objects.all()
        formNuevaTarea=TareaForm()
        context['extra'] = {"tareasDelProyecto":tareasDelProyecto, "form":formNuevaTarea, "estados":estados}
        return context

class ProyectoCreate(LoginRequiredMixin, CreateView):
    model=Proyecto
    success_url="/apptodo/proyecto/list"
    fields=["Titulo", "Descripcion"]

class ProyectoUpdate(LoginRequiredMixin, UpdateView):
    model=Proyecto
    success_url="/apptodo/proyecto/list"
    fields=["Titulo", "Descripcion"]

class ProyectoDelete(LoginRequiredMixin, DeleteView):
    model=Proyecto
    success_url="/apptodo/proyecto/list"

#endregion

#region Tareas

@login_required
def TareaCreate(request, idProyecto):
    if request.method == "POST":
        datos = request.POST
        estadoPorDefecto=Estado.objects.filter(PorDefecto=1)[0]
        proyectoSeleccionado=Proyecto.objects.filter(id=idProyecto)[0]
        tarea = Tarea(Titulo=datos["Titulo"], Contenido=datos["Contenido"], Estado=estadoPorDefecto, Proyecto=proyectoSeleccionado)
        tarea.save()
    return redirect("proyecto_detail", idProyecto)

@login_required
def TareaDelete(request, idProyecto, idTarea):
    if request.method == "POST":
        tarea = Tarea.objects.get(id=idTarea)
        tarea.delete()
    return redirect("proyecto_detail", idProyecto)

@login_required
def TareaUpdate(request, idProyecto, idTarea):
    tarea = Tarea.objects.get(id=idTarea)

    if request.method == "POST":
        datos = request.POST
        tarea.Titulo=datos["Titulo"]
        tarea.Contenido=datos["Contenido"]
        tarea.save()
        return redirect("proyecto_detail", idProyecto)
    
    formularioVacio=TareaForm(initial={"Titulo":tarea.Titulo, "Contenido":tarea.Contenido})
    return render(request, "apptodo/tarea_update.html", {"form":formularioVacio})

@login_required
def TareaUpdateEstado(request, idProyecto, idTarea, idEstado):
    tarea=Tarea.objects.get(id=idTarea)
    estado=Estado.objects.get(id=idEstado)
    tarea.Estado=estado
    tarea.save()
    return redirect("proyecto_detail", idProyecto)

#endregion

@login_required
def Buscar(request):
    if request.method == "POST":
        datos = request.POST
        if str(datos["Criterio"]) == "Tareas":
            tareas=Tarea.objects.filter(Q(Titulo__icontains=datos["TextoBusqueda"]) | Q(Contenido__icontains=datos["TextoBusqueda"]))
            return render(request, "apptodo/busqueda_resultados_tareas.html", {"tareas":tareas})
        elif str(datos["Criterio"]) == "Proyectos":
            proyectos=Proyecto.objects.filter(Titulo__contains=datos["TextoBusqueda"])
            return render(request, "apptodo/busqueda_resultados_proyectos.html", {"proyectos":proyectos})

    formularioVacio=BuscarProyectosYTareas()
    return render(request, "apptodo/busqueda.html", {"form":formularioVacio})

@staff_member_required
def Configuraciones(request):  
    estados=Estado.objects.all()    
    return render(request, "configuraciones.html", {"estados":estados})

@staff_member_required
def Configuraciones_estado_por_defecto(request, idEstado=''):
    estado = Estado.objects.get(PorDefecto=1)
    estado.PorDefecto=0
    estado.save()
    estado = Estado.objects.get(id=int(idEstado))
    estado.PorDefecto=1
    estado.save()
    return redirect("configuraciones")

@staff_member_required
def CrearEstados(request):
    if request.method == "POST":
        datos = request.POST
        estado=Estado(Titulo=datos["Titulo"], PorDefecto=datos.get('PorDefecto', False))
        estado.save()
        return redirect("estados")
        
    formularioVacio=NuevoEstado()
    return render(request, "crearestado.html", {"form":formularioVacio})
