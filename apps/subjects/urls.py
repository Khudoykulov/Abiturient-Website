from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SubjectViewSet,
    TestViewSet,
    AnswerViewSet,
    TagAPIView
)

app_name = 'subject'

router = DefaultRouter()
router.register('Subjects', SubjectViewSet)
router.register('Tests', TestViewSet)
router.register('answer', AnswerViewSet)
router.register(r'block/tag', TagAPIView)


urlpatterns = [
    path('', include(router.urls)),
]
