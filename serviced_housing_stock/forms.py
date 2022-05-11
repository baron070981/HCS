from django.forms import ModelForm
from django import forms

from .models import ServiceAddressModel



class CreateServiceAddressForm(ModelForm):
    '''форма добавления нового адреса по которому было отключение'''
    class Meta:
        model = ServiceAddressModel
        fields = '__all__'






