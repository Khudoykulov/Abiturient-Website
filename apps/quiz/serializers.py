from rest_framework import serializers
from .models import FirstSubject, SecondSubject, BlockTest
from apps.subjects.models import Subjects, Tests, Answers
from apps.subjects.serializers import SubjectsSerializer, TestSerializer, AnswerSerializer
from rest_framework.exceptions import ValidationError


class FirstSubjectSerializer(serializers.Serializer):
    first_subject_id = serializers.IntegerField()

    class Meta:
        fields = ['first_subject_id']


class SecondSubjectSerializer(serializers.Serializer):
    second_subject_id = serializers.IntegerField()

    class Meta:
        fields = ['second_subject_id']


class BlockSubjectSerializer(serializers.ModelSerializer):
    tests = AnswerSerializer(many=True)
    subject = SubjectsSerializer(read_only=True)

    class Meta:
        model = Tests
        fields = ['id', 'subject', 'body', 'tests']

    def create(self, validated_data):
        first_id = self.context.get('first_id')
        validated_data['first_id'] = first_id
        return super().create(validated_data)
