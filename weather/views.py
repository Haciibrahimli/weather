# from base64 import urlsafe_b64decode
# import asyncio
# import os
# from .forms import CityForm
from aiohttp import RequestInfo
from django.template import RequestContext
import python_weather
from django.shortcuts import render


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_APP_KEY'

    city = 'Las Vegas'

    city_weather = RequestContext.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    return render(request, 'weather/index.html') #returns the index.html template

def index(request):
    return render(request, 'weather/index.html') #returns the index.html template

...
def index(request):
    ...
    print(city_weather) #temporarily view output

    return render(request, 'weather/index.html') #returns the index.html template
...
def index(request):
    ...
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    return render(request, 'weather/index.html') #returns the index.html template

...
def index(request):
    ...
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    return render(request, 'weather/index.html') #returns the index.html template
...
def index(request):
    ...
    context = {'weather' : weather}

    return render(request, 'weather/index.html', context) #returns the index.html template



# ...
# def index(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_APP_KEY'

#     cities = City.objects.all() #return all the cities in the database

#     if request.method == 'POST': # only true if form is submitted
#         form = CityForm(request.POST) # add actual request data to form for processing
#         form.save() # will validate and save if validate

#     form = CityForm()
#     ...

# def index(request):
#     ...
#     form = CityForm()

#     weather_data = []
#     ...
#     context = {'weather_data' : weather_data, 'form' : form}

# ...
# def index(request):
#     ...
#     cities = City.objects.all() #return all the cities in the database

#     weather_data = []

#     for city in cities:

#         city_weather = RequestInfo.get(urlsafe_b64decode.format(city)).json() #request the API data and convert the JSON to Python data types

#         weather = {
#             'city' : city,
#             'temperature' : city_weather['main']['temp'],
#             'description' : city_weather['weather'][0]['description'],
#             'icon' : city_weather['weather'][0]['icon']
#         }

#         weather_data.append(weather) #add the data for the current city into our list

#     context = {'weather_data' : weather_data}

#     return render(request, 'weather/index.html', context) #returns the index.html template