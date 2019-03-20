from django.contrib import admin
from .models import Autor, Libro
# Register your models here.

@admin.register(Autor)
class AdminAutor(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais',)
    list_filter = ('nombre',)

@admin.register(Libro)
class AdminLibro(admin.ModelAdmin):
    list_display = ('id', 'autor', 'nombre', 'editorial', 'precio',)
    list_filter = ('nombre',)