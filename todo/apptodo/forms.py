from email.policy import default
from django import forms
from .models import *

class NuevaTarea(forms.Form):
    Titulo=forms.CharField(max_length=50, label=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}))
    Contenido=forms.CharField(max_length=8000, label=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido'}))

class NuevoEstado(forms.Form):
    Titulo=forms.CharField(max_length=30, label="Estado")
    PorDefecto=forms.BooleanField(label="Es estado por defecto", required=False, initial=False)

class NuevoProyecto(forms.Form):
    Clave=forms.CharField(max_length=10, label=False, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Clave'}))
    Titulo=forms.CharField(max_length=50, label=False, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}))
    Descripcion=forms.CharField(max_length=8000, label=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}))

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