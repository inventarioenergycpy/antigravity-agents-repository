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
