---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: contratos
num_rows: 22250
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/contratos
  - documentada/negocio
aliases:
  - "XXCO_DEPOSITOS_GARANTIA_VIG"
---

# 🔧 XXCO_DEPOSITOS_GARANTIA_VIG

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 22,250

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TFA_CODIGO` | VARCHAR2 | NO |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `IMPORTE_DEPOSITO` | NUMBER | YES |  |  |
| `ANIO_MAYOR` | NUMBER | YES |  |  |
| `MES_MAYOR` | NUMBER | YES |  |  |
| `IMPORTE_MAYOR` | NUMBER | YES |  |  |
| `ANIO_SIGUIENTE` | NUMBER | YES |  |  |
| `MES_SIGUIENTE` | NUMBER | YES |  |  |
| `IMPORTE_SIGUIENTE` | NUMBER | YES |  |  |
| `IMPORTE_GAR_VENCIDO` | NUMBER | YES |  |  |
| `IMPORTE_GAR_NO_VENCIDO` | NUMBER | YES |  |  |
| `CNT_FECHA_INICIO` | DATE | YES |  |  |
