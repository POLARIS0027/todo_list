from django.shortcuts import get_object_or_404, redirect, render
from board.models import Answer, Question
from django.views.generic import ListView, DetailView
from board.forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    #페이지
    page = request.GET.get('page', '1')
    #조회
    question_list = Question.objects.order_by('-create_date')
    #페이지 처리
    paginator = Paginator(question_list, 10) #페이지당 글 10개
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
        #else: 이거 켜면 alert 작동안함
        #    form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'board/question_form.html', context)
