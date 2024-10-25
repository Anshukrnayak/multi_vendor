from django import forms
from .models import product_model

class product_form(forms.ModelForm):
    class Meta:
        model=product_model
        fields=['name','category','description','price','image']

        widgets={
            
            'name':forms.TextInput(attrs={'class':'form-control border-secondary'}),
            'category':forms.Select(attrs={'class':'form-control border-secondary'}),
            'description':forms.Textarea(attrs={'class':'form-control border-secondary'}),
            'price':forms.NumberInput(attrs={'class':'form-control border-secondary'}),
            
        }        

