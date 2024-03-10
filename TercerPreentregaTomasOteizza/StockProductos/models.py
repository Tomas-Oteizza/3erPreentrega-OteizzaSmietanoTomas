from django.db import models

# Create your models here.
class Procesador(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    
class PlacaVideo(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
    
class Teclado(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 200)
