from tkinter import CASCADE
from django.db import models


# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name='질문제목')
    content = models.TextField(verbose_name='질문내용')
    create_date = models.DateTimeField(auto_now=True, verbose_name='작성일시')
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='답변제목')
    content = models.TextField(verbose_name='답변내용')
    create_date = models.DateTimeField(auto_now=True, verbose_name='작성일시')
    