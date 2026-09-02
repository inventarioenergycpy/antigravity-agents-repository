---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: equipos
num_rows: 231880
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/equipos
  - documentada/negocio
aliases:
  - "XXXCO_LAST_TELEMEDICIION"
---

# 📋 XXXCO_LAST_TELEMEDICIION

**Prefijo `STE_`:** Stock de equipos — atributos del medidor físico (STOCK_EQUIPOS)

**Filas estimadas:** 231,880

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `STE_NUMERO` | NUMBER | NO |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `STE_MARCA` | VARCHAR2 | YES |  |  |
| `ULTIMA_LECTURA` | DATE | YES |  |  |
