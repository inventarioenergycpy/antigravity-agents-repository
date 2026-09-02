---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: contratos
num_rows: 302880
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/contratos
  - documentada/negocio
aliases:
  - "ANEXOS_JN"
---

# 📝 ANEXOS_JN

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 302,880

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `JN_USR_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `AXO_FECHA_RESOL` | DATE | YES |  |  |
| `AXO_VENC_RESOL` | DATE | YES |  |  |
| `AXO_NUMERO_RESOL` | NUMBER | YES |  |  |
| `AXO_FECHA_CARGA_RESOL` | DATE | YES |  |  |
| `AXO_ORIGEN_RESOL` | VARCHAR2 | YES |  |  |
| `OBSERVA` | VARCHAR2 | YES |  |  |
| `CNT_CONDICION_SUBSIDIO` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
