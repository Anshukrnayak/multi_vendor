from django.db import models
from core.models import product_model
from django.contrib.auth.models import User



class CartItem(models.Model):
    product = models.ForeignKey(product_model, on_delete=models.CASCADE,related_name='product')
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


