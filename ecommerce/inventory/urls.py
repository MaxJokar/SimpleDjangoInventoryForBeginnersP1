from django.urls import path
from . import views

app_name ='inventory_ecom'


urlpatterns = [
    
    path('', views.all_products , name ="index"),
    
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    
    
]