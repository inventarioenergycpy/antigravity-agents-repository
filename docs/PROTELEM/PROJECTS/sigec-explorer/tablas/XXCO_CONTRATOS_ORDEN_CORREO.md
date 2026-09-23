---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 489290
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_CONTRATOS_ORDEN_CORREO"
---

# 🔧 XXCO_CONTRATOS_ORDEN_CORREO

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 489,290

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | VARCHAR2 | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | VARCHAR2 | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SUCURSAL` | VARCHAR2 | YES |  |  |
| `ZONA` | VARCHAR2 | YES |  |  |
| `RECOLECCION` | VARCHAR2 | YES |  |  |
| `PARADA` | VARCHAR2 | YES |  |  |
| `SRV_CNT` | VARCHAR2 | YES |  |  |
