from django.shortcuts import render
from contas.models import conta
from caixa.models import caixa_geral

# Create your views here.

def contas(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name'):
            name = request.POST.get('name')
            valor = request.POST.get('valor')
            desc = request.POST.get('desc')
            data = request.POST.get('date')
            nava_conta = conta(nome=name, valor=valor, descricao=desc, data=data, estado=1)
            nava_conta.save()
            msg = "Conta agendada com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'contas.html', {'title':'Contas'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        c_obj = conta.objects.all().order_by('nome')
        if request.method == 'GET' and request.GET.get('c_id') != None:
            c_id = request.GET.get('c_id')
            c1 = conta.objects.filter(id=c_id).all()
            return render(request, 'buscar_conta.html', {'title':'Busca Conta', 'c1':c1})
        elif request.method == 'POST' and request.POST.get('id') != None:
            conta_id = request.POST.get('id')
            conta_obj = conta.objects.filter(id=conta_id).get()
            return render(request, 'editar_conta.html', {'title':'Editar Conta', 'conta_obj':conta_obj})
        return render(request, 'buscar_conta.html', {'title':'Busca Conta', 'c_obj':c_obj})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar1(request):
    if request.user.is_authenticated():
        if  request.method == 'GET' and request.POST.get('edit_id') != None:
            edit_id = request.GET.get('edit_id')
            c1_obj = conta.objects.filter(id=edit_id).get()
            return render(request, 'editar.html', {'title':'Editar Conta', 'c1_obj':c1_obj})
        elif request.method == 'POST' and request.POST.get('id') != None:
            conta_id = request.POST.get('id')
            conta_obj = conta.objects.filter(id=conta_id).get()
            conta_nome = request.POST.get('name')
            conta_valor = request.POST.get('valor')
            conta_desc = request.POST.get('desc')
            conta_data = request.POST.get('date')
            conta_obj.nome = conta_nome
            conta_obj.valor = conta_valor
            conta_obj.descricao = conta_desc
            conta_obj.data = conta_data
            conta_obj.save()
            msg = "Conta editada com sucesso."
            return render(request, 'home/home.html', {'title':'Home', "msg":msg})
        return render(request, 'editar_conta.html', {'title':'Editar Conta'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def pagar(request):
    if request.user.is_authenticated():
        contas = conta.objects.filter(estado=1).all()
        if request.method == "POST" and request.POST.get('conta_id') != None:
            conta_id = request.POST.get('conta_id')
            conta_obj = conta.objects.filter(id=conta_id).get()
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total - conta_obj.valor
            desc = "Conta numero "+str(conta_id)+"."
            novo_caixa = caixa_geral(tipo=2, total=total, desc=desc)
            novo_caixa.save()
            conta_obj.estado = 2
            conta_obj.save()
            msg = "Conta paga com sucesso."
            return render(request, 'home/home.html', {'title':'Home', "msg":msg})
        return render(request, 'pagar.html', {'title':'Pagar Conta', 'contas':contas})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})