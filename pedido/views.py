from django.shortcuts import render
from django.contrib.auth import authenticate
from cliente.models import cliente
from produto.models import produto, refeicao
from pedido.models import pedido, refe_item, prod_item
from decimal import *

# Create your views here.

def pedido1(request):
    if request.user.is_authenticated():
        cli = cliente.objects.all().order_by('nome')
        pro = produto.objects.all().order_by('nome')
        ref = refeicao.objects.all().order_by('nome')

        return render(request, 'pedido.html', {'title':'Pedidos', 'cli':cli, 'pro':pro, 'ref':ref})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def abrir(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('refe_id') == None and request.POST.get('prod_id') == None:
            cli_id = request.POST.get('cliente_id')
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            novo_pedido = pedido(cliente_pedido=cli_obj, estado=1, total=0)
            novo_pedido.save()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':novo_pedido, 'pro':pro, 'ref':ref})
        elif request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('refe_id') != None and request.POST.get('prod_id') == None:
            cli_id = request.POST.get('cliente_id')
            refe_id = request.POST.get('refe_id')
            refe_qnt = request.POST.get('qnt_refe')
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            refe_obj = refeicao.objects.all().filter(id=refe_id).get()
            refe_total = Decimal(refe_obj.valor)*Decimal(refe_qnt)
            novo_ref_item = refe_item(refeicoes=refe_obj, quantidade=refe_qnt, total=Decimal(refe_total))
            novo_ref_item.save()
            novo_pedido = pedido(cliente_pedido=cli_obj, estado=1, total=refe_total)
            novo_pedido.save()
            novo_pedido.refeicao_item.add(novo_ref_item)
            novo_pedido.save()
            refes1 = novo_pedido.refeicao_item.all()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':novo_pedido, 'refes1':refes1, 'pro':pro, 'ref':ref})
        elif request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('refe_id') == None and request.POST.get('prod_id') != None:
            cli_id = request.POST.get('cliente_id')
            prod_id = request.POST.get('prod_id')
            qnt_prod = request.POST.get('qnt_prod')
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            prod_obj = produto.objects.all().filter(id=prod_id).get()
            prod_obj.quantidade = int(prod_obj.quantidade) - int(qnt_prod)
            prod_obj.save()
            prod_total = Decimal(prod_obj.valor_venda)*Decimal(qnt_prod)
            novo_prod_item = prod_item(produtos=prod_obj, quantidade=qnt_prod, total=prod_total)
            novo_prod_item.save()
            novo_pedido = pedido(cliente_pedido=cli_obj, estado=1, total=prod_total)
            novo_pedido.save()
            novo_pedido.produto_item.add(novo_prod_item)
            novo_pedido.save()
            prods1 = novo_pedido.produto_item.all()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':novo_pedido, 'prods1':prods1, 'pro':pro, 'ref':ref})
        return render(request, 'abrir.html', {'title':'Abrir Pedido'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def entrega(request):
    if request.user.is_authenticated():
        return render(request, 'entrega.html', {'title':'Entrega'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def busca2(request):
    if request.user.is_authenticated():
        return render(request, 'busca2.html', {'title':'Busca'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})