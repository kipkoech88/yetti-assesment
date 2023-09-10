from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def register(request):
    return render(request, 'base/register.html')

def login(request):
    return render(request, 'base/login.html')