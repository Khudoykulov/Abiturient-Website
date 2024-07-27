from django.contrib import admin
from .models import Subjects, Answers, Tests, Tag
from modeltranslation.admin import TranslationAdmin


@admin.register(Tag)
class Tag(TranslationAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Subjects)
class Subjects(TranslationAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    filter_horizontal = ('tags',)


@admin.register(Tests)
class Tests(admin.ModelAdmin):
    list_display = ['id', 'level', 'subject', 'body']
    search_fields = ['body', 'subject__name', 'level']


@admin.register(Answers)
class Answers(admin.ModelAdmin):
    list_display = ['id', 'test', 'body', 'is_correct']
    search_fields = ['is_correct']

