from django.shortcuts import render
from .models import cliente

# Create your views here.

def cliente1(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            name = request.POST.get('name')
            tel = request.POST.get('tel')
            cel = request.POST.get('cel')
            mail = request.POST.get('mail')
            cnpj = request.POST.get('cnpj')
            insc = request.POST.get('insc')
            novo_cliente = cliente(nome=name, telefone=tel, celular=cel, email=mail, cnpj=cnpj, insc=insc)
            novo_cliente.save()
            msg = 'Cliente salvo com sucesso'
            return render(request, 'home/home.html', {'title':'Clientes ', 'msg':msg})
        return render(request, 'cliente.html', {'title':'Clientes '})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        clientes = cliente.objects.all().order_by('nome')
        if request.method == 'POST':
            cliente_id = request.POST.get('cliente_id')
            cliente_obj = cliente.objects.filter(id=cliente_id).get()
            return render(request, 'busca.html', {'title':'Busca Clientes', 'cliente_obj':cliente_obj})
        return render(request, 'busca.html', {'title':'Busca Clientes', 'clientes':clientes})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            cli_id = request.GET.get('cliente_id')
            cli_obj = cliente.objects.filter(id=cli_id).get()
            return render(request, 'editar.html', {'title':'Editar Cliente', 'cliente_obj':cli_obj})
        elif request.method == 'POST' and request.POST.get('id') != None:
            cliente_id = request.POST.get('id')
            cliente_obj = cliente.objects.filter(id=cliente_id).get()
            cliente_nome = request.POST.get('name')
            cliente_tel = request.POST.get('tel')
            cliente_cel = request.POST.get('cel')
            cliente_email = request.POST.get('mail')
            cliente_cnpj = request.POST.get('cnpj')
            cliente_insc = request.POST.get('insc')
            cliente_obj.nome = cliente_nome
            cliente_obj.telefone = cliente_tel
            cliente_obj.celular = cliente_cel
            cliente_obj.email = cliente_email
            cliente_obj.cnpj = cliente_cnpj
            cliente_obj.insc = cliente_insc
            cliente_obj.save()
            msg = 'Cliente editado com sucesso'
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})