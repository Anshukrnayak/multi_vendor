from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('',views.Home_Page.as_view(),name='home'),
    path('product_detail/<int:pk>',views.Product_detail_page.as_view(),name='product_detail'),
    path("create_product/", views.create_product.as_view(), name="create_product"),

]
