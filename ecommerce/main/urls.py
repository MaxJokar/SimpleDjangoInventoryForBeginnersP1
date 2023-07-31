from django.urls import path
from . import views



app_name='main'

urlpatterns = [
    # path('',views.now, name="block"),
    
    
    path('',views.MainView.as_view(), name="index"),
    path('register/',views.add_memoir, name="registermemoir"),
    # path('showuser/',views.ShowUserForBlockView.as_view(), name="showuser"),
    # path('block/',views.block, name="block"),
    # path('unblock/',views.unblock, name="unblock"),



]
