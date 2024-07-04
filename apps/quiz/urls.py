from django.urls import path
from .views import (
    FirstSubjectViewAPI,
    SecondSubjectViewAPI,
    BlockTestViewAPI,
    BlockPostTestViewAPI,
    BlockPost1111111111TestViewAPI
)
app_name = 'quiz'

urlpatterns = [
    path('firstSubject/', FirstSubjectViewAPI.as_view()),
    path('secondSubject/', SecondSubjectViewAPI.as_view()),
    path('first/<int:first_id>/', BlockTestViewAPI.as_view()),
    path('quiz_post/', BlockPostTestViewAPI.as_view()),
    path('quiz_post11111111111111111/', BlockPost1111111111TestViewAPI.as_view()),



]
