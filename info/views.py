from distutils.log import info
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from info.models import Post

# Create your views here.

class InfoListView(ListView):
    model = Post
    template_name = 'info/infolist.html'
    paginator = Paginator(question_list, 10) #페이지당 글 10개
    page_obj = paginator.get_page(page)
    context = {'info_list': page_obj}

    
class InfoDetailView(DetailView):
    model = Post
    template_name = 'info/info_detail.html'
    context_object_name = 'info'
    
