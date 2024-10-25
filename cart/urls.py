
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('',views.view_cart,name='cart'),
    path('delete_cart/<int:pk>',views.remove_from_cart,name='delete_cart'),
    path('add_cart/<int:pk>',views.add_to_cart,name='add_cart'),
    path('descrease/<int:pk>',views.descrease_to_cart,name='descrease'),
    


]
