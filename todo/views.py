from email.mime import image
from django.forms import ImageField
from django.shortcuts import redirect, render
from requests import request
from todo.forms import TodoCreateForm
from todo.models import TodoList
from django.views.generic import ListView, TemplateView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#Loginが必要なviewには、LoninRequiredMixinを継承させる。

class TodoIndexView(LoginRequiredMixin, ListView):
    context_object_name = 'todo_list'
    template_name = 'todo/todo_index.html' 
    login_url='common:login'
    
    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user)
    
class TodoListView(LoginRequiredMixin, ListView):
    model = TodoList
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_list'
    login_url='common:login'
    
    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user)
    
    #filterをつけて、要請したユーザのものとidが一致するTodoだけど表示する
    
class TodoDetailView(LoginRequiredMixin, DetailView):
    model = TodoList
    context_object_name = 'todo'
    template_name = 'todo/todo_detail.html'
    login_url='common:login'

    
class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo:index')
    login_url='common:login'
    
class TodoCompleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    template_name = 'todo/todo_complete.html'
    success_url = reverse_lazy('todo:index')
    login_url='common:login'

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoList
    fields = ['name', 'description', 'date_deadline','image', 'file']
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('todo:index')
    login_url='common:login'
    
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    form_class = TodoCreateForm
    template_name = 'todo/todo_create.html'
    success_url = reverse_lazy('todo:index')
    login_url='common:login'
    
    def form_valid(self, form):
            todoimage = form.save(commit=False) #commit=Falseにしてしたの行も適応できるようにする。
            todoimage.adress =form.cleaned_data['image']
            todoimage.author = self.request.user
            todoimage.save()
            return super().form_valid(form)
