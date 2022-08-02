from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


# regauth

class LoginUser(LoginView):
    ''''''
    form_class = AuthenticationForm
    template_name = 'regauth/loginout.html'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
    
    def get_success_url(self):
        return reverse_lazy('appselbar')
    
    
    
def logout_user(request):
    logout(request)
    return redirect('appselbar')




