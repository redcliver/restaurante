from django.shortcuts import render
from decimal import *
from .models import caixa_geral
from pedido.models import pedido

# Create your views here.
def caixa(request):
    if request.user.is_authenticated():
        caixa = caixa_geral.objects.latest('id')
        return render(request, 'caixa.html', {'title':'Caixa', 'caixa':caixa})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def fechar(request):
    if request.user.is_authenticated():
        caixa = caixa_geral.objects.latest('id')
        if request.method =='POST' and request.POST.get('retirada') != None:
            valor =request.POST.get('retirada')
            fechamento = caixa_geral.objects.latest('id')
            total = fechamento.total - Decimal(valor)
            desc = "Fechamento"
            nova_op = caixa_geral(total=total, tipo=2, desc=desc)
            nova_op.save()
            msg = "Caixa fechado com secesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'fechar.html', {'title':'Caixa', 'caixa':caixa})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def retirada(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="abertura")
            caixa.save()
            total = caixa.total
        if request.method == 'POST' and request.POST.get('retirada') != None:
            valor_ret = request.POST.get('retirada')
            desc = request.POST.get('motivo')
            total = caixa.total - Decimal(valor_ret)
            nova_op = caixa_geral(total=total, tipo=2, desc=desc)
            nova_op.save()
            msg = "Retirada concluida com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'retirada.html', {'title':'Retirada', 'total':total})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def inf_geral(request):
    if request.user.is_authenticated():
        caixa = caixa_geral.objects.latest('id')
        caixa_1 = caixa_geral.objects.get(id=1)
        dia_1 = caixa_1.data.strftime('%d/%m/%Y')
        total_dim = 0
        total_cd = 0
        total_cc = 0
        
        for a in pedido.objects.filter(estado=2, metodo=1).all():
            total_dim = total_dim + a.total
        for b in pedido.objects.filter(estado=2, metodo=2).all():
            total_cd = total_cd + b.total
        for c in pedido.objects.filter(estado=2, metodo=3).all():
            total_cc = total_cc + c.total
        
        return render(request, 'inf_geral.html', {'title':'Retirada', 'dia_1':dia_1, 'total_dim':total_dim, 'total_cd':total_cd, 'total_cc':total_cc, 'caixa':caixa, 'dia_1':dia_1})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})