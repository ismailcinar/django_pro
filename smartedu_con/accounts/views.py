

# Create your views here.
from pickle import READONLY_BUFFER
from django.shortcuts import get_object_or_404, redirect, render
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                         password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                
                else:
                    messages.info(request, 'Disabled Account')
            
            else:
                messages.info(request, 'Check Your Usernama and password')

    else:
        form = LoginForm
    
    return render(request, 'login.html', {'form': form})


def user_register(request):
    return render(request, 'register.html')

def user_logout(request):
    pass

def user_dashboard(request):
    pass