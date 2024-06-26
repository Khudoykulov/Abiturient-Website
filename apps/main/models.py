from django.db import models
from apps.account.models import User


class Portfolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    balance = models.IntegerField(max_length=7, null=True, blank=True)

    def total_balance(self):
        a = self.balance
        print(a)

