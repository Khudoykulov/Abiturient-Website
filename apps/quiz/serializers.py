from rest_framework import serializers
from .models import (
    TestQuiz

)
from apps.subjects.models import Subjects, Tests, Answers
from apps.subjects.serializers import (
    SubjectsSerializer,
    TestSubjectSerializer

)


class TestQuizSerializer(serializers.ModelSerializer):
    test_quiz = TestSubjectSerializer(many=True, read_only=True)
    subject_quiz = SubjectsSerializer(read_only=True)

    class Meta:
        model = TestQuiz
        fields = ['id', 'subject_quiz', 'test_quiz', 'max_point']


class TestQuizPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestQuiz
        fields = ['id', 'subject_quiz', 'test_quiz', 'max_point']




