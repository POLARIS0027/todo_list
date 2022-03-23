from django.contrib import admin
from todo.models import TodoList, TodoList_files, TodoList_images
# Register your models here.

class TodoList_imagesInline(admin.StackedInline):
    model = TodoList_images

class TodoList_filesInline(admin.StackedInline):
    model = TodoList_files

class TodoListAdmin(admin.ModelAdmin):
    inlines = [TodoList_filesInline, TodoList_imagesInline]
    list_display = ('name', 'description', 'date_created','date_deadline',          'remaining_days')
    list_filter = ['date_created']
    
admin.site.register(TodoList, TodoListAdmin)