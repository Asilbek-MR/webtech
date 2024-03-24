from django.shortcuts import render, redirect
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
    test = Test.objects.filter(number=id)
    name = request.POST.get('name')
    if name == "True":
        print("Please enter")
    context = {
       "test":test,
    #    "answer":answer
    }
    return render(request, 'test-detail.html', context)


# def test_detail(request):
   
#     return render(request, 'test-detail.html')


def quiz(request):
    tests = Test.objects.all()
    context = {
        'tests': tests
    }
    return render(request, 'quiz.html', context)

def submit_quiz(request):
    correct_answers = 0
    if request.method == 'POST':
        score = 0  # Natijani hisoblash uchun boshlang'ich qiymat
        for i in range(1, 4):  # test obyektlar soni (1 dan 11 gacha)
            correct_answers = request.POST.get(f'q{i}_correct')  # To'g'ri javob
            selected_answers = request.POST.getlist(f'q{i}') # Tanlangan javoblar
            print(selected_answers,"selected_answers")
            print(correct_answers,"correct_answers")
            if correct_answers in selected_answers:
                score += 1
                print(score)
        return render(request, 'result.html', {'correct_answers': correct_answers})
        

        
    return redirect('quiz')


def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    text = request.POST.get('message')
    Feedback.objects.create(name=name, email=email, subject=subject, text=text)
    return render(request, 'feedback.html')


