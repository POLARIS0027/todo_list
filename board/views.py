from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from board.models import Answer, Question, Image
from django.views.generic import ListView, DetailView, CreateView
from board.forms import QuestionForm, AnswerForm, ImageFormSet
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

# Create your views here.

def index(request):
    #ページ
    page = request.GET.get('page', '1')
    #ページ照会
    question_list = Question.objects.order_by('-create_date')
    #ページ処理
    paginator = Paginator(question_list, 10) #１ページあたり掲示物の数
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'board/question_list.html', context)

@login_required(login_url='common:login') #関数型viewの場合は、デコレーターをつけてログインを必要とさせる
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
        
    context = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST': #同じフォームを再利用するため、postとgetに分けて作成、修正を分ける。
        question_form = QuestionForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if question_form.is_valid() and image_formset.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question.save()
            image_formset.instance = question
            image_formset.save()
            return redirect('board:index')
    else:
        question_form = QuestionForm()
        image_formset = ImageFormSet()
    context = {'question_form': question_form, 'image_formset': image_formset}
    return render(request, 'board/question_form.html', context)

#질문 수정
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author: #本人確認
        messages.error(request, '수정 권한이 없습니다')
        return redirect('board:detail', question_id=question.id)
    if request.method == "POST":
        question_form = QuestionForm(request.POST, instance=question)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if question_form.is_valid() and image_formset.is_valid():
            question = question_form.save(commit=False)
            question.save()
            image_formset.instance = question
            image_formset.save()
            return redirect('board:detail', question_id=question.id)
    else:
        question_form = QuestionForm(instance = question)
        image_formset = ImageFormSet(instance = question)
    context={'question_form': question_form, 'image_formset': image_formset}
    return render(request, 'board/question_form.html', context)

#답변 수정
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
    
    def get_success_url(self):
        return reverse('board:detail', kwargs={'question_id': self.object.question.id})
    
def search(request):
    content_list = Question.objects.all() #まずはobjectを読み取る
    search = request.GET.get('search','')
    if search:
        search_list = content_list.filter(
            Q(subject__icontains = search)|Q(content__icontains = search) #QとicontainsでOR検索し小文字大文字区別をしなくする。
        )
        paginator = Paginator(search_list, 10)
        page = request.GET.get('page','')
        questions = paginator.get_page(page)
        question = Question.objects.all()
        
        return render(request, 'board/search.html',{'questions':questions, 'question':question, 'search':search})
    
    

        
    

    

