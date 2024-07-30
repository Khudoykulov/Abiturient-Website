from django.contrib import admin
# from .models import FirstSubject, SecondSubject, TestQuiz,
from .models import TestQuiz, BlockTestPrice, Mandatory


@admin.register(TestQuiz)
class TestQuiz(admin.ModelAdmin):
    list_display = ['id', 'subject_quiz', 'max_point', 'test_count']
    search_fields = ("subject_quiz__name", 'test_quiz')
    # autocomplete_fields = ['test_quiz']
    filter_horizontal = ('test_quiz',)


@admin.register(BlockTestPrice)
class BlockTestPrice(admin.ModelAdmin):
    list_display = ['id', 'price']


@admin.register(Mandatory)
class BlockTestPrice(admin.ModelAdmin):
    list_display = ['id', 'ona_tili', 'tarix', 'matematika']
