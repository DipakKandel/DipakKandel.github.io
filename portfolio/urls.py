from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('experience/<int:experience_id>/', views.experience_detail, name='experience_detail'),
]
