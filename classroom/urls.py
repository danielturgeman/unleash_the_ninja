"""billboard URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.my_view, name='my_view'),
    url(r'^student/$', views.register_student, name='register_student'),
    url(r'^teacher/$', views.register_teacher, name='register_teacher'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^student/(?P<id>\d)+$', views.student_page, name='student_page'),
    url(r'^student/(?P<id>\d)+/courses$', views.student_courses, name='student_courses'),
    url(r'^student/(?P<id>\d)+/joincourse$', views.student_join_course, name='student_join_course'),
    url(r'^courses/(?P<id>\d)+$', views.course, name='course'),
    url(r'^teacher/(?P<id>\d)+$', views.teacher_page, name='teacher_page'),

]