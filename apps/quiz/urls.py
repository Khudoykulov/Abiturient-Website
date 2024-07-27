from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TestQuizAPIView,
    BlockTestAPIView
)
app_name = 'quiz'
router = DefaultRouter()
router.register(r'block', TestQuizAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('block_test/', BlockTestAPIView.as_view())
]
