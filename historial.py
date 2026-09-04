import csv
import os

ARCHIVO = "historial.csv"

def guardar_busqueda(p1, p2, gp, año, resultado):
    try:
        with open(ARCHIVO, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([p1, p2, gp, año, resultado])
    except Exception as e:
        print(f"Error al guardar historial: {e}")

def leer_historial():
    try:
        if not os.path.exists(ARCHIVO):
            return []
        with open(ARCHIVO, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    except Exception as e:
        return []
    