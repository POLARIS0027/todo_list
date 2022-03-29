from django import forms
from .models import TodoList

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('name', 'description', 'date_deadline', 'image', 'file')