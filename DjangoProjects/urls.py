
from django.contrib import admin
from django.urls import path
from myFirstApp import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('update/', views.update),
    path('delete/', views.delete),
    path('address/', views.address)
]

