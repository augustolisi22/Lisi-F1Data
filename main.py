import flet as ft
from telemetria import comparar_ritmo
from historial import guardar_busqueda, leer_historial


def main(page: ft.Page):
    page.title = "Lisi-F1-Data"
    page.theme_mode = "dark" 
