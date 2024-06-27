from django.db import models
from apps.subjects.models import Subjects, Tests, Answers


class FirstSubject(models.Model):
    first_stage = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='first_stage',)

    def __str__(self):
        return f'{self.first_stage}'


class SecondSubject(models.Model):
    second_subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='second_subject')

    def __str__(self):
        return f'{self.second_subject}'


