from django.shortcuts import render ,redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models  import User,auth


def SignUp(request):
    if request.method=='POST':

        userform= UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            messages.success(request,"registration successful")
            return redirect("home:index")
        
    userform=UserForm()
    return render(request,'registration/SignUp.html',{'form':userform})
def success(request):
    return HttpResponse("welcome to success")

def signIn(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('/stu_deskboard')

				#return HttpResponseRedirect("/stu_deskboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/signIn.html", context={"form":form})