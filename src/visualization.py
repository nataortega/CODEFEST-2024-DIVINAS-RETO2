import matplotlib.pyplot as plt

def plot_spectrum(frequency, magnitude, title="Espectro de Frecuencia"):
    """
    Genera un gráfico de línea del espectro de frecuencia vs. magnitud.
    
    :param frequency: Lista o array de frecuencias.
    :param magnitude: Lista o array de magnitudes correspondientes.
    :param title: Título del gráfico.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(frequency, magnitude)
    plt.title(title)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud (dBm)')
    plt.grid(True)
    plt.show()

def plot_peaks(frequency, magnitude, peak_freq, peak_mag, title="Picos Detectados en el Espectro"):
    """
    Grafica el espectro de frecuencia y resalta los picos detectados.
    
    :param frequency: Lista o array de frecuencias.
    :param magnitude: Lista o array de magnitudes correspondientes.
    :param peak_freq: Lista o array de las frecuencias de los picos detectados.
    :param peak_mag: Lista o array de las magnitudes de los picos detectados.
    :param title: Título del gráfico.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(frequency, magnitude, label='Espectro')
    plt.plot(peak_freq, peak_mag, 'rx', label='Picos Detectados')  # Resaltar los picos con "x" rojas
    plt.title(title)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud (dBm)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_spectrogram(time, frequency, magnitude, title="Espectrograma"):
    """
    Grafica un espectrograma para visualizar la evolución temporal de las frecuencias y magnitudes.
    
    :param time: Lista o array de tiempos.
    :param frequency: Lista o array de frecuencias.
    :param magnitude: Matriz de magnitudes donde las filas representan frecuencias y las columnas tiempos.
    :param title: Título del gráfico.
    """
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(time, frequency, magnitude, shading='auto', cmap='viridis')
    plt.title(title)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    plt.colorbar(label='Magnitud (dBm)')
    plt.show()
