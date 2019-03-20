from django.shortcuts import render
from .models import Autor, Libro
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader, render
'''Librerias para las class based views'''
from django.views.generic import ListView
from django.views.generic.detail import DetailView
''' Fin '''
from .forms import AutorForm, LibroForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

class AutorList(ListView):
    model = Autor
class AutorDetail(DetailView):
    model = Autor
def new_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.save()
            """ return HttpResponseRedirect('/') """
            return HttpResponseRedirect('/Autor')
    else:
        form = AutorForm()
    template = loader.get_template('librera/new_autor.html')
    context = { 'form': form }
    return HttpResponse(template.render(context, request)) 


class LibroList(ListView):
    model = Libro
class LibroDetail(DetailView):
    model = Libro
def new_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
            return HttpResponseRedirect('/Libro')
    else:
        form = LibroForm()
    template = loader.get_template('librera/new_libro.html')
    context = { 'form': form }
    return HttpResponse(template.render(context, request))