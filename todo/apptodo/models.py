from django.db import models
from django.conf import settings

class Proyecto(models.Model):
    Titulo=models.CharField(max_length=50)
    Descripcion=models.TextField(max_length=8000, default="")
    Usuario=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.Titulo}"
    
class CategoriaEstado(models.Model):
    Nombre=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.Nombre

class Estado(models.Model):
    Titulo=models.CharField(max_length=30)
    PorDefecto=models.BooleanField(default=0)
    Categoria=models.ForeignKey(CategoriaEstado, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.Titulo

class Tarea(models.Model):
    Titulo=models.CharField(max_length=50)
    Contenido=models.TextField(max_length=8000)
    Estado=models.ForeignKey(Estado, on_delete=models.CASCADE)
    Proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.Titulo