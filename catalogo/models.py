from django.core.validators import RegexValidator
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    
    # Validador para asegurar que el número de teléfono siga el formato requerido
    phone_validator = RegexValidator(
        regex=r'^09\d{8}$', 
        message="El número de celular debe tener exactamente 10 numeros y comenzar con '09'."
    )
    nummber_phone = models.CharField(validators=[phone_validator], max_length=10, null=False)
    
    # Validador para asegurar que la cédula de identidad ecuatoriana tenga 10 dígitos
    id_card_validator = RegexValidator(
        regex=r'^\d{10}$',
        message="El número de cédula ecuatoriana debe tener exactamente 10 numeros."
    )
    identification_card = models.CharField(
        validators=[id_card_validator],
        max_length=10,
        null=False
    )
 
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    TYPE_CHOICES = [
        ('Smartphone', 'Smartphone'),
        ('Feature Phone', 'Feature Phone'),
    ]
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, null=False)
    
    BRAND_CHOICES = [
        ('Apple', 'Apple'),
        ('Samsung', 'Samsung'),
        ('Xiaomi', 'Xiaomi'),
        ('Huawei', 'Huawei'),
        ('Sony', 'Sony'),
        ('Nokia', 'Nokia'),
    ]
    brand = models.CharField(max_length=30, choices=BRAND_CHOICES, null=False)
    
    OPERATING_SYSTEM_CHOICES = [
        ('iOS', 'iOS'),
        ('Android', 'Android'),
        ('Windows', 'Windows'),
        ('Others', 'Others'),
    ]
    operating_system = models.CharField(max_length=30, choices=OPERATING_SYSTEM_CHOICES, null=False)

    def __str__(self):
        return f"{self.name} ({self.type})"
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(null=False, default=1, max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=1, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='product_images')
 
    def __str__(self):
        return f"{self.name}"
    
class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    total_price = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.date} {self.customer} {self.total_price}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
