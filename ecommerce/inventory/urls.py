from django.urls import path
from . import views

app_name ='inventory'


urlpatterns = [
    
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('', views.all_products , name ="index"),
    #path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    
]