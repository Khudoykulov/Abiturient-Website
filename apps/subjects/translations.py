from modeltranslation.translator import translator, TranslationOptions
from .models import Tests, Subjects


class SubjectsTranslation(TranslationOptions):
    fields = ['name']


translator.register(Subjects, SubjectsTranslation)

