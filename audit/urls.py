from django.urls import path, include
from audit import views


urlpatterns = [
    path('audit_personality/',views.audit_personality, name='audit_personality'),
    path('audit_skill/',views.audit_skill, name='audit_skill'),
    path('audit_attitude/',views.audit_attitude, name='audit_attitude'),
    path('audit_licence/', views.audit_licence, name='audit_licence'),
    path('audit_result/', views.audit_result, name='audit_result'),
]