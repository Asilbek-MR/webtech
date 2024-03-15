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
    print(test)
    print(request.POST.get('name'))
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
    l1=[]
    if request.method == 'POST':
        print(request.POST.get('a'))
        print(request.POST.get('a'))
        print(request.POST.get('a'))
        print(request.POST.get('a'))
        # print(request.POST.get('5'))
        # print(request.POST.get('6'))
        # print(request.POST.get('7'))
        # print(request.POST.get('8'))
        # print(request.POST.get('9'))
        # print(request.POST.get('10'))
        # print(request.POST.get('11'))
        # print(request.POST.get('12'))
        # print(request.POST.get('13'))
        # print(request.POST.get('14'))
        # print(request.POST.get('15'))
        # print(request.POST.get('16'))
        # print(request.POST.get('17'))
        # print(request.POST.get('18'))
        # print(request.POST.get('19'))
        # print(request.POST.get('20'))
        l1.append(request.POST.get('1'))
        l1.append(request.POST.get('2'))
        l1.append(request.POST.get('3'))
        l1.append(request.POST.get('4'))
        l1.append(request.POST.get('5'))
        print(l1)
        correct_answers = 0
        for key, value in request.POST.items():
            if key.startswith('question_'):
                test_id = int(key.split('_')[1])
                test = Test.objects.get(id=test_id)
                correct_answer = test.answers.first().correct
                if correct_answer == value:
                    correct_answers += 1
        return render(request, 'result.html', {'correct_answers': correct_answers})
    return redirect('quiz')


def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    text = request.POST.get('message')
    Feedback.objects.create(name=name, email=email, subject=subject, text=text)
    return render(request, 'feedback.html')


