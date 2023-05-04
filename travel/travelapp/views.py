from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Place, seven

def static(request):
    obj = Place.objects.all()
    obj1 = seven.objects.all()
    return render(request,'index.html',{'res':obj,'res1':obj1})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cfpass = request.POST['password1']
        if password==cfpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.info(request,"Password not matched")
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
