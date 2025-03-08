from django.shortcuts import render
from .models import Proyecto

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})


def home(request):
    return render(request, 'proyectos/home.html')