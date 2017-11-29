"""teste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from testando.views import index, home,contato, curso, calendario, area_aluno, curso_home, sobre, aluno, professor, restrito, questao_form, resposta_form, restrito_aluno
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^index', index, name="index"),
    url(r'^$', home, name="home"),
    url(r'^home', home),
    url(r'^aluno/', aluno),
    url(r'^calendario/', calendario),
    url(r'^curso_home/', curso_home, name = "curso_home"),
    url(r'^professor/', professor),
    url(r'^contato/', contato), 
    url(r'^curso/', curso),
    url(r'^sobre/', sobre),
    url(r'^login/', login, { "template_name": "login.html" }), 
    url(r'^logout/', logout),
    url(r'^restrito/$', restrito, name="restrito"),
    url(r'^restrito_aluno/$', restrito_aluno, name="restrito_aluno"),
    url(r'^restrito/(?P<turma_sigla>[A-Z,a-z]+)/questao/(?P<questao_id>[0-9]*)', questao_form, name="questao_form"),
    url(r'^restrito/(?P<turma_sigla>[A-Z,a-z]+)/resposta/(?P<resposta_id>[0-9]*)', resposta_form, name="resposta_form"),
    url(r'^change-password/', auth_views.PasswordChangeView.as_view(template_name='mudar_senha.html'), name="mudar",),
    url(r'^admin/', admin.site.urls),
]

#media/ doc, jpg
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_ROOT=settings.MEDIA_ROOT)
 