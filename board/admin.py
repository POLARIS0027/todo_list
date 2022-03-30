from django.contrib import admin
from board.models import Question, Answer
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    
admin.site.register(Question, QuestionAdmin)
    
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']

admin.site.register(Answer, AnswerAdmin)