---
title: "Especificación de Disposición Visual Qlik Sense: Tablero MI - Zona A (Equivalencia Power BI PBIP)"
tags:
  - #qlik-sense
  - #power-bi
  - #pbip
  - #layout
  - #wireframe
  - #grid-24
  - #set-analysis
  - #epec
  - #ami
created: 2026-10-27
updated: 2026-10-27
---

# 📐 Especificación y Codificación de Disposición Visual en Qlik Sense
## Equivalencia Exacta del Reporte Power BI (`Tablero MI - Zona A.pbip`)

Documento técnico elaborado por el **Squad Ágil Multi-Agente** bajo el liderazgo del **Copiloto Orquestador (Agente 11 / PM)** y el **Especialista en Ciencia de Datos (Agente 02)**.

---

## 🏛️ 1. Fundamentos Técnicos: Cómo se Codifica la Disposición en Qlik Sense

A diferencia del script de carga (`.qvs`), que es código procedural de transformación y modelado asociativo de datos, **la disposición visual de los gráficos en Qlik Sense se codifica de manera declarativa mediante el modelo de objetos genéricos (Generic Objects) de la QIX Engine API**.

### 1.1. Grilla Celular Nativa (Grid System)
Qlik Sense estructura cada hoja (`sheet`) como una grilla de **24 columnas** de ancho variable y filas fijas/extensibles:
* **Eje X (Columnas)**: Se divide en 24 unidades discretas (`col: 0` a `23`).
* **Eje Y (Filas)**: Se divide en filas de altura proporcional (`row: 0` a `N`).
* **Bounding Box**: Cada objeto visual ocupa un rectángulo definido por:
  ```json
  {
    "name": "id_objeto_visual",
    "type": "kpi | pivot-table | table | barchart | combochart | map | filterpane",
    "col": 0,        // Columna inicial (0-23)
    "row": 0,        // Fila inicial (0-N)
    "colspan": 6,    // Ancho en columnas (1-24)
    "rowspan": 3     // Alto en filas
  }
  ```

### 1.2. Fórmula de Transformación Cartesiana (Power BI $\rightarrow$ Qlik Sense)
A partir del análisis de los archivos nativos PBIP (`Tablero MI - Zona A.Report/definition/pages/*/visuals/*/visual.json`), se aplicó la transformación matemática:

$$\text{Col}_{\text{Qlik}} = \left\lfloor \frac{X_{\text{PBI}}}{\text{Ancho}_{\text{Canvas}}} \times 24 \right\rceil, \quad \text{Colspan}_{\text{Qlik}} = \max\left(1, \left\lfloor \frac{\text{Width}_{\text{PBI}}}{\text{Ancho}_{\text{Canvas}}} \times 24 \right\rceil\right)$$

$$\text{Row}_{\text{Qlik}} = \left\lfloor \frac{Y_{\text{PBI}}}{H_{\text{fila}}} \right\rceil, \quad \text{Rowspan}_{\text{Qlik}} = \max\left(1, \left\lfloor \frac{\text{Height}_{\text{PBI}}}{H_{\text{fila}}} \right\rceil\right)$$

Donde $H_{\text{fila}} = 60\text{ px}$ en lienzos de 720 px (12 filas estándar) y lienzos extendidos de 900 px (15 filas) o 1500 px (25 filas).

---

## 📦 2. Entregables y Automatizaciones Generadas

1. **Catálogo Canónico JSON**:
   * [`D:\Usuarios\jidiaz\Downloads\qlik_sense_sheets_layout_specification.json`](file:///D:/Usuarios/jidiaz/Downloads/qlik_sense_sheets_layout_specification.json): Especificación completa de todas las hojas, objetos, tipos de visual, dimensiones, medidas, filtros, títulos y posiciones `(col, row, colspan, rowspan)`.
2. **Bundle Maestro QIX Engine**:
   * [`D:\Usuarios\jidiaz\Downloads\qlik_sense_app_sheets_bundle.json`](file:///D:/Usuarios/jidiaz/Downloads/qlik_sense_app_sheets_bundle.json): Formato nativo de importación directa para Qlik CLI, Enigma.js o Engine API.
3. **Visor Interactivo Web (Blueprint UI)**:
   * [`D:\Usuarios\jidiaz\Downloads\viewer_layout_qlik.html`](file:///D:/Usuarios/jidiaz/Downloads/viewer_layout_qlik.html) y versionado en [`scripts/viewer_layout_qlik.html`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/viewer_layout_qlik.html). Permite ver y navegar la grilla de 24 columnas en el navegador, inspeccionar cada tile y copiar la configuración.
4. **Script de Inyección Automática en Caliente**:
   * [`scripts/aplicar_layout_qlik_engine.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/aplicar_layout_qlik_engine.py): Conector WebSocket para inyectar automáticamente las hojas y objetos en Qlik Sense Desktop (`ws://localhost:4848/app/...`).

---

## 🗺️ 3. Planos de Disposición por Hoja (Wireframe Blueprints)

### 3.1. Hoja 1: Suministros (Canvas 1280x720 $\rightarrow$ Grilla 24x12)

#### Matriz de Ubicación (ASCII Grid Layout)
```text
Col: 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23
R00: [----------------- Título Tablero MI Zona A -------------------] [--Logo-]
R01: [K1:TOTAL] [K2:SELECC] [K3:CLOU ] [K4:NANS ] [K5:CHUP ] [K6:COM] [Filtro]
R02: [K1:TOTAL] [K2:SELECC] [K3:CLOU ] [K4:NANS ] [K5:CHUP ] [K6:COM] [Filtro]
R03: [Pivot: Tarifa x Clase ] [Pivot: Medidores x Marca/Plan ] [Busca] [Filtro]
R04: [Pivot: Tarifa x Clase ] [Pivot: Medidores x Marca/Plan ] [Busca] [Filtro]
R05: [Pivot: Tarifa x Clase ] [Pivot: Medidores x Marca/Plan ] [Busca] [Filtro]
R06: [Combo Chart: Evolución Temporal Ejecución (Día/Mes)   ] [Tabla Detalle ]
R07: [Combo Chart: Evolución Temporal Ejecución (Día/Mes)   ] [Tabla Detalle ]
R08: [Combo Chart: Evolución Temporal Ejecución (Día/Mes)   ] [Tabla Detalle ]
R09: [Combo Chart: Evolución Temporal Ejecución (Día/Mes)   ] [Tabla Detalle ]
R10: [Tabla Detalle Operativa de Suministros (27 Columnas Con Semáforo)     ]
R11: [Tabla Detalle Operativa de Suministros (27 Columnas Con Semáforo)     ]
```

#### Catálogo de Objetos Qlik Sense
| Objeto Qlik | Col | Row | Ancho | Alto | Título en Power BI | Métrica / Expresión Qlik Sense Script (`05_SPRINT2...qvs`) |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **`text-image`** | 5 | 0 | 13 | 1 | `titulo_tablero_MI_zona` | Título dinámico institucional |
| **`kpi`** | 0 | 1 | 4 | 2 | `TOTAL SUMINISTROS` | `Count({1<ZONA={'A'}>} DISTINCT SUMINISTRO)` |
| **`kpi`** | 4 | 1 | 4 | 2 | `SUMINISTROS SELECCIÓN` | `Count(DISTINCT SUMINISTRO)` |
| **`kpi`** | 8 | 1 | 4 | 2 | `CLOU` | `Count({<TELEMEDIBLE={'CLOU'}>} DISTINCT SUMINISTRO)` |
| **`kpi`** | 12 | 1 | 4 | 2 | `NANSEN` | `Count({<TELEMEDIBLE={'NANSEN'}>} DISTINCT SUMINISTRO)` |
| **`kpi`** | 16 | 1 | 4 | 2 | `CHUPETE` | `Count({<TELEMEDIBLE={'CHUPETE'}>} DISTINCT SUMINISTRO)` |
| **`kpi`** | 20 | 1 | 4 | 2 | `COMUN NO INTELIGENTE` | `Count({<TELEMEDIBLE={'OTROS'}>} DISTINCT SUMINISTRO)` |
| **`pivot-table`**| 0 | 3 | 10 | 3 | `Pivot Tarifa / Clase` | Filas: `ZONA`, `TARIFA` \| Cols: `CLASE` \| `Count(DISTINCT SUMINISTRO)` |
| **`pivot-table`**| 10 | 3 | 10 | 3 | `Pivot Marca / Plan` | Filas: `NOMBRES_TELEMEDIBLE`, `suministro_plan` \| Cols: `nombre_FASES` |
| **`filterpane`** | 20 | 3 | 4 | 3 | `Filtros Operativos` | `BARRIO`, `ZONA`, `TARIFA`, `SUBESTACION` |
| **`combochart`** | 0 | 6 | 14 | 4 | `Evolución Ejecución` | Dim: `PERIODO_EJECUCION` \| Barras: `Count({<FLAG_ORD_EJECUTADO={1}>} DISTINCT SUMINISTRO)` |
| **`table`** | 14 | 6 | 10 | 4 | `Resumen Medición` | Dim: `TELEMEDIBLE`, `Estado_Telemetria` \| `Count(DISTINCT SUMINISTRO)` |
| **`table`** | 0 | 10 | 24 | 2 | `Listado de Suministros`| 27 columnas normalizadas con semaforización condicional |

---

### 3.2. Hoja 2: Control de Ordenativos (Canvas 1280x1500 $\rightarrow$ Grilla 24x25)

#### Matriz de Ubicación
```text
Col: 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23
R00: [----------------- Título Tablero MI Zona A -------------------]
R01: [Filtro: GRUPO] [K1: EJECUTADOS] [K2: PENDIENTES] [Mapa Georreferenciado  ]
R02: [Filtro: GRUPO] [K1: EJECUTADOS] [K2: PENDIENTES] [Mapa Georreferenciado  ]
R03: [Filtro: ESTAD] [Pivot: MedidorTipo vs Estado   ] [Mapa Georreferenciado  ]
R04: [Filtro: ESTAD] [Pivot: MedidorTipo vs Estado   ] [Mapa Georreferenciado  ]
R05: [Filtro: RELEV] [Tabla 1: Listado de Ordenativos (17 Columnas)          ]
R06: [Filtro: RELEV] [Tabla 1: Listado de Ordenativos (17 Columnas)          ]
R07: [Filtro: SECTOR] [Tabla 1: Listado de Ordenativos (17 Columnas)         ]
R08: [Filtro: SECTOR] [Combo Chart: Ejecutados por Mes                       ]
R09: [Buscador Parte] [Combo Chart: Ejecutados por Mes                       ]
R10: [Buscador Parte] [Combo Chart: Ejecutados por Mes                       ]
R11: [Buscador Sumi ] [Combo Chart: Ejecutados por Mes                       ]
R12: [Buscador Sumi ] [Combo Chart: Ejecutados por Día                       ]
R13: [Filtro: Fecha ] [Combo Chart: Ejecutados por Día                       ]
R14: [Filtro: Fecha ] [Combo Chart: Ejecutados por Día                       ]
```

#### Catálogo de Objetos Qlik Sense
| Objeto Qlik | Col | Row | Ancho | Alto | Título en Power BI | Métrica / Expresión Qlik Sense Script (`06_SPRINT3...qvs`) |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **`kpi`** | 5 | 1 | 4 | 2 | `EJECUTADOS` | `Count({<FLAG_ORD_EJECUTADO={1}>} DISTINCT SUMINISTRO)` |
| **`kpi`** | 9 | 1 | 3 | 2 | `PENDIENTES` | `Count({<FLAG_ORD_PENDIENTE={1}>} DISTINCT SUMINISTRO)` |
| **`map`** | 12 | 1 | 12 | 4 | `Mapa de Ordenativos` | Lat/Long: `DC_LATITUD`, `DC_LONGITUD` \| Color por `EJECUTADOSvsPENDIENTES` |
| **`pivot-table`**| 5 | 3 | 7 | 2 | `Ejecución x Tipo Medidor`| Filas: `EJECUTADOSvsPENDIENTES` \| Cols: `MedidorTipo` \| `Count(DISTINCT SUMINISTRO)` |
| **`table`** | 5 | 5 | 19 | 3 | `Listado de Ordenativos` | `NUMERO_ORDENATIVO`, `SECTOR_ASIGNADO`, `FECHA_EJECUCION`, `ORD_RESULTADO`, etc. |
| **`combochart`** | 5 | 8 | 19 | 4 | `EJECUTADOS POR MES` | Dim: `PERIODO_EJECUCION` \| Barras: `Count({<FLAG_ORD_EJECUTADO={1}>} DISTINCT NUMERO_ORDENATIVO)` |
| **`combochart`** | 5 | 12 | 19 | 4 | `EJECUTADOS POR DÍA` | Dim: `DIA_EJECUCION` \| Barras: `Count({<FLAG_ORD_EJECUTADO={1}>} DISTINCT NUMERO_ORDENATIVO)` |
| **`filterpane`** | 0 | 1 | 4 | 2 | `GRUPO_LECTURA` | Dimensión `GRUPO_LECTURA` |
| **`filterpane`** | 0 | 3 | 4 | 2 | `ESTADO ORDENATIVOS` | Dimensión `EJECUTADOSvsPENDIENTES` |
| **`filterpane`** | 0 | 5 | 4 | 2 | `ESTADO_RELEVAMIENTO`| Dimensión `ESTADO_RELEVAMIENTO` |
| **`filterpane`** | 0 | 7 | 4 | 2 | `SECTOR_EJECUTANTE` | Dimensión `SECTOR_EJECUTANTE` |

---

### 3.3. Hoja 3: Telemetría (Canvas 1280x900 $\rightarrow$ Grilla 24x15)

#### Matriz de Ubicación
```text
Col: 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23
R00: [----------------- Título Tablero MI Zona A -------------------]
R01: [---------------------- Barra de Navegación -------------------]
R02: [K1: INSTALADOS] [K2: NUNCA ] [Filtro Tarifa] [Diag Plan] [Diag Marca ]
R03: [K1: INSTALADOS] [K3: SIN TEL] [Filtro Plan  ] [Diag Plan] [Diag Marca ]
R04: [K1: INSTALADOS] [K4: TEL OK ] [Filtro Marca ] [Diag Plan] [Diag Marca ]
R05: [Filtro Estado ] [Tabla Diagnóstico x Plan   ] [Mapa Conectividad AMI  ]
R06: [Filtro Estado ] [Tabla Diagnóstico x Plan   ] [Mapa Conectividad AMI  ]
R07: [Buscador Sumi ] [Tabla Diagnóstico x Plan   ] [Mapa Conectividad AMI  ]
R08: [Buscador Sumi ] [Tabla Diagnóstico x SET    ] [Mapa Conectividad AMI  ]
R09: [Buscador Med  ] [Tabla Diagnóstico x SET    ] [Mapa Conectividad AMI  ]
R10: [Buscador SET  ] [Tabla Diagnóstico x SET    ] [Mapa Conectividad AMI  ]
R11: [Buscador SET  ] [Tabla Diagnóstico x SET    ] [Mapa Conectividad AMI  ]
R12: [Tabla Detalle Operativa de Telemetría (11 Columnas Con Enlace)        ]
R13: [Tabla Detalle Operativa de Telemetría (11 Columnas Con Enlace)        ]
R14: [Tabla Detalle Operativa de Telemetría (11 Columnas Con Enlace)        ]
```

#### Catálogo de Objetos Qlik Sense
| Objeto Qlik | Col | Row | Ancho | Alto | Título en Power BI | Métrica / Expresión Qlik Sense Script (`07_SPRINT4...qvs`) |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **`kpi`** | 0 | 2 | 4 | 3 | `MEDIDORES INSTALADOS` | `Count({<TELEMEDIBLE={'CLOU','NANSEN'}>} DISTINCT SUMINISTRO)` |
| **`kpi`** | 5 | 2 | 4 | 1 | `NUNCA TELEMIDIERON` | `Count({<TELEMEDIBLE={'CLOU','NANSEN'}, FLAG_NUNCA_TELEMEDIDO={1}>} DISTINCT SUMINISTRO)` |
| **`kpi`** | 5 | 3 | 4 | 1 | `SIN TELEMETRÍA` | `Count({<TELEMEDIBLE={'CLOU','NANSEN'}, FLAG_SIN_TELEMETRIA={1}>} DISTINCT SUMINISTRO)` |
| **`kpi`** | 5 | 4 | 4 | 1 | `TELEMETRÍA OK` | `Count({<TELEMEDIBLE={'CLOU','NANSEN'}, FLAG_TELEMETRIA_OK={1}>} DISTINCT SUMINISTRO)` |
| **`table`** | 7 | 5 | 7 | 3 | `Diagnóstico x Plan` | Dim: `suministro_plan` \| `Total Medidores`, `Sum([Telemetria_<6])`, `no telemide_%` |
| **`table`** | 7 | 8 | 7 | 3 | `Diagnóstico x SET` | Dim: `SUBESTACION` \| `Total Medidores`, `Sum([Telemetria_<6])`, `no telemide_%` |
| **`map`** | 15 | 5 | 9 | 10 | `Mapa Telemetría` | Lat/Long: `DC_LATITUD`, `DC_LONGITUD` \| Color por `Estado_Telemetria` (Verde/Ámbar/Rojo) |
| **`table`** | 0 | 12 | 14 | 3 | `Detalle Telemetría` | 11 columnas operativas (`SUMINISTRO`, `MEDIDOR`, `Estado_Telemetria`, etc.) |

---

### 3.4. Hoja 4: Relevamiento (Canvas 1280x720 $\rightarrow$ Grilla 24x12)

#### Matriz de Ubicación
```text
Col: 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23
R00: [----------------- Título Tablero MI Zona A -------------------]
R01: [Mapa Relevamiento y Auditoría] [Pivot Semáforo] [Filtro SET] [KPI Fecha]
R02: [Mapa Relevamiento y Auditoría] [Pivot Semáforo] [Filtro SET] [KPI Fecha]
R03: [Mapa Relevamiento y Auditoría] [Pivot Novedad ] [Filtro SET] [---------]
R04: [Mapa Relevamiento y Auditoría] [Pivot Novedad ] [Filtro SET] [---------]
R05: [Mapa Relevamiento y Auditoría] [Pivot Novedad ] [Filtro SET] [---------]
R06: [Mapa Relevamiento y Auditoría] [Tabla Detalle Relevamiento (9 Cols)    ]
R07: [Mapa Relevamiento y Auditoría] [Tabla Detalle Relevamiento (9 Cols)    ]
R08: [Mapa Relevamiento y Auditoría] [Tabla Detalle Relevamiento (9 Cols)    ]
R09: [Mapa Relevamiento y Auditoría] [Tabla Detalle Relevamiento (9 Cols)    ]
R10: [Mapa Relevamiento y Auditoría] [Tabla Detalle Relevamiento (9 Cols)    ]
```

#### Catálogo de Objetos Qlik Sense
| Objeto Qlik | Col | Row | Ancho | Alto | Título en Power BI | Métrica / Expresión Qlik Sense Script (`09_SPRINT5...qvs`) |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **`map`** | 0 | 1 | 10 | 10 | `Mapa Relevamiento` | Lat/Long: `DC_LATITUD`, `DC_LONGITUD` \| Color por `Semaforo_protelem_color` |
| **`pivot-table`**| 11 | 1 | 6 | 2 | `Semáforo x Medidor` | Filas: `Semaforo_protelem_color` \| Cols: `MedidorTipo` \| `Count(DISTINCT SUMINISTRO)` |
| **`pivot-table`**| 11 | 4 | 6 | 2 | `Novedades x Medidor`| Filas: `Filtro_novedad` \| Cols: `MedidorTipo` \| `Count(DISTINCT SUMINISTRO)` |
| **`kpi`** | 20 | 1 | 4 | 1 | `Fecha de actualización`| `Date(Min(FECHA_ACTUALIZACION), 'DD/MM/YYYY')` |
| **`filterpane`** | 17 | 3 | 4 | 3 | `Filtro SETs Polígonos`| Dimensión `t_poligonos.SETs` |
| **`table`** | 11 | 6 | 13 | 5 | `Detalle Relevamiento` | 9 columnas (`SUMINISTRO`, `MEDIDOR`, `TARIFA`, `SUBESTACION`, `ACOMETIDA`, `TAPA`) |

---

### 3.5. Hoja 5: Tarifas y Lecturas (Canvas 1280x720 $\rightarrow$ Grilla 24x12)

#### Catálogo de Objetos Qlik Sense
| Objeto Qlik | Col | Row | Ancho | Alto | Hoja | Métrica / Expresión Qlik Sense Script (`10_SPRINT6...qvs`) |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **`pivot-table`**| 13 | 0 | 8 | 5 | `TARIFAS` | Filas: `TIPO_CLIENTE`, `TARIFA` \| Cols: `TELEMEDIBLE` \| `Count(SUMINISTRO)` |
| **`pivot-table`**| 7 | 1 | 5 | 4 | `TARIFAS` | Filas: `TIPO_CLIENTE`, `TARIFA` \| Cols: `ZONA` \| `Count(SUMINISTRO)` |
| **`kpi`** | 1 | 2 | 5 | 2 | `TARIFAS` | `Count(DISTINCT PCT)` (Total PCTs Relevados) |
| **`pivot-table`**| 1 | 5 | 5 | 3 | `TARIFAS` | Filas: `PCT` \| Cols: `MedidorTipo` \| `Count(DISTINCT SUMINISTRO)` |
| **`table`** | 7 | 6 | 11 | 5 | `TARIFAS` | Detalle `TIPO_CLIENTE`, `TELEMEDIBLE`, `TARIFA`, `ZONA`, `DISTRITO`, `SUMINISTRO` |
| **`map`** | 19 | 8 | 5 | 4 | `TARIFAS` | Lat/Long: `DC_LATITUD`, `DC_LONGITUD` \| Color por `suministro_plan` |
| **`pivot-table`**| 5 | 1 | 18 | 10 | `LECTURAS` | Filas: `cuadrantes_medidos` \| Cols: `TELEMEDIDA_STE_MARCA` \| `Count(DISTINCT MEDIDOR)` |

---

## 🛠️ 4. Guía Operativa de Implementación en Qlik Sense

### Opción A: Despliegue Automatizado vía WebSocket (Recomendado)
1. Abrir la aplicación `Tablero_MI_Zona_A.qvf` en Qlik Sense Desktop o Qlik Sense Enterprise.
2. Ejecutar el script:
   ```powershell
   python scripts/aplicar_layout_qlik_engine.py --inject
   ```
3. El motor Qlik crea automáticamente todas las hojas con sus nombres, resoluciones y los objetos vinculados a las medidas maestras.

### Opción B: Construcción Asistida por Visor Visual Interactivo
1. Abrir en cualquier navegador el visor interactivo:
   * Local: [`D:\Usuarios\jidiaz\Downloads\viewer_layout_qlik.html`](file:///D:/Usuarios/jidiaz/Downloads/viewer_layout_qlik.html)
2. Seleccionar la hoja deseada (`Suministros`, `Control de Ordenativos`, `Telemetría`, `Relevamiento`, `Tarifas`).
3. En el editor de Qlik Sense, arrastrar cada objeto guiándose por las coordenadas mostradas (`Col X, Row Y, Ancho W, Alto H`).
4. Al hacer clic sobre cualquier bloque del visor, se copian al instante la dimensión y la expresión Set Analysis exacta.
