from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand
# Create your views here.
def new(request):
    return HttpResponse("hi")