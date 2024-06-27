from django.contrib import admin
from .models import FirstSubject, SecondSubject


@admin.register(FirstSubject)
class FirstSubject(admin.ModelAdmin):
    list_display = ['id', 'first_stage',]


@admin.register(SecondSubject)
class SecondSubject(admin.ModelAdmin):
    list_display = ['id', 'second_subject']
