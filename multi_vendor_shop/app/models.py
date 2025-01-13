from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    profile_image=models.ImageField(upload_to='profile')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    is_vendor=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
        

    def __str__(self): return f' {self.first_name} {self.last_name} '

class CategoryModel(models.Model):
    
    name=models.CharField(max_length=50)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    
    
    def __str__(self): return self.name

class ProductModel(models.Model):
    
    product_image=models.ImageField(upload_to='product')
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    profile=models.ForeignKey(ProfileModel,on_delete=models.CASCADE,related_name='profile')
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.FloatField()
    is_sold=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    
    def __str__(self): return self.name


class CartItem(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,related_name='product')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)    
    
