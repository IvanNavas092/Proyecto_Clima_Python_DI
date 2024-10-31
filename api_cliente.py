# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:48:46 2024

@author: navas
"""
#%% Importar Módulos
import requests
from config import API_KEY, GEOCODE_API_KEY

#%% Funciones
class MeteostatAPIClient:
    def __init__(self):
        self.base_url = "https://meteostat.p.rapidapi.com/point/daily"
        self.geocode_url = "https://api.opencagedata.com/geocode/v1/json"

    def get_coordinates(self, city):
        """Obtiene las coordenadas de la ciudad dada."""
        params = {
            'q': city,
            'key': GEOCODE_API_KEY  # API Key de OpenCage
        }
        response = requests.get(self.geocode_url, params=params)
        if response.status_code == 200:
            results = response.json()['results']
            if results:
                lat = results[0]['geometry']['lat']
                lon = results[0]['geometry']['lng']
                return lat, lon
        print(f"Error {response.status_code}: {response.json()}")
        return None, None

    def get_weekly_data(self, lat, lon, start_date, end_date):
        """Obtiene datos diarios de temperatura, precipitaciones y velocidad del viento para una semana."""
        params = {
            'lat': lat,
            'lon': lon,
            'start': start_date,
            'end': end_date,
            'units': 'metric'
        }
        headers = {
            'x-rapidapi-key': API_KEY,
            "x-rapidapi-host": "meteostat.p.rapidapi.com"
        }

        response = requests.get(self.base_url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(f"Error {response.status_code}: {response.json()}")
            return None
