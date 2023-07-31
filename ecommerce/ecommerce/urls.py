from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls',namespace ='inventory')),
    
    path('api/', include('inventory.urls',namespace ='inventory_api')),
    path('api-auth/', include('rest_framework.urls')),
    
    path("accounts/",include("account.urls",namespace='account')),
    path('main/', include('main.urls',namespace ='main')),
    
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
