from django.shortcuts import render

# Create your views here.

# this is my views.py

def home(request):
	return render(request,'home.html',{})


def about(request):
	return render(request,'about.html',{})
