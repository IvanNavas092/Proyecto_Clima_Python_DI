# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:49:07 2024

@author: navas
"""

# App de Clima Semanal

Esta aplicación obtiene y visualiza datos meteorológicos semanales de cualquier ciudad
usando la API de Meteostat y la API de OpenCage. Muestra datos de temperatura,
precipitaciones y velocidad del viento en gráficos generados con `matplotlib`
y `seaborn`, con una interfaz gráfica de usuario creada con `Tkinter`.

## Características

- **Obtención de datos**: Realiza consultas a la API de Meteostat y OpenCage para obtener
  información meteorológica de cualquier ciudad.
- **Visualización**: Genera gráficos de línea y de dispersión para temperatura, precipitaciones
  y velocidad del viento.
- **Interfaz gráfica**: Permite al usuario introducir el nombre de una ciudad y obtener los
  gráficos meteorológicos de la semana.
- **Archivos de salida**: Los gráficos generados se guardan como imágenes PNG en una carpeta
  específica de cada ciudad.

## Requisitos

- Python 3.8+
- Bibliotecas de Python:
  - `requests`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `tkinter`
- Claves de API:
  - [Meteostat API](https://rapidapi.com/meteostat/api/meteostat)
  - [OpenCage API](https://opencagedata.com/)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/usuario/repositorio.git
    cd repositorio
    ```
2. Instala las dependencias:
    ```bash
    pip install requests pandas matplotlib seaborn
    ```
3. Configura tus claves de API en el archivo `config.py`:
    ```python
    API_KEY = "TU_METEOSTAT_API_KEY"
    GEOCODE_API_KEY = "TU_OPENCAGE_API_KEY"
    ```

## Estructura del Proyecto

- `api_cliente.py`: Obtiene coordenadas y datos meteorológicos.
- `data_manager.py`: Procesa los datos y calcula promedios semanales.
- `plotter.py`: Genera gráficos de temperatura, precipitaciones y velocidad del viento.
- `main.py`: Ejecuta la interfaz gráfica para introducir la ciudad y mostrar los gráficos generados.
- `config.py`: Contiene las claves de API.

## Uso

1. Ejecuta la aplicación:
    ```bash
    python main.py
    ```
2. Introduce el nombre de una ciudad en la interfaz y haz clic en "Obtener Clima".

3. La aplicación generará los gráficos correspondientes y los guardará en la carpeta `graphics/<nombre_ciudad>`.

## Ejemplo de Salida

Se generarán gráficos como los siguientes para la ciudad consultada:
- **Temperatura semanal**
- **Precipitaciones semanales**
- **Velocidad del viento semanal**
- **Tabla de calor de temperaturas máximas, medias y mínimas**

## Notas

- Los gráficos se guardarán como archivos PNG en una carpeta específica de cada ciudad dentro de la
  carpeta `graphics`.
- Asegúrate de tener conexión a Internet, ya que se realiza una consulta a las APIs en tiempo real.

---


