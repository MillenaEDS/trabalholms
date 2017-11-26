from django.shortcuts import render
from testando.models import Curso, Turma
from testando.forms import ContatoForm, CursoForm, QuestaoForm
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    
    contexto = {
        "perfil":"sbruble", 
        "cursos":Curso.objects.all()
    }
    
    return render(request, "index.html", contexto)

def checa_aluno(user):
     return user.perfil == 'A'

def checa_professor(user):
     return user.perfil == 'P'

@login_required(login_url='/login')
@user_passes_test(checa_aluno, login_url='/?error=acessonegado', redirect_field_name=None)

def aluno(request):
     return render(request,"aluno.html")

@user_passes_test(checa_professor, login_url='/?error=acessonegado', redirect_field_name=None)
@login_required(login_url='/login')

def professor(request):
     return render(request,"professor.html")

def contato(request):
    
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.enviar_email()
    else:
        form = ContatoForm()
    
    contexto = {
        "form":form
    }
    
    return render(request, "contato.html", contexto)

def curso(request):

    if request.POST:
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()

    contexto = {
        "form":form
    }

    return render(request, "curso.html", contexto)

def disciplina(request):

    contexto = {
        "disciplina":form
    }

    return render(request, "curso.html", contexto)

def restrito(request):
    contexto={
        "turmas":Turma.objects.all()
    }
    return render(request, "restrito.html", contexto)

def questao_form(request):
    
    if request.POST:
        form = QuestaoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestaoForm()
    
    contexto = {
        "form":form
    }
    
    return render(request, "questao_form.html", contexto)
