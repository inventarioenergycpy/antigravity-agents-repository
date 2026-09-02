---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 9
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TARIFAS_AGRUPADAS"
---

# 📋 TARIFAS_AGRUPADAS

> [!info] Significado de negocio
> Mapa corto de rubros (9 filas): TCL_CODIGO 100→Residencial, 200→Gral. y Servicios, 300→Grandes Consumos, 400→Cooperativas, 500→Gob. y Otros Us. Esp., 600→Alumbrado Público, 700→Servicio de Agua, 800→Servicio de Peaje, 900→Contratos Especiales. Equivale a TARIFAS.TCL_GRUPO×100.

**Filas estimadas:** 9

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TCL_DESCRIPCION` | VARCHAR2 | YES |  |  |
