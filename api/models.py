from django.db import models
from pytils.translit import translify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField(max_length=500)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    PAYMENT_CHOICES = [
        ('kaspi', 'Kaspi Gold'),
        ('cash', 'Наличными курьеру'),
    ]
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ №{self.id} от {self.name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()

    def __str__(self):
        return f"Позиция заказа №{self.id}, от {self.order.id} товары {self.product.name}"
    

