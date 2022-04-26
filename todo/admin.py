from django.contrib import admin
from todo.models import TodoList
# Register your models here.


class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_created','date_deadline',          'remaining_days','image','author')
    list_filter = ['date_created', 'author']
    #admin pageでの管理のためfilterをつけて、作成日順、user順でまとめて見られるようにする。
    
admin.site.register(TodoList, TodoListAdmin,)