from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('memberInfo/', views.memberInfo, name='memberInfo'),
    path('experience/', views.experience, name='experience'),
    path('delete_experience/', views.delete_experience, name='delete_experience'),
    path('myAudit/', views.myAudit, name='myAudit'),
    path('myAudit_result/', views.myAudit_result, name='myAudit_result'),
    path('myCareer/', views.myCareer, name='myCareer'),
    path('delete_love/', views.delete_love, name='delete_love'),
    path('myPlan_skill/', views.myPlan_skill, name='myPlan_skill'),
    path('myPlan_attitude/', views.myPlan_attitude, name='myPlan_attitude'),
    path('myPlan_licence/', views.myPlan_licence, name='myPlan_licence'),
    path('addPlan_skill/', views.addPlan_skill, name='addPlan_skill'),
    path('addPlan_attitude/', views.addPlan_attitude, name='addPlan_attitude'),
    path('addPlan_licence/', views.addPlan_licence, name='addPlan_licence'),
    path('delete_plan_skill/', views.delete_plan_skill, name='delete_plan_skill'),
    path('delete_plan_attitude/', views.delete_plan_attitude, name='delete_plan_attitude'),
    path('delete_plan_licence/', views.delete_plan_licence, name='delete_plan_licence'),
]