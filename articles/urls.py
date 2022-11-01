from django.urls import path, redirect
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index')
]