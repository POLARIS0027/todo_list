from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name='질문제목')
    content = models.TextField(verbose_name='질문내용')
    create_date = models.DateTimeField(auto_now=True, verbose_name='작성일시')
    author = models.ForeignKey(User, on_delete=models.CASCADE) #userが脱退すると、質問も消える。
    modify_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
    
    def get_absolute_url(self): #answer登録の時、そのquesitonのURLにrideirectする必要があるから設定
        return reverse("board:detail", kwargs={"question_id": self.id})
    
    
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='답변제목') #質問が消えれば答えも消える。
    content = models.TextField(verbose_name='답변내용')
    create_date = models.DateTimeField(auto_now=True, verbose_name='작성일시') #現在時刻で自動入力
    author = models.ForeignKey(User, on_delete=models.CASCADE) #userが脱退すると答えも消える。
    modify_date = models.DateTimeField(auto_now=True) #現在時刻で自動入力
    
class Image(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='imagepost')
    image= models.ImageField(upload_to='board/images', verbose_name='photo', blank=True)
    