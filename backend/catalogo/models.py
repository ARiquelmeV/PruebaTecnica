from django.db import models

# Create your models here.

class Producto(models.Model):
    #producto_id = models.AutoField(primary_key=True, unique=True, default=1000)
    nombre = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
    medidas = models.CharField(max_length=15)
    colores = models.CharField(max_length=20)
    foto = models.ImageField('images')

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['stock']








"""
atributos producto:  id, nombre, precio, foto, características generales. (Ej. medidas, colores,etc)
"""