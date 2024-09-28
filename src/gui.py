import tkinter as tk
from tkinter import filedialog
from procesamiento import cargar_datos, procesar_datos
from visualizacion import mostrar_espectrograma

def iniciar_gui():
    root = tk.Tk()
    root.title("Analizador de Señales RF")

    def cargar_archivo():
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.xslx")])
        if file_path:
            datos = cargar_datos(file_path)
            procesar_datos(datos)
            mostrar_espectrograma(datos)

    boton_cargar = tk.Button(root, text="Cargar CSV", command=cargar_archivo)
    boton_cargar.pack(pady=20)

    root.mainloop()
