"""TASK_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from ITSP import views

admin.site.site_header = "ITSP Admin"
admin.site.site_title = "ITSP Portal"
admin.site.index_title = "Welcome to ITSP Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ITSP.urls')),
    path('form',include('ITSP.urls')),
    path('navigate',views.navigate),
    path('ITS2020<int:id>',views.details),
    path('list',views.ITSP_List),
    path('list/<int:id>',views._List),
]
