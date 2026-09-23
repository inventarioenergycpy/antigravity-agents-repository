---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 66
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "GRUPOS_CAMMESA"
---

# 📋 GRUPOS_CAMMESA

**Filas estimadas:** 66

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ID_GRUPO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TCL_GRUPO` | VARCHAR2 | YES |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |
| `RESTRICCION` | VARCHAR2 | YES |  |  |
| `DEMANDA_DESDE` | NUMBER | YES |  |  |
| `DEMANDA_HASTA` | NUMBER | YES |  |  |
| `CONSUMO_DESDE` | NUMBER | YES |  |  |
| `CONSUMO_HASTA` | NUMBER | YES |  |  |
| `CONS_DIARIO_DESDE` | NUMBER | YES |  |  |
| `CONS_DIARIO_HASTA` | NUMBER | YES |  |  |
| `PESO_GRUPO` | NUMBER | YES |  |  |
| `DESC_GRUPO` | VARCHAR2 | YES |  |  |
| `GC_HABILITADO` | VARCHAR2 | NO |  |  |
| `GC_DECLARA` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
