from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')


            else:
                messages.info(request, 'Porfavor verificar usuario o contraseña!')

        else:
            messages.info(request, 'Inicio de sesion fallido!')

        return  redirect('AppCoderInicio')



    contexto = {
        'form': AuthenticationForm(),
        'name_submit': 'Login'
    }
    return render(request, 'UserCoder/login.html', contexto)