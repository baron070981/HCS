from django.contrib import admin
from django.urls import path

# urls disabled_address_lists


from .views import *
 
urlpatterns = [
    path('', DisabledAddressListView.as_view(), name='disaddresslist'),
    path('create/', CreateDisabledAddress.as_view(), name='createaddress'),
    path('upd/<int:pk>', UpdateDisabledAddress.as_view(), name='updaddress'),
    path('del/<int:pk>', DeleteDisabledAddress.as_view(), name='deladdress'),
]







