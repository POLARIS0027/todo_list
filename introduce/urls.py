from django.contrib import admin
from django.urls import path 
from . import views



app_name = 'introduce'

urlpatterns =[
    path('', views.IntroView.as_view(), name='intro'),
    path('jlpt/', views.JLPTView.as_view(), name='jlpt'),
    path('eju/', views.EJUView.as_view(), name='eju'),
    path('converstaion/', views.ConvView.as_view(), name='conversation'),

]