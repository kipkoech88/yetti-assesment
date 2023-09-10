from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

# def register(request):
#     context = {}
#     return render(request, 'base/register.html', context)

# def login(request):
#     context = {}
#     return render(request, 'base/login.html', context)