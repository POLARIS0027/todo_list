from django.contrib import admin
from info.models import Post
# Register your models here.


class InfoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_created','file')
    list_filter = ['date_created']
    
admin.site.register(Post, InfoListAdmin,)