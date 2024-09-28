import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks

def compute_fft(signal_data, sample_rate):
    """
    Realiza la Transformada Rápida de Fourier (FFT) para convertir datos del dominio
    del tiempo al dominio de la frecuencia.
    
    :param signal_data: Listado de magnitudes en el dominio del tiempo (magnitude data).
    :param sample_rate: La frecuencia de muestreo de los datos (frecuencia de adquisición).
    :return: Las frecuencias (xf) y las magnitudes (yf) transformadas por la FFT.
    """
    N = len(signal_data)  # Número de puntos de datos
    yf = fft(signal_data)  # Realiza la FFT
    xf = fftfreq(N, 1 / sample_rate)  # Calcula las frecuencias correspondientes
    return xf[:N//2], np.abs(yf[:N//2])  # Retorna solo la mitad positiva (frecuencia real)


def detect_peaks(frequency_data, magnitude_data, height=None):
    """
    Detecta picos en los datos de magnitud.

    :param frequency_data: Frecuencias obtenidas del análisis FFT.
    :param magnitude_data: Magnitudes asociadas a las frecuencias.
    :param height: Umbral opcional para la detección de picos.
    :return: Las frecuencias y magnitudes correspondientes a los picos detectados.
    """
    peaks, _ = find_peaks(magnitude_data, height=height)
    return frequency_data[peaks], magnitude_data[peaks]


def calculate_bandwidth(frequency_data, magnitude_data, threshold=3):
    """
    Calcula el ancho de banda de la señal utilizando el criterio de -3 dB.
    
    :param frequency_data: Frecuencias obtenidas del análisis FFT.
    :param magnitude_data: Magnitudes asociadas a las frecuencias.
    :param threshold: Nivel de umbral en dB para calcular el ancho de banda.
    :return: El ancho de banda calculado (en Hz).
    """
    max_amplitude = np.max(magnitude_data)
    indices = np.where(magnitude_data > (max_amplitude - threshold))[0]
    bandwidth = frequency_data[indices[-1]] - frequency_data[indices[0]]
    return bandwidth
