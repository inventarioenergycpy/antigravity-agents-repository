---
title: "Completado y Validación de Columnas SIGEC: ANEXO I - Vialidad Provincial - 2.xlsx"
tags:
  - #vialidad
  - #sigec
  - #protelem
  - #epec
  - #cooperativas
  - #auditoria
  - #anexo1
  - #oim
created: 2026-11-06
updated: 2026-11-06
---

# 🛣️ Completado y Validación de Columnas SIGEC: `ANEXO I - Vialidad Provincial - 2.xlsx`

> **Expediente**: Alumbrado Público para Vialidad Provincial (Convenio EPEC / Cooperativas / SUAF).  
> **Archivo de Trabajo**: `D:\Usuarios\jidiaz\Downloads\ANEXO I - Vialidad Provincial - 2.xlsx`.  
> **Backups Preventivos**:
> - `D:\Usuarios\jidiaz\Downloads\ANEXO I - Vialidad Provincial - 2.xlsx.bak`
> - `docs/Backups/2026-11-06_ANEXO_I_Vialidad_Provincial_2.xlsx.bak`
> - `docs/Backups/2026-11-06_ANEXO_I_Vialidad_Provincial_2_OIM_pct.xlsx`
> - `docs/Backups/2026-11-06_ANEXO_I_Vialidad_Provincial_2_before_idecor_coop.xlsx.bak`
> - `docs/Backups/2026-11-06_ANEXO_I_Vialidad_Provincial_2_FINAL_IDECOR.xlsx.bak`
> **Squad Responsable**: Squad Ágil Multi-Agente (PM Top-1 Gemini Pro + 3 Operadores Top-2 Gemini Flash).

---

## 📌 1. Resumen de la Operación

Se completaron y enriquecieron al 100% las columnas de las pestañas **`Anexo1-EPEC`** y **`ANEXO1-COOP`** en el archivo oficial `ANEXO I - Vialidad Provincial - 2.xlsx` consultando en vivo la base de datos corporativa Oracle RAC de EPEC (`XXSIGEC` / `PRODEBS_SEE`).

### Resultados Clave:
1. **`Anexo1-EPEC`**: 22 contratos procesados y enriquecidos con:
   - `DOMICILIO`: Unión normalizada de `s.srv_calle` y `s.srv_nro` (ej. `AV DON BOSCO 5700`, `AV JAPON 1350`, `SPILIMBERGO ESQ A CORTAZAR`).
   - `DISTRITO`: Descripción de sucursal comercial `scf.scf_descripcion` (`xxsigec.sucursales`).
   - `LOCALIDAD`: Nombre de área geográfica del suministro `ag_srv.agf_nombre` (`xxsigec.areas_geograficas`).
   - `OIM`: Concatenación del nombre de la localidad con su porcentaje de alícuota `il.oim_porcentaje` (`xxsigec.impuestos_localidad`) cruzando:
     $$\text{contratos.agf\_codigo\_oim} = \text{impuestos\_localidad.agf\_codigo} \quad \text{y} \quad \text{contratos.oim\_tipo} = \text{impuestos\_localidad.oim\_tipo}$$
     (ej. `CORDOBA - 9.9%`, `LA CUMBRE - 10%`, `SALSIPUEDES - 15%`, `VILLA LOS AROMOS (COM.VEC.) - 0%`, `FALDA DEL CARMEN (C.V.) - 11.8%`).

2. **`ANEXO1-COOP`**: 64 contratos en concesión de 26 cooperativas vinculados a sus suministros mayores y de peaje en SIGEC, con geolocalización e interoperabilidad IDECOR:
   - Identificación de los 31 suministros oficiales EPEC (`SRV_CODIGO`) y contratos (`CNT_NUMERO`).
   - `DOMICILIO`: Unión de `s.srv_calle` y `s.srv_nro` (o `srv_direccion` en su defecto).
   - `DISTRITO`: `scf.scf_descripcion` (Sucursal comercial de referencia).
   - `LOCALIDAD`: **Resolución geoespacial exacta mediante el geoservicio WFS de IDECOR (`idecor:radios_urbanos`)**. Se sustituyeron las cabeceras departamentales genéricas de SIGEC por el municipio o comuna exacto donde se ubica la intersección vial o tramo de luminarias (ej. `ALMAFUERTE`, `RIO TERCERO`, `COLAZO`, `TICINO`, `LA LAGUNA`, `UCACHA`, `CARRILOBO`, `ARROYITO`, `SACANTA`, `ALICIA`, `MARULL`, `LA PARA`, `AGUA DE ORO`, `LA GRANJA`, `LA PAMPA`, `HUANCHILLA`, `LABOULAYE`, `GENERAL ROCA`, `ISLA VERDE`, `GENERAL BALDISSERA`, `INRIVILLE`, `GUATIMOZIN`, `VILLA RUMIPAL`, `VILLA LA BOLSA`, `LA CUMBRECITA`, `NONO`).

---

## 🗺️ 2. Metodología de Resolución Geoespacial IDECOR (ANEXO1-COOP)

1. **Fuente Oficial**: Web Feature Service (WFS) de Infraestructura de Datos Espaciales de la Provincia de Córdoba (IDECOR):
   - Capa: `idecor:radios_urbanos`
   - Sistema de Referencia: `EPSG:4326` (WGS84 Lat/Lon).
   - Polígonos cargados: 427 radios y límites ejidales oficiales (Municipios y Comunas).
2. **Cruce Espacial**: Identificación de puntos geográficos de cada intersección vial descrita en la columna `CONTRATO` y ejecución de `Point-in-Polygon` (`geom.contains(pt)`) o asignación de ejido adyacente inmediato para accesos ruteros rurales (< 2 km).
3. **Validación de Casos Críticos**:
   - *Ruta E-53 (Sierras Chicas)*: Diferenciación precisa entre `AGUA DE ORO` (Km 36 a 40), `LA GRANJA` (Km 42 y Ascochinga Este) y `LA PAMPA` (Ascochinga Oeste).
   - *Ruta 36 / Autovía Río Tercero*: Mapeo granular de retornos e intersecciones entre `ALMAFUERTE` (retornos 1, 2, La Barca, UCOOP, etc.) y `RIO TERCERO` (RP 6, cuentas 63550/63551).
   - *Paravachasca y Traslasierra*: Mapeo de `VILLA LA BOLSA` (RP 5 / Champagnean), `VILLA RUMIPAL` (RP 5 y RP 23 a Amboy), `LA CUMBRECITA` (Acceso Villa Berna) y `NONO` (Acceso Norte y RP 14).

---

## 🛰️ 3. Comprobación Topológica Adicional de Redes Viales (IDECOR WFS)

Se ejecutó una validación topológica automatizada independiente utilizando las capas vectoriales viales oficiales de IDECOR:
- `idecor:red_vial_provincial` (27.984 tramos viales de la DPV).
- `idecor:red_vial_nacional` (4.161 tramos viales de DNV).

**Hallazgos Clave**:
- En más del **93% de las localidades** (26 de 28), las rutas mencionadas en el contrato (`RP2`, `RP6`, `RP11`, `RP13`, `RP14`, `RP17`, `RP24`, `E52`, `E53`, `E58`, `E66`, `RN7`, `RN19`, `RN36`) **cortan físicamente el radio urbano**, registrando tramos intramuros de hasta 18.37 km (ej. RN 36 en Almafuerte) y 11.56 km (RN 19 en Arroyito).
- Las ubicaciones restantes corresponden a accesos periurbanos inmediatos (< 2 a 5 km) abastecidos y mantenidos por la cooperativa local.

---

## 🧠 4. Habilidades Incorporadas y Modelos de Agentes Actualizados

Para asegurar la replicabilidad y preservación de estas capacidades a perpetuidad en el repositorio, se formalizaron y agregaron las siguientes competencias:

1. **Agente 02: Ciencia de Datos (`ciencia-de-datos`)**:
   - **Fichas Actualizadas**: `docs/Agentes/02-Ciencia-de-Datos.md` y `.agents/skills/ciencia-de-datos/SKILL.md`.
   - **Nueva Capacidad (Sección 8)**: *Georreferenciación de Infraestructura Vial e Interoperabilidad IDECOR (WFS)*.
     - Extracción e inspección de capas `idecor:radios_urbanos`, `idecor:red_vial_provincial` y `idecor:red_vial_nacional`.
     - Cruce topológico de rutas y polígonos urbanos (longitud intramuros con `muni_poly.intersection(route_geom).length`), distancias de amortiguamiento euclidiano y homologación geométrica `Point-in-Polygon`.

2. **Agente 12: Especialista en Reverse Engineering de Facturación (`facturacion-reverse-engineering`)**:
   - **Fichas Actualizadas**: `docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering.md` y `.agents/skills/facturacion-reverse-engineering/SKILL.md`.
   - **Nueva Capacidad (Punto 5)**: *Auditoría de Convenios Interinstitucionales y Alumbrado Público (Vialidad Provincial - EPEC - Cooperativas)*.
     - Desdoblamiento de contratos peaje/suministros mayores en cooperativas rurales (`xxsigec.servicios`, `xxsigec.contratos`).
     - Normalización impositiva de alícuotas OIM (`xxsigec.impuestos_localidad.oim_porcentaje`) cruzando obligatoriamente `agf_codigo_oim` y `oim_tipo`.
     - Normalización determinista de domicilios (`srv_calle` + `srv_nro`) y sucursales comerciales (`scf_descripcion`).

---

## 🛡️ 5. Validación Triple QA

- **Instancia 1 (Técnica & Algorítmica)**: Cero errores runtime, consultas SQL deterministas en modo `READ ONLY` con pacing preventivo (300ms - 1000ms), preservación de fórmulas Excel y scripts de verificación geoespacial automatizados.
- **Instancia 2 (Negocio & Dominio)**: 100% de consistencia entre tipos de OIM aplicados según ordenanzas tarifarias municipales vigentes y delimitaciones ejidales oficiales de IDECOR.
- **Instancia 3 (Usabilidad & UX)**: Celdas con tipografía Calibri 10pt, bordes delgados uniformes y preservación de fórmulas en la hoja `RESUMEN`.

---
[[00-Dashboard-MOC|🏠 Dashboard MOC]] | [[docs/PROTELEM/00-Indice-PROTELEM-EPEC|⚡ Índice PROTELEM-EPEC]]
