from django.urls import path, include
from .views import (
    BalanceView,
    MainTestAPIView2,
    MainAnswerAPIView,
)
from rest_framework.routers import DefaultRouter
app_name = 'main'

router = DefaultRouter()

urlpatterns = [
    path('balance/', BalanceView.as_view()),
    path('subject/<int:subject_id>/', MainTestAPIView2.as_view()),
    path('main_answer/', MainAnswerAPIView.as_view()),
]
