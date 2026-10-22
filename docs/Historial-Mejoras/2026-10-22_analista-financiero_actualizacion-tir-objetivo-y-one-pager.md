# Historial de Mejoras — 2026-10-22
## Protocolo del Agente 01 (Analista Financiero de Proyectos) & Estabilidad One-Pager

### 1. Resumen Ejecutivo de la Intervención
Bajo la supervisión y directrices del **Agente 01 (Analista Financiero de Proyectos)** coordinado con el **Agente 11 (Copiloto Orquestador)**, se implementó la redefinición del benchmark de rentabilidad y la profundización analítica en los 24 proyectos de la cartera EnergyCPY en el showroom digital (showroom-energycpy), optimizando la experiencia del usuario y blindando el comportamiento de apertura del Resumen Ejecutivo (One-Pager).

---

### 2. Modificaciones Implementadas

#### A. Actualización de la Leyenda de Rentabilidad (TIR Objetivo)
- **Modificación**: Se sustituyó cualquier referencia ambigua por la directriz unificada:
  \text{TIR Objetivo: } >9\%
- **Criterio Financiero**: En inversiones corporativas e infraestructura en moneda dura (USD) en Argentina, la tasa de corte (*hurdle rate*) del 9% en USD representa el piso mínimo de corte frente a tasas libres de riesgo internacionales + prima de liquidez corporativa.
- **Implementación**:
  - En cada una de las 24 tarjetas del catálogo: La métrica clave muestra la etiqueta oficial TIR Objetivo: >9% con el valor modelado del proyecto (e.g. 14.5% - 18.2%).
  - En el One-Pager (Resumen Ejecutivo de 1 Página): La barra de Deal Terms y la nueva sección técnica detallan el cálculo y el spread sobre el piso mínimo de corte.

#### B. Información Financiera Enriquecida por Proyecto (24 Proyectos)
Cada activo del portafolio fue enriquecido en data/projects-master.json con los siguientes campos cuantitativos y cualitativos:
1. 	ir: Rango o porcentaje modelado de TIR de proyecto en USD.
2. 	ir_target: Constante corporativa TIR Objetivo: >9%.
3. ebitda: EBITDA operativo proyectado y margen porcentual.
4. capitalStructure: Esquema de financiamiento (Project Finance, Equity/Deuda, Co-inversión).
5. egulatoryRegime: Marco de incentivos aplicable (RIGI Ley 27.742, PPA MATER Ley 27.191, Ley Minera 24.196, Ley 24.922).
6. inancialNote_es / inancialNote_en: Metodología analítica del Flujo de Fondos Descontados (DCF), horizonte de proyección, WACC de referencia y blindaje macroeconómico.

#### C. Protocolo de Apertura del Resumen Ejecutivo (One-Pager) & Control Anti-Retipeo
Se realizó una auditoría técnica profunda del comportamiento al pulsar el botón **Resumen Ejecutivo 1 Pág**:
1. **Prevención de Retipeo / Layout Shift**:
   - En pantallas desktop, la inserción y remoción de overflow: hidden en el ody solía eliminar el scrollbar vertical, produciendo un salto o retipeo de la grilla de ~17px. Se solucionó incorporando scrollbar-gutter: stable; en la raíz html de css/styles.css.
   - Se añadió control estricto de eventos (event.preventDefault(), event.stopPropagation()) y atributo 	ype=button en todos los botones disparadores para evitar navegación fantasma o recarga de tarjeta.
2. **Control Anti-Repaginación en Impresión / PDF**:
   - Para garantizar que el resumen sea rigurosamente de **1 sola página A4** sin desbordes ni repaginación accidental en hoja 2 (re-tipeo de página), se configuró @page { size: A4 portrait; margin: 6mm 8mm; } y max-height: 282mm con page-break-after: avoid; break-after: avoid;.
3. **Cierre Ergonómico de Modal**:
   - Se habilitó el cierre mediante click en el backdrop (modal-backdrop-blur) y tecla Escape, con restauración suave del estado del viewport.

---

### 3. Validación y Registro
- Validación automática alidate_financial_update.py: 100% exitosa (0 errores de sintaxis, 24 proyectos validados, HTTP 200).
- Repositorios sincronizados:
  - showroom-energycpy: Commit 807b98 en rama eat/cartera-inversiones-sincronizada.
  - ntigravity-agents-repository: Documentación histórica incorporada en master.

#### D. Ajuste de Tarjetas de Métricas Ejecutivas (Stats Grid)
- Se removió la tarjeta de estadística Track Record en Pesca Industrial (+25 Años / 600M USD/año).
- La grilla ejecutiva (.stats-grid) queda armónicamente balanceada en 3 pilares estratégicos de alto impacto:
  1. **Volumen Total en Portafolio**: USD 4,111.5M (+4.1B USD) en 24 proyectos.
  2. **CAPEX Solar Pre-Financiado**: 50% co-financiado respaldado por fabricante global.
  3. **Plazo PPA Indexado en Dólares**: 20 Años bajo régimen MATER / PPA.

#### E. Regla de Negocio: Clasificación Escalonada de TIR en el Resumen
Siguiendo las instrucciones directas para la presentación ejecutiva de rentabilidades:
- **TIR entre 9% y 14.99%**: Se categoriza e indica formalmente como **TIR > 9%** (e.g. eit-strategy con TIR neta institucional del 13.5% y mandatos fiduciarios de estructuración soberana).
- **TIR $\ge$ 15%**: Se categoriza e indica formalmente como **TIR > 15%** (e.g. Parques Solares 18.5% - 24.0%, Oil & Gas 27.5% - 45.0%, Minería 29.0% - 42.0%, Pesca 28.0% - 32.5%, Hotelería 25.5% - 65.0%).

**Implementación técnica aplicada**:
1. Función universal getTirCategory(tir, isEn) en js/main.js que parsea dinámicamente el valor numérico de la TIR y asigna el tramo correspondiente.
2. En las **Tarjetas del Catálogo**: La métrica 3 exhibe la tasa modelada y la etiqueta TIR > 15% o TIR > 9%.
3. En el **Resumen Ejecutivo 1 Pág (One-Pager)**:
   - Barra de Deal Terms: Exhibe la categoría (TIR > 15% / TIR > 9%) junto a la TIR proyectada modelada.
   - Grilla de 4 Métricas Clave: Etiqueta dinámica ${tirCategory} con valor ${tirProjectVal}.
   - Bloque de Protocolo del Analista Financiero: Ítems separados para *Calificación de Rentabilidad* (TIR > 15% / TIR > 9%) y *TIR Proyectada del Activo*.
   - Mensaje de derivación directa de leads por WhatsApp: Integra la calificación y el valor modelado.
4. En data/projects-master.json: Sincronización completa de los 24 proyectos con las notas metodológicas DCF actualizadas.
