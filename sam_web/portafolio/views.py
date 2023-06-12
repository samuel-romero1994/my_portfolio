from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()#importa todos los objetos en una lista con diccionarios
    return render(request, "portafolio/portfolio.html", {'projects':projects})#diccionario de contexto