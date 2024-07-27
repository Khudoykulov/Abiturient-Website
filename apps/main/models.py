from django.db import models
from apps.account.models import User
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.quiz.models import TestQuiz
from apps.subjects.models import Tests, Answers


class Portfolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balance')
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
        return f'{self.main_test.subject_quiz.name} --> {self.id}'
    @property
    def subject_name(self):
        return self.main_test.subject_quiz.name


class MainAnswerBlock(models.Model):
    block = models.ForeignKey(MainTest, on_delete=models.CASCADE, related_name='block')

    def block_author(self):
        return self.block.author.email

    @property
    def correct_count(self):
        answers = self.main.all().values_list('answer__is_correct', flat=True)
        correct_count = sum(1 for is_correct in answers if is_correct)
        return correct_count

    def ball(self):
        return self.correct_count * self.block.main_test.max_point

class MainAnswer(models.Model):
    main = models.ForeignKey(MainAnswerBlock, on_delete=models.CASCADE, related_name='main')
    quiz = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='main_quiz')
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    # modified_date = models.DateTimeField(auto_now=True)
    # created_date = models.DateTimeField(auto_now_add=True)


