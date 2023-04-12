from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


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