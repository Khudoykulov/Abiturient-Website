from rest_framework import serializers
from .models import FirstSubject, SecondSubject
from apps.subjects.models import Subjects, Tests, Answers
from apps.subjects.serializers import SubjectsSerializer, TestSerializer, AnswerSerializer
from rest_framework.exceptions import ValidationError


# class FirstSubjectSerializer(serializers.ModelSerializer):
#     first_stage = SubjectsSerializer(read_only=True)
#
#     class Meta:
#         model = BlockSubject
#         fields = ['id', 'first_stage']


class FirstSubjectSerializer(serializers.Serializer):
    first_subject_id = serializers.IntegerField()

    class Meta:
        fields = ['first_subject_id']


class SecondSubjectSerializer(serializers.Serializer):
    second_subject_id = serializers.IntegerField()

    class Meta:
        fields = ['second_subject_id']

