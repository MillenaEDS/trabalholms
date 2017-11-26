from django.contrib.auth.admin import UserAdmin

from django import forms

from django.contrib import admin

from testando.models import *

from random import randint


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', )
    list_filter =('sigla',)

admin.site.register(Curso, CursoAdmin)

class GradecurricularAdmin(admin.ModelAdmin):
    list_display = ('sigla_curso', 'ano', 'semestre',)
    list_filter =('sigla_curso', 'ano', 'semestre',)
admin.site.register(Gradecurricular, GradecurricularAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('sigla_curso', 'ano_grade', 'semestre_grade','numero',)
    list_filter =('sigla_curso', 'ano_grade', 'semestre_grade','numero',)
admin.site.register(Periodo, PeriodoAdmin)

def testar_Aluno(n):
    lista = []
    contexto = Usuario.objects.all()
    for x in contexto:
        lista.append(x.ra)
    while n in lista:
        n = randint(100000,199999)
    return n   

class NovoAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('email','sigla_curso', 'nome', 'celular')

    def save(self, commit=True):
        user = super(NovoAlunoForm, self).save(commit=False)
        user.set_password('aluno@floresta')
        user.perfil = 'A'
        n = randint(100000,199999)
        ra_unico = testar_Aluno(n)
        user.ra = ra_unico        
        if commit:
            user.save()
        return user

class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('email','sigla_curso', 'nome','celular')
        
class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm


class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'sigla_curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('email','sigla_curso', 'nome','celular')}),)
    add_fieldsets = (
        (None, {
            'fields': ('email','sigla_curso', 'nome', 'celular')

            } ),
             
         )
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

admin.site.register(Aluno, AlunoAdmin)

def testar_Professor(n):
    lista = []
    contexto = Usuario.objects.all()
    for x in contexto:
        lista.append(x.ra)
    while n in lista:
        n = randint(100000,199999)
    return n   

class NovoProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('ra','email', 'nome','apelido')

    def save(self, commit=True):
        user = super(NovoProfessorForm, self).save(commit=False)
        user.set_password('professor@floresta')
        user.perfil = 'P'
        n = randint(100000,199999)
        ra_unico = testar_Professor(n)
        user.ra = ra_unico        
        if commit:
            user.save()
        return user

class AlterarProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('email', 'nome', 'apelido')
        
class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm


class ProfessorAdmin(UserAdmin):
    form = AlterarProfessorForm
    add_form = NovoProfessorForm
    list_display = ('ra', 'nome','apelido')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('email', 'nome','apelido')}),)
    add_fieldsets = (
        (None, {
            'fields': ( 'email', 'nome','apelido')

            } ),
             
         )
    search_fields = ('email',)
    ordering = ('nome',)
    filter_horizontal = ()
admin.site.register(Professor, ProfessorAdmin)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria','ementa', 'conteudo','bibliografia_basica',)
    list_filter =('nome', 'carga_horaria',)
admin.site.register(Disciplina, DisciplinaAdmin)

class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ('nome_disciplina', 'ano','semestre',)
    list_filter =('nome_disciplina', 'ano','semestre',)
admin.site.register(Disciplinaofertada, DisciplinaOfertadaAdmin)

class PeriodoDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('sigla_curso', 'numero_periodo', 'nome_disciplina', 'ano_grade','semestre_grade',)
    list_filter =('sigla_curso', 'numero_periodo', 'nome_disciplina', 'ano_grade','semestre_grade',)
admin.site.register(Periododisciplina, PeriodoDisciplinaAdmin)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'turno', 'ra_professor', 'nome_disciplina', 'ano_ofertado','semestre_ofertado',)
    list_filter =('turma', 'ra_professor', 'turno',)
admin.site.register(Turma, TurmaAdmin)

class CursoTurmaAdmin(admin.ModelAdmin):
    list_display = ('sigla_curso', 'cod_turma', 'nome_disciplina', 'ano_ofertado','semestre_ofertado',)
    list_filter =('sigla_curso', 'cod_turma', 'nome_disciplina', 'ano_ofertado','semestre_ofertado',)
admin.site.register(Cursoturma, CursoTurmaAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('ra_aluno', 'cod_turma', 'nome_disciplina', 'ano_ofertado','semestre_ofertado',)
    list_filter = ('ano_ofertado','semestre_ofertado',)
admin.site.register(Matricula, MatriculaAdmin)

#admin.site.register(Questao)

#admin.site.register(Arquivoquestao)

#admin.site.register(Resposta)

#admin.site.register(Arquivoresposta)