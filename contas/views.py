from django.shortcuts import render

# Create your views here.

def contas(request):
    return render(request, 'contas.html', {'title':'Contas'})

def busca(request):
    return render(request, 'busca1.html', {'title':'Buscar Conta'})

def editar(request):
    return render(request, 'editar.html', {'title':'Editar Conta'})

def pagar(request):
    return render(request, 'pagar.html', {'title':'Pagar Conta'})