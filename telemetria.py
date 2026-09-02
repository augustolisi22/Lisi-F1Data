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
