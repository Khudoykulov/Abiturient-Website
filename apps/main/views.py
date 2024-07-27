import random
from apps.quiz.models import TestQuiz
from .serializers import (
    BalanceSerializer,
    MainTestSerializer,
    MainTestPostSerializer,
    MainAnswerBlockSerializer,
    MainAnswerBlockPostSerializer,
)

from .models import Portfolio, MainTest, MainAnswer, MainAnswerBlock
from rest_framework import generics, viewsets, status
from .permissions import IsAuthor
from rest_framework.response import Response


class BalanceView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        user_id = self.request.user.id
        qs = super().get_queryset()
        if user_id:
            return qs.filter(author_id=user_id)
        return qs.none()


class MainTestAPIView2(generics.ListCreateAPIView):
    queryset = MainTest.objects.all()
    serializer_class = MainTestSerializer
    serializer_post_class = MainTestPostSerializer
    # permission_classes = [IsAuthor]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MainTestPostSerializer
        return MainTestSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        subject_id = self.kwargs.get('subject_id')
        ctx['subject_id'] = subject_id
        return ctx

    def get_queryset(self):
        queryset = super().get_queryset()
        subject_id = self.kwargs.get('subject_id')
        author_id = self.request.user.id
        queryset = queryset.filter(main_test__subject_quiz_id=subject_id, author_id=author_id).all()
        return queryset

    def create(self, request, *args, **kwargs,):
        author = request.user
        subject_id = self.kwargs.get('subject_id')
        main_test = TestQuiz.objects.filter(subject_quiz_id=subject_id).all()
        main_test_random = random.choice(main_test).id
        print(main_test_random, 'random')
        if subject_id is None:
            return Response({"error": "subject_id is required in URL"}, status=status.HTTP_400_BAD_REQUEST)

        if author is None:
            return Response({"error": "author is required in request data"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_post_class(data=request.data)

        if serializer.is_valid():
            serializer.save(author=author, main_test_id=main_test_random)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MainAnswerAPIView(generics.ListCreateAPIView):
    queryset = MainAnswerBlock.objects.all()
    serializer_class = MainAnswerBlockSerializer
    serializer_post_class = MainAnswerBlockPostSerializer
    # permission_classes = [IsAuthor]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MainAnswerBlockPostSerializer
        return MainAnswerBlockSerializer

    def get_serializer_context(self):
        user = self.request.user
        ctx = super().get_serializer_context()
        ctx['user'] = user
        return ctx

    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.request.user.id
        queryset = queryset.filter(block__author_id=author_id).all()
        return queryset










