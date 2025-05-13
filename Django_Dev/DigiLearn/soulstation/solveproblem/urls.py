from django.urls import path
from . import views

urlpatterns = [
    # path('solveproblem/', views.members, name='solveproblem'),
    path('question/', views.question_page, name='question_page'),
    path('next-question/', views.get_next_question, name='next_question'),
    path('previous-question/', views.get_previous_question, name='previous_question'),
    path('get-answer/', views.get_answer_view, name='get_answer'),
    # path('question/', views.show_question, name='show_question'),
]