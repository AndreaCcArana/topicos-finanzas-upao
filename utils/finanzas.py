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
# Semana 4: Valor terminal y DCF de dos etapas
# ============================================================

def valor_terminal(cf_n: float, r: float, g: float) -> float:
    """Valor terminal en el anio n por perpetuidad creciente (Gordon).

    Usa el flujo del anio siguiente: VT_n = cf_n * (1 + g) / (r - g).
    El resultado queda expresado en unidades del anio n (falta descontarlo).
    """
    if g >= r:
        raise ValueError("El crecimiento g debe ser menor que la tasa de descuento r.")
    return cf_n * (1 + g) / (r - g)


def valor_terminal_multiplo(metrica_n: float, multiplo: float) -> float:
    """Valor terminal por multiplo de salida: VT_n = multiplo x metrica del anio n (p. ej. EV/EBITDA x EBITDA_n)."""
    return multiplo * metrica_n


def dcf_dos_etapas(flujos, r: float, vt: float) -> dict:
    """DCF de dos etapas: valor presente de los flujos explicitos mas el VT descontado.

    Parameters
    ----------
    flujos : lista de flujos de los anios 1..n
    r : tasa de descuento (WACC para FCFF, Ke para FCFE)
    vt : valor terminal expresado en unidades del anio n (p. ej. de valor_terminal())

    Returns
    -------
    dict con vp_flujos, vp_vt, valor (la suma) y peso_vt (fraccion del valor que es VT).
    """
    n = len(flujos)
    vp_flujos = sum(cf / (1 + r) ** i for i, cf in enumerate(flujos, start=1))
    vp_vt = vt / (1 + r) ** n
    valor = vp_flujos + vp_vt
    return {"vp_flujos": vp_flujos, "vp_vt": vp_vt, "valor": valor, "peso_vt": vp_vt / valor}


# ============================================================
# Semana 5: Multiplos y comparables
# ============================================================

def per_justificado(payout: float, ke: float, g: float, forward: bool = False) -> float:
    """P/E justificado por fundamentos (modelo de crecimiento constante).

    Trailing: payout * (1+g) / (ke - g).  Forward: payout / (ke - g).
    payout: fraccion de la utilidad que se reparte (usar capacidad de pago,
    FCFE/NI, cuando difiera del dividendo).
    """
    if g >= ke:
        raise ValueError("El crecimiento g debe ser menor que el costo del equity ke.")
    base = payout / (ke - g)
    return base if forward else base * (1 + g)


def valor_por_multiplo_ev(multiplo: float, metrica: float, deuda_neta: float, acciones: float) -> float:
    """Valor por accion implicito de un multiplo EV: (multiplo x metrica - deuda neta) / acciones."""
    return (multiplo * metrica - deuda_neta) / acciones


# ============================================================
# Semana 6: Riesgo y rendimiento
# ============================================================

def estadisticos_escenarios(probs, rets) -> tuple[float, float]:
    """Retorno esperado y desviacion estandar de un activo a partir de escenarios.

    probs: probabilidades (suman 1). rets: retorno del activo en cada escenario.
    Devuelve (E[r], sigma) en las mismas unidades de rets.
    """
    p, r = np.asarray(probs, dtype=float), np.asarray(rets, dtype=float)
    if abs(p.sum() - 1) > 1e-9:
        raise ValueError("Las probabilidades deben sumar 1.")
    e = float(p @ r)
    return e, float(np.sqrt(p @ (r - e) ** 2))


def covarianza_escenarios(probs, rets_a, rets_b) -> float:
    """Covarianza entre dos activos a partir de escenarios: suma de p x desvio_a x desvio_b."""
    p = np.asarray(probs, dtype=float)
    a, b = np.asarray(rets_a, dtype=float), np.asarray(rets_b, dtype=float)
    return float(p @ ((a - p @ a) * (b - p @ b)))


def portafolio_dos_activos(w_a: float, mu_a: float, mu_b: float,
                           sigma_a: float, sigma_b: float, rho: float) -> tuple[float, float]:
    """Retorno esperado y riesgo de un portafolio de dos activos (w_b = 1 - w_a).

    Devuelve (E[r_p], sigma_p). El riesgo NO es el promedio ponderado salvo que rho = 1.
    """
    w_b = 1 - w_a
    var = (w_a * sigma_a) ** 2 + (w_b * sigma_b) ** 2 + 2 * w_a * w_b * rho * sigma_a * sigma_b
    return w_a * mu_a + w_b * mu_b, float(np.sqrt(max(var, 0.0)))


def peso_minima_varianza(sigma_a: float, sigma_b: float, rho: float) -> float:
    """Peso del activo A en el portafolio de minima varianza de dos activos."""
    cov = rho * sigma_a * sigma_b
    return (sigma_b ** 2 - cov) / (sigma_a ** 2 + sigma_b ** 2 - 2 * cov)


def riesgo_portafolio(pesos, cov) -> float:
    """Desviacion estandar de un portafolio de n activos: raiz de w' x Cov x w."""
    w = np.asarray(pesos, dtype=float)
    return float(np.sqrt(w @ np.asarray(cov, dtype=float) @ w))


def riesgo_equiponderado(n: int, sigma_media: float, rho_media: float) -> float:
    """Riesgo de un portafolio de n activos con pesos iguales.

    var_p = var_media / n + (n - 1) / n x cov_media. Cuando n crece, el primer
    termino (idiosincratico) desaparece y queda el piso sistematico: la covarianza media.
    """
    var_media = sigma_media ** 2
    cov_media = rho_media * var_media
    return float(np.sqrt(var_media / n + (n - 1) / n * cov_media))


def anualizar(mu: float, sigma: float, periodos: int = 12) -> tuple[float, float]:
    """Anualiza media y desviacion estandar periodicas: mu x k y sigma x raiz(k).

    periodos: 12 para datos mensuales, 52 semanales, 252 diarios.
    """
    return mu * periodos, sigma * float(np.sqrt(periodos))


# ============================================================
# Semana 7: Markowitz y la frontera eficiente
# ============================================================

def _optimizar(objetivo, n: int, cortos: bool, w_max: float, restricciones=()):
    """Minimiza una funcion de los pesos sujeto a que sumen 1 (uso interno)."""
    from scipy.optimize import minimize
    limites = None if cortos else [(0.0, w_max)] * n
    escala = abs(objetivo(np.full(n, 1 / n))) or 1.0          # objetivo cerca de 1: SLSQP converge mejor
    res = minimize(lambda w: objetivo(w) / escala, np.full(n, 1 / n), method="SLSQP", bounds=limites,
                   constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1}, *restricciones],
                   options={"maxiter": 1000, "ftol": 1e-10})
    factible = abs(res.x.sum() - 1) < 1e-6 and all(abs(r["fun"](res.x)) < 1e-6 for r in restricciones)
    if not (res.success or factible):
        raise RuntimeError(f"La optimizacion no convergio: {res.message}")
    return res.x


def _etiquetar(w, referencia):
    return pd.Series(w, index=referencia.index) if isinstance(referencia, (pd.Series, pd.DataFrame)) else w


def min_varianza(cov, cortos: bool = False, w_max: float = 1.0):
    """Pesos del portafolio de minima varianza global.

    cortos=False impide ventas en corto (pesos entre 0 y w_max). Solo necesita la
    matriz de covarianzas: no depende de los retornos esperados.
    """
    c = np.asarray(cov, dtype=float)
    w = _optimizar(lambda w: w @ c @ w, len(c), cortos, w_max)
    return _etiquetar(w, cov)


def portafolio_tangente(mu, cov, rf: float, cortos: bool = False, w_max: float = 1.0):
    """Pesos del portafolio tangente: el de maximo ratio de Sharpe, (E[Rp] - rf) / sigma_p.

    mu, cov y rf deben estar en las mismas unidades y la misma frecuencia (todo anual, por ejemplo).
    """
    m, c = np.asarray(mu, dtype=float), np.asarray(cov, dtype=float)
    w = _optimizar(lambda w: -(w @ m - rf) / np.sqrt(w @ c @ w), len(m), cortos, w_max)
    return _etiquetar(w, mu)


def frontera_eficiente(mu, cov, n_puntos: int = 40, cortos: bool = False, w_max: float = 1.0) -> pd.DataFrame:
    """Frontera eficiente: para cada retorno objetivo, el portafolio de menor riesgo.

    Recorre desde el retorno del portafolio de minima varianza hasta el maximo alcanzable.
    Devuelve un DataFrame con columnas retorno, riesgo y el peso de cada activo.
    """
    m, c = np.asarray(mu, dtype=float), np.asarray(cov, dtype=float)
    nombres = list(mu.index) if isinstance(mu, pd.Series) else [f"w{i + 1}" for i in range(len(m))]
    w_mv = np.asarray(min_varianza(c, cortos, w_max))
    if cortos:
        tope = m.max()
    else:                                   # maximo retorno alcanzable respetando el tope por activo
        orden, resto, tope = np.argsort(m)[::-1], 1.0, 0.0
        for i in orden:
            tope += min(w_max, resto) * m[i]
            resto -= min(w_max, resto)
    filas = []
    for objetivo in np.linspace(w_mv @ m, tope, n_puntos):
        w = _optimizar(lambda w: w @ c @ w, len(m), cortos, w_max,
                       restricciones=[{"type": "eq", "fun": lambda w, o=objetivo: w @ m - o}])
        filas.append([w @ m, np.sqrt(w @ c @ w), *w])
    return pd.DataFrame(filas, columns=["retorno", "riesgo", *nombres])


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
# Semana 10: sharpe(), treynor(), jensen(), var_historico(), var_parametrico()
# Semana 12: nelson_siegel(), bootstrap_curva()

