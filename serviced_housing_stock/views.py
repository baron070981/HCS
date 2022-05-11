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

from .models import *
from .forms import *



class ServiceAddressListView(ListView):
    '''Представление списка адресов'''
    paginate_by = 15 # количество адресов отображаемых на странице. пагинация
    model = ServiceAddressModel
    template_name = 'serviced_housing_stock/serviceadresseslist.html'
    context_object_name = 'serviceaddresslist'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = [{'name':'добавить адрес', 'urls':'createservaddress'}]
        context['delete'] = {'text':'удал.', 'urls':'delservaddress'}
        context['home'] = {'text':'на главную', 'urls':'appselbar'}
        return context
    
    
    def get_queryset(self):
        return ServiceAddressModel.objects.order_by('city', 'street', 'house')



class CreateServiceAddress(CreateView):
    ''''''
    form_class = CreateServiceAddressForm
    template_name = 'serviced_housing_stock/create_service_address.html'
    context_object_name = 'form'
    success_url = reverse_lazy('servaddresslist')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return dict(list(context.items()))




class DeleteServiceAddress(DeleteView):
    ''''''
    model = ServiceAddressModel
    template_name = 'disabled_address_lists/delete_disabled_address.html'
    success_url = reverse_lazy('servaddresslist')














