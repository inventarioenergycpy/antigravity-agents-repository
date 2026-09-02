---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1021
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "FACTURADO_GRUPO_TARIFA_EDI"
---

# 📋 FACTURADO_GRUPO_TARIFA_EDI

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 1,021

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ANIO` | NUMBER | NO |  |  |
| `PER` | NUMBER | NO |  |  |
| `GRF` | VARCHAR2 | NO |  |  |
| `IMP_FACT` | NUMBER | YES |  |  |
| `CANT_FACT` | NUMBER | YES |  |  |
| `IMP_SINREC_COB` | NUMBER | YES |  |  |
| `CANT_SINREC_COB` | NUMBER | YES |  |  |
| `IMP_RECA_COB` | NUMBER | YES |  |  |
| `CANT_RECA_COB` | NUMBER | YES |  |  |
| `IMP_RECB_COB` | NUMBER | YES |  |  |
| `CANT_RECB_COB` | NUMBER | YES |  |  |
| `IMP_RECB_15_COB` | NUMBER | YES |  |  |
| `CANT_RECB_15_COB` | NUMBER | YES |  |  |
| `IMP_RECB_30_COB` | NUMBER | YES |  |  |
| `CANT_RECB_30_COB` | NUMBER | YES |  |  |
| `IMP_RECB_60_COB` | NUMBER | YES |  |  |
| `CANT_RECB_60_COB` | NUMBER | YES |  |  |
| `IMP_RECB_M60_COB` | NUMBER | YES |  |  |
| `CANT_RECB_M60_COB` | NUMBER | YES |  |  |
| `DOC_NUMERO_DESDE` | NUMBER | YES |  |  |
| `DOC_NUMERO_HASTA` | NUMBER | YES |  |  |
| `FAC_FECHA_COBRO_ULTIMA` | DATE | YES |  |  |
| `TFA_CODIGO` | VARCHAR2 | YES |  |  |
| `ZON_CODIGO` | VARCHAR2 | YES |  |  |
| `TCL_GRUPO` | VARCHAR2 | YES |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |
| `EDI_NUMERO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
