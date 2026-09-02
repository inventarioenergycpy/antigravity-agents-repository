---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 76
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "CAMMESA_RECARGOS"
---

# 📋 CAMMESA_RECARGOS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

> Tabla creada para responder al requerimiento 14364

**Filas estimadas:** 76

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `AGENTE` | VARCHAR2 | YES |  |  |
| `GUDI` | VARCHAR2 | YES |  |  |
| `RECARGO_IMPORTE` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
