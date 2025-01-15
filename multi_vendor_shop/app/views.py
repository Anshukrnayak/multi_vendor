from django.shortcuts import render,get_list_or_404,redirect,Http404,HttpResponse
from django.views.generic import View,TemplateView
from app.models import ProductModel,CategoryModel,ProfileModel
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import ProfileForm
from app.forms import ProdcutForm
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy



class IndexView(View):    
    def get(self,request,*args,**kwargs):
            context=ProductModel.objects.all()            
            return render(request,'home/index.html',{'product_list':context})

    
class ProfilePage(View,LoginRequiredMixin):

    def get(self,request,*args,**kwargs):
        try:        
            profile=ProfileModel.objects.get(user=self.request.user)
            return render(request,'home/profile.html',{'profile':profile})
    
        except ProfileModel.DoesNotExist:
            raise Http404('page not found ')
        
        
class AddProduct(View,LoginRequiredMixin):
    def get(self,request,*args,**kwargs):
        form=ProdcutForm()
        return render(request,'home/add_product.html',{'form':form})

    def post(self,request,*args,**kwargs):
        
        try:
            profile=ProfileModel.objects.get(user=self.request.user)
            
        except profile.DoesNotExist:
            messages.error(request,'profile instance not exitst ')
            return redirect('home')
        
        
        form=ProdcutForm(request.POST,request.FILES)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.profile=profile
            instance.save()
            
            return redirect('profile_view')
        
        return render(request,'home/add_product.html',{'form':form})
    

class ProductDetail(View,LoginRequiredMixin):
    def get(self,request,*args,**kwargs):
        try:
            pk=kwargs['pk']
            product=ProductModel.objects.get(id=pk)        
        except product.DoesNotExist:
         
            raise Http404('product not found ')
            messages.error(request,'product id not present ')
            return redirect('home')
        
        related_product=ProductModel.objects.filter(category=product.category).exclude(id=product.id)
        return render(request,'home/product_detail.html',{'product':product,'related_product':related_product})
    

    
# manage products : 


class ManageProducts(View,LoginRequiredMixin):
    def get(self,request,*args,**kwargs):
        try:
            profile=ProfileModel.objects.get(user=self.request.user)
            product_list=ProductModel.objects.filter(profile=profile)
        except:
            raise Http404('profile has no products : ')
        
            
        return render(request,'home/manage_product.html',{'product_list':product_list})
        
        

class EditProduct(View,LoginRequiredMixin):
    def get(self,request,*args,**kwargs):
        try:
            pk=kwargs['pk']
            product=ProductModel.objects.get(id=pk)
            form=ProdcutForm(instance=product)
            return render(request,'home/add_product.html',{'form':form})
        except Exception as e:
            print(e)
            return Http404('product not found ')
    
    def post(self,request,*args,**kwargs):
        try:
            pk=kwargs['pk']
            product=ProductModel.objects.get(id=pk)
            form=ProdcutForm(instance=product,data=request.POST)
            
            if form.is_valid():
                form.save()
                
                return redirect('manage_products')
        except Exception as e:
            print(e)
            messages.error(request,'product has not updated ')
            return redirect('manage_products')


class ProductDeleteView(generic.DeleteView):
    model = ProductModel
    template_name = 'home/delete_product.html'  # Template to confirm deletion
    context_object_name = 'product'  # The context variable name to access the object in the template
    success_url = reverse_lazy('manage_products')  # URL to redirect after successful deletion

    
    
    
    
    
    
    