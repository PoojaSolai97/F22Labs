"""Shark_Tank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path
from SharkTank_App.views import *
from django_filters.views import FilterView
from SharkTank_App.models import Data
from SharkTank_App.filters import DataFilter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('home1/', home1),
    path('home2/', home2),
    path('filter/', filter_opr),
    ]
