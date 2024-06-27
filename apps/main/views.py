from django.shortcuts import render
from .serializers import BalanceSerializer
from .models import Portfolio
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
