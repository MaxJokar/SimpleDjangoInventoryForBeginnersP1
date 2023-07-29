from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def all_products(request):

    # Primitive :
    # page_obj = Product.objects.all()
    # return render(request,'index.html', {'page_obj':page_obj})
    
    # with Paginator:
    objs = Product.objects.all()
    paginator = Paginator(objs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj':page_obj})

