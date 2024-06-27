from rest_framework import serializers
from .models import Portfolio
from django.core.exceptions import ValidationError


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

