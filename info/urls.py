from django.contrib import admin
from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
path('', views.InfoListView.as_view(), name='index'),
path('detail/<int:pk>', views.InfoDetailView.as_view(), name='detail'),
path('search/', views.search, name='search'),  
  
]


