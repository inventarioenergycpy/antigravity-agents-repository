---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "CONSUMOS_ESTADISTICOS"
---

# 📋 CONSUMOS_ESTADISTICOS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `CDR_UNIDAD` | CHAR | NO | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `COE_MAXIMO` | NUMBER | YES |  |  |
| `COE_PROMEDIO` | NUMBER | YES |  |  |
| `COE_MINIMO` | NUMBER | YES |  |  |
