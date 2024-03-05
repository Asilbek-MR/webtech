from django.urls import path
from .views import index, detail, done, feedback,contact

app_name = 'downapp'

urlpatterns = [
    path('', index, name='index'),
    path('detail/', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('done/', done, name='done'),
    path('feedback/', feedback, name='feedback'),
    
]
