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

    except:
        return "⚠️ Error al buscar."