from rest_framework import serializers
from rest_framework.response import Response

from .models import (
    TestQuiz,
    Mandatory

)
from apps.subjects.models import Subjects, Tests, Answers
from apps.subjects.serializers import (
    SubjectsSerializer,
    TestSubjectSerializer

)
import random


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


class BlockTestPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestQuiz
        fields = ['id', 'subject_quiz', 'max_point']


    def create(self, validated_data):
        subject_id = validated_data.get('subject_quiz').id
        print(subject_id)
        max_point = validated_data.get('max_point')
        print(max_point)

        # 1. Tests modelidan kerakli testlarni olish
        filtered_tests = Tests.objects.filter(subject_id=subject_id, level=max_point)
        # 2. Tasodifiy 3 ta testni tanlash
        all_tests = list(filtered_tests)
        if len(all_tests) < 3:
            selected_tests = all_tests
        else:
            selected_tests = random.sample(all_tests, 3)

        # 3. Yangi TestQuiz instansiyasini yaratish
        test_quiz_instance = TestQuiz.objects.create(
            subject_quiz_id=subject_id,
            max_point=max_point
        )

        # 4. Tanlangan testlarni TestQuiz instansiyasiga qo'shish
        test_quiz_instance.test_quiz.set(selected_tests)

        return test_quiz_instance


class MandatoryBlockPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mandatory
        fields = ['id']

    def create(self, validated_data):
        test_quizzes_ona_tili = list(TestQuiz.objects.filter(subject_quiz__name='ona tili', max_point=1.1).all())
        print(test_quizzes_ona_tili)
        test_quizzes_matem = list(TestQuiz.objects.filter(subject_quiz__name='matematika', max_point=1.1).all())
        print(test_quizzes_matem)
        test_quizzes_tarix = list(TestQuiz.objects.filter(subject_quiz__name='tarix', max_point=1.1).all())
        print(test_quizzes_tarix)

        # Randomly select TestQuiz instances
        ona_tili = random.choice(test_quizzes_ona_tili)
        tarix = random.choice(test_quizzes_tarix)
        matematika = random.choice(test_quizzes_matem)
        mandatory = Mandatory.objects.create(
            ona_tili=ona_tili,
            tarix=tarix,
            matematika=matematika
        )

        return mandatory


class MandatoryBlockSerializer(serializers.ModelSerializer):
    ona_tili = TestQuizSerializer()
    tarix = TestQuizSerializer()
    matematika = TestQuizSerializer()

    class Meta:
        model = Mandatory
        fields = ['id', 'ona_tili', 'tarix', 'matematika']
