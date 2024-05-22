from django.urls import path
from .views import (
    index, detail, done, feedback,
    contact,test,course,course_detail,test_detail,
    quiz,submit_quiz, article
    )


urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('tests/', test, name='test'),
    path('courses/', course, name='course'),
    path('course-detail/', course_detail, name='course_detail'),
    path('test-detail/<int:id>/', test_detail, name='test_detail'),
    path('done/', done, name='done'),
    path('feedback/', feedback, name='feedback'),
    path('quiz/', quiz, name='quiz'),
    path('submit_quiz/', submit_quiz, name='submit_quiz'),
    path('blog-detail/<int:id>/', article, name='article'),

    
]
