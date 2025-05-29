import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import CitySearch

def get_weather(city):
    geo_resp = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json")
    if geo_resp.status_code != 200 or not geo_resp.json().get('results'):
        return {}

    location = geo_resp.json()['results'][0]
    lat, lon = location['latitude'], location['longitude']

    weather_resp = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&forecast_days=1"
    )

    if weather_resp.status_code != 200:
        return {}

    data = weather_resp.json()
    data['city'] = location['name']
    return data


def weather_view(request):
    city = request.GET.get("city")
    weather_data = None
    hourly_data = []

    if city:
        session_id = request.session.session_key or request.session.save()
        CitySearch.objects.create(city=city, session_id=request.session.session_key)
        request.session['last_city'] = city
        weather_data = get_weather(city)

        if 'hourly' in weather_data:
            times = weather_data['hourly']['time'][:24]
            temps = weather_data['hourly']['temperature_2m'][:24]
            hourly_data = list(zip(times, temps))

    last_city = request.session.get('last_city')
    return render(request, 'weather/index.html', {
        'weather': weather_data,
        'last_city': last_city,
        'hourly_data': hourly_data,
    })
def stats_api(request):
    from django.db.models import Count
    stats = CitySearch.objects.values('city').annotate(count=Count('city')).order_by('-count')
    return JsonResponse(list(stats), safe=False)

def autocomplete_city(request):
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse([], safe=False)

    resp = requests.get(
        f'https://geocoding-api.open-meteo.com/v1/search?name={query}&count=5&language=ru&format=json'
    )

    suggestions = []
    if resp.status_code == 200:
        data = resp.json()
        for item in data.get('results', []):
            suggestions.append(item['name'])

    return JsonResponse(suggestions, safe=False)