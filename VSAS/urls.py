"""VSAS URL Configuration

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

from vsasApp import views

urlpatterns = [
    path('', views.login),
    path('index/<username>/<where>/', views.index, name='index'),
    path('index/<username>/Project/<project_name>/', views.projectShow, name='projectShow'),
    path('index/<username>/Table/<table_name>/', views.tableShow, name='tableShow'),
    path('admin/', admin.site.urls),
    path('test/echarts', views.testEcharts)
]
