
import random
from rest_framework import viewsets, generics, status
from apps.subjects.permissions import IsAuthor
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.subjects.models import Subjects, Tests, Answers
from apps.subjects.mixins import CreateViewSetMixin
from rest_framework import generics, viewsets
from .serializers import (
    TestQuizSerializer,
    TestQuizPostSerializer,
    BlockTestPostSerializer
)
from .models import (
    TestQuiz,
)


class TestQuizAPIView(CreateViewSetMixin, viewsets. ModelViewSet):
    model = TestQuiz
    queryset = TestQuiz.objects.all()
    serializer_class = TestQuizSerializer
    serializer_post_class = TestQuizPostSerializer


class BlockTestAPIView(generics.ListCreateAPIView):
    queryset = TestQuiz.objects.all()
    serializer_class = TestQuizSerializer
    serializer_post_class = BlockTestPostSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlockTestPostSerializer
        return TestQuizSerializer
