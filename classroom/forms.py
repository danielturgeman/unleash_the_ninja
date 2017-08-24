from django.contrib.auth.models import User
from django import forms
from classroom.models import Student, Teacher, Course

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    hash(password)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ()

class TeacherForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        exclude = ()

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['category', 'difficulty', 'name', 'teacher', 'limit', 'student']

class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
