from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#イメージ一枚だけを表示する予定なので、TemplateViewだけで十分

class IntroView(TemplateView):
    template_name = 'introduce/intro.html'
    
class JLPTView(TemplateView):
    template_name = 'introduce/jlpt.html'
    
class EJUView(TemplateView):
    template_name = 'introduce/eju.html'
    
class ConvView(TemplateView):
    template_name = 'introduce/conv.html'
