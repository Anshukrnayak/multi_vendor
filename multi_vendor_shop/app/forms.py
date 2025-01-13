from django import forms
from app.models import ProductModel

class ProdcutForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields=['category','name','price','description','product_image']

        
        widgets={
            
            
            'category':forms.Select(attrs={'class':'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'name':forms.TextInput(attrs={'class':'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'description':forms.Textarea(attrs={'class':'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'price':forms.NumberInput(attrs={'class':'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        
        
        }
        
        