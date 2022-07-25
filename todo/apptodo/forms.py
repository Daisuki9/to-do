from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class TareaForm(forms.Form):
    Titulo=forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}))
    Contenido=forms.CharField(max_length=8000, label=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido'}))

class NuevoEstado(forms.Form):
    categoriaEstado = ['Pendiente','En Curso', 'Listo']
    OPCION_1 = 'Pendiente'
    OPCION_2 = 'En Curso'
    OPCION_3 = 'Listo'
    CATEGORIA = (
        (OPCION_1, u"Pendiente"),
        (OPCION_2, u"En Curso"),
        (OPCION_3, u"Listo")
    )
    Titulo=forms.CharField(max_length=30, label="Estado")
    Categoria=forms.ChoiceField(choices=CATEGORIA, label=False, widget=forms.RadioSelect(attrs={'class': 'form-check'}))
    PorDefecto=forms.BooleanField(label="Es estado por defecto", required=False, initial=False)

class BuscarProyectosYTareas(forms.Form):
    tipoBusqueda = ['tareas','proyectos']
    OPCION_1 = 'Tareas'
    OPCION_2 = 'Proyectos'
    CRITERIO = (
        (OPCION_1, u"Tareas"),
        (OPCION_2, u"Proyectos")
    )
    TextoBusqueda=forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un texto aquí'}))
    Criterio = forms.ChoiceField(choices=CRITERIO, label=False, widget=forms.RadioSelect(attrs={'class': 'form-check'}))

class UsuarioNuevoForm(UserCreationForm):
    
    username = forms.CharField(label="Usuario", required=True)
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UsuarioEditarForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña nueva", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        
        help_texts = {k:"" for k in fields}