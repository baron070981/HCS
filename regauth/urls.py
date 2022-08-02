from django.contrib import admin
from django.urls import path

from .views import *

# urls regauth
 
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
