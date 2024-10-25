from django.shortcuts import render, redirect
from .models import CartItem
from django.contrib.auth.models import User

from core.models import product_model
from django.contrib.auth.decorators import login_required



@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'home/cart.html', {'product_list': cart_items, 'total_price': total_price})


@login_required
def add_to_cart(request,pk):
    product = product_model.objects.get(id=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart') 



@login_required
def descrease_to_cart(request,pk):
    product = product_model.objects.get(id=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity -= 1

    if cart_item.quantity==0:
        cart_item.delete()

        return redirect('home')

    cart_item.save()
    return redirect('cart') 




@login_required
def remove_from_cart(request, pk):
    cart_item = CartItem.objects.get(id=pk)
    cart_item.delete()
    return redirect('home')


