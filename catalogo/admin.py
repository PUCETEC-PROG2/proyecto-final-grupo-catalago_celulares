from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    pass