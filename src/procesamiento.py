import csv
import pandas as pd
import numpy as np
import re


def leer_rango_filas(csv_path, fila_inicio, fila_fin):
    filas_en_rango = []
    with open(csv_path, 'r', encoding='utf-8') as archivo_csv:
        lector = csv.reader(archivo_csv)  # Usa el delimitador si es diferente a la coma.
        for numero_fila, fila in enumerate(lector, start=1):
            if fila_inicio <= numero_fila <= fila_fin:
                # Almacena la fila completa como un string separado por comas
                filas_en_rango.append(','.join(fila))
            elif numero_fila > fila_fin:
                # Detenemos la lectura si ya estamos fuera del rango
                break
    return filas_en_rango

# Cargar archivo CSV
import pandas as pd

# Leer el CSV

file_path = 'data/SPG_002.csv'
markers_list = leer_rango_filas(file_path,42,53)

    
    # Leer el archivo línea por línea
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

    # Inicializar un diccionario para almacenar los valores de los markers
markers = {}

    # Expresión regular para buscar los valores de los markers
marker_pattern = re.compile(r'Marker (\d+);([\d,.]+);Hz')

    # Iterar sobre las líneas buscando los markers
for line in lines:
    match = marker_pattern.search(line)
    if match:
        marker_num = int(match.group(1))  # Número del marker
        marker_value = match.group(2).replace(',', '')  # Eliminar comas de los valores
        markers[f'Marker {marker_num}'] = float(marker_value)

    # Mostrar los valores extraídos
for marker, value in markers.items():
    print(f"{marker}: {value} Hz")

    # Guardar los valores en variables individuales si es necesario
marker_1 = markers.get('Marker 1')
marker_2 = markers.get('Marker 2')
marker_3 = markers.get('Marker 3')
marker_4 = markers.get('Marker 4')
marker_5 = markers.get('Marker 5')
marker_6 = markers.get('Marker 6')



    
ruta_csv = 'data/SPG_002.csv'
n_filas_a_eliminar = 687 # Cambia este valor al número de filas que quieras eliminar

# Leer el archivo y saltar las primeras n líneas
with open(ruta_csv, 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

# Eliminar las primeras n líneas
lineas_sin_filas_iniciales = lineas[n_filas_a_eliminar:]

# Guardar el contenido restante en un nuevo archivo o sobrescribir el existente
with open('data/SPG_002_sin_filas.csv', 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.writelines(lineas_sin_filas_iniciales)

print(f'Se han eliminado las primeras {n_filas_a_eliminar} filas del archivo.')


df = pd.read_csv('data/SPG_002_sin_filas.csv', delimiter=';', skiprows=[0])
print(df.info())
df['Timestamp (Relative)'] = df['Timestamp (Relative)'].str.replace(',', '.')
df['Timestamp (Relative)'] = pd.to_numeric(df['Timestamp (Relative)'], errors='coerce')

    # Visualizar las primeras filas
print(df.head(15))
print(df.tail(15))

print("MARKER1: SATELITE 1 \n")

marker1_filtro = df[(df['Timestamp (Relative)'] >= marker_1-100000) & (df['Timestamp (Relative)'] < marker_1+100000)]
print(marker1_filtro.head(5))
print(marker1_filtro.tail(5))


print("MARKER2: SATELITE 1 \n")
marker2_filtro = df[(df['Timestamp (Relative)'] >= marker_2-100000) & (df['Timestamp (Relative)'] < marker_2+100000)]
print(marker2_filtro.head(5))
print(marker2_filtro.tail(5))



print("MARKER4: SATELITE 2 \n")
marker4_filtro = df[(df['Timestamp (Relative)'] >= marker_4-100000) & (df['Timestamp (Relative)'] < marker_4+100000)]
print(marker4_filtro.head(5))
print(marker4_filtro.tail(5))
print("MARKER5:  SATELITE 2 \n")
marker5_filtro = df[(df['Timestamp (Relative)'] >= marker_5-100000) & (df['Timestamp (Relative)'] < marker_5+100000)]
print(marker5_filtro.head(5))
print(marker5_filtro.tail(5))
print("MARKER6: SATELITE 6 \n")
marker6_filtro = df[(df['Timestamp (Relative)'] >= marker_6-100000) & (df['Timestamp (Relative)'] < marker_6+100000)]
print(marker6_filtro.head(5))
print(marker6_filtro.tail(5))
    # Extracción de columnas Timestamp y Magnitude para análisis


mayor_marker_1 = marker1_filtro['Timestamp (Relative)'].max()
mayor_marker_2 = marker2_filtro['Timestamp (Relative)'].max()


mayor_marker_4 = marker4_filtro['Timestamp (Relative)'].max()
mayor_marker_5 = marker5_filtro['Timestamp (Relative)'].max()
mayor_marker_6 = marker6_filtro['Timestamp (Relative)'].max()

mayor_sat1 = max([mayor_marker_1, mayor_marker_2])

mayor_sat2 = max([mayor_marker_4, mayor_marker_5, mayor_marker_6])
print("Maximo Satelite 1:" + str(mayor_sat1))
print("Maximo Satelite 2:" + str(mayor_sat2))

