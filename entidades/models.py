from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Juegos_de_Mesa(models.Model):
    codigo = models.IntegerField()
    nombre= models.CharField(max_length=50)
    cant_jugadores = models.CharField(max_length=50)
    edad_recomendada = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenesproductos/', null=True, blank=True)
    
    def __str__(self):
            return f"{self.nombre}"

class Miniaturas(models.Model):
    codigo = models.IntegerField()
    nombre= models.CharField(max_length=50)
    escala = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenesproductos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre}"

class Libros(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    cant_pag = models.IntegerField()
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenesproductos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Consolas(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenesproductos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre}"

class ImagenUsuario(models.Model):   
    imagen = models.ImageField(upload_to="imagenesusuarios/") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"        
    