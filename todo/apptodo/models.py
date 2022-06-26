from django.db import models

class Proyecto(models.Model):
    Titulo=models.CharField(max_length=50)

class CategoriaDeEstado(models.Model):
    Titulo=models.CharField(max_length=30)

class Estado(models.Model):
    Titulo=models.CharField(max_length=30)
    Categoria=models.ForeignKey(CategoriaDeEstado, on_delete=models.CASCADE)

class Tarea(models.Model):
    Titulo=models.CharField(max_length=50)
    Fecha=models.DateField()
    Contenido=models.TextField(max_length=8000)
    Completado=models.BooleanField()
    Estado=models.ForeignKey(Estado, on_delete=models.CASCADE)
    Proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)