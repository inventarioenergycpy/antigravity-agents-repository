---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 436267
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "GARANTES"
---

# 📋 GARANTES

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 436,267

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GAR_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `SRV_CODIGO_GARANTIZADO` | NUMBER | NO |  |  |
| `CNT_NUMERO_GARANTIZADO` | NUMBER | NO |  |  |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `GAR_NUMERO_REFINAN` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `GAR_FECHA_CARGA` | DATE | YES |  |  |
| `PRS_NUMERO_GARANTIZADO` | NUMBER | YES |  |  |
| `GAR_FECHA_FIN` | DATE | YES |  |  |
| `GAR_SC_FECHA_INICIO` | DATE | YES |  |  |
| `GAR_SEGURO_CAUCION` | VARCHAR2 | YES |  |  |
| `GAR_SC_POLIZA` | VARCHAR2 | YES |  |  |
| `GAR_SC_IMPORTE` | NUMBER | YES |  |  |
| `GAR_SC_FECHA_FIN` | DATE | YES |  |  |
| `GAR_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
