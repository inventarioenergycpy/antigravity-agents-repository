---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 870733
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_SUBSIDIOS_CONTRATO"
---

# 🔧 XXCO_SUBSIDIOS_CONTRATO

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 870,733

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ID_USUAR` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `IMPORTE` | NUMBER | YES |  |  |
