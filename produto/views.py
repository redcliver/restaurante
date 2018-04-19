from django.shortcuts import render
from .models import produto, refeicao

# Create your views here.

def novo_prod(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name'):
            name = request.POST.get('name')
            valor_vend = request.POST.get('valor_vend')
            valor_comp = request.POST.get('valor_comp')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            novo_produto = produto(nome=name, valor_venda=valor_vend, valor_compra=valor_comp, qnt_min=qnt_min, quantidade=qnt)
            novo_produto.save()
            msg = "Produto cadastrado com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'produto.html', {'title':'Produto'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def buscar_prod(request):
    if request.user.is_authenticated():
        prods = produto.objects.all().order_by('nome')
        if request.method == 'GET' and request.GET.get('prod_id') != None:
            name = request.GET.get('prod_id')
            produtos = produto.objects.filter(nome__icontains=name)
            return render(request, 'buscar_prod.html', {'title':'Busca Produto', 'produtos':produtos})
        elif request.method == 'POST':
            produto_id = request.POST.get('id')
            produto_obj = produto.objects.filter(id=produto_id).get()

            return render(request, 'edit_prod.html', {'title':'Editar Produto', 'produto_obj':produto_obj})
        return render(request, 'buscar_prod.html', {'title':'Busca Produto', 'prods':prods})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def edit_prod(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('id') != None:
            produto_id = request.POST.get('id')
            produto_obj = produto.objects.filter(id=produto_id).get()
            produto_nome = request.POST.get('name')
            produto_valor = request.POST.get('valor_vend')
            produto_qnt = request.POST.get('qnt')
            prod_valor_comp = request.POST.get('valor_comp')
            produto_qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = produto_nome
            produto_obj.valor_venda = produto_valor
            produto_obj.quantidade = produto_qnt
            produto_obj.valor_compra = prod_valor_comp
            produto_obj.qnt_min = produto_qnt_min
            produto_obj.save()
            msg = "Produto editado com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def nova_refe(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name'):
            name = request.POST.get('name')
            valor = request.POST.get('valor')
            nova_refeicao = refeicao(nome=name, valor=valor)
            nova_refeicao.save()
            msg = "Refeicao cadastrada com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'refeicao.html', {'title':'Produto'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def buscar_refe(request):
    if request.user.is_authenticated():
        refes = refeicao.objects.all().order_by('nome')
        if request.method == 'GET' and request.GET.get('refe_id') != None:
            name = request.GET.get('refe_id')
            refeicoes = refeicao.objects.filter(nome__icontains=name)
            return render(request, 'buscar_refe.html', {'title':'Busca Refeicao', 'refeicoes':refeicoes})
        elif request.method == 'POST':
            refeicao_id = request.POST.get('id')
            refeicao_obj = refeicao.objects.filter(id=refeicao_id).get()

            return render(request, 'edit_refe.html', {'title':'Editar Produto', 'refeicao_obj':refeicao_obj})
        return render(request, 'buscar_refe.html', {'title':'Busca Refeicao', 'refes':refes})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def edit_refe(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('id') != None:
            refeicao_id = request.POST.get('id')
            refeicao_obj = refeicao.objects.filter(id=refeicao_id).get()
            refeicao_nome = request.POST.get('name')
            refeicao_valor = request.POST.get('valor')
            refeicao_obj.nome = produto_nome
            refeicao_obj.valor = produto_valor
            refeicao_obj.save()
            msg = "Refeicao editada com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})