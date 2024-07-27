from .models import Tests, Answers, Subjects, Tag
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


class SubjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = ['id', 'name']


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tests
        fields = ['id', 'body']
        read_only_fields = ['subject']


class TestPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tests
        fields = ['id', 'subject', 'level', 'body']


class AnswerSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True)

    class Meta:
        model = Answers
        fields = ['id', 'test', 'body', 'is_correct']
        read_only_fields = ['test']


class AnswerPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ['id', 'test', 'body', 'is_correct']


# class AnswerQuizSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#
#     class Meta:
#         model = Answers
#         fields = ['id',]


# class TestSubjectSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#
#     class Meta:
#         model = Tests
#         fields = ['id', 'body']
class AnswerQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['id', 'body', 'is_correct']


class TestSubjectSerializer(serializers.ModelSerializer):
    tests = AnswerQuizSerializer(many=True)

    class Meta:
        model = Tests
        fields = ['id', 'body', 'tests']


