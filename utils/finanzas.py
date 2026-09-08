"""Mini-librería del curso Tópicos de Finanzas Avanzadas.

Crece semana a semana: cada clase añade las funciones que construimos juntos.
Al final del curso este archivo es tu caja de herramientas de finanzas
cuantitativas (finanzas cuantitativas estilo CFA en Python).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# ============================================================
# Semana 1: Valor del dinero en el tiempo
# ============================================================

def vp(flujos, r: float) -> float:
    """Valor presente de una lista de flujos CF_1..CF_n a la tasa r."""
    return sum(cf / (1 + r) ** t for t, cf in enumerate(flujos, start=1))


def vpn(cf0: float, flujos, r: float) -> float:
    """VPN = -inversión inicial + valor presente de los flujos."""
    return -cf0 + vp(flujos, r)


def tir(cf0: float, flujos) -> float:
    """Tasa interna de retorno: la r que hace VPN = 0 (raíz real relevante)."""
    coefs = list(reversed(list(flujos))) + [-cf0]
    raices = np.roots(coefs)
    reales = raices[np.isreal(raices)].real
    candidatas = [1 / x - 1 for x in reales if x > 0]
    return min([r for r in candidatas if r > -1], key=abs)


# ============================================================
# Semana 2: Costo de capital (CAPM y WACC)
# ============================================================

def capm(rf: float, beta: float, erp: float, crp: float = 0.0, lam: float = 1.0) -> float:
    """Costo del equity: CAPM con prima por riesgo país opcional."""
    return rf + beta * erp + lam * crp


def wacc(E: float, D: float, ke: float, kd: float, t: float) -> float:
    """Promedio ponderado del costo de capital, pesos a valor de mercado."""
    V = E + D
    return E / V * ke + D / V * kd * (1 - t)


def beta_ajustado(beta_ols: float) -> float:
    """Ajuste de Blume: los betas tienden a 1 en el tiempo."""
    return 0.67 * beta_ols + 0.33


def beta_desapalancar(beta_e: float, d_e: float, t: float) -> float:
    """Beta del negocio (unlevered) a partir del beta del equity."""
    return beta_e / (1 + (1 - t) * d_e)


def beta_reapalancar(beta_u: float, d_e: float, t: float) -> float:
    """Beta del equity para una estructura de capital objetivo."""
    return beta_u * (1 + (1 - t) * d_e)


# ============================================================
# Semana 3: Flujo de caja libre (FCFF y FCFE)
# ============================================================

def fcff_desde_ebit(ebit: float, t: float, dep: float, fcinv: float, wcinv: float) -> float:
    """FCFF = EBIT(1-t) + Dep - FCInv - WCInv."""
    return ebit * (1 - t) + dep - fcinv - wcinv


def fcff_desde_ni(ni: float, ncc: float, interes: float, t: float, fcinv: float, wcinv: float) -> float:
    """FCFF = NI + NCC + Int(1-t) - FCInv - WCInv."""
    return ni + ncc + interes * (1 - t) - fcinv - wcinv


def fcff_desde_cfo(cfo: float, interes: float, t: float, fcinv: float) -> float:
    """FCFF = CFO + Int(1-t) - FCInv."""
    return cfo + interes * (1 - t) - fcinv


def fcfe_desde_fcff(fcff: float, interes: float, t: float, endeudamiento_neto: float) -> float:
    """FCFE = FCFF - Int(1-t) + endeudamiento neto."""
    return fcff - interes * (1 - t) + endeudamiento_neto


def valor_crecimiento_constante(cf1: float, r: float, g: float) -> float:
    """Valor presente de una perpetuidad creciente: V0 = CF1 / (r - g). Requiere g < r."""
    if g >= r:
        raise ValueError("El crecimiento g debe ser menor que la tasa de descuento r.")
    return cf1 / (r - g)


# ============================================================
# Retornos y utilidades básicas
# ============================================================

def retornos(precios: pd.Series | pd.DataFrame, log: bool = False) -> pd.Series | pd.DataFrame:
    """Retornos simples (P_t/P_{t-1} - 1) o logarítmicos (ln P_t - ln P_{t-1})."""
    if log:
        return np.log(precios / precios.shift(1)).dropna()
    return precios.pct_change().dropna()


def resumen_regresion(modelo) -> pd.DataFrame:
    """Tabla compacta de un modelo statsmodels: coeficiente, ee, t, p-valor."""
    return pd.DataFrame({
        "coef": modelo.params,
        "std_err": modelo.bse,
        "t": modelo.tvalues,
        "p_valor": modelo.pvalues,
    })

# ============================================================
# Próximas semanas (se completan en clase)
# ============================================================
# Semana 4:  valor_terminal(), dcf_dos_etapas()
# Semana 5:  multiplos()
# Semana 7:  frontera_eficiente(), min_varianza(), portafolio_tangente()
# Semana 10: sharpe(), treynor(), jensen(), var_historico(), var_parametrico()
# Semana 12: nelson_siegel(), bootstrap_curva()
