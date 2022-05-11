from django.forms import ModelForm
from django import forms

from .models import DisabledAdressesModel, AddressModel





class CreateDisabledAddressForm(ModelForm):
    '''форма добавления нового адреса по которому было отключение'''
    class Meta:
        model = DisabledAdressesModel
        fields = '__all__'















