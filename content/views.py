from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cour,Document,Devoir,Exam,Comment,Annonce
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt
from .forms import CommentForm


@login_required(login_url='login')
def home(request):
	obj=Cour.objects.all()
	context={
    'cours':obj

	}
	return render(request,'home.html',context)
	
@login_required(login_url='login')	
def cours(request):
	obj=Document.objects.all()
	context={
	'doc':obj,
	'lien':'hell'
	}

	return render(request,'cours.html',context)
@login_required(login_url='login')	
@xframe_options_exempt
def content(request,slug):
	c=Cour.objects.get(slug=slug)
	d=Document.objects.all()

	context={
	'cours':c,
	'doc':d,



	}
	return render(request,'cours.html',context)

def about(request):
	return render(request,'about.html') 
@login_required(login_url='login')	
def devoir(request,slug):
	c=Cour.objects.get(slug=slug)
	d=Devoir.objects.all()
	context={
	'cours':c,
	'devoir':d,
	}
	return render(request,'devoir.html',context)
@login_required(login_url='login')	
def exam(request,slug):
	c=Cour.objects.get(slug=slug)
	d=Exam.objects.all()
	context={
	'cours':c,
	'exam':d,
	}
	return render(request,'exam.html',context)
def comments(request):
	return render(request,'comment.html',context)
def rendre(request):
	return render(request,'rendre.html')
def annoce(request,slug):
	c=Cour.objects.get(slug=slug)
	d=Annonce.objects.all()
	context={
	'cours':c,
	'devoir':d,
	}
	return render(request,'annonce.html',context)	