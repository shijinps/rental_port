from django.shortcuts import render, redirect
from .forms import bookform, userform
from .models import Booking, Car, usermanage

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
# from django.core.mail import send_mail
# from myproject.settings import EMAIL_HOST_USER

# ------------------ Basic Pages ------------------ #
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

# ------------------ Car View ------------------ #
@login_required
def carview(request):
    data = Car.objects.all()
    return render(request, 'carview.html', {'cars': data})

# ------------------ User Info ------------------ #
def userinfo(request):
    if request.method == 'POST':
        obj = userform(request.POST, request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('userview')
    else:
        obj = userform()
    return render(request, 'user.html', {'data': obj})

def userview(request):
    obj = usermanage.objects.all()
    return render(request, 'userview.html', {'form': obj})

# ------------------ Booking ------------------ #
@login_required
def bookdata(request):
    if request.method == 'POST':
        data = bookform(request.POST)
        if data.is_valid():
            data.save()
            return redirect('viewbooking')
    else:
        data = bookform()
    return render(request, 'booking.html', {'form': data})

@login_required
def bookingview(request):
    data = Booking.objects.all()
    return render(request, 'bookview.html', {'data': data})

# ------------------ Authentication ------------------ #
def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('carview')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    if request.method == "POST":
        uform = UserCreationForm(request.POST)
        if uform.is_valid():
            username = uform.cleaned_data.get('username')
            password = uform.cleaned_data.get('password1')
            email = uform.cleaned_data.get('email')
            user1 = User.objects.create_user(username=username, password=password, email=email)
            user1.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        uform = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': uform})

# ------------------ Password Reset ------------------ #
def Resethome(request):
    return render(request, 'registration/ResetPassword.html')

def resetPassword(request):
    responseDic = {}
    if request.method == "POST":
        try:
            username = request.POST['username']
            recepient = request.POST['email']
            pwd = request.POST['password']

            try:
                user = User.objects.get(username=username)
                if user:
                    user.set_password(pwd)
                    user.save()
                    responseDic["errmsg"] = "Password reset successfully"
                    return render(request, "registration/ResetPassword.html", responseDic)
            except Exception as e:
                print(e)
                responseDic["errmsg"] = "Email doesn't exist"
                return render(request, "registration/ResetPassword.html", responseDic)

        except Exception as e:
            print(e)
            responseDic["errmsg"] = "Failed to reset password"
            return render(request, "registration/ResetPassword.html", responseDic)

    return render(request, "registration/ResetPassword.html")
