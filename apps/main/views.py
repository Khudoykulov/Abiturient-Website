import random
from apps.quiz.models import TestQuiz
from django.shortcuts import render
from apps.subjects.mixins import CreateViewSetMixin
from .serializers import BalanceSerializer, MainTestSerializer, MainTestPostSerializer, MainAnswerSerializer, MainAnswerBlockSerializer, MainAnswerBlockPostSerializer
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


class MainTestAPIView1(generics.ListCreateAPIView):
    queryset = MainTest.objects.all()
    serializer_class = MainTestSerializer
    serializer_post_class = MainTestPostSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MainTestPostSerializer
        return MainTestSerializer


class MainTestAPIView(CreateViewSetMixin, viewsets.ModelViewSet):
    model = MainTest
    queryset = MainTest.objects.all()
    serializer_class = MainTestSerializer
    serializer_post_class = MainTestPostSerializer


class MainTestAPIView2(generics.ListCreateAPIView):
    queryset = MainTest.objects.all()
    serializer_class = MainTestSerializer
    serializer_post_class = MainTestPostSerializer

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
        queryset = queryset.filter(main_test__subject_quiz_id=subject_id).all()
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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MainAnswerBlockPostSerializer
        return MainAnswerBlockSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['main'] = self.request.data.get('main')
        return ctx

    def create(self, request, *args, **kwargs):
        block_id = self.request.data.get('block')
        main_list = request.data.get('main')

        # Data validation
        if not isinstance(main_list, list):
            return Response({"error": "Invalid data format. 'main' should be a list."},
                            status=status.HTTP_400_BAD_REQUEST)

        created_instances = []
        errors = []

        # Iterate through main_list
        for item in main_list:
            quiz_id = item.get('quiz')
            answer_id = item.get('answer')

            # Create and save the MainAnswer instance
            serializer = self.get_serializer(data={
                'main': block_id,
                'quiz': quiz_id,
                'answer': answer_id
            })

            if serializer.is_valid():
                instance = serializer.save()
                created_instances.append(instance)
            else:
                errors.append(serializer.errors)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(MainAnswerSerializer(created_instances, many=True).data, status=status.HTTP_201_CREATED)













        #
        # main = self.request.data.get('main')
        # data = self.request.data
        # print(block_id)
        # print(main)
        # print(data)
        # serializer = self.serializer_post_class(data=request.data)
        # if serializer.is_valid():
        #     for i in main:
        #         quiz_id = i['quiz']
        #         answer_id = i['answer']
        #         print(i['quiz'])
        #         print(i['answer'])
        #         serializer.save(block_id=block_id, main__quiz=quiz_id, main__answer=answer_id)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
