from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        email= request.POST['email']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"user name is already exist")
                print("User name is already exists")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"user mailid is already exist")
                print("Mail id is already exists")
                return redirect('register')

            else:
                user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user is succesfully created")
        else:
            print("password is not correct")
            return redirect('register')

        return redirect('/')

    else:
       return render(request,'register.html')


def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

