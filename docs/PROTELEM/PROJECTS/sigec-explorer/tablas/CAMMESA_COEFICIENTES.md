---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 42
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CAMMESA_COEFICIENTES"
---

# 📋 CAMMESA_COEFICIENTES

**Filas estimadas:** 42

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `GRUPO_CAMMESA` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TCL_GRUPO` | VARCHAR2 | YES |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |
| `COEF_PICO` | NUMBER | YES |  |  |
| `COEF_VALLE` | NUMBER | YES |  |  |
| `COEF_RESTO` | NUMBER | YES |  |  |
| `PERIODO_VIGENCIA` | DATE | YES |  |  |
