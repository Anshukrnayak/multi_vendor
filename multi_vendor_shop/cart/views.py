from django.shortcuts import render,Http404,redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import CartItem,ProductModel
from django.contrib import messages
from django.shortcuts import render, Http404, redirect
from django.contrib import messages

class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs['pk']
            product = ProductModel.objects.get(id=pk)
            cartItem, created = CartItem.objects.get_or_create(product=product, user=self.request.user)
            
            # Safely increment quantity if item exists, otherwise create with quantity = 1
            if created:
                cartItem.quantity = 1
            else:
                cartItem.quantity += 1
            cartItem.save()

            total_price = cartItem.total_price()  # Ensure this method is implemented in CartItem model
            print(total_price)
            
            return redirect('view_cart')

        except ProductModel.DoesNotExist:
            messages.error(request, "Product not found")
            raise Http404("Product not found")

        

class CartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            cart_list = CartItem.objects.filter(user=self.request.user)
            if not cart_list:
                messages.info(request, "Your cart is empty.")
                return redirect('index')

            total_price = sum(item.product.price * item.quantity for item in cart_list)

            return render(request, 'home/cart.html', {'cart_list': cart_list, 'total_price': total_price})

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, "An error occurred while retrieving your cart.")
            return redirect('index')


class DecreaseCartQuantity(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs['pk']
            cartitem = CartItem.objects.get(id=pk)

            if cartitem.quantity > 1:
                cartitem.quantity -= 1
                cartitem.save()
            else:
                messages.info(request, "Quantity cannot be less than 1.")
                return redirect('view_cart')

            return redirect('view_cart')

        except CartItem.DoesNotExist:
            messages.error(request, "Cart item not found.")
            return redirect('view_cart')

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, f"Error: {e}")
            return redirect('view_cart')


        
class DeleteCartItem(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs['pk']
            cart_item = CartItem.objects.get(id=pk)
            cart_item.delete()

            messages.success(request, "Item deleted from cart.")
            return redirect('view_cart')

        except CartItem.DoesNotExist:
            messages.error(request, "Cart item not found.")
            return redirect('view_cart')

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, f"An error occurred: {e}")
            return redirect('view_cart')
