import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, StudentForm, TeacherForm, CourseForm, LoginForm
from classroom.models import Student, Teacher, Course
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


import json
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')


def register_student(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            student = Student(user=user)
            student.save()
            return HttpResponseRedirect('/student/' + str(student.id))
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
                user.set_password(user.password)
                user.save()
                teacher = Teacher(user=user)
                teacher.save()
                return HttpResponseRedirect('/teacher/' + str(teacher.id))
            else:
                context = {
                    'user_form': user_form
                }
        else:
            context = {
                'user_form': UserForm()
            }
        return render(request, 'registration/teacher_registration.html', context)

def courses(request):
    if request.method == 'POST':
        pass

    else:
        print('get request for courses')
        course_list = Course.objects.values()
        print(course_list)
        context = {
            'courses': course_list
        }
        return JsonResponse(
            {'courses': list(course_list)}
        )


#/student/<id>/courses
def student_courses(request, id):
    json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)

    student_id = id
    student = Student.objects.get(pk=id)
    print(student)
    print('get request for student courses')
    course_list = Course.objects.filter(student_id=id).values()
    teacher_list = []
    #can later return list of teachers
    for course in course_list:
        print(course['teacher_id'])
        teacher_list.append(course['teacher_id'])
    for i in teacher_list:
        teachers = []
        teacher = Teacher.objects.get(pk=i)
        name = '{} {}'.format(teacher.user.first_name, teacher.user.last_name)
        teachers.append(name)
        print(teachers)
    teachers = json.dumps(teachers)

    print('course list')
    print(course_list)
    context = {
        'student_id': student_id,
        'courses': list(course_list),
        'teachers': teachers
    }

    if request.method == 'POST':
        pass

    else:
        return HttpResponse(json.dumps(context))


@login_required
def teacher_page(request, id):
    teacher = Teacher.objects.get(pk=id)
    course_list = Course.objects.filter(teacher=id)

    context = {"teacher": teacher,
               "courses": course_list}

    if request.method == 'POST':
        pass

    else:
        return render(request, 'teacher.html', context)

@login_required()
def student_page(request, id):
    student = Student.objects.get(pk=id)
    course_list = Course.objects.filter(student=id)

    context = {"student": student,
               "courses": course_list}

    if request.method == 'POST':
        pass

    else:
        return render(request, 'student.html', context)

#/student/id/join_course
def student_join_course(request, id):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)

        if course_form.is_valid():
            course = course_form.save()
            #course exists
            if Course.objects.filter(name=course.name).count() > 0:
                courses = Course.objects.filter(name=course.name)


            return HttpResponseRedirect('/student/' + str(id))
        else:
            context = {
                'user_form': CourseForm()
            }

    else:
        context = {
            'course_form': CourseForm()
        }
        return render(request, 'join_course.html', context)

def teacher_add_course(request, id):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)

        if course_form.is_valid():
            course = course_form.save()
            #course exists
            if Course.objects.filter(name=course_form.name).count() > 0:
                #add students to course
                print(course_form['name'])
                courses = Course.objects.filter(name=course.name)

            return HttpResponseRedirect('/teacher/' + str(id))
        else:
            context = {
                'user_form': CourseForm()
            }

    else:
        context = {
            'course_form': CourseForm()
        }
        return render(request, 'add_course.html', context)

def course(request,id):
    course = Course.objects.get(pk=id)
    context = {
        'course': course
    }
    return render(request, 'course.html', context )

def my_view(request):
    context = {
        'login_form': LoginForm()
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        try:
            student = Student.objects.get(user=user)
            is_student = True
        except Exception as e:
            is_student = False
        try:
            teacher = Teacher.objects.get(user=user)
            is_teacher = True
        except Exception as e:
            is_teacher = False

        if user is not None:
            if user.is_active and is_student:
                login(request, user)
                return HttpResponseRedirect('/student/' + str(student.id))
            elif user.is_active and is_teacher:
                login(request, user)
                return HttpResponseRedirect('/teacher/' + str(teacher.id))

            else:
                return HttpResponse('Not an active account')
        else:
            return HttpResponse('No such user')
    else:
        return render(request, 'login.html', context)
