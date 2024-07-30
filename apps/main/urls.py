from django.urls import path, include
from .views import (
    BalanceView,
    MainTestAPIView2,
    MainAnswerAPIView,
    MainTestDetailAPIView2,
    MainTestListAPIView2

)
from rest_framework.routers import DefaultRouter
app_name = 'main'

router = DefaultRouter()

urlpatterns = [
    path('block_detail/<int:pk>/', MainTestDetailAPIView2.as_view()),
    path('block_list/', MainTestListAPIView2.as_view()),
    path('balance/', BalanceView.as_view()),
    path('block/<int:subject_id>/', MainTestAPIView2.as_view()),
    path('block_answer/', MainAnswerAPIView.as_view()),
]
