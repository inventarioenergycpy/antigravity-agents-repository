---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: equipos
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/equipos
  - documentada/negocio
aliases:
  - "EXT_BAJA_MED"
---

# 📋 EXT_BAJA_MED

**Prefijo `STE_`:** Stock de equipos — atributos del medidor físico (STOCK_EQUIPOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
