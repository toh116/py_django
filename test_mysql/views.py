from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'front/home.html')


def news(request):
    return render(request, 'front/news.html')


def about(request):
    return render(request, 'front/about.html')


def studentLogin(request):
    return render(request, 'front/studentLogin.html')


def teacherLogin(request):
    return render(request, 'front/teacherLogin.html')


def parentLogin(request):
    return render(request, 'front/parentLogin.html')


def studentRegister(request):
    return render(request, 'front/studentRegister.html')


def teacherRegister(request):
    return render(request, 'front/teacherRegister.html')


def parentRegister(request):
    return render(request, 'front/parentRegister.html')


def test(request):
    return render(request, 'test/test.html', {'test': 'hello'})


def test1(request):
    return render(request, 'test/test.html', {'test': Teachers.objects.all().values()})
