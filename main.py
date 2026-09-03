import flet as ft
from telemetria import comparar_ritmo
from historial import guardar_busqueda, leer_historial


def main(page: ft.Page):
    page.title = "Lisi-F1-Data"
    page.theme_mode = "dark" 
    
    lista_gps = [
        "Bahrain", "Jeddah", "Melbourne", "Suzuka", 
        "Shanghai", "Miami", "Imola", "Monaco", 
        "Montreal", "Barcelona", "Spielberg", "Silverstone", 
        "Hungaroring", "Spa", "Zandvoort", "Monza", 
        "Baku", "Singapore", "Austin", "Mexico", 
        "Interlagos", "Las Vegas", "Lusail", "Abu Dhabi"
    ]
    
    lista_pilotos = [
        "RUS (#63 - ⚪ Mercedes)", "ANT (#12 - ⚪ Mercedes)",
        "HAM (#44 - 🔴 Ferrari)", "LEC (#16 - 🔴 Ferrari)",
        "NOR (#4 - 🟠 McLaren)", "PIA (#81 - 🟠 McLaren)",
        "VER (#1 - 🔵 Red Bull)", "HAD (#6 - 🔵 Red Bull)",
        "ALO (#14 - 🟢 Aston Martin)", "STR (#18 - 🟢 Aston Martin)",
        "GAS (#10 - 🩵 Alpine)", "COL (#43 - 🩵 Alpine)",
        "SAI (#55 - 💙 Williams)", "ALB (#23 - 💙 Williams)",
        "LAW (#30 - 🔵 VCARB)", "LIN (#7 - 🔵 VCARB)",
        "OCO (#31 - ⚪ Haas)", "BEA (#87 - ⚪ Haas)",
        "HUL (#27 - 🟢 Audi)", "BOR (#5 - 🟢 Audi)",
        "PER (#11 - 🟡 Cadillac)", "BOT (#77 - 🟡 Cadillac)"
    ]
    
    lista_años = ["2023", "2024", "2025", "2026"]

    txt_gp = ft.Dropdown(label="Gran Premio", width=300, options=[ft.dropdown.Option(gp) for gp in lista_gps])
    txt_año = ft.Dropdown(label="Año", width=300, options=[ft.dropdown.Option(año) for año in lista_años])
    txt_p1 = ft.Dropdown(label="Piloto 1", width=300, options=[ft.dropdown.Option(p) for p in lista_pilotos])
    txt_p2 = ft.Dropdown(label="Piloto 2", width=300, options=[ft.dropdown.Option(p) for p in lista_pilotos])

    page.add(
        ft.Row([txt_gp, txt_año]),
        ft.Row([txt_p1, txt_p2])
    )

ft.app(target=main)
 
