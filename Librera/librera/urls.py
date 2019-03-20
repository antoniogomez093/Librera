from django.contrib import admin
from django.urls import path
from . import views

app_name='librera'

urlpatterns = [
    path('', views.index, name='index'),
    path('Autor/', views.AutorList.as_view(), name='AutorList'),
    path('Autor/<int:pk>/', views.AutorDetail.as_view(), name='AutorDetail'),
    path('Autor/new/', views.new_autor, name='new_autor'),
    path('Libro/', views.LibroList.as_view(), name='LibroList'),
    path('Libro/<int:pk>/', views.LibroDetail.as_view(), name='LibroDetail'),
    path('Libro/new/', views.new_libro, name='new_libro'),
]