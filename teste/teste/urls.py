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
from testando.views import index, contato, curso, aluno, professor, restrito, questao_form
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^aluno/', aluno),
    url(r'^professor/', professor),
    url(r'^contato/', contato), 
    url(r'^curso/', curso),
    url(r'^login/', login, { "template_name": "login.html" }), 
    url(r'^logout/', logout),
    url(r'^restrito/$', restrito, name="restrito"),
    url(r'^restrito/questao', questao_form, name="questao_form"),
    url(r'^change-password/', auth_views.PasswordChangeView.as_view(template_name='mudar_senha.html'),),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_ROOT=settings.MEDIA_ROOT)
 