from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('busqueda/inicio=<int:inicio>/cantidad=<int:cantidad>/', views.busqueda, name='busqueda'),
]