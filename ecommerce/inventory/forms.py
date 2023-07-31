from django.forms import ModelForm
from .models import Product


class CustomerForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name' , 'category','is_active' ]