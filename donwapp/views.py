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

def detail(request,id):
    category = Category.objects.filter(id=id).first()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Feedback.objects.create(name=name, email=email, subject=subject, text=message)
    context = {
        "category":category
    }
    return render(request, 'meeting-details.html', context)

def done(request):
    return render(request, 'done.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Feedback.objects.create(name=name, email=email, subject=subject, text=message)
    return render(request, 'contact.html')

def test(request):
    category = Category.objects.all()
    test = Test.objects.all()
    obj = Article.objects.all()
    
    context = {
        "article":obj,
        "category":category,
        'test':test
    }
    return render(request, 'test.html',context)


def course(request):
    return render(request, 'course.html')


def course_detail(request):
    return render(request, 'course-detail.html')

def test_detail(request,id):
    test = Test.objects.filter(id=id).first()
    answer = test.answer.all()
    
    print(request.POST.get('name'))
    name = request.POST.get('name')
    if name == "True":
        print("Please enter")
    context = {
       "test":test,
       "answer":answer
    }
    return render(request, 'test-detail.html', context)


# def test_detail(request):
   
#     return render(request, 'test-detail.html')



def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    text = request.POST.get('message')
    Feedback.objects.create(name=name, email=email, subject=subject, text=text)
    return render(request, 'feedback.html')


