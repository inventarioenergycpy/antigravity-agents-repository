---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 5023880
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "OIM_COBRADO"
---

# 📋 OIM_COBRADO

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 5,023,880

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `ANIO_COBRO` | NUMBER | YES |  |  |
| `MES_COBRO` | NUMBER | YES |  |  |
| `AGF_CODIGO_OIM` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `OIM_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `ITM_IMPORTE` | NUMBER | YES |  |  |
| `DOC_IMPORTE_BASICO` | NUMBER | YES |  | NO USAR como neto de la factura: coincide con DOC_IMPORTE_GRAVADO en solo el 70,6% y es MENOR en el 28,2% (muestra 322.120 docs de 2025). Poblada al 100% pero con semántica distinta al neto gravado. Para el neto usar DOC_IMPORTE_GRAVADO. |
| `DOC_IMPORTE_ORIGINAL` | NUMBER | YES |  |  |
| `DOC_PERCEPCION` | VARCHAR2 | YES |  | ES UN FLAG 'S'/NULL, NO UN IMPORTE, pese al nombre. 'S' en 13.657.099 de 14,09M facturas 2025. Sumarlo o compararlo como número tira ORA-01722 (invalid number). |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `ANIO_COBRO_2` | NUMBER | YES |  |  |
| `MES_COBRO_2` | NUMBER | YES |  |  |
