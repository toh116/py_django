# 子路由
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("Home/", views.home, name="Home"),
    path("News/", views.news, name="News"),
    path("About/", views.about, name="About"),
    path("studentLogin/", views.studentLogin, name="studentLogin"),
    path("teacherLogin/", views.teacherLogin, name="teacherLogin"),
    path("parentLogin/", views.parentLogin, name="parentLogin"),
    path("studentRegister/", views.studentRegister, name="studentRegister"),
    path("teacherRegister/", views.teacherRegister, name="teacherRegister"),
    path("parentRegister/", views.parentRegister, name="parentRegister"),
    path("ajaxStudentLogin/", views.ajaxStudentLogin, name="ajaxStudentLogin"),
    path("StudentLoginSuccessful/", views.StudentLoginSuccessful, name="StudentLoginSuccessful"),
    path("test/", views.test),
    path("test1/", views.test1),
]
