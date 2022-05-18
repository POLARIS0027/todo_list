from django import forms
from .models import TodoList

class DateInput(forms.DateInput):
    input_type = 'date'
    
#モデルフォームを使ってモデルのフィルドを指定すると自動にフォームができる。
class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('name', 'description', 'date_deadline', 'image','file')
        widgets = {'date_deadline':DateInput()}
        