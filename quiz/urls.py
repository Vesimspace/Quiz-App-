from django.urls import path
from . views import QuizList, quiz_view, quiz_data_view, save_quiz_view

app_name = 'quiz'

urlpatterns = [
    path('', QuizList.as_view(), name="main-view"),
    path('<pk>/', quiz_view, name="quiz-view"),
    path('<pk>/data/', quiz_data_view, name="quiz-data-view"),
    path('<pk>/save/', save_quiz_view, name="save-view"),
]