---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: equipos
num_rows: 350030
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/equipos
  - documentada/negocio
aliases:
  - "XXCO_ULTIMA_TELEMEDICION_VM"
---

# 🔧 XXCO_ULTIMA_TELEMEDICION_VM

> [!info] Significado de negocio
> Vista del último estado de telelectura por medidor. Columnas: STE_NUMERO, STE_MARCA, LEC_FECHA_ULTIMA_LECTURA, ULTIMA_ACTUALIZACION. Útil para diagnosticar qué medidores están activos vs. con brecha de comunicación.

**Prefijo `STE_`:** Stock de equipos — atributos del medidor físico (STOCK_EQUIPOS)

**Filas estimadas:** 350,030

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `STE_NUMERO` | NUMBER | NO |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `STE_MARCA` | VARCHAR2 | YES |  |  |
| `LEC_FECHA_ULTIMA_LECTURA` | DATE | NO |  |  |
| `ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
