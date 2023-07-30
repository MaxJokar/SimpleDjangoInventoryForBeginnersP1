from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# DRF
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .serializers import ProductSerializer
from . import models
from .models import Product



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

#DRF
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


























