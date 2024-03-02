from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    read_time = models.IntegerField(default=0)
    body = models.TextField()
    
    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(default=0)
    body = models.TextField()
    
    def __str__(self):
        return self.name


class Answer(models.Model):
    incorrert1 = models.CharField(max_length=255)
    incorrert2 = models.CharField(max_length=255)
    incorrert3 = models.CharField(max_length=255)
    correct = models.CharField(max_length=255)
    test = models.ForeignKey(Test,on_delete=models.CASCADE)

    def __str__(self):
        return self.correct




class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=70)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name