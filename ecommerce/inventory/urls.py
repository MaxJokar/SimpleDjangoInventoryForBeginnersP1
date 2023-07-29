from django.urls import path
from . import views

app_name ='inventory'


urlpatterns = [
    
    # path('teacher/', views.TeacherList.as_view()),
    # path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('', views.all_products , name ="index"),
    #path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    
]