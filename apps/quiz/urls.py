from django.urls import path
from .views import (
    FirstSubjectViewAPI,
    SecondSubjectViewAPI
)
app_name = 'quiz'

urlpatterns = [
    path('firstSubject', FirstSubjectViewAPI.as_view()),
    path('secondSubject', SecondSubjectViewAPI.as_view()),

]
