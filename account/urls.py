from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.Signup_page.as_view(),name='signup'),
    path('login/',views.Login_page.as_view(),name='login'),
    path('my_account/',views.My_account.as_view(),name='my_account'),
    path('logout/',views.Logout_page,name='logout'),
    path('delete_account/<int:pk>',views.delete_product,name='delete_account'),


]
