from django.views.decorators.csrf import csrf_exempt
from .weatherDetect import weather
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import urllib.request
import json
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def submit(request):
    if request.method == "POST":
        try:
            city = request.POST.get("location")
            temp, humidity, weather_state = weather(city)
            response_html = f"<h2>Weather Information for {city}</h2>"
            response_html += f"<p>Temperature: {temp}</p>"
            response_html += f"<p>Humidity: {humidity}</p>"
            response_html += f"<p>Weather Condition: {weather_state}</p>"
            return HttpResponse(response_html)
        except KeyError:
            template = loader.get_template('index.html')
            return HttpResponse(template.render())

    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
    
