import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

# Cargar archivo CSV
import pandas as pd

# Leer el CSV
df = pd.read_csv('C:/Users/Usuario/Documents/codefest/divinas/CODEFEST-2024-DIVINAS-RETO2/resources/SPG_001.csv', delimiter=';', skiprows=[0], on_bad_lines='skip')
print(df.columns)

# Visualizar las primeras filas
print(df.head())

# Extracción de columnas Timestamp y Magnitude para análisis
timestamps_absolute = df['Timestamp (Relative)']
magnitudes = df.filter(like='Magnitude')  # Selecciona todas las columnas de Magnitudes

# Mostrar un resumen de las magnitudes y el tiempo
print(magnitudes.describe())

# Si se desea analizar una frecuencia en específico:
frecuencia_especifica = df[df['Frequency [Hz]'] == 420000000]
print(frecuencia_especifica[['Timestamp (Relative)', 'Magnitude [dBm]']])



# Filtrar ruido (filtro pasa bajos)
def filtrar_ruido(signal, cutoff_freq, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, signal)
    return y

# Detectar picos en la señal
def detectar_picos(signal, height=None, distance=None):
    picos, _ = find_peaks(signal, height=height, distance=distance)
    return picos

# Procesar datos
def procesar_datos(df):
    # Suponemos que la columna de frecuencia es 'Frequency [Hz]' y amplitud 'Magnitude [dB]'
    signal = df['Magnitude [dB]'].values
    freqs = df['Frequency [Hz]'].values

    # Filtrado de ruido
    cutoff_freq = 300  # Definir frecuencia de corte
    fs = 1000  # Frecuencia de muestreo (modificar según los datos)
    señal_filtrada = filtrar_ruido(signal, cutoff_freq, fs)

    # Detección de picos
    picos = detectar_picos(señal_filtrada, height=-50)
    print(f"Picos detectados en las frecuencias: {freqs[picos]}")
