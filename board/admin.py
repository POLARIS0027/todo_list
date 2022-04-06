from django.contrib import admin
from board.models import Question, Answer, Image
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    
admin.site.register(Question, QuestionAdmin)
    
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']

admin.site.register(Answer, AnswerAdmin)

class ImageInline(admin.StackedInline):
    model = Image
    extra = 2

@admin.register(Image)    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'image')