import matplotlib.pyplot as plt
import numpy as np

# Mostrar el espectrograma
def mostrar_espectrograma(df):
    signal = df['Magnitude [dB]'].values
    freqs = df['Frequency [Hz]'].values

    plt.specgram(signal, Fs=1000)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    plt.colorbar(label='Amplitud (dB)')
    plt.show()
