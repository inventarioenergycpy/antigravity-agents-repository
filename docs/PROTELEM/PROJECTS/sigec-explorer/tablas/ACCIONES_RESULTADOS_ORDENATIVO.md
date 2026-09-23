---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1502
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
aliases:
  - "ACCIONES_RESULTADOS_ORDENATIVO"
---

# 📋 ACCIONES_RESULTADOS_ORDENATIVO

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 1,502

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `SEC_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `ROD_RESULTADO` | VARCHAR2 | NO | 🔑 PK |
| `ARO_ORDEN` | NUMBER | NO | 🔑 PK |
| `ARO_TIPO_ACCION` | VARCHAR2 | NO |  |
| `ARO_ACCION` | VARCHAR2 | NO |  |
| `ARO_PARAMETROS` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[ARO_PARAM_ADICIONALES]] via `ARO_ORDEN`, `ROD_RESULTADO`, `SEC_CODIGO`, `TOR_CODIGO`
