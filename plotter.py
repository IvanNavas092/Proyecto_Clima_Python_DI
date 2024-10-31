# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:48:46 2024

@author: navas
"""
#%% Importar Módulos
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#%% Importar Módulos
class WeatherPlotter:
    # Inicializa el plotter con datos y ciudad y creo carpeta de gráficos
    def __init__(self, data_df, city):
        self.data_df = data_df
        self.city = city
        self.folder_path = self.create_folder_path(city)

        # Crea la carpeta si no existe
        os.makedirs(self.folder_path, exist_ok=True)

    def create_folder_path(self, city):
        base_path = os.path.join("graphics", city)
        folder_path = base_path
        counter = 1
        
        # Verificar si la carpeta ya existe y crea un nuevo nombre si es necesario
        while os.path.exists(folder_path):
            folder_path = f"{base_path}_{counter}"
            counter += 1
        
        return folder_path

    # Grafica la temperatura media semanal
    def plot_temperature(self):
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=self.data_df, x='date', y='tavg', marker='o', color='#FF6347', linewidth=2.5)
        plt.title(f"Temperatura media semanal en {self.city}")
        plt.xlabel("Fecha")
        plt.ylabel("Temperatura (°C)")
        plt.grid(color='#444444')
        plt.savefig(os.path.join(self.folder_path, f"{self.city}_temperatura.png"), bbox_inches='tight', dpi=100)
        plt.show()
        
     # Grafica las precipitaciones de la semana
    def plot_precipitation(self):
        plt.figure(figsize=(12, 6))
        sns.scatterplot(data=self.data_df, x='date', y='prcp', color='blue', marker='o', s=100, edgecolor='black', alpha=0.7)
        plt.title(f"Precipitaciones semanales en {self.city}")
        plt.xlabel("Fecha")
        plt.ylabel("Precipitación (mm)")
        plt.grid(color='#444444')
        plt.savefig(os.path.join(self.folder_path, f"{self.city}_precipitacion.png"), bbox_inches='tight', dpi=100)
        plt.show()


   # Grafica la velocidad del viento semanal
    def plot_wind_speed(self):
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=self.data_df, x='date', y='wspd', marker='o', color='#32CD32', linewidth=2.5)
        plt.title(f"Velocidad del viento semanal en {self.city}")
        plt.xlabel("Fecha")
        plt.ylabel("Velocidad del viento (km/h)")
        plt.grid(color='#444444')
        plt.savefig(os.path.join(self.folder_path, f"{self.city}_viento.png"), bbox_inches='tight', dpi=100)
        plt.show()

    # Crea una tabla de calor de las temperaturas (máxima, media y mínima)
    def plot_temperature_table(self):
        # Crear un DataFrame para almacenar las maximas, medias y minimas
        temperature_data = {
            "Día": self.data_df['date'].dt.strftime('%A').tolist(),
            "Máxima": self.data_df['tmax'].tolist(),  # Asegúrate de que 'tmax' esté en los datos
            "Media": self.data_df['tavg'].tolist(),
            "Mínima": self.data_df['tmin'].tolist()  # Asegúrate de que 'tmin' esté en los datos
        }
        temp_df = pd.DataFrame(temperature_data)

        # Configurar el DataFrame para el heatmap
        heatmap_data = temp_df.set_index("Día")

        # Crear un gráfico de calor usando seaborn
        plt.figure(figsize=(8, 4))
        sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="coolwarm", linewidths=.5, cbar_kws={'label': 'Temperatura (°C)'})

        # Título del gráfico
        plt.title(f"Temperaturas en {self.city} - Semana", fontsize=16)
        plt.savefig(os.path.join(self.folder_path, f"{self.city}_temperaturas_heatmap.png"), bbox_inches='tight', dpi=100)
        plt.show()
