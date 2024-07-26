from rest_framework import serializers
from .models import Portfolio, MainTest, MainAnswer, MainAnswerBlock
from django.core.exceptions import ValidationError
from apps.quiz.serializers import TestQuizSerializer
from ..quiz.models import TestQuiz
from ..subjects.serializers import SubjectsSerializer, TestSubjectSerializer
from apps.subjects.models import Tests, Answers

class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['id', 'balance', 'total_balance',]


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
        fields = ['id',]

    def create(self, validated_data):
        return super().create(validated_data)


class TestQuizAnswerSerializer(serializers.ModelSerializer):
    subject_quiz = SubjectsSerializer(read_only=True)

    class Meta:
        model = TestQuiz
        fields = ['subject_quiz', 'max_point']


class MainTestAnswerSerializer(serializers.ModelSerializer):
    main_test = TestQuizAnswerSerializer(read_only=True)

    class Meta:
        model = MainTest
        fields = ['id', 'main_test']


class MainAnswerQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tests
        fields = ['id', 'body']


class MainAnswerAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ['id', 'body', 'is_correct']


class MainAnswerSerializer(serializers.ModelSerializer):
    quiz = MainAnswerQuizSerializer(read_only=True)
    answer = MainAnswerAnswerSerializer(read_only=True)

    class Meta:
        model = MainAnswer
        fields = ['quiz', 'answer']


class MainAnswerBlockSerializer(serializers.ModelSerializer):
    block = MainTestAnswerSerializer(read_only=True)
    main = MainAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = MainAnswerBlock
        fields = ['id', 'block', 'main']


class MainAnswerPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainAnswer
        fields = ['id', 'quiz', 'answer']


class MainAnswerBlockPostSerializer(serializers.ModelSerializer):
    main = MainAnswerPostSerializer(many=True,)

    class Meta:
        model = MainAnswerBlock
        fields = ['id', 'block', 'main']

    def create(self, validated_data):
        main_data = validated_data.pop('main', [])
        block = MainAnswerBlock.objects.create(**validated_data)
        for main_item in main_data:
            MainAnswer.objects.create(main=block, **main_item)
        return block





