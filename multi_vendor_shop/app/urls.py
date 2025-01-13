from django.urls import path
from app import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('add_product/',views.AddProduct.as_view(),name='add_product'),
    path('profile_view/',views.ProfilePage.as_view(),name='profile_view'),
    path('product_detail/<int:pk>',views.ProductDetail.as_view(),name='product_detail'),
        
    
]
