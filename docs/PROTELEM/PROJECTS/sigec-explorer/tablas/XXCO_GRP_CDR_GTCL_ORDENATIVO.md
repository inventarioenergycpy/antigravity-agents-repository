---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 70
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_GRP_CDR_GTCL_ORDENATIVO"
---

# 🔧 XXCO_GRP_CDR_GTCL_ORDENATIVO

**Filas estimadas:** 70

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GCG_CODIGO` | VARCHAR2 | YES |  |  |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |  |
| `CDR_CODIGO` | VARCHAR2 | YES |  |  |
| `GCG_DISPLAY_COLECTOR` | VARCHAR2 | YES |  |  |
| `TCL_GRUPO` | NUMBER | YES |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TCU_ORDEN` | NUMBER | YES |  |  |
