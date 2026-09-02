---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 238
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "SNAP$_SALDOS_ENTE_VENC"
---

# 📋 SNAP$_SALDOS_ENTE_VENC

> snapshot table for snapshot ALAMO.SALDOS_ENTE_VENC

**Filas estimadas:** 238

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `SALDO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
