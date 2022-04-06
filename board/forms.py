from urllib import request
from django import forms
from board.models import Answer, Question, Image
from django.forms import inlineformset_factory

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용하는 모델
        fields = ['subject', 'content',] #폼에서 사용할 모델 속성
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
