from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import generic,View
from .forms import SignupForm,ProfileForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginPage(View):

    def get(self,request):
    
        return render(request,'account/login.html')

    def post(self,request):

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.info(request,'Login successfully ')

            return redirect('index')

        messages.error(request,'please check username or password ')

        return render(request,'account/login.html')


class SignupPage(View):

    def get(self,request):
        form=SignupForm
        return render(request,'account/singup.html',{'form':form})

    def post(self,request):

        form=SignupForm(data=request.POST)

        if form.is_valid():
            login(request,form.save())
          
            messages.info(request,'You account created successfully...')
    
            return redirect('profile')
        print(form.errors)
        return render(request,'account/singup.html',{'form':form})


class ProfiePage(View,LoginRequiredMixin):
    def get(self,request,*args,**kwargs):
        form=ProfileForm()
        return render(request,'account/profile.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=ProfileForm(request.POST,request.FILES)
        
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=self.request.user 
            instance.save()
            
            return redirect('index')
        print(form.errors)
        return render(request,'account/profile.html',{'form':form})
    
    
@login_required
def logout_page(request): 

    logout(request)

    messages.info(request,'User logout successfully')
    return redirect('index')






