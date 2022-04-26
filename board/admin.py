from django.contrib import admin
from board.models import Question, Answer, Image
# Register your models here.

#質問と答えの数が多くなると、検索が必要なので、search_fieldsを指定してadmin pageで検索できるようにする
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content', 'author']
    
admin.site.register(Question, QuestionAdmin)
    
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content', 'author']

admin.site.register(Answer, AnswerAdmin)

class ImageInline(admin.StackedInline):
    model = Image
    extra = 2

@admin.register(Image)    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'image')