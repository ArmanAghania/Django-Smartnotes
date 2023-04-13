from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class SingupVeiw(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'


    
# def home(request):
#     return render(request, 'home/welcome.html', {})

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {}) 