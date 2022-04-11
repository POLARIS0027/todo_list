from django.shortcuts import render
from django.db.models import Q
from board.models import Question, Answer

# Create your views here.

def searchResult(request):
    if 'kw' in request.POST:
        query = request.POST.get('kw',"")
        questions_search = Question.objects.all().filter(Q(subject__icontains=query)|Q(content__icontains=query))
        context = {'query': query, 'question_search': questions_search }
        
    return render(request, 'search/search.html', context)

