from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Info(models.Model):
    title = models.CharField(max_length=60, verbose_name='title')
    content = models.TextField(max_length=200, verbose_name='content')
    date_created = models.DateField(auto_now_add=True, verbose_name='date')
    file = models.FileField(null=True, blank=True, upload_to="uploads/", verbose_name='file')
    
