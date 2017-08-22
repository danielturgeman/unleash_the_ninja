from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, StudentForm, TeacherForm
from classroom.models import Student, Teacher

# Create your views here.
def index(request):
    return render(request, 'base.html')


def register_student(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            student = Student(user=user)
            student.save()
            return HttpResponseRedirect('/student')
        else:
            context = {
                'user_form': user_form
            }
    else:
        context = {
            'user_form': UserForm()
        }
    return render(request, 'registration/student_registration.html', context)


def register_teacher(request):
        if request.method == 'POST':
            user_form = UserForm(request.POST)

            if user_form.is_valid():
                user = user_form.save()
                teacher = Teacher(user=user)
                teacher.save()
                return HttpResponseRedirect('/success')
            else:
                context = {
                    'user_form': user_form
                }
        else:
            context = {
                'user_form': UserForm()
            }
        return render(request, 'registration/teacher_registration.html', context)

