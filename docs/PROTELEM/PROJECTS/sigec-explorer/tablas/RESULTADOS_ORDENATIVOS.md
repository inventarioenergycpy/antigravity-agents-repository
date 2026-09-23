---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1185
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "RESULTADOS_ORDENATIVOS"
---

# 📋 RESULTADOS_ORDENATIVOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 1,185

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `SEC_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `ROD_RESULTADO` | VARCHAR2 | NO | 🔑 PK |
| `SEC_CODIGO_GENERADO` | VARCHAR2 | YES |  |
| `TOR_CODIGO_GENERADO` | VARCHAR2 | YES |  |
| `ROD_DESCRIPCION` | VARCHAR2 | NO |  |
| `EVE_CODIGO_SRV` | VARCHAR2 | YES |  |
| `EVE_CODIGO_CNT` | VARCHAR2 | YES |  |
| `GCR_CODIGO` | VARCHAR2 | YES |  |
| `ROD_ORD_EJECUTADO` | VARCHAR2 | NO |  |
| `ROD_ORD_ACOMETIDA_REALIZADA` | VARCHAR2 | YES |  |
| `ROD_ORD_TAPA_REEMPLAZADA` | VARCHAR2 | YES |  |
| `ROD_ORD_CAMBIO_EQUIPO` | VARCHAR2 | YES |  |
| `ROD_TOB_CODIGO_HIGH` | VARCHAR2 | YES |  |
| `ROD_HABILITADO_AUTO_CIERRE` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[ACCIONES_ORDENATIVOS]] via `ROD_RESULTADO`, `SEC_CODIGO`, `TOR_CODIGO`
