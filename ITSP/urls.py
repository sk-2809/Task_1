from django.contrib import admin
from django.urls import path
from ITSP import views

urlpatterns = [
    path('',views.index,name='ITSP'),
    path('form',views.form,name='form'),
    
]