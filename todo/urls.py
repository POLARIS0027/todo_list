from django.contrib import admin
from django.urls import path 
from todo.views import TodoDeleteView, TodoIndexView, TodoListView, TodoDetailView, TodoUpdateView, TodoCreateView, TodoCompleteView

#includeしてもらったURLを分けて管理すると、app_nameを通じて簡単にurlを管理できる。

app_name = 'todo'

urlpatterns =[
    path('', TodoIndexView.as_view(), name='index'),
    path('list/', TodoListView.as_view(), name='list'),
    path('detail/<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='update'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('complete/<int:pk>/', TodoCompleteView.as_view(), name='complete'),
    
    
]