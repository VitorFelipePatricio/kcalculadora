from django.shortcuts import render

import os.path

import pandas

def index(request):
    BASE = os.path.dirname(os.path.abspath(__file__))
    df = pandas.read_csv(os.path.join(BASE, 'static/taco-db-nutrientes.csv'), encoding='UTF-8', sep=';')
    
    context = {'titulo' : 'Kcalculator'}
    return render(request, 'calculadora/index.html', context)
