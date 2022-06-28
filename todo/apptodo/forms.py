from email.policy import default
from django import forms
from .models import *

class NuevaTarea(forms.Form):
    Titulo=forms.CharField(max_length=50, label="Título")
    Contenido=forms.CharField(widget=forms.Textarea)

class NuevoEstado(forms.Form):
    Titulo=forms.CharField(max_length=30, label="Estado")
    PorDefecto=forms.BooleanField(label="Es estado por defecto", required=False, initial=False)

class NuevoProyecto(forms.Form):
    Clave=forms.CharField(max_length=10)
    Titulo=forms.CharField(max_length=50)