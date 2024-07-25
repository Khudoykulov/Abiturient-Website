from django.urls import path, include
from .views import (
    BalanceView,
    MainTestAPIView2,
    # MainTestAPIView,
    MainAnswerAPIView
)
from rest_framework.routers import DefaultRouter
app_name = 'main'

router = DefaultRouter()
# router.register('main_test', MainTestAPIView)

urlpatterns = [
    path('balance/', BalanceView.as_view()),
    # path('main_block1/', MainTestAPIView1.as_view()),
    # path('', include(router.urls)),
    path('subject/<int:subject_id>/', MainTestAPIView2.as_view()),
    path('main_answer/', MainAnswerAPIView.as_view())
]
