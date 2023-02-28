from django.shortcuts import render,redirect
from django.http import HttpResponse
from  django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/registration/signIn')
def deskboard(request):
    return render(request,'stu_deskboard/deshboard.html')

def  stu_logout(request):
    logout(request)
    return redirect('/stu_deskboard')
def stu_profile_edit(request):
    return HttpResponse("welcome to profile edit")