from django.contrib import admin
from django.urls import path

from .views import *

# urls serviced_housing_stock
 
urlpatterns = [
    # список адресов
    path('', ServiceAddressListView.as_view(), name='servaddresslist'),
    # добавление адреса
    path('create/', CreateServiceAddress.as_view(), name='createservaddress'),
    # удаление адреса
    path('del/<int:pk>', DeleteServiceAddress.as_view(), name='delservaddress'),
    path('upd/<int:pk>', UpdateServiceAddress.as_view(), name='updservaddress'),
]











