from django.shortcuts import render

# Create your views here.

# this is my views.py

def home(request):

	import json
	import requests

	api_requests= requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=E48705BF-EE6B-408D-945E-89BCC0B8E69B")

	try:
		api = json.loads(api_requests.content)
	except Exception as e:
		api = "Error ..."

	return render(request,'home.html',{ 'api' : api})


def about(request):
	return render(request,'about.html',{})
