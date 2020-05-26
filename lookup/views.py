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

	if api[0]['Category']['Name'] == "Good":
		category_description = "(0-50) Air quality is considred statisfactory, and air pollution poses little or no risk."
		category_color = "good"
	elif api[0]['Category']['Name'] == "Moderate":
		category_description = "(51-100) Air quality is accepatable."
		category_color = "moderate"
	elif api[0]['Category']['Name'] == "USG":
		category_description = "(101-150) Healthy people may experience slight irritations and sensitive individuals will be slightly affected to a larger extent."
		category_color = "usg"
	elif api[0]['Category']['Name'] == "Unhealthy":
		category_description = "(151-200) Sensitive individuals will experience more serious conditions. The hearts and respiratory systems of healthy people may be affected."
		category_color = "unhealthy"
	elif api[0]['Category']['Name'] == "Very Unhealthy":
		category_description = "(201-300) Healthy people will commonly show symptoms. People with respiratory or heart diseases will be significantly affected and will experience reduced endurance in activities."
		category_color = "very unhealthy"
	elif api[0]['Category']['Name'] == "Hazardous":
		category_description = "(>300)Healthy people will experience reduced endurance in activities and may also show noticeably strong symptoms. Other illnesses may be triggered in healthy people. Elders and the sick should remain indoors and avoid exercise. Healthy individuals should avoid outdoor activities."
		category_color = "hazardous"
	return render(request,'home.html',{ 'api' : api, 'category_description': category_description, 'category_color': category_color})


def about(request):
	return render(request,'about.html',{})
