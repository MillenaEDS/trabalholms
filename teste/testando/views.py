from django.shortcuts import render, redirect
from testando.models import Curso, Turma, Questao, Resposta
from testando.forms import ContatoForm, CursoForm, QuestaoForm, RespostaForm
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, "home.html")

def curso_home(request):
    return render(request, "curso_home.html")

def calendario(request):
    return render(request, "calendario_aluno.html")

def sobre(request):
    return render(request, "sobre.html")

def area_aluno(request):
    return render(request, "area_aluno.html")

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

@user_passes_test(checa_professor, login_url='/?error=acessonegado', redirect_field_name=None)
@login_required(login_url='/login')

def restrito(request):
    turmas = Turma.objects.all()
    for turma in turmas:
        turma.questoes = Questao.objects.filter(turma=turma)
    contexto={
        "turmas": turmas
    }
    return render(request, "restrito.html", contexto)

@login_required(login_url='/login')
@user_passes_test(checa_aluno, login_url='/?error=acessonegado', redirect_field_name=None)

def restrito_aluno(request):
    turmas = Turma.objects.all()
    for turma in turmas:
        turma.respostas = Resposta.objects.filter(turma=turma)
    contexto={
        "turmas": turmas
    }
    return render(request, "restrito_aluno.html", contexto)

def questao_form(request, turma_sigla, questao_id=None):
    turma = Turma.objects.get(turma_sigla=turma_sigla)
    if questao_id:
        questao = Questao.objects.get(id=questao_id)
    else:
        questao=Questao(turma=turma)

    if request.POST:
        form = QuestaoForm(request.POST, request.FILES, instance=questao)
        if form.is_valid():
            form.save()
            return redirect("/restrito")
    else:
        form = QuestaoForm(instance=questao)
    
    contexto = {
        "form": form,
        "turma_sigla":turma
    }
    
    return render(request, "questao_form.html", contexto)

def resposta_form(request, turma_sigla, resposta_id=None):
    turma = Turma.objects.get(turma_sigla=turma_sigla)
    if resposta_id:
        resposta = Resposta.objects.get(id=resposta_id)
    else:
        resposta=Resposta(turma=turma)

    if request.POST:
        form = RespostaForm(request.POST, request.FILES, instance=resposta)
        if form.is_valid():
            form.save()
            return redirect("/restrito_aluno")
    else:
        form = RespostaForm(instance=resposta)
    
    contexto = {
        "form": form,
        "turma_sigla":turma
    }
    
    return render(request, "resposta_form.html", contexto)