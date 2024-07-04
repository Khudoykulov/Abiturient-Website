from django.db import models
from apps.subjects.models import Subjects, Tests, Answers


class TestQuiz(models.Model):
    subject_quiz = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_quiz')
    test_quiz = models.ManyToManyField(Tests, related_name='test_quiz',)
    max_point = models.FloatField(default=2.1)

    def __str__(self):
        return f'{self.subject_quiz} ----> {self.max_point}'

    def test_count(self):
        return self.test_quiz.count()






