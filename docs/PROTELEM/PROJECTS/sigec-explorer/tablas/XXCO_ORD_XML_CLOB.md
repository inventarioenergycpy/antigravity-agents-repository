---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 6159
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_ORD_XML_CLOB"
---

# 🔧 XXCO_ORD_XML_CLOB

**Filas estimadas:** 6,159

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ORD_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `STE_NUMERO` | NUMBER | NO | 🔑 PK | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `OXC_TIPO_ARCHIVO` | VARCHAR2 | NO | 🔑 PK |  |
| `OXC_ARCHIVO` | VARCHAR2 | YES |  |  |
| `OXC_XML_CLOB` | CLOB | YES |  |  |
| `OXC_FECHA` | DATE | YES |  |  |
