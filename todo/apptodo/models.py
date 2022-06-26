from django.db import models

class Tarea(models.Model):
    Titulo=models.CharField(max_length=50)
    Fecha=models.DateField()
    Contenido=models.TextField(max_length=8000)
    Completado=models.BooleanField()
    Proyecto=models.ForeignKey(Proyecto)

class Proyecto(models.Model):
    Titulo=models.CharField(max_length=50)

class CategoriaDeEstado(models.Model):
    Titulo=models.CharField(max_length=30)

class Estado(models.Model):
    Titulo=models.CharField(max_length=30)
    Categoria=models.ForeignKey(CategoriaDeEstado)