from django.urls import path
from cart import views

urlpatterns = [
    path('<int:pk>',views.AddToCartView.as_view(),name='cart'),
    path('view_cart/',views.CartView.as_view(),name='view_cart'),
    path('descrease/<int:pk>',views.DecreaseCartQuantity.as_view(),name='descrease'),
    path('delete/<int:pk>',views.DeleteCartItem.as_view(),name='delete_cart'),   
]
