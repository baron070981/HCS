"""HCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

# urls всего проекта


urlpatterns = [
    path('admin/', admin.site.urls),
    # списки отключенных адресов
    path('dis/', include('disabled_address_lists.urls')),
    # вход/выход
    path('loginout/', include('regauth.urls')),
    # главное меню. выбор приложения
    path('', include('app_selection_bar.urls')),
    # списки ослуживаемого жил.фонда
    path('serv/', include('serviced_housing_stock.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
