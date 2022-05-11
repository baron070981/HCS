from django.contrib import admin
from django.urls import path

# urls disabled_address_lists


from .views import *
 
urlpatterns = [
    path('', AppListView.as_view(), name='appselbar')
]
