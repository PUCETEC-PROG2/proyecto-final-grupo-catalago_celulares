# Generated by Django 4.2 on 2024-08-19 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_categoria_cliente_compra_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='camara',
        ),
    ]
