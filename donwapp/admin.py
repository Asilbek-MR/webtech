from django.contrib import admin
from .models import Feedback,Answer,Test,Category,Article,Student,LangCategory,Course

# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject','created')

@admin.register(LangCategory)
class LangCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display =  ('correct','incorrert1', 'incorrert2','incorrert3')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'number','body')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','name', 'summary','read_time','body')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary','body')

@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'succeeded','students','teachers','awards')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'title','courseurl')