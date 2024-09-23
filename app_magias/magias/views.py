from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from .models import *

def index(request):
    magias = Magias.objects.all()
    
    # Configuração da paginação
    paginator = Paginator(magias, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'magias': page_obj,
        'classes': Classes.objects.all(),
        'escolas': Escolas.objects.all(),
        'paginator': paginator,
    }
    return render(request, 'magias/index.html', context)

def filter_magias(request):
    # Filtrando magias com base nos parâmetros de consulta
    magias = Magias.objects.all()
    
    nome = request.GET.get('nome')
    escola_id = request.GET.get('escola')
    nivel = request.GET.get('nivel')
    componente = request.GET.getlist('componentes')
    classe_id = request.GET.get('classe')

    # Lógica para filtrar as magias
    if nome:
        magias = magias.filter(nome__icontains=nome)
    if escola_id:
        magias = magias.filter(escola_id=escola_id)
    if nivel:
        magias = magias.filter(nivel=nivel)
    if componente:
        magias = magias.filter(componentes__nome__in=componente)
    if classe_id:
        magias = magias.filter(classes__id=classe_id)
        
    # Lógica para ordenar as magias
    order = request.GET.get('order', 'nome_asc')
    if order == 'nome_asc':
        magias = magias.order_by('nome')
    elif order == 'nome_desc':
        magias = magias.order_by('-nome')
    elif order == 'nivel_asc':
        magias = magias.order_by('nivel')
    elif order == 'nivel_desc':
        magias = magias.order_by('-nivel')
    
    # Configuração da paginação
    paginator = Paginator(magias, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Para exibir todas as opções de filtro
    escolas = Escolas.objects.all()
    classes = Classes.objects.all()
    componentes = Componentes.objects.all()

    context = {
        'magias': page_obj,
        'escolas': escolas,
        'classes': classes,
        'componentes': componentes,
        'paginator': paginator,
    }
    
    return render(request, 'magias/index.html', context)

def autocomplete_magias(request):
    if 'term' in request.GET:
        qs = Magias.objects.filter(nome__icontains=request.GET.get('term'))
        nomes = list(qs.values_list('nome', flat=True))
        return JsonResponse(nomes, safe=False)
    return JsonResponse([], safe=False)