from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                return redirect('index')
            else:
                messages.error(request, 'Error ao efetuar login.')
                return redirect('login')
    else:
        form = LoginForms()
        return render(request, 'galeria/usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha'].value()

            if User.objects.filter(username = nome).exists() or User.objects.filter(email = email).exists():
                messages.error(request, 'Email ou usuário ja cadastrado.')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )
            usuario.save()
            messages.success(request, f"Cadastro efetuado com sucesso!")
            return redirect('login')
    return render(request, 'galeria/usuarios/cadastro.html', {"form": form})

def logout(request):
    if  not request.user.is_authenticated:
        messages.error(request, 'Você já esta deslogado.')
        return redirect('login')
    auth.logout(request)
    messages.success(request,'Deslogado com sucesso!')
    return redirect('login')
