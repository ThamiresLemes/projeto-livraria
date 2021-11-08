from django.shortcuts import render
from django.http import HttpResponse
from.models import Usuario
from django.shortcuts import redirect

def login(request):
    return HttpResponse('login')

def cadastro(request):
    return render(request,'cadastro.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(nome.strip()) == 0:
        return redirect('/auth/login/?status=1')

    if len(usuario) > 0:
        return redirect('/auth/login/?status=2
        7')

    try:
        usuario = Usuario(nome=nome, senha=senha, email=email)
        usuario.save

        return redirect('/auth/login/')

    except:
        return redirect('/auth/login/')