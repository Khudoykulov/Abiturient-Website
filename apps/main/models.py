from django.db import models
from apps.account.models import User
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.quiz.models import TestQuiz


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
    main_test = models.ForeignKey(TestQuiz, on_delete=models.CASCADE, related_name='main_test')

    def __str__(self):
        return self.author.username

