"""KAudit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from career import views


urlpatterns = [
    path('career/',views.career, name='career'),
    path('myCareer_result/', views.myCareer_result, name='myCareer_result'),
    path('search/',views.search, name='search'),
    path('message/',views.message, name='message'),
    path('love/', views.love, name='love'),
    path('add/', views.add, name='add'),
    path('addCareer/', views.addCareer, name='addCareer'),
]