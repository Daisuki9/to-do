from django.test import TestCase

from .models import *

class ProyectosTest(TestCase):
    
    def setUp(self):
        Proyecto.objects.create(Titulo="Proyecto de prueba", Descripcion="Descripción de proyecto de prueba")
        
    def test_proyecto_creado(self):
        proyectos = Proyecto.objects.all()
        self.assertEqual(proyectos.count(), 1)

    def test_proyecto_datos_descripcion(self):
        proyecto = Proyecto.objects.get(id=1)
        self.assertEqual(proyecto.Descripcion, "Descripción de proyecto de prueba")

    def test_proyecto_datos_titulo(self):
        proyecto = Proyecto.objects.get(id=1)
        self.assertEqual(proyecto.Titulo, "Proyecto de prueba")

class EstadoTest(TestCase):
    
    def setUp(self):
        CategoriaEstado.objects.create(Nombre="Pendiente")
        CategoriaEstado.objects.create(Nombre="En Curso")
        CategoriaEstado.objects.create(Nombre="Listo")
        Estado.objects.create(Titulo="Pendiente", PorDefecto=1)
        Estado.objects.create(Titulo="En Curso")

    def test_estado_pordefecto1(self):
        estado = Estado.objects.get(id=1)
        self.assertEqual(estado.PorDefecto, 1)

    def test_estado_pordefecto2(self):
        estado = Estado.objects.get(id=2)
        self.assertEqual(estado.PorDefecto, 0)

    def test_estado_categoriapendiente(self):
        estado = Estado.objects.get(id=2)
        self.assertEqual(estado.Categoria.Nombre, "Pendiente")