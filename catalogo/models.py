from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    apellidos = models.CharField(max_length=150, null=False)
    cedula = models.BigIntegerField(null=False)
    telefono = models.BigIntegerField(null=False)
    correo = models.EmailField(null=False)

    def __str__(self) -> str:
        return f'{self.apellidos} {self.nombre}'
    
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.nombre_categoria

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200, null=False)
    precio = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    marca = models.CharField(max_length=100, null=False)
    cantidad = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    procesador = models.CharField(max_length=500, null=False)
    pantalla = models.TextField(max_length=500, null=False)
    ram = models.IntegerField(null=False)
    almacenamiento = models.IntegerField(null=False)
    imagen = models.ImageField(upload_to='celulares_images', null=False)
    
    def __str__(self) -> str:
        return self.nombre_producto

class Compra(models.Model):
    ciudad = models.CharField(max_length=50, null=False)
    fecha_compra = models.DateField(null=False)
    precio_total = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    productos = models.ManyToManyField(Producto)

    def __str__(self) -> str:
        return f'Compra de {self.cliente} - {self.fecha_compra}'