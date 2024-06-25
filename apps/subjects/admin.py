from django.contrib import admin
from .models import Subjects, Answers, Tests
# Register your models here.


@admin.register(Subjects)
class Subjects(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Tests)
class Tests(admin.ModelAdmin):
    list_display = ['id', 'level', 'subject', 'body']
    search_fields = ['unit', 'subject']


@admin.register(Answers)
class Answers(admin.ModelAdmin):
    list_display = ['id', 'test', 'body', 'is_correct']
    search_fields = ['is_correct']

