from urllib import request
from django import forms
from board.models import Answer, Question, Image
from django.forms import inlineformset_factory

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #使用するモデル
        fields = ['subject', 'content',] #フォームで使おうとするモデルのフィルド
        labels = {
            'subject': '제목',
            'content': '내용',
            
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels ={
            'content': '답변내용',
        }
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image',]
        
ImageFormSet = inlineformset_factory(Question, Image, form=ImageForm, extra=3)
#Inlineformset_factoryを利用して、フォームの中に他のフォームを挿入し一つのフォームのように使える。
