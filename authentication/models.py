from django.db import models
from django import forms

User_type = (
    ("Doctor", "Doctor"),
    ("Receptionist", "Receptionist"),
    ("View Patient","View Patient"),
)

Gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other","Other"),
)

Blood_group = (
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ("AB+","AB+"),
    ("AB-","AB-"),
    ("O+","O+"),
    ("O-","O-"),
)

class Doctor(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=32)
    type = models.CharField(max_length=10,default='doctor')

    def __str__(self):
        return self.Username

    def is_doctor(self):
        return self.type

class receptionist(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=32)
    type = models.CharField(max_length=10,default='Receptionist')


    def __str__(self):
        return self.Username

    def is_receptionist(self):
        return self.type

class patient(models.Model):
    Patient_ID = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Age = models.CharField(max_length=200)
    DOB = models.DateTimeField()
    Gender = models.CharField(max_length=200 ,choices=Gender)
    BloodGroup = models.CharField(max_length=200 ,choices=Blood_group)
    Phone = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)