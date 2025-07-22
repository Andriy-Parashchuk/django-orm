from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=30)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Class(models.Model):
    name = models.CharField(max_length=10)


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    in_class = models.ForeignKey(Class, on_delete=models.CASCADE)
