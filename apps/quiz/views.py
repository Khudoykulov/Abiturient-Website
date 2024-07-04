from rest_framework import viewsets, generics, status
from apps.subjects.permissions import IsAuthor
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.subjects.models import Subjects, Tests, Answers
from apps.subjects.mixins import CreateViewSetMixin
from rest_framework import generics, viewsets
from .serializers import (
    TestQuizSerializer,
    TestQuizPostSerializer
)
from .models import (
    TestQuiz
)


class TestQuizAPIView(CreateViewSetMixin, viewsets. ModelViewSet):
    model = TestQuiz
    queryset = TestQuiz.objects.all()
    serializer_class = TestQuizSerializer
    serializer_post_class = TestQuizPostSerializer

