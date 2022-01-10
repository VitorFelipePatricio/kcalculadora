from django.shortcuts import render

import os.path

import pandas

BASE = os.path.dirname(os.path.abspath(__file__))
arquivo = pandas.read_csv(os.path.join(BASE, 'static/taco-db-nutrientes.csv'))


def index(request):

    search = request.GET.get('search')
    alimentos,nutrientes = pequisarAlimento(search,['proteína (g)'])
   
    context = {'titulo' : 'Kcalculator','alimentos':alimentos}   
    
   
    return render(request, 'calculadora/index.html', context)

def obterNutrientes(alimento,nutrientes):
  alimento = alimento.lower()
  alimento = arquivo['nome']==alimento
  listaDeNutrientes=[]
  if (type(nutrientes)==list):
    for i in range(len(nutrientes)):
      listaDeNutrientes.append(float(arquivo[alimento][nutrientes[i]]))
  else:
    listaDeNutrientes.append(float(arquivo[alimento][nutrientes]))
  
  return listaDeNutrientes

def pequisarAlimento(alimento, nutrientes ):
  nomeDosAlimentos = []
  listaNutrientes = []
  if(alimento):
    alimento = alimento.lower()
    listaDeAlimentos = []
    for i in arquivo['nome']:
      if alimento in i:
        listaDeAlimentos.append(True)
      else:
        listaDeAlimentos.append(False)
    listaDeAlimentos=arquivo[listaDeAlimentos]
   
    for i in range(len(listaDeAlimentos)):

      nomeDosAlimentos.append(listaDeAlimentos.iloc[i]['nome'])
      listaNutrientes.append(obterNutrientes(nomeDosAlimentos[i],nutrientes))
  
  return nomeDosAlimentos, listaNutrientes