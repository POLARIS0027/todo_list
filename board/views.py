from django.shortcuts import get_object_or_404, redirect, render
from board.models import Answer, Question
from django.views.generic import ListView, DetailView
from board.forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse

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

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
        #else: 이거 켜면 alert 작동안함
        #    form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('board:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context={'form':form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('board:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()
            return redirect('board:detail', question_id=answer.question.id)
    else:
        form = QuestionForm(instance=answer)
    context={'form':form}
    return render(request, 'board/answer_form.html', context)

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'board/question_delete.html'
    success_url = reverse_lazy('board:index')
    
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('board:index')
        else:
            return super(QuestionDeleteView, self).dispatch(request, *args, **kwargs)
        
class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = 'board/answer_delete.html'
    success_url = reverse_lazy('board:index')
    
    

        
    

    

