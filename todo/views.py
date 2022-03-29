from email.mime import image
from django.forms import ImageField
from django.shortcuts import redirect, render
from todo.forms import TodoCreateForm
from todo.models import TodoList
from django.views.generic import ListView, TemplateView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from datetime import date
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
    context_object_name = 'todo'
    template_name = 'todo/todo_detail.html'
    
class TodoDeleteView(DeleteView):
    model = TodoList
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo:index')
    
class TodoCompleteView(DeleteView):
    model = TodoList
    template_name = 'todo/todo_complete.html'
    success_url = reverse_lazy('todo:index')

class TodoUpdateView(UpdateView):
    model = TodoList
    fields = ['name', 'description', 'date_deadline','image', 'file']
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('todo:index')
    
class TodoCreateView(CreateView):
    model = TodoList
    form_class = TodoCreateForm
    template_name = 'todo/todo_create.html'
    success_url = reverse_lazy('todo:index')
    
    def form_valid(self, form):
            todoimage = form.save(commit=False)
            todoimage.adress =form.cleaned_data['image']
        
            todoimage.save()
            return super().form_valid(form)
