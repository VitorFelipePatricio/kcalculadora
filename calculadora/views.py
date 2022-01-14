from django.shortcuts import render

from calculadora.utils import pequisarAlimento




def index(request):

    search = request.GET.get('search')
    alimentos,nutrientes = pequisarAlimento(search,['proteína (g)'])
   
    context = {'titulo' : 'Kcalculator','alimentos':alimentos}   
    
   
    return render(request, 'calculadora/index.html', context)

