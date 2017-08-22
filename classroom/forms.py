from django.contrib.auth.models import User
from django import forms
from classroom.models import Student, Teacher, Course

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

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
