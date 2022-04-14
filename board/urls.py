from django.contrib import admin
from django.urls import path 
from board.views import index, detail, answer_create, QuestionDeleteView, AnswerDeleteView, question_create, question_modify
from board import views

app_name = 'board'

urlpatterns =[
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_create, name='answer_create'),
    path('question/create/', question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_modify, name='question_modify'),
    path('question/delete/<int:pk>/', QuestionDeleteView.as_view(), name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:pk>/', AnswerDeleteView.as_view(), name='answer_delete'),
    path('search/', views.search, name='search'),
]