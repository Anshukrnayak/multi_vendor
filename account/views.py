from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views.generic import View
from .forms import SignupForm
from .models import Profile_Model
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages
from core.models import product_model
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib import messages

# register page : 

class Signup_page(View):

    def get(self,request):

        form=SignupForm()

        return render(request,'account/signup.html',{'form':form})

    def post(self,request):

        form=SignupForm(data=request.POST)

        if form.is_valid():

            user=form.save()

            
            login(request,user)

            Profile_Model.objects.create(user=request.user)

            return redirect('home')


        return render(request,'account/login.html',{'form':form})

# Login Authentication 

class Login_page(View):

    def get(self,request):

        return render(request,'account/login.html')

    
    def post(self,request):


        username=request.POST['username']
        password=request.POST['password']

        print('username : ',username)
        print('password ',password)

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)

            return redirect('home')
        
        messages.info(request,'please enter correct username or password ')
            
        return render(request,'account/login.html',{})

@login_required
def Logout_page(request):
    logout(request)

    return redirect('home')

class My_account(View):

    def get(self,request):
        
     
        product_list=product_model.objects.filter(vendor=request.user).filter(is_delete=False)


        return render(request,'account/my_account.html',{'product_list':product_list})




@login_required
def delete_product(request,pk):
      
    product= product_model.objects.get(id=pk)
    product.is_delete=True
    product.delete()

    messages.info(request,'product has been deleted ')

    return redirect('my_account')






    






