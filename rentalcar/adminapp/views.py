from django.shortcuts import redirect, render
from .forms import bookform, userform
from adminapp.forms import userform
from adminapp.models import Booking, Car, usermanage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
#from django.contrib.auth.hashers import make_password
#from django.core.mail import send_mail
#from myproject.settings import EMAIL_HOST_USER

#----------index templates------------#
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
#-----------------------------------------#

# --------------car view-------------#
# @login_required
def carview(request):
    data=Car.objects.all()
    return render(request,'carview.html',{'cars':data})

#-------------for signin-----------#
def userinfo(request):
    if request.method == 'POST':
        obj = userform(request.POST, request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('userview')
            # return render(request, 'user.html', {'data': obj})
    else:  # Handle the GET method
        obj = userform()
    return render(request, 'user.html', {'data': obj})

def userview(request):
    obj=usermanage.objects.all()
    return render(request,'userview.html',{'form':obj})


# ---------for booking--------#
@login_required
def bookdata(request):
    if request.method == 'POST':
        data=bookform(request.POST)
        if data.is_valid():
            data.save()
            return redirect('viewbooking')
    else:
        data=bookform()
    return render(request,'booking.html',{'form':data})

@login_required
def bookingview(request):
    data=Booking.objects.all()
    return render(request,'bookview.html',{'data':data})




# ---------------------------------------------------------------------#




def loginview(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except MultiValueDictKeyError:
        return render(request,"login.html")

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('carview')
    else:
        return render(request,"login.html")


# def loginview(request):
#     uname = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=uname, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('home')
#     else:
#         return render(request,"login.html")
        
def logout_view(request):
    logout(request)
    return redirect('login')


def sign_up(request):
        uform = UserCreationForm(request.POST)
        if request.method == "POST":
            if uform.is_valid():
                username = uform.cleaned_data.get('username')
                password = uform.cleaned_data.get('password1')
                email=uform.cleaned_data.get('email')
                user1=User.objects.create_user(username=username,password=password,email=email)
                user1.save()
                user = authenticate(request, username=username, password=password)
                login(request,user)
                return redirect('login')
        else:
            uform = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': uform})
    
def Resethome(request):
    return render(request,'registration/ResetPassword.html')

def resetPassword(request):
    responseDic={}
    try:
        username = request.POST['username']
        recepient=request.POST['email']
        pwd=request.POST['password']
        #subject="Password reset"
        try:
            user=User.objects.get(username=username)
            if user is not None:
                user.set_password(pwd)
                user.save()
                #send_mail(subject,message, EMAIL_HOST_USER, [recepient])
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,"registration/ResetPassword.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["errmsg"]="Email doesnt exist"
            return render(request,"registration/ResetPassword.html",responseDic)
        
    except Exception as e:
        print(e)
        responseDic["errmsg"]="Failed to reset password"
        return render(request," registration/ResetPassword.html",responseDic)

     



