from django.shortcuts import render, redirect
from pytube import YouTube
from io import BytesIO
from django.http import StreamingHttpResponse
from .models import Feedback
import re
from django.contrib import messages

# Create your views here.



def index(request):
    return render(request, 'index.html')

def detail(request):
    return render(request, 'meeting-details.html')

def done(request):
    return render(request, 'done.html')

def contact(request):
    return render(request, 'contact.html')

def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    text = request.POST.get('message')
    Feedback.objects.create(name=name, email=email, subject=subject, text=text)
    return render(request, 'feedback.html')


