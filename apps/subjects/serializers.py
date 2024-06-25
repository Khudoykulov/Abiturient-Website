from .models import Tests, Answers, Subjects
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class SubjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = ['id', 'name']


class TestSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer(read_only=True)

    class Meta:
        model = Tests
        fields = ['id', 'subject', 'level', 'body']
        read_only_fields = ['subject']


class TestPostSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer(read_only=True)

    class Meta:
        model = Tests
        fields = ['id', 'subject', 'level', 'body']
        read_only_fields = ['subject']
