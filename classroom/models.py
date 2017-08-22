from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now

education = (
    ('middleschool', 'Middle School'),
    ('highschool', 'High School'),
    ('university', 'University'),
    ('graduate', 'Graduate')
)

categories = (
    ('literature', 'Literature'),
    ('programming', 'Programming'),
    ('math', 'Math'),
    ('science', 'Science'),
    ('history', 'History'),
)


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Student - {0} {1} ".format(self.user.first_name, self.user.last_name)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Teacher - {0} {1} ".format(self.user.first_name, self.user.last_name)


class Course(models.Model):
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=13, choices=education, default='university')
    category = models.CharField(max_length=11, choices=categories, default='english')
    start_date = models.DateTimeField(default=datetime.now)
    limit = models.IntegerField()

    def _str_(self):
        return "Course - '{}'".format(self.name)