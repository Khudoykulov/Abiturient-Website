from django.db import models
from apps.subjects.models import Subjects, Tests, Answers


class TestQuiz(models.Model):
    subject_quiz = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_quiz')
    test_quiz = models.ManyToManyField(Tests, related_name='test_quiz',)
    max_point = models.FloatField(default=1.1)

    def __str__(self):
        return f'{self.subject_quiz} ----> {self.max_point}'

    def test_count(self):
        return self.test_quiz.count()


class BlockTestPrice(models.Model):
    price = models.IntegerField(max_length=123, default=5000)

    def __str__(self):
        return f'{self.price}'


class Mandatory(models.Model):
    ona_tili = models.ForeignKey(TestQuiz, models.CASCADE, related_name='ona_tili')
    tarix = models.ForeignKey(TestQuiz, models.CASCADE, related_name='tarix')
    matematika = models.ForeignKey(TestQuiz, models.CASCADE, related_name='matematika')

    def __str__(self):
        return (f'{self.id} {self.ona_tili.subject_quiz.name},{self.tarix.subject_quiz.name},'
                f'{self.matematika.subject_quiz.name}, ')


