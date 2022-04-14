from distutils.log import info
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

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

    
class InfoDetailView(LoginRequiredMixin, DetailView):
    login_url='common:login'
    model = Info
    template_name = 'info/info_detail.html'
    context_object_name = 'info'
    
def search(request):
    content_list = Info.objects.all()
    search = request.GET.get('search','')
    if search:
        search_list = content_list.filter(
            Q(title__icontains = search)|Q(content__icontains = search)|Q(file__icontains = search )
        )
        paginator = Paginator(search_list, 10)
        page = request.GET.get('page','')
        infos = paginator.get_page(page)
        info = Info.objects.all()
        
        return render(request, 'info/search.html',{'infos':infos, 'info':info, 'search':search})