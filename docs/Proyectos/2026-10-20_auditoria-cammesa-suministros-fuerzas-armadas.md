---
title: "Auditoría CAMMESA 2025-2026: Suministros Vigentes, Potencias y Consumos de Fuerzas Armadas (FADEA, EAM, FAA, IOSFA, Ejército Argentino)"
proyecto: "auditoria-cammesa-fuerzas-armadas"
fecha: 2026-10-20
agentes:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Agente 02 - Ciencia de Datos]]"
  - "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Agente 06 - Arquitecto de Sistemas EPEC]]"
tags:
  - #cammesa
  - #sigec
  - #fuerzas-armadas
  - #fadea
  - #fuerza-aerea
  - #iosfa
  - #ejercito-argentino
  - #auditoria-energetica
---

# ⚡ Auditoría de Mercado Eléctrico Mayorista (CAMMESA) 2025-2026: Suministros Vigentes de Fuerzas Armadas

> [!NOTE]
> **ENTREGABLE DISPONIBLE EN DESCARGAS Y REPOSITORIO**
> - **Ruta Principal en Descargas**: [`%USERPROFILE%\Downloads\Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026.xlsx`](file:///C:/Users/jidiaz/Downloads/Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026.xlsx)
> - **Copia en Bóveda/Data**: [`data/Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026.xlsx`](file:///D:/Proyectos/antigravity-agents-repository/data/Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026.xlsx)
> - **Script Automatizado de Extracción y Formato**: [`scripts/generar_excel_auditoria_cammesa.py`](file:///D:/Proyectos/antigravity-agents-repository/scripts/generar_excel_auditoria_cammesa.py)

---

## 1. Alcance y Objetivos de la Auditoría

A requerimiento del usuario, se ejecutó un relevamiento integral mediante el **Agente 02 (Ciencia de Datos)** sobre la base productiva Oracle de EPEC (`xxsigec.auditoria_cammesa`, `xxsigec.contratos`, `xxsigec.servicios`, `xxsigec.personas`, `xxsigec.tarifas`, `xxsigec.clases`, `xxsigec.tensiones` y `xxsigec.sucursales`), con el fin de:
1. Buscar e identificar todos los **suministros vigentes** (`CNT_ESTADO = 'V'`) para las 5 razones sociales y CUITs solicitados.
2. Extraer las variables regulatorias y técnicas exigidas: Razón Social, CUIT/CUIL, Suministro, Distrito / Sucursal, Tarifa, Clase, Nivel de Tensión, Potencia Contratada (kW), Potencia Leída (kW) y Consumos de Energía en Resto, Pico y Valle para los años **2025 y 2026**.
3. Construir un modelo analítico y un libro Excel ejecutivo de alta gama con 5 hojas operativas, tablas estructuradas, formatos numéricos y trazabilidad completa de casos especiales.

---

## 2. Síntesis General por Entidad

| Entidad Solicitada | CUIT Solicitado / EPEC | Suministros Vigentes | Suministros en CAMMESA | Tarifas Dominantes | Tensión | Pot. Contratada Máx (kW) | Energía Total 2025-2026 (kWh) |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: | :---: |
| **FÁBRICA ARGENTINA DE AVIONES BRIG. SAN MARTÍN S.A.** | `30-67822197-6` | **0** | **0** | 1304, 1305, 240 *(Históricas)* | Baja Tensión | 0.00 kW | 0 kWh *(Operación GUMA)* |
| **Escuela de Aviación Militar** | `30-52275191-6` *(Reg. `30-54669785-8`)* | **1** | **0** | 541 (Alumbrado / Oficial) | Baja Tensión | 0.00 kW | 0 kWh *(Integrado a FAA)* |
| **Fuerza Aérea Argentina** | `33-62830272-9` / `30-54669785-8` | **7** | **7** | 350 (Grandes Usuarios MT), 541, 140 | Media Tensión / BT | 4.787,50 kW | 37.556 kWh |
| **Instituto de Obra Social de las Fuerzas Armadas (IOSFA)** | `30-71429214-1` | **11** | **11** | 140, 240, 241, 350, 541 | Baja Tensión | 174,00 kW | 38.152 kWh |
| **Ejército Argentino** | `30-54669051-9` | **47** | **43** | 140, 353, 541, 543, 604 | Baja Tensión | 1.295,00 kW | 383.367 kWh |
| **TOTAL GENERAL CONSOLIDADO** | - | **66** | **61** | - | - | **6.256,50 kW** | **459.075 kWh** |

---

## 3. Diagnóstico Técnico de Casos Especiales

### A. FADEA (Fábrica Argentina de Aviones Brig. San Martín S.A.) - CUIT `30-67822197-6`
* **Hallazgo en SIGEC**: Se detectaron 3 contratos históricos registrados a nombre de FADEA:
  * Suministro `3055615` (Av. Fuerza Aérea 5500, Tarifa 1305 - Enlace/Internet). Cancelado el 31/08/2021.
  * Suministro `3055617` (Av. Fuerza Aérea 5500, Tarifa 1304 - Internet Dedicado). Cancelado el 30/08/2021.
  * Suministro `3083168` (Av. Fuerza Aérea 5200, Tarifa 240). Cancelado el 14/09/2021.
* **Causa de Ausencia en CAMMESA 2025-2026**: FADEA no posee suministros minoristas activos de distribución eléctrica en EPEC. Como gran planta aeronáutica, opera en el Mercado Eléctrico Mayorista bajo la figura de **GUMA** (Gran Usuario Mayorista) o recibe energía mediante la infraestructura de alta/media tensión de la Guarnición Militar.

### B. Escuela de Aviación Militar - CUIT `30-52275191-6`
* **Hallazgo en SIGEC**: La Escuela de Aviación Militar figura en el padrón bajo el registro institucional `335160` con CUIT `30-54669785-8`:
  * Suministro `420687` (Ruta 20 Km. 6 1/2, Tarifa 541, Contrato `1`, Estado **VIGENTE** desde 01/01/1995).
* **Causa de Ausencia en CAMMESA 2025-2026**: A pesar de estar vigente, este suministro no se declara en la tabla `xxsigec.auditoria_cammesa`. El predio de la Escuela y la Guarnición se abastece a través del suministro troncal mayorista de la Fuerza Aérea Argentina (`420603`).

### C. Fuerza Aérea Argentina - CUIT `33-62830272-9`
* **Suministro Troncal Activo**: Suministro **`420603`** ubicado en `AV. FUERZA AEREA KM. 5 1/2`:
  * Tarifa `350` (Grandes Usuarios).
  * Clase `2` (G.C. DFP > 100 BT/MT).
  * Tensión `2` (**Media Tensión**).
  * Registros: 21 períodos declarados en `auditoria_cammesa` entre 2025 y 2026.
* **Suministros Adicionales Activos**:
  * `420556` (Av. Sabattini 1907 - Tarifa 541).
  * `420774` y `2698987` (Av. Colón 1116 - Tarifa 140).
  * `776137` (Balcarce 448 - Tarifa 140).

### D. IOSFA - CUIT `30-71429214-1`
* Posee 11 suministros vigentes con facturación ininterrumpida en CAMMESA en Cosquín (`329118`, `329120`, `329121`, `329123`, `329126`, `329127`, `329431`), Córdoba Capital (`420478`, `420479`, `1006628`) y La Calera (`699104`).

### E. Ejército Argentino - CUIT `30-54669051-9`
* Concentra 47 suministros vigentes y 43 con declaración activa en CAMMESA. Destacan el Hospital Militar Córdoba (`699106`, `699112`), la Jefatura de Barrio Militar (`420718`, `420721`, `420730`), el Batallón 141 y los polígonos sobre Camino a La Calera y Av. Ejército Argentino.

---

## 4. Estructura del Libro Excel Generado

El archivo [`Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026.xlsx`](file:///C:/Users/jidiaz/Downloads/Auditoria_CAMMESA_Fuerzas_Armadas_2025_2026.xlsx) cuenta con 5 hojas de cálculo diseñadas con altos estándares ejecutivos:

1. **`00_Resumen_Ejecutivo`**: Tablero directivo con tarjetas KPI, síntesis comparativa por entidad con totales de energía y potencia, y notas metodológicas.
2. **`01_Suministros_Vigentes`**: Padrón de los 66 suministros vigentes con sus datos de contrato, dirección, sucursal, distrito catastral, tarifa, tensión y consumos acumulados 2025 vs. 2026.
3. **`02_Detalle_CAMMESA_2025_2026`**: **3.101 registros mensuales** detallados de la tabla `xxsigec.auditoria_cammesa` con potencias punta/fuera de punta (contratadas y leídas), consumos desagregados (Resto, Pico, Valle, Total) y grupo CAMMESA.
4. **`03_Consolidado_Anual`**: Tabla dinámica por suministro y año (2025 vs. 2026) con meses declarados, potencias máximas y desglose de energía.
5. **`04_Diagnostico_FADEA_EAM`**: Ficha técnica detallada de los suministros de FADEA y Escuela de Aviación Militar con fechas de inicio/fin y causales de exclusión en la tabla CAMMESA.


## 5. Control de Reglas Específicas Aplicadas

### A. Exclusión de Valores de Energía Negativa
- Se identificaron y excluyeron del cómputo oficial **8 registros** con valores de energía total negativos originados por notas de crédito, ajustes de aforo y refacturaciones contables.
- Dichos registros quedaron documentados con fecha, período y suministro en la hoja `04_Contratos_GUDI_y_Especiales`.

### B. Detección e Inclusión de Contratos GUDI (Grandes Usuarios de Distribuidora)
- Se auditó el campo `CNT_GUDI` en `xxsigec.contratos` para toda la muestra.
- **Contrato GUDI Vigente Confirmado**:
  - **Entidad**: Fuerza Aérea Argentina (`33-62830272-9`)
  - **Suministro**: `420603` (Av. Fuerza Aérea Km. 5 1/2)
  - **Contrato**: `3` (Estado `V`)
  - **Código GUDI Oficial**: `GD0633XI`
  - **Tarifa**: `350` (Grandes Usuarios en Media Tensión)
- Se constató que las demás entidades no poseen contratos vigentes bajo encuadre GUDI en EPEC.

### C. Integridad en las Relaciones Tabulares EPEC-CAMMESA
Se verificó el 100% de consistencia relacional sin registros huérfanos ni productos cartesianos:
- `xxsigec.auditoria_cammesa[tcl_codigo_gral]` -> `xxsigec.tarifas[tcl_codigo]` (Descripciones oficiales de tarifa).
- `xxsigec.auditoria_cammesa[cla_codigo_gral]` -> `xxsigec.clases[cla_codigo]` condicionada por `tcl_codigo` (Subdivisiones de clase según cuadro tarifario).
- `xxsigec.auditoria_cammesa[ten_codigo_gral]` -> `xxsigec.tensiones[ten_codigo]` (Baja, Media y Alta Tensión).
