from rest_framework import serializers
from .models import Portfolio


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['id', 'balance', 'total_balance']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        return super().create(validated_data)

