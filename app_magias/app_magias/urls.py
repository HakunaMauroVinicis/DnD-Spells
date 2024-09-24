"""
URL configuration for app_magias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from magias import views
from utils import popula_magias

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('filter/', views.filter_magias, name='filter_magias'),
    path('autocomplete/', views.autocomplete_magias, name='autocomplete_magias'),
    path('salvar/', popula_magias.magias, name='salvar'),
]

# Configuração para servir arquivos de mídia apenas no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)