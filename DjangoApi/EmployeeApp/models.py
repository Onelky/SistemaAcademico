import serializers as serializers
from django.db import models
from rest_framework import serializers
from django.utils.timezone import datetime
# from EmployeeApp.models import Employees, Department

# Create your models here.
# Aqui se agregan los modelos o clases del programa

#class DepartmentSerializer(serializers.ModelSerializer):

class Department(models.Model):
    DepartmentId = models.AutoField(primary_key = True)

    DepartmentName = models.CharField(max_length=20)
class Employee(models.Model):
    Id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=20)
    Department = models.IntegerField()
    Date_joining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

class Student (models.Model):
    Id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    createdDate = models.DateField(default= datetime.now())
    grade =  models.CharField(max_length=2)
    #lastUpdatedDate =  models.DateField()
    gender =  models.CharField(max_length=2)

class Student1 (models.Model):
    Id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    createdDate = models.DateField(default= datetime.now())
    grade =  models.CharField(max_length=2)
    #lastUpdatedDate =  models.DateField()
    gender =  models.CharField(max_length=2)