import tkinter as tk
from tkinter import ttk
import pandas as pd


def show_dataframe():
    # Crear un DataFrame de ejemplo
    data = {
        "Nombre": ["Juan", "María", "Pedro"],
        "Edad": [25, 30, 27],
        "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
    }
    df = pd.DataFrame(data)

    # Crear ventana y tabla
    window = tk.Tk()
    window.title("Mostrar DataFrame en Tkinter")

    frame = ttk.Frame(window)
    frame.pack(pady=20)

    # Crear tabla
    table = ttk.Treeview(frame)
    table["columns"] = list(df.columns)

    # Configurar encabezados de columna
    for column in df.columns:
        table.heading(column, text=column)

    # Agregar filas al árbol
    for _, row in df.iterrows():
        table.insert("", tk.END, values=list(row))

    # Ajustar el ancho de las columnas
    for column in df.columns:
        table.column(column, width=100, anchor=tk.CENTER)

    # Mostrar tabla
    table.pack()

    window.mainloop()


# Ejecutar la función para mostrar el DataFrame en la interfaz gráfica
show_dataframe()
