from django.db import models

from django.contrib.auth.models import User



class category_model(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)

    def __str__(self): return self.name


class product_model(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey(category_model,on_delete=models.CASCADE,related_name='product')
    price=models.IntegerField()
    vendor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='product/images')
    is_delete=models.BooleanField(default=False)
    


    def __str__(self): return self.name


    # seventy percent descount 
    
    def discount_price(self): return self.price*0,7




