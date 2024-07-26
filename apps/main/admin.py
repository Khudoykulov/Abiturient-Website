from django.contrib import admin
from .models import Portfolio, MainTest, MainAnswer, MainAnswerBlock
from apps.subjects.models import Tests

@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ['id', 'author', 'balance', 'total_balance']


@admin.register(MainTest)
class MainTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_test', 'author']
    # fields = ['main_test']
    search_fields = ('main_test',)
    autocomplete_fields = ('main_test',)


class TestInlineAdmin(admin.TabularInline):
    model = MainAnswer
    extra = 0


@admin.register(MainAnswerBlock)
class MainAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'block', 'correct_count', 'ball']
    inlines = [TestInlineAdmin,]
