---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: contratos
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/contratos
  - documentada/negocio
aliases:
  - "DEUDA_CONTRATOS_TMP"
---

# ⏱️ DEUDA_CONTRATOS_TMP

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SUCURSAL` | NUMBER | YES |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `SRV` | VARCHAR2 | YES |  |  |
| `CNT` | VARCHAR2 | YES |  |  |
| `CNT_ESTADO` | VARCHAR2 | YES |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `NOMBRE` | VARCHAR2 | YES |  |  |
| `SALDOI` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
