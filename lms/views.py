from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def email(request):
    return render(request, "formemail.html")

def matricula(request):
    return render(request, "matricula.html")

def confirmacao(request):
    return render(request, "confirmacao.html")

def acesso(request):
    return render(request, "codigo.html")

def aviso(request):
    return render(request, "avi_prof.html")