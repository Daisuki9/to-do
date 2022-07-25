from django.db import models

class Proyecto(models.Model):
    Titulo=models.CharField(max_length=50)
    Descripcion=models.TextField(max_length=8000, default="")
    def __str__(self) -> str:
        return f"{self.Titulo} ({self.Clave})"

class Estado(models.Model):
    Titulo=models.CharField(max_length=30)
    PorDefecto=models.BooleanField(default=0)
    def __str__(self) -> str:
        return self.Titulo

class Tarea(models.Model):
    Titulo=models.CharField(max_length=50)
    Contenido=models.TextField(max_length=8000)
    Completado=models.BooleanField()
    Estado=models.ForeignKey(Estado, on_delete=models.CASCADE)
    Proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.Titulo