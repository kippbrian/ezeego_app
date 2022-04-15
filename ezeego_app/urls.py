
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('carrier/', views.carrier_page),
    path('client/', views.client_page),
]
