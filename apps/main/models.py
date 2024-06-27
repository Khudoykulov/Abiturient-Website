from django.db import models
from apps.account.models import User
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


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

