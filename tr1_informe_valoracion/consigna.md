# TR1: Informe de valoración de una empresa

**Tópicos de Finanzas Avanzadas (ECON-421, UPAO 2026-20)**

**Entrega: miércoles 7 de octubre de 2026 (semana 6), antes del inicio de la sesión** · Individual · Sobre 20 puntos

## Qué es

El TR1 es tu primer entregable profesional del curso: un informe de valoración por flujo de caja descontado, de principio a fin, sobre una empresa real que cotiza en bolsa. Integra todo lo trabajado en las semanas 1 a 4: tasa de descuento, flujos de caja libre, valor terminal, enterprise value y sensibilidad. La tarea de la semana 4 es su ensayo general.

Empresa: por defecto, la misma que vienes trabajando desde la semana 2. Puedes cambiarla si lo declaras en el informe con una línea de justificación (por ejemplo, porque sus datos públicos resultaron insuficientes).

## Qué se entrega

Dos piezas, ambas obligatorias:

1. **El informe (PDF, máximo 10 páginas incluyendo gráficos, sin contar anexos), subido a Canvas.** Es el documento que le entregarías a un cliente o a tu jefe: prosa clara, gráficos legibles, números redondeados con criterio.
2. **El notebook reproducible, vía commit en tu fork** (`tr1_informe_valoracion/tr1_apellido.ipynb`). Debe correr de inicio a fin con `Kernel Restart & Run All` y generar todos los números y gráficos del informe. El informe afirma; el notebook demuestra.

Sobre el uso de IA: permitido, con la misma regla de la PC1. El texto del informe va con tus palabras y aplicado a tu empresa; un informe genérico que podría ser de cualquier alumno y cualquier empresa pierde la mitad de los puntos de comunicación y la credibilidad del resto.

## Estructura requerida del informe

1. **Resumen ejecutivo (media página).** Empresa, recomendación condicionada, rango de valor por acción contra precio de mercado, y los dos supuestos que más mueven tu resultado. Se escribe al final, va al inicio.
2. **La empresa y su sector (1 página).** Qué hace, cómo gana dinero, qué riesgos enfrenta. Solo lo que un lector necesita para juzgar tus supuestos.
3. **Tasa de descuento (1 a 2 páginas).** Beta estimado por regresión (ventana y frecuencia declaradas, error estándar reportado, ajuste de Blume), tasa libre de riesgo con fuente y consistencia de horizonte y moneda, ERP justificada, prima por riesgo país si aplica, costo de deuda, estructura de capital a valor de mercado y WACC con su control de razonabilidad: $K_d(1-t) < WACC < K_e$.
4. **Flujos de caja proyectados (1 a 2 páginas).** FCFF histórico por dos rutas con la verificación de que coinciden, y proyección a 5 años con cada supuesto de crecimiento declarado y justificado. La coherencia entre crecimiento y reinversión ($g = RR \times ROIC$) será revisada.
5. **Valor terminal (1 página).** Por los dos métodos: perpetuidad (g perpetuo con fuente, nunca mayor que el crecimiento nominal de la economía relevante) y múltiplo de salida (múltiplo declarado y razonado). Reporta el múltiplo implícito del Gordon y comenta su coherencia. Reporta el peso del VT en el EV.
6. **Valoración y puente (1 página).** EV, puente completo al equity (deuda neta como mínimo; preferentes, minoritarios y dilución si aplican) y valor por acción por cada método de VT.
7. **Sensibilidad y recomendación (1 a 2 páginas).** Tabla de valor por acción para al menos 4 valores de WACC y 4 de g (el VT recalculado en cada celda), mapa de calor, y el veredicto en rango: en qué fracción de escenarios la acción está subvaluada, dónde cae el precio dentro de tu rango, y una recomendación condicionada.
8. **Anexo (no cuenta para el límite).** Supuestos completos en una tabla y cualquier detalle técnico adicional.

## Rúbrica (20 puntos)

| Criterio | Pts | Qué se evalúa |
|---|---|---|
| Tasa de descuento | 4 | Insumos con fuente, beta bien estimado y ajustado, pesos a valor de mercado, control de razonabilidad verificado. |
| Flujos proyectados | 4 | FCFF por dos rutas verificadas; supuestos de proyección declarados, justificados y coherentes con la reinversión. |
| Valor terminal | 3 | Dos métodos correctos (flujo del año n+1, VT descontado), múltiplo implícito reportado y discutido, peso del VT. |
| Valoración y puente | 3 | EV correcto, puente completo con deuda neta, valor por acción por ambos métodos. |
| Sensibilidad y veredicto | 3 | Tabla bien construida (VT recalculado por celda), mapa de calor, recomendación en rango y condicionada. |
| Comunicación profesional | 2 | Informe claro dentro del límite, gráficos legibles, prosa propia y aplicada a la empresa. |
| Reproducibilidad y puntualidad | 1 | El notebook corre de inicio a fin y ambas piezas llegaron a tiempo. |

**Penalidades transversales** (se descuentan del total, hasta 4 puntos): violación de la regla de consistencia (flujo con tasa equivocada), interés sin ajuste de impuestos en el FCFF, g perpetuo mayor que la economía sin justificación extraordinaria, VT sin descontar. Son los errores de las láminas de "errores comunes" de las semanas 3 y 4: están avisados.

## Preguntas frecuentes

**¿Puedo valorar un banco o una aseguradora?** No para el TR1: los flujos de caja libre no aplican bien a financieras (su deuda es materia prima, no financiamiento). Elige una empresa no financiera.

**¿Qué pasa si mi empresa tiene FCFE negativo o capex muy volátil?** Nada malo: documéntalo, normaliza con promedios si hace falta y explica tu criterio. Manejar datos imperfectos con criterio declarado vale más que una empresa de datos perfectos.

**¿En soles o en dólares?** En la moneda de los estados financieros de tu empresa, con la tasa de descuento consistente con esa moneda (regla de la semana 2).

**¿Se puede entregar tarde?** Se aplica el criterio general del curso: la puntualidad es parte de la nota y la retroalimentación del TR1 se da en clase la semana 7, así que una entrega tardía la pierde.

