from django.contrib import admin
from .models import (
    Portfolio,
    MainTest,
    MainAnswer,
    MainAnswerBlock,
    BlockMainTest5,
    MainAnswer5,
    MainAnswerBlock5
)
from apps.subjects.models import Tests


@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ['id', 'author', 'balance', 'total_balance']


@admin.register(MainTest)
class MainTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_test', 'author', 'created_date']
    search_fields = ('main_test',)
    autocomplete_fields = ('main_test',)


class TestInlineAdmin(admin.TabularInline):
    model = MainAnswer
    extra = 0


@admin.register(MainAnswerBlock)
class MainAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'block_author', 'block', 'correct_count', 'ball']
    inlines = [TestInlineAdmin,]


class BLockTest5InlineAdmin(admin.TabularInline):
    model = MainAnswer5
    extra = 0


@admin.register(MainAnswerBlock5)
class MainAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'block_author', 'block', 'first_subject_correct_count',
                    'second_subject_correct_count', 'mandatory_subject_correct_count', 'ball']
    inlines = [BLockTest5InlineAdmin,]


@admin.register(BlockMainTest5)
class MainAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'first_subject', 'second_subject', 'mandatory_subject']