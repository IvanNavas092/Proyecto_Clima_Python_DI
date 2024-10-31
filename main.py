# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:48:46 2024

@author: navas
"""
#%% Importar Módulos
import tkinter as tk
from api_cliente import MeteostatAPIClient
from data_manager import WeatherDataManager
from plotter import WeatherPlotter
from datetime import datetime, timedelta

#%% Funciones
class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("App Tiempo")
        self.root.geometry("300x200")
        self.root.iconbitmap("./icono.ico")
        
        self.label = tk.Label(root, text="Introduce la ciudad:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.boton = tk.Button(root, text="Obtener Clima", command=self.obtener_datos)
        self.boton.pack()

    def obtener_datos(self):
        city = self.entry.get()
        
        # Obtener coordenadas de la ciudad
        client = MeteostatAPIClient()
        lat, lon = client.get_coordinates(city)
    
        if lat is None or lon is None:
            print("No se pudieron obtener las coordenadas.")
            return
    
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        start_date, end_date = start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
    
        data = client.get_weekly_data(lat, lon, start_date, end_date)
    
        if data:
            manager = WeatherDataManager(data)
            df, weekly_avg = manager.extract_weekly_averages()
    
            plotter = WeatherPlotter(df, city)
            plotter.plot_temperature()          # Gráfico de temperatura
            plotter.plot_precipitation()        # Gráfico de precipitaciones
            plotter.plot_wind_speed()           # Gráfico de velocidad del viento
            plotter.plot_temperature_table()     # Gráfico de tabla
        else:
            print("No se pudieron obtener datos.")

#%% Main
if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()
