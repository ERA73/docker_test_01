from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('busqueda/inicio=<int:inicio>/final=<int:final>/', views.busqueda, name='busqueda'),
]