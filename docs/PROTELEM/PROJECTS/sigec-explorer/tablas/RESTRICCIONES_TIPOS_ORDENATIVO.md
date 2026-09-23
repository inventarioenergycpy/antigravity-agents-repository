---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 110
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "RESTRICCIONES_TIPOS_ORDENATIVO"
---

# 📋 RESTRICCIONES_TIPOS_ORDENATIVO

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 110

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TOR_CODIGO_RESTRICCION` | VARCHAR2 | NO | 🔑 PK |
| `RTO_RESTRICCION` | VARCHAR2 | NO |  |
| `TOR_CODIGO_GENERAR` | VARCHAR2 | YES |  |
| `SEC_CODIGO_GENERAR` | VARCHAR2 | YES |  |
