from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    read_time = models.IntegerField(default=0)
    body = models.TextField()
    image = models.ImageField(upload_to="category/")
    
    def __str__(self):
        return self.name
    
class LangCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Test(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(default=0)
    body = models.TextField()
    image = models.ImageField(upload_to="test/")
    summary = models.CharField(max_length=255)
    category = models.ForeignKey(LangCategory, null=True,on_delete=models.CASCADE,related_name="lang")
    incorrert1 = models.CharField(max_length=255)
    incorrert2 = models.CharField(max_length=255)
    incorrert3 = models.CharField(max_length=255)
    correct = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Answer(models.Model):
    incorrert1 = models.CharField(max_length=255)
    incorrert2 = models.CharField(max_length=255)
    incorrert3 = models.CharField(max_length=255)
    correct = models.CharField(max_length=255)
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name="answer")

    def __str__(self):
        return self.correct




class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='article')

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=255)
    succeeded = models.IntegerField(default=0)
    students = models.IntegerField(default=0)
    teachers = models.IntegerField(default=0)
    awards = models.IntegerField(default=0)
    image = models.ImageField(upload_to='students/')
    
    def __str__(self) -> str:
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=70)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
    
