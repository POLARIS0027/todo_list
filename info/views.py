from distutils.log import info
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from info.models import Info

# Create your views here.

class InfoListView(ListView):
    model = Info
    template_name = 'info/infolist.html'
    paginate_by = 10
    ordering = '-date_created'
    
    def get_context_data(self, **kwargs):
        context = super(InfoListView, self).get_context_data()
        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=0)
        context['pagelist'] = pagelist       
        return context
    
    def get_queryset(self):
        info_list = Info.objects.order_by('-date_created')
        return info_list

    
class InfoDetailView(DetailView):
    model = Info
    template_name = 'info/info_detail.html'
    context_object_name = 'info'
    
