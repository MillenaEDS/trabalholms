from django import forms
from testando.models import Curso, Questao, Resposta

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = "__all__"


class ContatoForm(forms.Form):
    
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()

    def enviar_email(self):
        print(
            "Email para você:\n"+
            "Aluno: "+self.cleaned_data["nome"]+"\n"+
            "E-mail: "+self.cleaned_data["email"]+"\n"+
            "Mensagem: "+self.cleaned_data["mensagem"]
        )

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        exclude = ["turma"]

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        exclude = ["turma"]
