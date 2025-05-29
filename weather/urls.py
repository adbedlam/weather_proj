from django.urls import path
from .views import weather_view, stats_api, autocomplete_city

urlpatterns = [
    path('', weather_view, name='weather_home'),
    path('autocomplete/',autocomplete_city, name='autocomplete_city'),

    path('api/stats/', stats_api, name='stats_api')
]
