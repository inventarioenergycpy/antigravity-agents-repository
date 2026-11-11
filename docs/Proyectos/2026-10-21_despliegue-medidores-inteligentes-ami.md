---
type: proyecto
proyecto: "Plan Maestro de Despliegue de Medidores Inteligentes AMI y Concentradores PLC"
agente_responsable: "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto de Sistemas EPEC]]"
agentes_colaboradores:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos & BI EPEC]]"
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]]"
repositorio_github: "https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami"
ubicacion_local: "D:\\Proyectos\\despliegue-medidores-inteligentes-ami"
fecha_creacion: 2026-10-21
licitacion_origen: "Licitación Pública N° 5573 / Resolución N° 0653/2026"
volumen_total: "400.000 Medidores (200k Sanxing + 200k CLOU) + 6.000 Concentradores PLC + 188.000 USE"
tags:
  - #proyecto
  - #telemedicion
  - #ami
  - #epec
  - #protelem
  - #subestaciones
  - #plc
  - #sanxing
  - #clou
  - #nansen
---

# ⚡ Proyecto: Plan Maestro de Despliegue de Medidores Inteligentes AMI & Concentradores PLC (EPEC)

## 📌 Resumen Ejecutivo
Planificación estratégica, simulación de curva de stock físico con **Verificación Primitiva (`VP 20d`)**, gobernanza de compatibilidad en **Subestaciones Transformadoras (`SET OK`)** y despliegue operativo en campo para **400.000 medidores inteligentes**, **6.000 concentradores de baja tensión** y **188.000 USE de mano de obra** adjudicados en la Licitación Pública N° 5573.

---

## 🔗 Repositorio Dedicado y Enlaces
* **Repositorio Central (PROTELEM-EPEC)**: [https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami](https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami)
* **Ruta de Trabajo Local**: `D:\Proyectos\despliegue-medidores-inteligentes-ami`
* **Vínculo Scratchpad**: `C:\Users\jidiaz\.gemini\antigravity-ide\scratch\despliegue-medidores-inteligentes-ami`

---

## 📑 1. Contratos y Órdenes de Provisión Adjudicadas
1. **OP 27131 - SANFORD GLOBAL TRADE LLC**: USD 11.688.100 (160.000 Monofásicos + 40.000 Trifásicos + 3.000 Concentradores PLC).
2. **OP 27133 - NICEMA S.A.**: USD 11.688.100 (160.000 Monofásicos + 40.000 Trifásicos + 3.000 Concentradores PLC).
3. **OP 27132 - ROWING S.A.**: $10.583.507.000 ARS (94.000 USE mano de obra e instalación).
4. **OP 27134 - CONECTAR S.R.L.**: $10.583.507.000 ARS (94.000 USE mano de obra e instalación).

---

## 📅 2. Cronograma de Disponibilidad Real en Campo (`Disp.`)

Conforme a la **Resolución 247/2019 de la Secretaría de Comercio**, todo lote ingresado debe cumplir los **20 días de Verificación Primitiva (VP)** antes de salir a campo:

| Lote / Marca | Cantidad | Días Contractuales | Verificación Primitiva | Disponibilidad Real (`Disp.`) | Destino Asignado |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Sanxing E1** | **34.000** | 120 d | VP 20 d | **18/02/2027** | Arranque: Plan 18 (Capital) + San Francisco Lote 1 |
| **Sanxing E2** | **31.000** | 148 d | VP 20 d | **18/03/2027** | Cierre Distrito San Francisco (28.000 totales) |
| **CLOU E1** | **42.000** | 155 d | VP 20 d | **25/03/2027** | Arranque CLOU: Plan 6 (Continuidad con Plan 4) |
| **Sanxing E3** | **45.000** | 176 d | VP 20 d | **15/04/2027** | Plan 17 (Zona Aérea) + extensiones |
| **Sanxing E4** | **45.000** | 211 d | VP 20 d | **20/05/2027** | Distrito Río Cuarto (13.000 puntos) |
| **Sanxing E5** | **45.000** | 239 d | VP 20 d | **17/06/2027** | Distrito Villa María (6.000 puntos) + Cierre 100% Sanxing |
| **CLOU E2** | **41.500** | 330 d | VP 20 d | **16/09/2027** | Plan 8 (Post-relevamiento acometidas) |
| **CLOU E3** | **41.500** | 351 d | VP 20 d | **07/10/2027** | Plan 12 + Villa Allende (800) |
| **CLOU E4** | **75.000** | 421 d | VP 20 d | **16/12/2027** | Zona Centro Subterránea (Planes 14 y 15 GPRS) + Cierre Licitación |

---

## 🗺️ 3. Distribución Territorial y Compatibilidad por Subestación
* **Directiva de Oro**: Toda instalación requiere que la subestación asociada figure en estado **"SET OK"** (concentrador montado y comunicando con Headend).
* **Plan 19 (Capital)**: Preservar cuenca tecnológica de casi **10.000 Nansen preexistentes**.
* **Plan 6 (Capital)**: Asignación **CLOU** por colindancia y continuidad con Plan 4.
* **Plan 18 (Capital)**: Asignación **SANXING** para absorber la primera entrega de Febrero 2027.
* **San Francisco (Interior)**: Asignación masiva en bloque a **SANXING** (28.000 puntos).
* **Río Cuarto y Villa María**: Programados para el segundo trimestre de 2027 con Sanxing.

---

## 📈 4. Tasas Reales y Equilibrio Relevamiento / Instalación / Stock (Zona A) — 2026-10-23
* **Instalación MI Zona A (Nov-25..Abr-26)**: **7.559/mes** (SIGEC `EQUIPOS` ⨝ `STOCK_EQUIPOS`, marcas CLOU+NSEN).
* **Relevamiento Zona A (Nov-25..Abr-26)**: **3.620/mes** (`georef.relevamiento`, SET `1000-%`, DISTINCT `rel_medidor_id`); reciente May-Sep-26: 4.338/mes.
* **Backlog relevado no telemedido**: **162.156** · **Stock neto Zona A (90%)**: **316.980**.
* **Conclusión**: al ritmo histórico la restricción es la **mano de obra** → cierre Zona A **Jul-2030**; ~234k medidores ociosos en Dic-2027. Para cumplir el plazo de OP 27132/27134 (25-01-2028) se requieren ~**26.400 inst/mes** y ~**12.900 relev/mes**.
* **Plan Maestro Contractual (360k a Ene-2028)**: Despliegue en 12 meses (Feb-27 a Ene-28) con relevamiento previo a 15-30 días. Distribución: **316.980 en Zona A** (88,05%) y **43.020 en Interior** (11,95%: Río Cuarto completo 13.000 u., San Francisco 24.154 u., Villa María 5.176 u., Villa Allende 690 u.). Sin quiebres de stock.
* Informes: `docs/05_equilibrio_relevamiento_instalacion_stock_zona_a.md`, `docs/06_plan_maestro_despliegue_contractual_360k.md`.
* Scripts: `scripts/analisis_tasas_instalacion_relevamiento.py`, `scripts/simulacion_equilibrio_zona_a.py`, `scripts/plan_maestro_despliegue_360k.py`.
* Histórico: [[Historial-Mejoras/2026-10-23_copiloto-orquestador_equilibrio-relevamiento-instalacion-ami-zona-a]]

---

## 📂 Componentes del Proyecto
* `README.md`: Memoria técnica maestra.
* `index.html`, `style.css`, `app.js`: Tablero SPA ejecutivo interactivo.
* `data/`: Datasets JSON estructurados de entregas y diagnóstico territorial; tasas mensuales y plan maestro 360k (`plan_maestro_despliegue_360k.csv/json`).
* `docs/`: 6 informes de ingeniería (licitación, protocolo SET, compatibilidad, cuadrillas, equilibrio de tasas y plan maestro contractual) y pliegos PDF.
* `assets/img/`: Cartografía GIS de planes Zona A y diagrama Gantt de entregas.


---

## 🤝 5. Asignación Oficial de Medidores a Cooperativas Eléctricas (47.254 u. / 38 Entidades) — 2026-11-11
* **Fuente Oficial de Datos**: Ingesta del archivo interactivo y dataset `Entregas_Cooperativas_EPEC_despliegue_2027.html` (derivado de `Libro1.xlsx`, solapas *Cooperativa* y *Dato Coop*, consolidado al 05/11/2026).
* **Volumen Asignado a Cooperativas**: **47.254 medidores** (39.631 Monofásicos + 7.623 Trifásicos) y **445 Concentradores DCU**.
* **Cronograma en 4 Hitos**:
  - **1.ª Entrega (E1)**: 18.806 u. (14.902 mono + 3.904 tri) — 39,8%
  - **2.ª Entrega (E2)**: 13.040 u. (10.400 mono + 2.640 tri) — 27,6%
  - **3.ª Entrega (E3)**: 9.929 u. (8.850 mono + 1.079 tri) — 21,0%
  - **4.ª Entrega (E4 - Saldo)**: 5.479 u. (5.479 mono + 0 tri) — 11,6%
* **Impacto en Stock y Cobertura EPEC Provincial**:
  - Al requerir las cooperativas 47.254 medidores (frente a la hipótesis preliminar de 93.000 u.), **EPEC recupera +45.746 medidores efectivos** para sus usuarios directos, elevando su stock a **352.746 medidores**.
  - **Córdoba Capital (Zona A)**: 200.000 medidores asegurados al 100%.
  - **Interior Provincial**: Stock ampliado a **152.746 medidores**, lo que permite una cobertura del **100% en Río Cuarto (88.224 req)** y del **100% en Villa María (63.282 req)**, con saldo de 1.240 medidores para San Francisco. El déficit remanente del interior cae drásticamente de **-96.137 u.** a **-50.391 u.**
* **Artefactos y Datasets Generados**:
  - Datasets: `data/entregas_cooperativas_epec_2027.json`, `data/entregas_cooperativas_epec_2027.csv`, `data/cobertura_prioridades_interior_oficial_152k.json`, `data/simulacion_oficial_coop_47k_epec_352k.json`.
  - Pestaña interactiva en el Dashboard: `🤝 Cooperativas (47.254 u.)` con buscador reactivo, filtros por 7 zonas provinciales y tipos de medidor, tabla de entregas E1-E4 y tarjetas de distribución.
  - Script de simulación oficial: `scripts/simulacion_epec_coop_oficial_47k.py`.
  - Histórico: [[docs/Historial-Mejoras/2026-11-11_ingesta-entregas-cooperativas-epec-ami-2027|2026-11-11 Ingesta Entregas Cooperativas EPEC AMI 2027]].

---

## 🗺️ 6. Resolución Geoespacial Oficial de Zonas EPEC para Cooperativas (WFS & SIGEC) — 2026-11-11
* **Problema Identificado**: 3 cooperativas figuraban sin zona asignada en la planilla de entregas: Huanchilla (`c17`, 800 u.), Bulnes (`c25`, 550 u.) y Ascochinga (`c29`, 300 u.).
* **Metodología de Resolución**:
  - Búsqueda directa por Razón Social en `XXSIGEC.PERSONAS` y localización de Contrato Vigente bajo Tarifa 4xx (`TCL_CODIGO = '411'` - Venta en Bloque a Cooperativas Eléctricas).
  - Identificación del suministro (`XXSIGEC.SERVICIOS`), cabecera de sucursal comercial (`XXSIGEC.SUCURSALES`) y zona oficial (`XXSIGEC.ZONAS`), respaldado con poligonización WFS.
* **Dictamen Final (100% de Asignación por Contrato SIGEC Tarifa 411)**:
  - **HUANCHILLA** (`c17`): **Zona F** (Razón Social `COOP.ELEC.HUANCHILLA` · PRS 182204 · CNT 1 Tarifa 411 · SRV 278422 · Sucursal 33 Gral. Levalle · AGF 6300 Gral. Levalle / Huanchilla).
  - **BULNES** (`c25`): **Zona F** (Razón Social `COOP.ELEC.BULNES.` · PRS 182933 · CNT 1 Tarifa 411 · SRV 279152 · Sucursal 28 Río Cuarto · AGF 6000 Río Cuarto / Bulnes).
  - **ASCOCHINGA** (`c29`): **Zona E** (Razón Social `COOP ELEC DE SERV PUB Y ANEXOS LTDA ASCOCHINGA LA PAMPA` · PRS 762962 · CNT 1 Tarifa 411 · SRV 827893 · Sucursal 22 Río Ceballos · AGF 5000 Río Ceballos / La Granja).
  - **Hallazgo Provincial**: En SIGEC, la Sucursal 22 (Río Ceballos, Zona E) administra también los contratos de Tarifa 411 de Colonia Caroya (`c12`) y Agua de Oro (`c38`), ya que la Zona A está reservada a usuarios directos de Córdoba Capital.
* **Distribución Consolidada en 8 Zonas Provinciales**:
  - **Zona I** (Traslasierra): 2 coops, 13.493 medidores (28,6%).
  - **Zona H** (Calamuchita / Sierras Chicas Sur): 7 coops, 12.613 medidores (26,7%).
  - **Zona F** (Sur Provincial): 10 coops, 8.730 medidores (18,5%).
  - **Zona D** (San Justo): 7 coops, 5.711 medidores (12,1%).
  - **Zona G** (Marcos Juárez / Unión): 7 coops, 2.767 medidores (5,9%).
  - **Zona C** (Centro Provincial): 2 coops, 2.100 medidores (4,4%).
  - **Zona A** (Norte Provincial): 2 coops, 1.540 medidores (3,3%).
  - **Zona E** (Sierras Chicas / Río Ceballos): 1 coop, 300 medidores (0,6%).
* **Histórico y Memoria Técnica**: [[docs/Historial-Mejoras/2026-11-11_resolucion-geoespacial-zonas-cooperativas-epec|2026-11-11 Resolución Geoespacial Oficial de Zonas EPEC para Cooperativas Eléctricas AMI]].
