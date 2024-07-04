from rest_framework import serializers
from .models import FirstSubject, SecondSubject, BlockTest
from apps.subjects.models import Subjects, Tests, Answers
from apps.subjects.serializers import SubjectsSerializer, TestSerializer, AnswerSerializer, AnswerQuizSerializer, TestQuizSerializer
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
    test_id = serializers.IntegerField()

    class Meta:
        model = Tests
        fields = ['test_id']

    def create(self, validated_data):
        first_id = self.context.get('first_id')
        validated_data['first_id'] = first_id
        return super().create(validated_data)


class BlockPostSubjectSerializer(serializers.ModelSerializer):
    test_id = serializers.IntegerField()

    class Meta:
        model = Tests
        fields = ['test_id']



class BlockSubjectPostSerializer(serializers.ModelSerializer):
    tests = TestQuizSerializer(many=True,)

    class Meta:
        model = Tests
        fields = ['id', 'tests',]

    def create(self, validated_data):
        subject_id = validated_data.get('subject')
        a = validated_data.get('test')
        print(a)
        print(subject_id)
        return super().create(validated_data)
