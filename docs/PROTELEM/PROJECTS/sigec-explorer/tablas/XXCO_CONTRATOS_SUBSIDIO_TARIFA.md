---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: documentos
num_rows: 9142447
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_CONTRATOS_SUBSIDIO_TARIFA"
---

# 🔧 XXCO_CONTRATOS_SUBSIDIO_TARIFA

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 9,142,447

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TCL_GRUPO` | VARCHAR2 | YES |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |
| `TCL_CODIGO_GRAL` | VARCHAR2 | YES |  | Código de tarifa 'general' en AUDITORIA_CAMMESA. Se une a TARIFAS.TCL_CODIGO para clasificar el consumo por sector/rubro (vía TARIFAS.TCL_GRUPO). |
| `CLA_CODIGO_GRAL` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO_GRAL` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `CST_ANIO` | NUMBER | YES |  |  |
| `CST_PERIODO` | NUMBER | YES |  |  |
| `CST_IMPORTE` | NUMBER | YES |  |  |
| `CST_IMPORTE_ACTUALIZADO` | NUMBER | YES |  |  |
| `CST_FECHA_CARGA` | DATE | YES |  |  |
| `CST_COEFICIENTE` | NUMBER | YES |  |  |
| `CST_CONSUMO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `CST_FECHA_LEC_ANT` | DATE | YES |  |  |
| `CST_FECHA_LEC` | DATE | YES |  |  |
| `CST_CANT_DIAS` | NUMBER | YES |  |  |
| `CST_IMPORTE_ACTUALIZADO_1301` | NUMBER | YES |  |  |
| `CST_COEFICIENTE_1301` | NUMBER | YES |  |  |
| `CST_FECHA_CARGA_1301` | DATE | YES |  |  |
