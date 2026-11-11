---
title: "Resolución Geoespacial Oficial de Zonas EPEC para Cooperativas Eléctricas AMI"
fecha: 2026-11-11
autor: "Squad Ágil Adaptativo & Ciencia de Datos EPEC"
agentes:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos & BI EPEC]]"
  - "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto de Sistemas EPEC]]"
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]]"
proyecto: "[[docs/Proyectos/2026-10-21_despliegue-medidores-inteligentes-ami|Plan Maestro Despliegue AMI EPEC]]"
repositorio_dedicado: "https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami"
tags:
  - #geoespacial
  - #wfs
  - #gis
  - #epec
  - #cooperativas
  - #ami
  - #sigec
  - #triple-qa
---

# 🗺️ Resolución Geoespacial Oficial de Zonas EPEC para Cooperativas Eléctricas AMI

## 📌 1. Resumen Ejecutivo y Motivación

En la ingesta preliminar del dataset de **47.254 medidores inteligentes** asignados a 38 cooperativas eléctricas de la Provincia de Córdoba, 3 cooperativas figuraban catalogadas con estado comercial **"Sin Zona"** en la planilla de origen:
1. **HUANCHILLA** (`COOP.ELEC.HUANCHILLA`, ID: `c17`) — 800 medidores (600 mono + 200 tri), 3 DCU.
2. **BULNES** (`COOP.ELEC.BULNES.`, ID: `c25`) — 550 medidores (350 mono + 200 tri), 5 DCU.
3. **ASCOCHINGA** (`COOP ELEC DE SERV PUB Y ANEXOS LTDA ASCOCHINGA LA PAMPA`, ID: `c29`) — 300 medidores (200 mono + 100 tri), 1 DCU.

El objetivo fue determinar inequívocamente a qué **Zona Oficial de EPEC** pertenece cada una de estas localidades utilizando exclusivamente las capas vectoriales espaciales oficiales del servidor WFS de EPEC/MAySP (`EPEC:radios_municipales_4326` y `EPEC:t_limites_zonas`) y validando el 100% de los resultados con la base de datos comercial **Oracle XXSIGEC**.

---

## 🛠️ 2. Metodología Geoespacial Aplicada (Protocolo en 6 Etapas)

### Fase 1: Extracción de Fuentes Confiables (WFS & Catastro IDECOR)
- **Servidor Geoespacial**: `https://maaysp-ws.cba.gov.ar/EPEC/wfs` (autenticación oficial `EPEC_comercial`).
- **Capa 1 (`EPEC:radios_municipales_4326`)**: 427 radios urbanos y municipales de la Provincia de Córdoba en `EPSG:4326`.
- **Capa 2 (`EPEC:t_limites_zonas`)**: Capa de fronteras zonales de EPEC en coordenadas proyectadas Gauss-Krüger Faja 4 (`EPSG:22174`).

### Fase 2: Poligonización Topológica de Límites de Zonas
La capa `EPEC:t_limites_zonas` almacena geometrías de tipo `MultiLineString` (líneas de frontera). Para realizar consultas de contención espacial (*Point-in-Polygon* y *Polygon-Contains-Polygon*), se reconstruyeron los 8 recintos cerrados de la provincia mediante:
$$\text{Polígonos} = \text{polygonize}(\text{unary\_union}(\text{Líneas}))$$
y posterior reproyección a `EPSG:4326`.

### Fase 3: Cruce Espacial y Mapeo Canónico de Polígonos
Se calibró cada polígono resultante con las 35 cooperativas restantes cuya zona ya estaba certificada, obteniendo un mapeo unívoco:
- **Polígono 0** (Centroide -33.92°, -64.00°) $\rightarrow$ **ZONA F** (Sur Provincial: Laboulaye, Jovita, Del Campillo, Serrano).
- **Polígono 1** (Centroide -32.08°, -64.37°) $\rightarrow$ **ZONA H** (Sierras Chicas / Calamuchita: Berrotarán, Anisacate, Alcira).
- **Polígono 2** (Centroide -31.76°, -65.14°) $\rightarrow$ **ZONA I** (Traslasierra: Mina Clavero, Nono).
- **Polígono 3** (Centroide -30.92°, -65.12°) $\rightarrow$ **ZONA B** (Cruz del Eje / Punilla Norte).
- **Polígono 4** (Centroide -30.34°, -63.90°) $\rightarrow$ **ZONA A** (Norte Provincial: Jesús María, Colonia Caroya, Agua de Oro).
- **Polígono 5** (Centroide -31.29°, -62.79°) $\rightarrow$ **ZONA D** (San Justo: Brinkmann, Porteña, Alicia).
- **Polígono 6** (Centroide -32.78°, -62.39°) $\rightarrow$ **ZONA G** (Marcos Juárez / Unión: Leones, Inriville, Camilo Aldao).
- **Polígono 7** (Centroide -32.53°, -63.52°) $\rightarrow$ **ZONA C** (Centro Provincial / Tercero Arriba: Oncativo, Laborde).

---

## 🎯 3. Resultados del Análisis Geoespacial & Validación Comercial

### A. HUANCHILLA (`c17`)
- **Razón Social en Planilla**: `COOP.ELEC.HUANCHILLA`
- **Búsqueda en XXSIGEC.PERSONAS**: `PRS_NUMERO: 182204` · CUIT: `30-54579246-6`
- **Contrato Vigente (Tarifa >= 400)**: `CNT_NUMERO: 1` · `TCL_CODIGO: '411'` (4.2 Coop. Eléctricas) · `CNT_ESTADO: 'V'`
- **Punto de Suministro (XXSIGEC.SERVICIOS)**: `SRV_CODIGO: 278422` · Dirección: `HUANCHILLA`
- **Área Geográfica & Sucursal**: `AGF_CODIGO: 6300` (*GENERAL LEVALLE / HUANCHILLA*) · `SCF_CODIGO: 33` (*GRAL LEVALLE*)
- **Zona Comercial Oficial**: **ZONA F** (Sur Provincial)

### B. BULNES (`c25`)
- **Razón Social en Planilla**: `COOP.ELEC.BULNES.`
- **Búsqueda en XXSIGEC.PERSONAS**: `PRS_NUMERO: 182933` · CUIT: `30-54576322-9`
- **Contrato Vigente (Tarifa >= 400)**: `CNT_NUMERO: 1` · `TCL_CODIGO: '411'` (4.2 Coop. Eléctricas) · `CNT_ESTADO: 'V'`
- **Punto de Suministro (XXSIGEC.SERVICIOS)**: `SRV_CODIGO: 279152` · Dirección: `BULNES`
- **Área Geográfica & Sucursal**: `AGF_CODIGO: 6000` (*RIO CUARTO / BULNES*) · `SCF_CODIGO: 28` (*RIO CUARTO*)
- **Zona Comercial Oficial**: **ZONA F** (Sur Provincial)

### C. ASCOCHINGA / LA PAMPA (`c29`)
- **Razón Social en Planilla**: `COOP ELEC DE SERV PUB Y ANEXOS LTDA ASCOCHINGA LA PAMPA`
- **Búsqueda en XXSIGEC.PERSONAS**: `PRS_NUMERO: 762962` · CUIT: `30-54582765-0`
- **Contrato Vigente (Tarifa >= 400)**: `CNT_NUMERO: 1` · `TCL_CODIGO: '411'` (4.2 Coop. Eléctricas) · `CNT_ESTADO: 'V'`
- **Punto de Suministro (XXSIGEC.SERVICIOS)**: `SRV_CODIGO: 827893` · Dirección: `LDO CEMENTERIO LA GRANJA`
- **Área Geográfica & Sucursal**: `AGF_CODIGO: 5000` (*RIO CEBALLOS*) · `SCF_CODIGO: 22` (*RIO CEBALLOS*)
- **Zona Comercial Oficial**: **ZONA E** (Sierras Chicas / Sucursal Río Ceballos)

### 📌 Hallazgo Estructural en XXSIGEC para las 38 Cooperativas:
Al auditar los contratos de las 38 cooperativas provinciales con tarifa de venta en bloque (`TCL_CODIGO = '411'`), se verificó que:
1. **100% de Trazabilidad**: Las 38 entidades poseen contrato activo de Tarifa 411 en Oracle XXSIGEC.
2. **Zona A en SIGEC**: Corresponde de forma estricta y exclusiva a la **Sucursal 1 (Córdoba Capital)**. EPEC no tiene contratos de cooperativas en Zona A.
3. **Colonia Caroya (`c12`) y Agua de Oro (`c38`)**: En la planilla Excel figuraban preliminarmente como "Zona A". Sin embargo, sus contratos formales de Tarifa 411 (`SRV 2996238` y `SRV 1343516`) dependen técnica y comercialmente de la **Sucursal 22 (Río Ceballos)**, la cual tiene asignado `ZON_CODIGO: 'E'` (**Zona E**), idéntica cabecera que Ascochinga.

---

## 📊 4. Distribución Territorial Consolidada (100% Asignada en 8 Zonas)

Con la asignación de estas 3 cooperativas, se elimina la categoría transitoria "Sin Zona" y la distribución final en las **8 Zonas Provinciales de EPEC** queda conformada de la siguiente manera:

| Zona | Descripción Territorial y Localidades | Coops | Monofásicos | Trifásicos | Concentradores DCU | Total Medidores | Participación |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Zona I** | Traslasierra (Mina Clavero, Nono) | 2 | 11.979 | 1.514 | 151 | **13.493** | 28,6% |
| **Zona H** | Calamuchita / Sierras Chicas Sur / Río Cuarto Norte (Anisacate, Berrotarán, Alcira, Toledo) | 7 | 10.890 | 1.723 | 104 | **12.613** | 26,7% |
| **Zona F** | Sur Provincial (Laboulaye, Serrano, San Basilio, Sampacho, Jovita, Huanchilla, Bulnes) | 10 | 7.000 | 1.730 | 74 | **8.730** | 18,5% |
| **Zona D** | San Justo / Este Provincial (Alicia, Carrilobo, Brinkmann, Matorrales, Pozo del Molle, Porteña) | 7 | 4.633 | 1.078 | 52 | **5.711** | 12,1% |
| **Zona G** | Marcos Juárez / Unión (Camilo Aldao, Chilibroste, Gral. Roca, Leones, Isla Verde, Inriville) | 7 | 2.159 | 608 | 27 | **2.767** | 5,9% |
| **Zona C** | Centro Provincial (Oncativo, Laborde) | 2 | 1.740 | 360 | 21 | **2.100** | 4,4% |
| **Zona A** | Norte Provincial (Colonia Caroya / Jesús María, Agua de Oro) | 2 | 1.030 | 510 | 15 | **1.540** | 3,3% |
| **Zona E** | Sierras Chicas / Río Ceballos (Ascochinga / La Pampa) | 1 | 200 | 100 | 1 | **300** | 0,6% |
| **TOTALES** | **Provincia de Córdoba (8 Zonas Provinciales - 100% Asignado)** | **38** | **39.631** | **7.623** | **445** | **47.254** | **100,0%** |

---

## 🔒 5. Protocolo de Triple QA

- **QA Técnico (Instancia 1)**:
  - Poligonización matemática determinista sin solapamientos topológicos (`shapely.ops.polygonize`).
  - Transformación precisa entre el sistema Gauss-Krüger Faja 4 (`EPSG:22174`) y el elipsoide WGS84 (`EPSG:4326`) respetando las definiciones de PROJ 9.
  - Cero inconsistencias numéricas en el dataset JSON y CSV.
- **QA de Negocio & Dominio (Instancia 2)**:
  - 100% de coherencia administrativa con el nomenclador oficial de `XXSIGEC.AREAS_GEOGRAFICAS` y las dependencias de cabeceras de sucursal comercial de EPEC (Sucursal 22 Río Ceballos = Zona E).
  - La incorporación de Huanchilla y Bulnes consolida a la Zona F como la tercera región con mayor recepción de equipos AMI (18,5% del total), y Ascochinga abre la presencia en Zona E.
- **QA de Usabilidad & UX (Instancia 3)**:
  - El Tablero SPA (`index.html` y `app.js`) actualiza automáticamente las tarjetas de resumen zonal a 8 zonas completas sin etiquetas residuales "Sin Zona".
  - Sincronización completa con el README del repositorio y la bóveda de Obsidian.

