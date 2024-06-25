from django.shortcuts import render
from .mixins import CreateViewSetMixin
from .models import Subjects, Answers, Tests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import (
    SubjectsSerializer,
    TestSerializer,
    TestPostSerializer
)
from rest_framework import viewsets, generics, status, permissions
from .permissions import (
    IsAuthor,
    IsAdminOrReadOnly
)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['id', 'name']


class TestViewSet(viewsets.ModelViewSet, CreateViewSetMixin):
    queryset = Tests.objects.all()
    model = Tests
    serializer_class = TestSerializer
    serializer_post_class = TestPostSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['id', 'body', 'level', 'subject']
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['subject',]
