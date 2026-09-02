# Tópicos de Finanzas Avanzadas. ECON-421 (UPAO 2026-20)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![CFA](https://img.shields.io/badge/Alineado%20a-CFA%C2%AE-4B2E83)
![Made in Perú](https://img.shields.io/badge/Hecho%20en-Per%C3%BA-red)

Curso de pregrado del programa de **Economía y Negocios Internacionales - UPAO**.

> Sílabo oficial: ECON-421, semestre 2026-20 · NRC 11454-11455
> [Econ. Percy Jonathan Rosas Valderrama, MSc.](https://www.linkedin.com/in/percyjrosas/)

## Unidades

1. **Técnicas avanzadas de valorización** (sem 1–5): WACC, DCF (FCFF/FCFE), valor terminal, múltiplos.
2. **Estructuración y optimización de portafolios** (sem 6–10): Markowitz, CAPM, multifactoriales, desempeño.
3. **Macro y política monetaria en la valoración** (sem 11–15): ciclo y mercados, curva de rendimientos, transmisión monetaria, riesgo país.

## Cómo usar este repositorio

1. **Primera vez:** sigue la [guía de instalación](00_setup/guia_instalacion.md) (Python + VS Code + Git + GitHub).
2. Haz **fork** de este repo, clónalo desde VS Code y crea el entorno:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  |  source .venv/bin/activate en Mac/Linux
pip install -r requirements.txt
```

3. Abre el notebook de la semana, selecciona el kernel `.venv` y ejecuta con `Shift+Enter`.
4. Las tareas se entregan por **fork + commit + push** (Google Colab es el plan B: botón de cada semana).

## Contenido del curso

| Semana | Tema | Carpeta | Notebook |
|-------:|------|---------|----------|
| 0 | Instalación del entorno: Python, VS Code, Git y GitHub | [`00_setup`](00_setup/) | - |
| 1 | Fundamentos de la valoración financiera | [`01_fundamentos_valor`](01_fundamentos_valor/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/01_fundamentos_valor/clase01_practica.ipynb) |
| 2 | Costo de capital: CAPM y WACC | [`02_costo_capital_wacc`](02_costo_capital_wacc/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/02_costo_capital_wacc/clase02_practica.ipynb) |
| 3 | DCF: FCFF y FCFE (PC1) | [`03_dcf_fcff_fcfe`](03_dcf_fcff_fcfe/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/03_dcf_fcff_fcfe/clase03_practica.ipynb) |
| 4 | Valor terminal, Enterprise Value y sensibilidad | [`04_valor_terminal_ev`](04_valor_terminal_ev/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/04_valor_terminal_ev/clase04_practica.ipynb) |
| 5 | Valoración relativa: múltiplos comparables | [`05_multiplos_comparables`](05_multiplos_comparables/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/05_multiplos_comparables/clase05_practica.ipynb) |
| 6 | Riesgo y rendimiento (TR1) | [`06_riesgo_rendimiento`](06_riesgo_rendimiento/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/06_riesgo_rendimiento/clase06_practica.ipynb) |
| 7 | Markowitz y la frontera eficiente | [`07_markowitz_frontera`](07_markowitz_frontera/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/07_markowitz_frontera/clase07_practica.ipynb) |
| 8 |  Examen parcial | - |, |
| 9 | CAPM, SML y modelos multifactoriales | [`09_capm_multifactor`](09_capm_multifactor/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/09_capm_multifactor/clase09_practica.ipynb) |
| 10 | Desempeño de portafolios y gestión del riesgo | [`10_desempeno_riesgo`](10_desempeno_riesgo/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/10_desempeno_riesgo/clase10_practica.ipynb) |
| 11 | Variables macro y mercados financieros (PC2) | [`11_macro_mercados`](11_macro_mercados/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/11_macro_mercados/clase11_practica.ipynb) |
| 12 | Estructura temporal de tasas de interés | [`12_curva_rendimientos`](12_curva_rendimientos/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/12_curva_rendimientos/clase12_practica.ipynb) |
| 13 | Política monetaria y mercados financieros | [`13_politica_monetaria`](13_politica_monetaria/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/13_politica_monetaria/clase13_practica.ipynb) |
| 14 | Riesgo país y escenarios (TR2) | [`14_riesgo_pais_escenarios`](14_riesgo_pais_escenarios/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/14_riesgo_pais_escenarios/clase14_practica.ipynb) |
| 15 | Integración: valoración, portafolios y macro | [`15_integracion`](15_integracion/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JonathanRosasV/topicos-finanzas-upao/blob/main/15_integracion/clase15_practica.ipynb) |
| 16 | Examen final | - |, |
| 17 | Examen sustitutorio | - |, |
| - | TR2: propuesta de inversión ante comité | [`tr2_propuesta_inversion`](tr2_propuesta_inversion/) | - |


## Evaluación (escala vigesimal)

| Componente | Semana | Peso |
|---|---|---|
| PC1 (práctica calificada 1) | 3 | EP1 = 0.5·PC1 + 0.5·TR1  **20%** |
| TR1 (informe de valoración) | 6 | |
| **Examen parcial (EP)** | 8 | **30%** |
| PC2 (práctica calificada 2) | 11 | EP2 = 0.5·PC2 + 0.5·TR2  **20%** |
| TR2 (propuesta de inversión) | 14 | |
| **Examen final (EF)** | 16 | **30%** |

**PROMO = 20%·EP1 + 20%·EP2 + 30%·EP + 30%·EF** · Sustitutorio: semana 17 · Reforzamiento: semanas 7 y 14.

Calendario 2026-20: clases los miércoles, desde el 02/09/2026. Las tareas semanales se entregan hasta el lunes de la semana siguiente, vía commit en el fork.

## Estructura

```
├── 00_setup/            guía de instalación del entorno
├── data/                datasets de respaldo (todo se descarga por API)
├── utils/               mini-librería del curso (bcrp, fred, finanzas)
├── 01_.../ ... 15_.../  una carpeta por semana lectiva
└── tr2_propuesta_inversion/  consigna y rúbrica del trabajo final
```

## Referencias principales

- CFA Institute. *CFA Program Curriculum* (Equity, Corporate Issuers, Portfolio Management, Fixed Income, Economics).
- Pinto, J. et al. *Equity Asset Valuation*. CFA Institute Investment Series.
- Fernández, P. *Métodos de valoración de empresas*. IESE.
- Damodaran, A.: [pages.stern.nyu.edu/~adamodar](https://pages.stern.nyu.edu/~adamodar/)
- Mishkin, F. (2014). *Moneda, banca y mercados financieros*. Pearson.
- API BCRPData: `estadisticas.bcrp.gob.pe/estadisticas/series/ayuda/api`

## Licencia

MIT: úsalo, compártelo y cita la fuente. CFA® es marca registrada de CFA Institute; este curso es independiente y no está afiliado a CFA Institute.
