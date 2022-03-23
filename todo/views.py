from django.shortcuts import render
from todo.models import TodoList, TodoList_files, TodoList_images
from django.views.generic import ListView, DetailView

# Create your views here.

class IndexView(ListView):
    context_object_name = 'todo_list'
    template_name = 'todo/todo_list.html' 
    
    def get_queryset(self):
        return TodoList.objects.all()
    
