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


def index(request):
    data = {'menu':[('a','first'), ('b','second')]}
    return render(request, 'app_selection_bar/app_selection.html', context=data)




class AppListView(TemplateView):
    ''''''
    template_name = 'app_selection_bar/app_selection.html'
    context_object_name = 'applist'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = [{'name':'Списки отключенных адресов','urls': 'disaddresslist'}, 
                           {'name':'Списки жил.фонда на обслуживании','urls': 'servaddresslist'}]
        return context








