from django.shortcuts import render
from .models import Feedback,Answer,Article,Category,Student,Test
# Create your views here.



def index(request):
    obj = Article.objects.all()
    category = Category.objects.all()
    feedback = Feedback.objects.all()
    students = Student.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Feedback.objects.create(name=name, email=email, subject=subject, text=message)
    context = {
        "article":obj,
        "category":category,
        "feedback":feedback,
        "students":students

    }
    return render(request, 'index.html',context)

def detail(request):
    return render(request, 'meeting-details.html')

def done(request):
    return render(request, 'done.html')

def contact(request):
    
    return render(request, 'contact.html')

def test(request):
    return render(request, 'test.html')


def course(request):
    return render(request, 'course.html')


def course_detail(request):
    return render(request, 'course-detail.html')

def test_detail(request):
    return render(request, 'test-detail.html')


def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    text = request.POST.get('message')
    Feedback.objects.create(name=name, email=email, subject=subject, text=text)
    return render(request, 'feedback.html')


