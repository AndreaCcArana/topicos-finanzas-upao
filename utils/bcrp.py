"""Cliente mínimo de la API BCRPData (Banco Central de Reserva del Perú).

Documentación oficial: https://estadisticas.bcrp.gob.pe/estadisticas/series/ayuda/api

Ejemplo
-------
>>> from utils.bcrp import get_series
>>> tc = get_series("PN01207PM", "2015-1", "2026-6")   # tipo de cambio interbancario promedio
>>> tc.head()
"""
from __future__ import annotations

import pandas as pd
import requests

BASE = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"

# Meses en el formato que devuelve BCRPData (p. ej. "Ene.2020")
_MESES = {"Ene": 1, "Feb": 2, "Mar": 3, "Abr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Ago": 8, "Set": 9, "Sep": 9, "Oct": 10, "Nov": 11, "Dic": 12}


def get_series(codigo: str, inicio: str, fin: str) -> pd.Series:
    """Descarga una serie de BCRPData y la devuelve como pd.Series indexada por fecha.

    Parameters
    ----------
    codigo : str
        Código de la serie, p. ej. "PN01207PM". Búscalo en el portal BCRPData.
    inicio, fin : str
        Periodos en formato "AAAA-M" para series mensuales (p. ej. "2015-1")
        o "AAAA" para anuales.
    """
    url = f"{BASE}/{codigo}/json/{inicio}/{fin}"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()

    periodos = data["periods"]
    nombres = [p["name"] for p in periodos]
    valores = [pd.to_numeric(p["values"][0], errors="coerce") for p in periodos]

    idx = pd.to_datetime([_parse_periodo(n) for n in nombres])
    nombre_serie = data.get("config", {}).get("series", [{}])[0].get("name", codigo)
    return pd.Series(valores, index=idx, name=nombre_serie)


def _parse_periodo(name: str) -> str:
    """Convierte 'Ene.2020' -> '2020-01-01'; deja pasar otros formatos."""
    partes = name.replace(" ", "").split(".")
    if len(partes) == 2 and partes[0] in _MESES:
        mes, anio = _MESES[partes[0]], partes[1]
        return f"{anio}-{mes:02d}-01"
    return name
