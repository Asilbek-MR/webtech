from django.urls import path
from .views import index, detail, done, feedback,contact,test,course,course_detail,test_detail


urlpatterns = [
    path('', index, name='index'),
    path('detail/', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('test/', test, name='test'),
    path('course/', course, name='course'),
    path('course-detail/', course_detail, name='course_detail'),
    path('test-detail/', test_detail, name='test_detail'),
    path('done/', done, name='done'),
    path('feedback/', feedback, name='feedback'),
    
]
