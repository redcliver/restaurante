from django.shortcuts import render
from django.contrib.auth import authenticate
from cliente.models import cliente
from produto.models import produto, refeicao
from pedido.models import pedido, refe_item, prod_item
from caixa.models import caixa_geral
from django.utils import timezone
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
        if request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('refe_id') == None and request.POST.get('prod_id') == None and request.POST.get('ref_id') == None and request.POST.get('pro_id') == None:
            cli_id = request.POST.get('cliente_id')
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            novo_pedido = pedido(cliente_pedido=cli_obj, estado=1, total=0)
            novo_pedido.save()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':novo_pedido, 'pro':pro, 'ref':ref})
        elif request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('refe_id') != None and request.POST.get('prod_id') == None and request.POST.get('ref_id') == None and request.POST.get('pro_id') == None:
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
        elif request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('refe_id') == None and request.POST.get('prod_id') != None and request.POST.get('ref_id') == None and request.POST.get('pro_id') == None:
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
        elif request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('refe_id') != None and request.POST.get('prod_id') != None and request.POST.get('ref_id') == None and request.POST.get('pro_id') == None:
            cli_id = request.POST.get('cliente_id')
            prod_id = request.POST.get('prod_id')
            refe_id = request.POST.get('refe_id')
            qnt_prod = request.POST.get('qnt_prod')
            refe_qnt = request.POST.get('qnt_refe')
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            prod_obj = produto.objects.all().filter(id=prod_id).get()
            refe_obj = refeicao.objects.all().filter(id=refe_id).get()
            prod_obj.quantidade = int(prod_obj.quantidade) - int(qnt_prod)
            prod_obj.save()
            prod_total = prod_obj.valor_venda*Decimal(qnt_prod)
            refe_total = refe_obj.valor*Decimal(refe_qnt)
            total_total = Decimal(prod_total)+Decimal(refe_total)
            novo_prod_item = prod_item(produtos=prod_obj, quantidade=qnt_prod, total=prod_total)
            novo_prod_item.save()
            nova_refe_item = refe_item(refeicoes=refe_obj, quantidade=refe_qnt, total=refe_total)
            nova_refe_item.save()
            novo_pedido = pedido(cliente_pedido=cli_obj, estado=1, total=total_total)
            novo_pedido.save()
            novo_pedido.produto_item.add(novo_prod_item)
            novo_pedido.refeicao_item.add(nova_refe_item)
            novo_pedido.save()
            prods1 = novo_pedido.produto_item.all()
            refes1 = novo_pedido.refeicao_item.all()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':novo_pedido, 'prods1':prods1, 'refes1':refes1, 'pro':pro, 'ref':ref})
        return render(request, 'abrir.html', {'title':'Abrir Pedido'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def add_refe(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('ref_id') != None and request.POST.get('pro_id') == None and request.POST.get('refe_id') == None and request.POST.get('prod_id') == None:
            pedido_id = request.POST.get('ped_id')
            cli_id = request.POST.get('cli_id')
            refe_id = request.POST.get('ref_id')
            refe_qnt = request.POST.get('qnt_refe')
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            pedido_obj = pedido.objects.filter(id=pedido_id).get()
            refe_obj = refeicao.objects.all().filter(id=refe_id).get()
            refe_total = refe_obj.valor*Decimal(refe_qnt)
            novo_ref_item = refe_item(refeicoes=refe_obj, quantidade=refe_qnt, total=refe_total)
            novo_ref_item.save()
            pedido_obj.total = pedido_obj.total + refe_total
            pedido_obj.refeicao_item.add(novo_ref_item)
            pedido_obj.save()
            refes1 = pedido_obj.refeicao_item.all()
            prods1 = pedido_obj.produto_item.all()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':pedido_obj, 'refes1':refes1, 'prods1':prods1, 'pro':pro, 'ref':ref})
        return render(request, 'abrir.html', {'title':'Abrir Pedido'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})


def add_prod(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('ref_id') == None and request.POST.get('pro_id') != None and request.POST.get('refe_id') == None and request.POST.get('prod_id') == None:
            pedido_id = request.POST.get('ped_id')
            cli_id = request.POST.get('cli_id')
            prod_id = request.POST.get('pro_id')
            prod_qnt = request.POST.get('qnt_prod')
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            pedido_obj = pedido.objects.filter(id=pedido_id).get()
            prod_obj = produto.objects.all().filter(id=prod_id).get()
            prod_total = Decimal(prod_obj.valor_venda)*Decimal(prod_qnt)
            novo_pro_item = prod_item(produtos=prod_obj, quantidade=prod_qnt, total=prod_total)
            novo_pro_item.save()
            pedido_obj.total = pedido_obj.total + prod_total
            pedido_obj.produto_item.add(novo_pro_item)
            pedido_obj.save()
            refes1 = pedido_obj.refeicao_item.all()
            prods1 = pedido_obj.produto_item.all()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':pedido_obj, 'refes1':refes1, 'prods1':prods1, 'pro':pro, 'ref':ref})
        return render(request, 'abrir.html', {'title':'Abrir Pedido'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def metodo(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('pedido_id') != None:
            pedido_id = request.POST.get('pedido_id')
            pedido_obj = pedido.objects.filter(id=pedido_id).get()
            return render(request, 'metodo.html', {'title':'Meotodo de pagamento', 'pedido_obj':pedido_obj})
        return render(request, 'metodo.html', {'title':'Meotodo de pagamento'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})


def finalizar(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('pedido_id') != None and request.POST.get('metodo') != None:
            pedido_id = request.POST.get('pedido_id')
            met = request.POST.get('metodo')
            data = timezone.now()
            pedido_obj = pedido.objects.filter(id=pedido_id).get()
            caixa_atual = caixa_geral.objects.latest('id')
            desc = "Ref. pedido N: "+ str(pedido_obj.id) +"."
            total = caixa_atual.total + pedido_obj.total
            op_caixa = caixa_geral(tipo=1, total=total, desc=desc)
            op_caixa.save()
            pedido_obj.metodo = met
            pedido_obj.estado = 2
            pedido_obj.data_fechamento = data
            pedido_obj.save()
            msg = "Pedido finalizado com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'metodo.html', {'title':'Meotodo de pagamento'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def busca2(request):
    if request.user.is_authenticated():
        return render(request, 'busca2.html', {'title':'Busca'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def del_produto(request):
    if request.user.is_authenticated():
       if request.method == 'POST' and request.POST.get('del_prod') != None:
            del_prod_id = request.POST.get('del_prod')
            pedido_id = request.POST.get('pedido_id')
            cli_id = request.POST.get('cliente_id')
            prod_item_obj = prod_item.objects.filter(id=del_prod_id).get()
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            prod_preco = Decimal(prod_item_obj.total)
            prod_item_obj.delete()
            pedido_obj = pedido.objects.filter(id=pedido_id).get()
            pedido_obj.total = pedido_obj.total - prod_preco
            pedido_obj.save()
            refes1 = pedido_obj.refeicao_item.all()
            prods1 = pedido_obj.produto_item.all()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':pedido_obj, 'refes1':refes1, 'prods1':prods1, 'pro':pro, 'ref':ref})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def del_refe(request):
    if request.user.is_authenticated():
       if request.method == 'POST' and request.POST.get('del_refe') != None:
            del_refe_id = request.POST.get('del_refe')
            pedido_id = request.POST.get('pedido_id')
            cli_id = request.POST.get('cliente_id')
            ref_item_obj = refe_item.objects.filter(id = del_refe_id).get()
            cli_obj = cliente.objects.all().filter(id=cli_id).get()
            refe_preco = Decimal(ref_item_obj.total)
            ref_item_obj.delete()
            pedido_obj = pedido.objects.filter(id=pedido_id).get()
            pedido_obj.total = pedido_obj.total - refe_preco
            pedido_obj.save()
            prods1 = pedido_obj.produto_item.all()
            refes1 = pedido_obj.refeicao_item.all()
            pro = produto.objects.all().order_by('nome')
            ref = refeicao.objects.all().order_by('nome')
            return render(request, 'abrir.html', {'title':'Abrir Pedido', 'cli_obj':cli_obj, 'pedido_obj':pedido_obj, 'refes1':refes1, 'prods1':prods1, 'pro':pro, 'ref':ref})    
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})