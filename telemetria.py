import fastf1
import os

if not os.path.exists('cache'):
    os.makedirs('cache')

fastf1.Cache.enable_cache('cache')


def formato_tiempo(tiempo):
    try:
        minutos = int(tiempo.total_seconds() // 60)
        segundos = tiempo.total_seconds() % 60
        return f"{minutos:02d}:{segundos:06.3f}"
    except:
        return "No hay tiempo disponible"


def comparar_ritmo(piloto1, piloto2, gp, año):
    try:
        p1 = piloto1.strip().upper()
        p2 = piloto2.strip().upper()
        gran_premio = gp.strip().title()

        sesion = fastf1.get_session(int(año), gran_premio, 'R')
        sesion.load(telemetry=True, weather=False)

        resultado_p1 = sesion.results.loc[sesion.results['Abbreviation'] == p1].iloc[0]
        resultado_p2 = sesion.results.loc[sesion.results['Abbreviation'] == p2].iloc[0]

        try:
            pos_p1 = f"P{int(resultado_p1['Position'])}"
        except:
            pos_p1 = "No se encontró la posición del piloto"
            
        try:
            pos_p2 = f"P{int(resultado_p2['Position'])}"
        except:
            pos_p2 = "No se encontró la posición del piloto"

        laps_p1 = sesion.laps.pick_driver(p1)
        laps_p2 = sesion.laps.pick_driver(p2)
        
        vueltas_totales_p1 = len(laps_p1)
        vueltas_totales_p2 = len(laps_p2)
        
        vuelta_p1 = laps_p1.pick_fastest()
        vuelta_p2 = laps_p2.pick_fastest()
        
    except:
        return "⚠️ Error al buscar."