from scipy.signal import butter, filtfilt

def butter_bandpass(lowcut, highcut, sample_rate, order=5):
    """
    Calcula los coeficientes de un filtro de paso de banda (Bandpass) usando el filtro Butterworth.
    
    :param lowcut: Frecuencia de corte inferior.
    :param highcut: Frecuencia de corte superior.
    :param sample_rate: Frecuencia de muestreo de los datos.
    :param order: Orden del filtro. Un mayor orden genera un filtro más selectivo.
    :return: Coeficientes del filtro Butterworth.
    """
    nyquist = 0.5 * sample_rate  # Frecuencia de Nyquist
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, sample_rate, order=5):
    """
    Aplica un filtro de paso de banda (Bandpass) a los datos.
    
    :param data: Señal de entrada (los datos de magnitud).
    :param lowcut: Frecuencia de corte inferior.
    :param highcut: Frecuencia de corte superior.
    :param sample_rate: Frecuencia de muestreo de los datos.
    :param order: Orden del filtro.
    :return: Señal filtrada.
    """
    b, a = butter_bandpass(lowcut, highcut, sample_rate, order=order)
    y = filtfilt(b, a, data)
    return y

def butter_lowpass(cutoff, sample_rate, order=5):
    """
    Calcula los coeficientes de un filtro de paso bajo (Lowpass) usando el filtro Butterworth.
    
    :param cutoff: Frecuencia de corte del filtro.
    :param sample_rate: Frecuencia de muestreo de los datos.
    :param order: Orden del filtro.
    :return: Coeficientes del filtro Butterworth.
    """
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, sample_rate, order=5):
    """
    Aplica un filtro de paso bajo (Lowpass) a los datos.
    
    :param data: Señal de entrada (los datos de magnitud).
    :param cutoff: Frecuencia de corte del filtro.
    :param sample_rate: Frecuencia de muestreo de los datos.
    :param order: Orden del filtro.
    :return: Señal filtrada.
    """
    b, a = butter_lowpass(cutoff, sample_rate, order=order)
    y = filtfilt(b, a, data)
    return y

def butter_highpass(cutoff, sample_rate, order=5):
    """
    Calcula los coeficientes de un filtro de paso alto (Highpass) usando el filtro Butterworth.
    
    :param cutoff: Frecuencia de corte del filtro.
    :param sample_rate: Frecuencia de muestreo de los datos.
    :param order: Orden del filtro.
    :return: Coeficientes del filtro Butterworth.
    """
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, sample_rate, order=5):
    """
    Aplica un filtro de paso alto (Highpass) a los datos.
    
    :param data: Señal de entrada (los datos de magnitud).
    :param cutoff: Frecuencia de corte del filtro.
    :param sample_rate: Frecuencia de muestreo de los datos.
    :param order: Orden del filtro.
    :return: Señal filtrada.
    """
    b, a = butter_highpass(cutoff, sample_rate, order=order)
    y = filtfilt(b, a, data)
    return y
