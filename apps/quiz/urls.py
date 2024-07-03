from django.urls import path
from .views import (
    FirstSubjectViewAPI,
    SecondSubjectViewAPI,
    BlockTestViewAPI
)
app_name = 'quiz'

urlpatterns = [
    path('firstSubject/', FirstSubjectViewAPI.as_view()),
    path('secondSubject/', SecondSubjectViewAPI.as_view()),
    path('first/<int:first_id>/', BlockTestViewAPI.as_view())

]
