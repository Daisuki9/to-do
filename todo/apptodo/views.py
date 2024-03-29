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

#region Inicio

class ResumenProyecto:
    def __init__(self, idProyecto, tituloProyecto, tareas):
        self.idProyecto = idProyecto
        self.tituloProyecto = tituloProyecto
        self.tareasPendientes = tareas.filter(Estado__Categoria__Nombre="Pendiente").count()
        self.tareasEnCurso = tareas.filter(Estado__Categoria__Nombre="En Curso").count()
        self.tareasListas = tareas.filter(Estado__Categoria__Nombre="Listo").count()
        self.tareasTotal = tareas.count()
        self.tareas = tareas
    def completado(self):
        if self.tareasPendientes == 0 and self.tareasEnCurso == 0:
            return True
        return False

@login_required
def Inicio(request):
    username=request.user
    proyectos=Proyecto.objects.filter(Usuario=username)
    resumen=[]
    if proyectos.count()==0:
        return redirect("proyecto_list")
    for p in proyectos:
        tareas=Tarea.objects.filter(Proyecto=p)
        resumen.append(ResumenProyecto(p.id, p.Titulo, tareas))

    return render(request, "index.html", {"proyectos":proyectos, "resumen":resumen})
#endregion

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
        form=UsuarioNuevoForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            form.save()
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("inicio")
            return redirect("login")
        return render(request, "apptodo/register.html", {"form":form})
    form=UsuarioNuevoForm()
    return render(request, "apptodo/register.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

@login_required
def PerfilUpdate(request):
    usuario = request.user
    if request.method == "POST":
        form=UsuarioEditarForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email = info["email"]
            if info["password1"] != "":
                usuario.set_password(info["password1"])
            usuario.save()
            return redirect('inicio')
    form=UsuarioEditarForm(initial={"username":usuario.username, "email":usuario.email})
    return render(request, "apptodo/perfil_update.html", {"form":form})

#endregion

#region Proyectos

class ProyectoList(LoginRequiredMixin, ListView):
    model=Proyecto
    template_name="apptodo/proyecto_list.html"

    def get_queryset(self):
        return Proyecto.objects.filter(Usuario=self.request.user)

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
    
    def get_queryset(self):
        return Proyecto.objects.filter(Usuario=self.request.user)

class ProyectoCreate(LoginRequiredMixin, CreateView):
    model=Proyecto
    success_url="/apptodo/proyecto/list"
    fields=["Titulo", "Descripcion"]

    def form_valid(self, form):
        form.instance.Usuario = self.request.user
        return super().form_valid(form)

class ProyectoUpdate(LoginRequiredMixin, UpdateView):
    model=Proyecto
    success_url="/apptodo/proyecto/list"
    fields=["Titulo", "Descripcion"]

class ProyectoDelete(LoginRequiredMixin, DeleteView):
    model=Proyecto
    success_url="/apptodo/proyecto/list"

    def get_queryset(self):
        return Proyecto.objects.filter(Usuario=self.request.user)

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

#region Busqueda

@login_required
def Buscar(request):
    if request.method == "POST":
        datos = request.POST
        username=request.user
        if str(datos["Criterio"]) == "Tareas":
            tareas=Tarea.objects.filter(Q(Proyecto__Usuario=username), Q(Titulo__icontains=datos["TextoBusqueda"]) | Q(Contenido__icontains=datos["TextoBusqueda"]))
            if tareas.count() == 0:
                return render(request, "apptodo/busqueda_resultados_vacio.html", {})
            return render(request, "apptodo/busqueda_resultados_tareas.html", {"tareas":tareas})
        elif str(datos["Criterio"]) == "Proyectos":
            proyectos=Proyecto.objects.filter(Usuario=username, Titulo__contains=datos["TextoBusqueda"])
            if proyectos.count() == 0:
                return render(request, "apptodo/busqueda_resultados_vacio.html", {})
            return render(request, "apptodo/busqueda_resultados_proyectos.html", {"proyectos":proyectos})

    formularioVacio=BuscarProyectosYTareas()
    return render(request, "apptodo/busqueda.html", {"form":formularioVacio})

#endregion

#region Configuraciones
@staff_member_required
def Configuraciones(request):  
    estados=Estado.objects.all()
    formularioVacio=NuevoEstado()
    return render(request, "configuraciones.html", {"estados":estados, "form":formularioVacio})

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
def EstadoCreate(request):
    if request.method == "POST":
        datos = request.POST
        if str(datos["Categoria"]) == "Pendiente":
            categoria=CategoriaEstado.objects.get(Nombre="Pendiente")
        elif str(datos["Categoria"]) == "En Curso":
            categoria=CategoriaEstado.objects.get(Nombre="En Curso")
        elif str(datos["Categoria"]) == "Listo":
            categoria=CategoriaEstado.objects.get(Nombre="Listo")
        estado=Estado(Titulo=datos["Titulo"], PorDefecto=datos.get('PorDefecto', False), Categoria=categoria)
        estado.save()
        return redirect("configuraciones")
        
    return redirect("configuraciones")
#endregion

def About(request):
    return render(request, "apptodo/about.html", {})