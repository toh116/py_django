from django.shortcuts import render, HttpResponse

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


def ajaxStudentLogin(request):
    data = request.GET
    userid = data.get('userid')
    userpassword = data.get('userpassword')
    try:
        count = Students.objects.filter(id=userid, password=userpassword).count()
    except:
        count = 0
    s = ''
    if count >= 1:
        s = 'true'
    else:
        s = 'false'
    return HttpResponse(s)


def StudentLoginSuccessful(request):
    data = request.GET
    userid = data.get('userid')
    student = Students.objects.filter(id=userid)
    name = student.values('name')[0]
    return render(request, 'front/StudentLoginSuccessful.html', name)


def test(request):
    return render(request, 'test/test.html', {'test': 'hello'})


def test1(request):
    return render(request, 'test/test.html', {'test': Teachers.objects.all().values()})
