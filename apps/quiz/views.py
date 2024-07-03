from rest_framework import viewsets, generics, status
from apps.subjects.permissions import IsAuthor
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.subjects.models import Subjects, Tests, Answers
from apps.subjects.mixins import CreateViewSetMixin
from rest_framework import generics, viewsets
from .serializers import (
    FirstSubjectSerializer,
    SecondSubjectSerializer,
    BlockSubjectSerializer
)
from .models import SecondSubject, FirstSubject, BlockTest


class FirstSubjectViewAPI(generics.GenericAPIView):
    queryset = FirstSubject.objects.all()
    serializer_class = FirstSubjectSerializer
    permission_classes = [IsAuthor]

    def post(self, request, *args, **kwargs):
        """
            {
                "first_subject_id: 2"
            }
        """
        first_subject_id = request.data.get('first_subject_id')
        if not SecondSubject.objects.order_by('-id').first() is None:
            second_id = SecondSubject.objects.order_by('-id').first().id
        else:
            second_id = 1
        if not FirstSubject.objects.order_by('-id').first() is None:
            first_id = FirstSubject.objects.order_by('-id').first().id
        else:
            first_id = 1
        get_object_or_404(Subjects, id=first_subject_id)
        if first_id == second_id:
            FirstSubject.objects.create(first_stage_id=first_subject_id)
            return Response({'detail': 'First Subjects create '})
        return Response({'detail': 'birinchi blockni tanlab tulgansz ikkinchi blokni tanlang '})


class SecondSubjectViewAPI(generics.GenericAPIView):
    queryset = SecondSubject.objects.all()
    serializer_class = SecondSubjectSerializer
    permission_classes = [IsAuthor]

    def post(self, request, *args, **kwargs):
        """
            {
                "second_subject_id: 2"
            }
        """
        second_subject_id = request.data.get('second_subject_id')
        if not FirstSubject.objects.order_by('-id').first() is None:
            first_id = FirstSubject.objects.order_by('-id').first().id
        else:
            return Response({'detail': 'oldin birinchi blockni tanlang'})
        if not SecondSubject.objects.order_by('-id').first() is None:
            second_id = SecondSubject.objects.order_by('-id').first().id
        else:
            second_id = first_id-1
        get_object_or_404(Subjects, id=second_subject_id)
        first_subject_id = get_object_or_404(Subjects, name=FirstSubject.objects.order_by('-id').first()).id
        if second_id == first_id-1:
            if second_subject_id == first_subject_id:
                return Response({'detail': 'bu fanni birinchi blokga tanlagansz '})
            SecondSubject.objects.create(second_subject_id=second_subject_id)
            return Response({'detail': 'First Subjects create '})
        return Response({'detail': 'oldin birinchi blockni tanlang  '})


class BlockTestViewAPI(generics.ListCreateAPIView):
    queryset = Tests.objects.all()
    serializer_class = BlockSubjectSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        first_id = self.kwargs.get('first_id')
        ctx['first_id'] = first_id
        return ctx

    def get_queryset(self):
        first_id = self.kwargs.get('first_id')
        qs = super().get_queryset()
        if first_id:
            return qs.filter(subject_id=first_id)
        return qs.none()
