from django.db import models
from apps.account.models import User
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.quiz.models import TestQuiz
from apps.subjects.models import Tests, Answers


class Portfolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    balance = models.IntegerField(null=True, blank=True,
                                  validators=[MinValueValidator(0), MaxValueValidator(9999999)])
    @property
    def total_balance(self):
        balance_author = Portfolio.objects.filter(author=self.author)
        sum_balance = 0
        for author in balance_author:
            sum_balance += author.balance
        return sum_balance


class MainTest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    main_test = models.ForeignKey(TestQuiz, on_delete=models.CASCADE, related_name='main_test',)

    def __str__(self):
        return self.main_test.subject_quiz.name
    @property
    def subject_name(self):
        return self.main_test.subject_quiz.name


class MainAnswerBlock(models.Model):
    block = models.ForeignKey(MainTest, on_delete=models.CASCADE)


class MainAnswer(models.Model):
    main = models.ForeignKey(MainAnswerBlock, on_delete=models.CASCADE, related_name='main')
    quiz = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='main_quiz')
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)













# class MainAnswer(models.Model):
#     test = models.ManyToManyField(MainTest, related_name='test')
#     main_test_answer = models.ManyToManyField(Tests, related_name='main_test_answer',)

#     def __str__(self):
#         return f'{self.test}'
#
#
# class TestQuiz11(models.Model):
#     Answer = models.ForeignKey(MainAnswer, on_delete=models.CASCADE,)
#     test_quiz = models.ManyToManyField(Tests, related_name='test_quiz',)
#     max_point = models.FloatField(default=2.1)
#
#     def __str__(self):
#         return f'{self.max_point}'

