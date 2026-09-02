"""Descarga de series de la FED (FRED, St. Louis) sin necesidad de API key.

Usa el endpoint público fredgraph.csv. Para uso intensivo, crea una API key
gratuita en https://fred.stlouisfed.org y usa la librería `fredapi`.

Ejemplo
-------
>>> from utils.fred import get_series
>>> t10 = get_series("DGS10")   # rendimiento del Treasury a 10 años
"""
from __future__ import annotations

import pandas as pd

BASE = "https://fred.stlouisfed.org/graph/fredgraph.csv"


def get_series(codigo: str, inicio: str | None = None, fin: str | None = None) -> pd.Series:
    """Descarga una serie de FRED como pd.Series indexada por fecha.

    Parameters
    ----------
    codigo : str
        Código FRED, p. ej. "DGS10" (Treasury 10Y), "FEDFUNDS", "CPIAUCSL".
    inicio, fin : str, opcional
        Fechas "AAAA-MM-DD" para recortar la serie.
    """
    df = pd.read_csv(f"{BASE}?id={codigo}", parse_dates=["observation_date"])
    s = (df.set_index("observation_date")[codigo]
           .apply(pd.to_numeric, errors="coerce")
           .rename(codigo))
    if inicio:
        s = s.loc[inicio:]
    if fin:
        s = s.loc[:fin]
    return s
