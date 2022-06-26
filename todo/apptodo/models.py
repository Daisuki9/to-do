from django.db import models

class Proyecto(models.Model):
    Titulo=models.CharField(max_length=50)

class CategoriaDeEstado(models.Model):
    Titulo=models.CharField(max_length=30)

class Estado(models.Model):
    Titulo=models.CharField(max_length=30)
    Categoria=models.ForeignKey(CategoriaDeEstado)

class Tarea(models.Model):
    Titulo=models.CharField(max_length=50)
    Fecha=models.DateField()
    Contenido=models.TextField(max_length=8000)
    Completado=models.BooleanField()
    Estado=models.ForeignKey(Estado)
    Proyecto=models.ForeignKey(Proyecto)