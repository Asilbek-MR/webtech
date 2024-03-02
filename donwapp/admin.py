from django.contrib import admin
from .models import Feedback,Answer,Test,Category
# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject','created')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display =  ('correct','incorrert1', 'incorrert2','incorrert3')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'number','body')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary','read_time','body','title')


