from django.shortcuts import render

import requests

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=500ddbd31d297183f6f6292e03a32866'

    city ="Las Vegas"

    r = requests.get(url.format(city)).json()
    print(r.text)

    city_weather = {

        'city': city ,
        'temperature': r['main']['temp'] ,
        'description': r['weather'][0]['description'] ,
        'icon': r['weather'][0]['icon'],



    }

    return render(request,'weather/weather.html')
