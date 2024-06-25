from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SubjectViewSet,
    TestViewSet,
    AnswerViewSet,
)

app_name = 'subject'

router = DefaultRouter()
router.register('Subjects', SubjectViewSet)
router.register('Tests', TestViewSet)
router.register('answer', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
