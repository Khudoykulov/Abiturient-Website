from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SubjectViewSet,
    TestViewSet,
)

app_name = 'subject'

router = DefaultRouter()
router.register('Subjects', SubjectViewSet)
router.register('Tests', TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
