from django.db import models


class Subjects(models.Model):
    name = models.CharField(max_length=123,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subjects'


class Tests(models.Model):
    UNIT = (
        (3.1, 'difficult'),
        (2.1, 'easy')
    )
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject')
    level = models.FloatField(choices=UNIT, default=3.1)
    body = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.subject.name} {self.level} -----> {self.body}'

    class Meta:
        verbose_name_plural = 'Tests'


class Answers(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='tests')
    body = models.CharField(max_length=225)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.body}'

    class Meta:
        verbose_name_plural = 'Answers'

