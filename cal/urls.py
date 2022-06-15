from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cal'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
]