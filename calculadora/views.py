from django.shortcuts import render
from django.template import context

def index(request):
    context = {'titulo' : 'Kcalculator'}
    return render(request, 'calculadora/index.html', context)
