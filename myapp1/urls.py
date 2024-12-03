from django.urls import path
from myapp1 import views


urlspatterns=[

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('services/', views.services, name='services'),

    path('blogs/', views.blogs, name='blogs')
]