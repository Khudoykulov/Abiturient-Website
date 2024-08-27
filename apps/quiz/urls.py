from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # TestQuizAPIView,
    BlockTestAPIView,
    BlockTestRUPAPIView,
    MandatoryBlockAPIView,
    MandatoryBlockRUDAPIView
)
app_name = 'quiz'
router = DefaultRouter()
# router.register(r'block', TestQuizAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('block_test/', BlockTestAPIView.as_view()),
    path('mandatory/', MandatoryBlockAPIView.as_view()),
    path('block_test/<int:pk>/', BlockTestRUPAPIView.as_view()),
    path('mandatory/<int:pk>/', MandatoryBlockRUDAPIView.as_view())
]
