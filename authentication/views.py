from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework import viewsets

from .models import patient
from .serializers import PatientSerializer


class PatientView(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = PatientSerializer

def login_user(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user_type = request.POST['user_type']

        user = authenticate(username=username, password=password)

        #doctor is superuser and receptionist is normaluser

        if user is None:
            login(request, user)
            if user_type == 'Doctor':
                return render(request,'')
            elif user_type == 'Receptionist':
                return render(request, 'Auth/registration.html')
            else:
                return render(request,'')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('login')

    return render(request, "Auth/login.html")

def registration(request):
    if request.method == "POST":
        PID = request.POST['PID']
        Name = request.POST['Name']
        Age = request.POST['Age']
        DOB = request.POST['DOB']
        gender = request.POST['gender']
        BG = request.POST['BG']
        PN = request.POST['PN']
        Add = request.POST['Add']

        Patient = patient(PID=PID,Name=Name,Age=Age,DOB=DOB,gender=gender,BG=BG,PN=PN,Add=Add)
        Patient.save()

        return render(request,'Auth/registration.html')


    else:
        if request.user.is_staff:
            return render(request,'Auth/registration.html')
        else:
            return HttpResponseForbidden('<h1> 403 Forbidden <br>You are not allowed to access this page.</h1>')