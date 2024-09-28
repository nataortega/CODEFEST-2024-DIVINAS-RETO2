import pandas as pd

def load_csv_clean(file_path):
    """
    Carga un archivo CSV y extrae las tablas relevantes (frecuencia-magnitud y series temporales),
    eliminando los metadatos y limpiando el archivo.
    
    :param file_path: Ruta del archivo CSV a cargar.
    :return: Dos DataFrames, uno con la tabla de frecuencia-magnitud y otro con la tabla de series temporales.
    """
    try:
        # Leer el archivo completo en un DataFrame sin suponer estructura fija
        data = pd.read_csv(file_path, header=None)

        # Encontrar la fila donde empieza la tabla de frecuencia-magnitud
        freq_mag_start = data[data[0] == 'Frequency [Hz]'].index[0]
        
        # Encontrar la fila donde empieza la tabla de series temporales
        series_time_start = data[data[0] == 'Timestamp (Absolute)'].index[0]

        # Extraer la tabla de frecuencia-magnitud (desde el header hasta justo antes de la siguiente tabla)
        freq_mag_table = data.iloc[freq_mag_start:series_time_start].reset_index(drop=True)

        # Limpiar y formatear la tabla de frecuencia-magnitud
        freq_mag_table.columns = freq_mag_table.iloc[0]  # Asignar la primera fila como encabezado
        freq_mag_table = freq_mag_table.drop(0)  # Eliminar la fila del encabezado duplicado
        freq_mag_table = freq_mag_table.dropna()  # Eliminar filas vacías

        # Extraer la tabla de series temporales (desde su encabezado hasta el final)
        series_table = data.iloc[series_time_start:].reset_index(drop=True)

        # Limpiar y formatear la tabla de series temporales
        series_table.columns = series_table.iloc[0]  # Asignar la primera fila como encabezado
        series_table = series_table.drop(0).reset_index(drop=True)  # Eliminar la fila del encabezado duplicado
        series_table = series_table.dropna()  # Eliminar filas vacías

        return freq_mag_table, series_table

    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
        return None, None
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")
        return None, None
