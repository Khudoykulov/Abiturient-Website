from modeltranslation.translator import translator, TranslationOptions
from .models import Tests, Subjects, Tag

class SubjectsTranslation(TranslationOptions):
    fields = ['name']


class TagTranslation(TranslationOptions):
    fields = ['name']


translator.register(Subjects, SubjectsTranslation)
translator.register(Tag, SubjectsTranslation)

