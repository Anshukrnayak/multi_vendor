from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .models import product_model,category_model
from django.views.generic.detail import DetailView
from .forms import product_form
from django.views.generic import View
from django.contrib import messages
from django.template.defaultfilters import slugify


class Home_Page(ListView):

    template_name='home/index.html'
    model=product_model
    fields='__all__'
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] =  category_model.objects.all()
        context['product_list']=product_model.objects.filter(is_delete=False)



        return context

class Product_detail_page(DetailView):
    template_name='home/product_detail.html'
    model=product_model
    fields='__all__'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["product"] =product_model.objects.get(id=self.kwargs['pk'])
        category=product_model.objects.get(id=self.kwargs['pk']).category
        context['related_category']=product_model.objects.exclude(category=category)



        return context

# create product 
class create_product(View):

    def get(self,request):

        form=product_form()

        return render(request,'home/create_product.html',{'form':form})

    def post(self,request):

        form=product_form(request.POST,request.FILES)

        if form.is_valid():
            product=form.save(commit=False)
            product.vendor=self.request.user
            product.save()


            return redirect('home')

        
        messages.error(request,form.errors)

        return render(request,'home/create_product.html',{'form':form})
        
