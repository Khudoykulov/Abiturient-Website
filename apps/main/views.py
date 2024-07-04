from django.shortcuts import render
from apps.subjects.mixins import CreateViewSetMixin
from .serializers import BalanceSerializer, MainTestSerializer, MainTestPostSerializer
from .models import Portfolio, MainTest
from rest_framework import generics, viewsets
from .permissions import IsAuthor


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


# class MainTestAPIView(generics.ListAPIView):
#     queryset = MainTest.objects.all()
#     serializer_class = MainTestSerializer

class MainTestAPIView(CreateViewSetMixin, viewsets.ModelViewSet):
    model = MainTest
    queryset = MainTest.objects.all()
    serializer_class = MainTestSerializer
    serializer_post_class = MainTestPostSerializer