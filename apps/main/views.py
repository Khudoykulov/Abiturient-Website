import random
from apps.quiz.models import TestQuiz, Mandatory
from .serializers import (
    BalanceSerializer,
    MainTestSerializer,
    MainTestPostSerializer,
    MainAnswerBlockSerializer,
    MainAnswerBlockPostSerializer,
    BlockTestFirstPostSerializer,
    BlockTestSecondPostSerializer, BlockMainTest5Serializer, BlockMainTest5PostSerializer,
    MainAnswerBlock5PostSerializer
)

from .models import Portfolio, MainTest, MainAnswer, MainAnswerBlock, BlockMainTest5, MainAnswerBlock5
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


class MainTestDetailAPIView2(generics.RetrieveDestroyAPIView):
    queryset = MainTest.objects.all()
    serializer_class = MainTestSerializer
    # permission_classes = [IsAuthor]


class MainTestListAPIView2(generics.ListAPIView):
    queryset = MainTest.objects.all()
    serializer_class = MainTestSerializer
    # permission_classes = [IsAuthor]

    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.request.user.id
        queryset = queryset.filter(author_id=author_id).all()
        return queryset


class MainTestAPIView2(generics.CreateAPIView):
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

    def create(self, request, *args, **kwargs,):
        author = request.user
        subject_id = self.kwargs.get('subject_id')
        main_test = TestQuiz.objects.filter(subject_quiz_id=subject_id, max_point=3.1).all()
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


# class BlockTestFirstAPIView2(generics.CreateAPIView):
#     queryset = MainTest.objects.all()
#     serializer_class = MainTestSerializer
#     serializer_post_class = BlockTestFirstPostSerializer
#     # permission_classes = [IsAuthor]
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return BlockTestFirstPostSerializer
#         return MainTestSerializer
#
#     def get_serializer_context(self):
#         ctx = super().get_serializer_context()
#         subject_id = self.kwargs.get('subject_id')
#         ctx['subject_id'] = subject_id
#         return ctx
#
#     def create(self, request, *args, **kwargs,):
#         author = request.user
#         subject_id = self.kwargs.get('subject_id')
#         main_test = TestQuiz.objects.filter(subject_quiz_id=subject_id, max_point=3.1).all()
#         main_test_random = random.choice(main_test).id
#         print(main_test_random, 'random')
#         if subject_id is None:
#             return Response({"error": "subject_id is required in URL"}, status=status.HTTP_400_BAD_REQUEST)
#
#         if author is None:
#             return Response({"error": "author is required in request data"}, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = self.serializer_post_class(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save(author=author, main_test_id=main_test_random)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockMainTest5View(generics.CreateAPIView):
    queryset = BlockMainTest5
    serializer_class = BlockMainTest5PostSerializer

    def create(self, request, *args, **kwargs,):
        author = request.user
        mandatory_subject = Mandatory.objects.all()
        mandatory_subject_random = random.choice(mandatory_subject).id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(author=author, mandatory_subject_id=mandatory_subject_random)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockMainTest5RUDView(generics.RetrieveDestroyAPIView):
    queryset = BlockMainTest5
    serializer_class = BlockMainTest5Serializer


class MainAnswerBlock5APIView(generics.ListCreateAPIView):
    queryset = MainAnswerBlock5.objects.all()
    serializer_class = MainAnswerBlockSerializer
    serializer_post_class = MainAnswerBlock5PostSerializer
    # permission_classes = [IsAuthor]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MainAnswerBlock5PostSerializer
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
