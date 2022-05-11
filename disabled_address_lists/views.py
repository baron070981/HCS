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

from .models import DisabledAdressesModel
from .forms import CreateDisabledAddressForm



class DisabledAddressListView(ListView):
    ''''''
    paginate_by = 5
    model = DisabledAdressesModel
    template_name = 'disabled_address_lists/disabled_list_read.html'
    context_object_name = 'addresslist'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = {'ADD':'Новая запись'}
        return context





class CreateDisabledAddress(CreateView):
    ''''''
    form_class = CreateDisabledAddressForm
    template_name = 'disabled_address_lists/create_disabled_address.html'
    context_object_name = 'form'
    success_url = reverse_lazy('disaddresslist')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))




class UpdateDisabledAddress(UpdateView):
    ''''''
    model = DisabledAdressesModel
    form_class = CreateDisabledAddressForm
    template_name = 'disabled_address_lists/create_disabled_address.html'
    context_object_name = 'form'
    success_url = reverse_lazy('disaddresslist')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeleteDisabledAddress(DeleteView):
    ''''''
    model = DisabledAdressesModel
    template_name = 'disabled_address_lists/delete_disabled_address.html'
    success_url = reverse_lazy('disaddresslist')


















