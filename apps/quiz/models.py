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


class BlockTest(models.Model):
    # subject/{subject_id}/test/test_id/answer/answer_id
    first = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='first')
    second = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='second')
    test = models.ForeignKey(Tests, on_delete=models.SET_NULL, related_name='test', null=True, blank=True)
    answer = models.ForeignKey(Answers, on_delete=models.SET_NULL, related_name='answer', null=True, blank=True)
    is_answer = models.BooleanField()




