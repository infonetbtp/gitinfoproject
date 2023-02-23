from django.shortcuts import render ,redirect

from django.http import HttpResponse
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate


def SignUp(request):
    if request.method=='POST':

        userform= UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            messages.success(request,"registration successful")
            return redirect("home:index")
        
    userform=UserForm()
    return render(request,'registration/SignUp.html',{'form':userform})

def signIn(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('usernme')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
               login(request,user)
            #messages.info(request,f'your are login')
        return HttpResponse("welcome to login")
    form=AuthenticationForm()

    return render(request,'registration/SignIn.html',{'form':form})
