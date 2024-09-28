import tkinter as tk
from tkinter import filedialog, messagebox
from src.file_loader import load_csv_clean
from src.analysis import compute_fft, detect_peaks, calculate_bandwidth
from src.filters import butter_bandpass_filter
from src.visualization import plot_spectrum, plot_peaks

def open_file():
    """
    Función que se ejecuta cuando el usuario selecciona un archivo.
    Carga el archivo CSV, limpia los metadatos y extrae las tablas de datos.
    """
    file_path = filedialog.askopenfilename()
    if file_path:
        # Cargar y limpiar el archivo CSV
        freq_mag_table, series_table = load_csv_clean(file_path)
        
        if freq_mag_table is not None and series_table is not None:
            # Mostrar un mensaje indicando que el archivo fue procesado correctamente
            messagebox.showinfo("Éxito", "Archivo CSV cargado y procesado correctamente.")
            
            # Llamar a la función que permite analizar y graficar los datos
            analyze_data(freq_mag_table, series_table)
        else:
            messagebox.showerror("Error", "El archivo CSV no pudo ser procesado. Verifica su formato.")
    else:
        messagebox.showerror("Error", "No se seleccionó ningún archivo.")

def analyze_data(freq_mag_table, series_table):
    """
    Función que realiza el análisis de datos. Aplica un filtro de paso de banda,
    FFT, detección de picos y visualiza los resultados.
    """
    # Parámetros de filtrado y análisis (puedes ajustarlos según tus necesidades)
    lowcut = 400000000  # Frecuencia de corte inferior (400 MHz)
    highcut = 450000000  # Frecuencia de corte superior (450 MHz)
    sample_rate = 1000000  # Frecuencia de muestreo (ajustar según el archivo CSV)

    # Extraer los datos de frecuencia y magnitud de la tabla de frecuencia-magnitud
    frequency_data = freq_mag_table['Frequency [Hz]'].astype(float).values
    magnitude_data = freq_mag_table['Magnitude [dBm]'].astype(float).values
    
    # Aplicar filtro de paso de banda a los datos
    filtered_magnitude = butter_bandpass_filter(magnitude_data, lowcut, highcut, sample_rate)

    # Graficar el espectro de frecuencia con la señal filtrada
    plot_spectrum(frequency_data, filtered_magnitude, title="Espectro Frecuencia-Magnitud Filtrado")
    
    # Realizar FFT en los datos filtrados
    xf, yf = compute_fft(filtered_magnitude, sample_rate)
    
    # Detectar picos en la señal transformada
    peak_freq, peak_mag = detect_peaks(xf, yf, height=1)
    
    # Graficar los picos detectados
    plot_peaks(xf, yf, peak_freq, peak_mag, title="Picos Detectados en el Espectro")

def create_gui():
    """
    Función principal que crea la interfaz gráfica usando Tkinter.
    """
    root = tk.Tk()
    root.title("Aplicativo de Análisis de Señales")

    # Botón para cargar archivo CSV
    load_button = tk.Button(root, text="Cargar Archivo CSV", command=open_file)
    load_button.pack(pady=20)

    # Iniciar el bucle principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    create_gui()
