from django.db import models


class Subjects(models.Model):
    name = models.CharField(max_length=123,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subjects'


class Tests(models.Model):
    UNIT = (
        (0, 'difficult'),
        (1, 'easy')
    )
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subjects')
    level = models.IntegerField(choices=UNIT, default=1)
    body = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.subject.name} fan {self.body}'

    class Meta:
        verbose_name_plural = 'Tests'
        ordering = ('id', 'level')


class Answers(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    body = models.CharField(max_length=225)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.body} {self.is_correct}'

    class Meta:
        verbose_name_plural = 'Answers'

