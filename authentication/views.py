from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from clinic_auth import settings
from django.core.mail import EmailMessage,send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']

        # 4.to check whether username and password is correct or not (already stored in DB or not
        user = authenticate(username=Username, password=Password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentification/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('login')

    return render(request, "authentification/signin.html")

def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
