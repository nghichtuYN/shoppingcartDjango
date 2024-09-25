from django.db import models

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_total_price(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.total_price()
        return total
    
    def item_count(self):
        return self.cartitem_set.count()
    def __str__(self):
        return f"Cart {self.id} - Created at {self.created_at}"
