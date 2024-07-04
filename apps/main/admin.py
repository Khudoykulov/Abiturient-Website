from django.contrib import admin
from .models import Portfolio, MainTest


@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ['id', 'author', 'balance', 'total_balance']


@admin.register(MainTest)
class MainTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_test']
    # fields = ['main_test']
    search_fields = ('main_test',)
    autocomplete_fields = ('main_test',)

