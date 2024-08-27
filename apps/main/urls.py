from django.urls import path, include
from .views import (
    BalanceView,
    MainTestAPIView2,
    MainAnswerAPIView,
    MainTestDetailAPIView2,
    MainTestListAPIView2,
    BlockMainTest5RUDView,
    BlockMainTest5View,
    MainAnswerBlock5APIView

)
from rest_framework.routers import DefaultRouter
app_name = 'main'
router = DefaultRouter()

urlpatterns = [
    path('balance/', BalanceView.as_view()),
    path('block1_detail/<int:pk>/', MainTestDetailAPIView2.as_view()),
    path('block1_list/', MainTestListAPIView2.as_view()),
    path('block1/<int:subject_id>/', MainTestAPIView2.as_view()),
    path('block1_answer/', MainAnswerAPIView.as_view()),
    path('block5_detail/<int:pk>/', BlockMainTest5RUDView.as_view()),
    path('block5/', BlockMainTest5View.as_view()),
    path('block5_answer/', MainAnswerBlock5APIView.as_view())
]
