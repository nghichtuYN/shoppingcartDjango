from django.db import models
from src.carts.models import Cart
from src.products.models import Product

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.quantity * self.product.price
    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
