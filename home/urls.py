from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('links/', views.links, name='links'),
]