from django.shortcuts import render,get_list_or_404,redirect,Http404
from django.views.generic import View,TemplateView
from app.models import ProductModel,CategoryModel,ProfileModel
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import ProfileForm
from app.forms import ProdcutForm



class IndexView(View):
    
    def get(self,request,*args,**kwargs):
            context=ProductModel.objects.all()
            
            return render(request,'home/index.html',{'product_list':context})


    
class ProfilePage(View,LoginRequiredMixin):
    def get(self,request,*args,**kwargs):
        profile=ProfileModel.objects.get(user=self.request.user)
        print(profile.first_name)
        print(profile.last_name)
        
        return render(request,'home/profile.html',{'profile':profile})
    

class AddProduct(View,LoginRequiredMixin):
    def get(self,request,*args,**kwargs):
        form=ProdcutForm()
        return render(request,'home/add_product.html',{'form':form})

    def post(self,request,*args,**kwargs):
        profile=ProfileModel.objects.get(user=self.request.user)

        form=ProdcutForm(request.POST,request.FILES)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.profile=profile
            instance.save()
            
            return redirect('profile_view')
        print(form.errors)
        return render(request,'home/add_product.html',{'form':form})
    


class ProductDetail(View,LoginRequiredMixin):
    def get(self,request,*args,**kwargs):
        pk=kwargs['pk']
        product=ProductModel.objects.get(id=pk)    
        
        related_product=ProductModel.objects.filter(category=product.category).exclude(id=product.id)

        for product in related_product: print(product.name)
        
        return render(request,'home/product_detail.html',{'product':product,'related_product':related_product})
    
    

        
        

