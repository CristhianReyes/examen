from django.db import models
from django.utils import timezone

class Productos(models.Model):
    codigo = models.CharField(max_length=7)
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto_venta')
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    existencia = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre



class Usuarios(models.Model):
    dpi = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    productos = models.ManyToManyField(Productos)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    dpi = models.CharField(max_length=9)
    codigo = models.CharField(max_length=7)
    cantidad = models.CharField(max_length=3)
    fecha = models.DateField()
    productos = models.ManyToManyField(Productos)
