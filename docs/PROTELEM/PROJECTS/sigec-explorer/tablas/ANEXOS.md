---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 54746873
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "ANEXOS"
---

# 📋 ANEXOS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 54,746,873

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `TEN_CODIGO` | VARCHAR2 | NO |  |  |
| `AXO_FECHA_VIGENCIA` | DATE | NO | 🔑 PK |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `CAT_CODIGO` | VARCHAR2 | NO |  |  |
| `IVV_CODIGO` | NUMBER | YES |  |  |
| `AXO_FECHA_RESOL` | DATE | YES |  |  |
| `AXO_VENC_RESOL` | DATE | YES |  |  |
| `AXO_NUMERO_RESOL` | NUMBER | YES |  |  |
| `AXO_FECHA_CARGA_RESOL` | DATE | YES |  |  |
| `AXO_ORIGEN_RESOL` | VARCHAR2 | YES |  |  |
| `CNT_CONDICION_SUBSIDIO` | VARCHAR2 | YES |  |  |
| `CNT_COEF_RECUPERO_SUBSIDIO` | NUMBER | YES |  |  |
| `CNT_CODIGO_ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `CNT_ORIGEN_SUBSIDIO` | VARCHAR2 | YES |  |  |
| `CNT_FECHA_CBIO_COND_SUB` | DATE | YES |  |  |
| `AXO_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `AXO_PORCENTAJE_TCL_REC_BON` | NUMBER | YES |  |  |
| `AXO_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
| `DOMINIO_ASOCIADO` | VARCHAR2 | YES |  |  |
