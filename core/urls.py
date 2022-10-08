from unittest.mock import patch
from django.contrib import admin
from django.urls import path,include   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('crud.urls',namespace='crud')),
    path('api/',include('crud_api.urls',namespace='crud_api')),
]
