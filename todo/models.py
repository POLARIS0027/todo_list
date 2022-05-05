from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=40, verbose_name="Task")
    description = models.TextField(max_length=200, verbose_name="Description")
    date_created = models.DateField(auto_now_add=True, verbose_name="Date")
    date_deadline = models.DateField(verbose_name="Deadline")
    image = models.ImageField(null=True, blank=True, upload_to="", verbose_name='Image')
    file = models.FileField(null=True, blank=True, upload_to="uploads/", verbose_name='File')
    author = models.ForeignKey(User, on_delete=models.CASCADE, name='author')
    
    #別のクラスを作らないでimage,fileフィルドを作ると、１枚しか添付できない。
    
    def remaining_days(self):
        delta = self.date_deadline - date.today()
        days = delta.days
        if days > 0:
            return f'{days}Days reamining'
        elif days == 0:
            return 'Do It Today!!'
        else:
            days = abs(days)
            return f'{days}days passed'
        
    #残った日数を返還するためにdeltaを指定し、daysを与える。
        
    
    def __str__(self):
        return f'{self.name} | {self.description} | {self.date_created} |       {self.date_deadline}'
    
    # __str__を利用してモデルの表示形式を指定する。
    
