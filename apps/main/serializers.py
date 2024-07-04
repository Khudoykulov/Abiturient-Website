from rest_framework import serializers
from .models import Portfolio, MainTest
from django.core.exceptions import ValidationError
from apps.quiz.serializers import TestQuizSerializer


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['id', 'balance', 'total_balance',]

    # def validated_data(self):
    #     if self.balance < 0:
    #         raise ValidationError('detail', 'promo name is required')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        return super().create(validated_data)


class MainTestSerializer(serializers.ModelSerializer):
    main_test = TestQuizSerializer(read_only=True)

    class Meta:
        model = MainTest
        fields = ['id', 'main_test']


class MainTestPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainTest
        fields = ['id', 'main_test']
