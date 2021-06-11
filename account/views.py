from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,login as log,authenticate


# Create your views here.
def register(request):
	 form=UserCreationForm()
	 if request.user.is_authenticated:
	 	return redirect('/')
	 if request.method=='POST':
	 	form=UserCreationForm(request.POST)
	 	if form.is_valid():
	 		form.save()
	 		return redirect('/login')
	 return render(request,'registration/register.html',{'form':form})

