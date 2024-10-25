from django.contrib import admin
from .models import product_model,category_model



@admin.register(category_model)
class category_admin(admin.ModelAdmin):
    list_display=['name','slug']


@admin.register(product_model)
class product_admin(admin.ModelAdmin):
    list_display=['name','description','category','price','vendor','updated_at','image']

