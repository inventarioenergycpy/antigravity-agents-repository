---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 1210710
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "ITEMS_LIQUIDACIONES"
---

# 📋 ITEMS_LIQUIDACIONES

**Filas estimadas:** 1,210,710

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `LIQ_NUMERO` | NUMBER | YES | 🔗 → [[LIQUIDACIONES_ILICITOS]] |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |  |
| `ITM_CANTIDAD` | NUMBER | YES |  |  |
| `ITM_PRECIO_UNIT` | NUMBER | YES |  |  |
| `ITM_IMPORTE` | NUMBER | YES |  |  |
| `TCL_GRUPO` | VARCHAR2 | YES |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |

## FK declaradas → otras tablas

- **ITL_LIQ_FK**: `LIQ_NUMERO` → [[LIQUIDACIONES_ILICITOS]] (`LIQ_NUMERO`)

## FK inferidas (alta confianza)

- `LIQ_NUMERO` → [[LIQUIDACIONES_ILICITOS]] _LIQ_NUMERO es PK de LIQUIDACIONES_ILICITOS_
