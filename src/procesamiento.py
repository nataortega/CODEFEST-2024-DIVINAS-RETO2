import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, find_peaks

# Cargar archivo CSV
def cargar_datos(file_path):
    df = pd.read_excel(file_path)
    return df

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
