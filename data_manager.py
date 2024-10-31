# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:48:46 2024

@author: navas
"""
#%% Importar Módulos
import pandas as pd

#%% Funciones
class WeatherDataManager:
    def __init__(self, data):
        self.data = data

    def extract_weekly_averages(self):
        """Extrae las temperaturas, precipitaciones y viento semanales en formato de DataFrame."""
        df = pd.DataFrame(self.data)
        df['date'] = pd.to_datetime(df['date'])

        # Calcular la media semanal de temperatura, precipitaciones y viento
        weekly_avg = {
            'temperature': df['tavg'].mean(),
            'precipitation': df['prcp'].sum(),
            'wind_speed': df['wspd'].mean()
        }
        return df, weekly_avg
