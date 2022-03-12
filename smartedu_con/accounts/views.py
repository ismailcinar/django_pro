

# Create your views here.
from django.shortcuts import get_object_or_404, render

def user_login(request):
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')

def user_logout(request):
    pass

def user_dashboard(request):
    pass