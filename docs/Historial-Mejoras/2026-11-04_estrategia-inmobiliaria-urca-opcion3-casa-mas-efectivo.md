# Historial de Mejoras: Estrategia Inmobiliaria "1 x 2" (Opción 3: Venta/Permuta Urca por Casa en Bajo Palermo/Villa Cabrera más Excedente en Efectivo)

- **Fecha**: 2026-11-04
- **Autor / Squad**: Squad Ágil Adaptativo de Inversiones Inmobiliarias / Agente 15 (`15-Experto-en-Bienes-Raices-e-Inversiones-Inmobiliarias`) en articulación con el PM y el Copiloto Orquestador
- **Tipo de Tarea**: Modelado de Estrategia Inmobiliaria, Scouting de Ofertas, Valuación Catastral IDECOR y Plan de Desinversión/Reinversión
- **Ficha de Proyecto Asociada**: `docs/Proyectos/2026-11-04_estrategia-inmobiliaria-urca-opcion3-casa-mas-efectivo.md`
- **Inmueble de Referencia**: Mario Arruabarrena 1319, Barrio Urca, Córdoba Capital (Nomenclatura: `1101010518014013`, Cuenta: `110110150709`)
- **Repositorio Central**: `https://github.com/inventarioenergycpy/antigravity-agents-repository.git`

---

## 📌 1. Resumen Ejecutivo de la Tarea

A requerimiento del usuario, el Squad configuró y ejecutó el análisis estratégico completo para desinvertir la propiedad de **Mario Arruabarrena 1319 (Barrio Urca)** (398 m² lote / 253 m² cubiertos, 4 habitaciones, 3 baños, living, comedor, cocina, 2 estudios, pileta, 2 cocheras cubiertas, patio social con asador y patio de luz) mediante la **Tesis de Inversión "1 x 2"** orientada a la **Opción 3: Adquisición de una casa de reemplazo de menor mantenimiento para seguir viviendo (Bajo Palermo / Villa Cabrera) más retención de una diferencia sustancial en efectivo en dólares billete**.

### Principales Conclusiones y Modelado:
1. **Valuación Re-calibrada de Urca**: Al incorporar los atributos completos (4 dormitorios + 2 estudios independientes + pileta + 2 cocheras), el valor de publicación se sitúa en **USD 255.000 - USD 265.000**, con un valor objetivo de cierre en efectivo de **USD 245.000** y valor de toma en permuta de **USD 260.000 - USD 275.000**.
2. **Selección de la Casa de Reemplazo (USD 120.000 - USD 135.000)**: Se relevaron oportunidades concretas en Bajo Palermo (Rufino Cuervo a USD 135k, Javier López a USD 125k) y Villa Cabrera (La Ramada a USD 120k con cochera doble, Alto Verde con pileta a USD 120k), garantizando 3 dormitorios, cochera, patio con asador y cercanía inmediata al circuito habitual de Zona Norte.
3. **Monetización del Excedente Líquido (USD 105.000 - USD 112.000)**: Se demostró que colocar el excedente en una cartera conservadora de Obligaciones Negociables corporativas en dólares (7,5% a 8,5% anual) genera un flujo pasivo limpio de **USD 680 a USD 740 / mes**, superando en más de un 40% la renta neta de un segundo inmueble alquilado, con cero inquilinos, cero morosidad y liquidez disponible en 48 horas.
4. **Análisis de las Dos Modalidades Operativas**:
   - *Modalidad A*: Venta tradicional en efectivo con **cláusula de posesión diferida a 60-90 días** para comprar de contado con poder de negociación agresivo.
   - *Modalidad B*: Permuta directa con saldo a favor ("Trade-Up" cordobés), facilitando el canje con familias de Bajo Palermo o Villa Cabrera que buscan agrandarse hacia Urca.

---

## 📂 2. Archivos Impactados

| Archivo | Ruta | Descripción |
| :--- | :--- | :--- |
| **Ficha de Proyecto** | `docs/Proyectos/2026-11-04_estrategia-inmobiliaria-urca-opcion3-casa-mas-efectivo.md` | Ficha técnica completa, diagnóstico catastral, tablas comparativas, opciones testigo y ficha comercial. |
| **Historial de Mejoras** | `docs/Historial-Mejoras/2026-11-04_estrategia-inmobiliaria-urca-opcion3-casa-mas-efectivo.md` | Esta nota técnica histórica. |
| **Dashboard Central** | `docs/00-Dashboard-MOC.md` | Actualización de la evolución reciente y registro relacional en el MOC. |

---

## 🛡️ 3. Protocolo de Validación Multi-Perspectiva (Triple QA)

- **QA 1: Técnico & Algorítmico**: Georreferenciación de la parcela catastral `-31.382179, -64.234657` en Urca, validación de tolerancias de m² y balance de partida doble de fondos (Venta USD 245k = Compra USD 125k + Costos USD 8k + Cash USD 112k).
- **QA 2: Dominio & Negocio Inmobiliario**: Alineación con el Observatorio del Mercado Inmobiliario (OMI) de IDECOR, normativa CPI de Córdoba (Ley 9445), no aplicación de ITI (Ley 27.743) y régimen contractual de permuta con saldo (CCCN Art. 1172).
- **QA 3: Usabilidad, Replicabilidad & UX**: Esquemas de decisión Mermaid, ficha comercial lista para publicar y compartir con agentes inmobiliarios, y comparativa clara de rendimiento financiero.
