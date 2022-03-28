from email.mime import image
from django.forms import ImageField
from django.shortcuts import render
from todo.models import TodoList, TodoList_files, TodoList_images
from django.views.generic import ListView, TemplateView, DetailView, DeleteView

# Create your views here.

class TodoIndexView(ListView):
    context_object_name = 'todo_list'
    template_name = 'todo/todo_index.html' 
    
    def get_queryset(self):
        return TodoList.objects.all()
    
class TodoListView(ListView):
    model = TodoList
    template_name = 'todo/todo_list.html'
    
class TodoDetailView(DetailView):
    model = TodoList
    template_name = 'todo/todo_detail.html'
    
class TodoDeleteView(DeleteView):
    model = TodoList
    template_name = 'todo/todo_delete.html'

