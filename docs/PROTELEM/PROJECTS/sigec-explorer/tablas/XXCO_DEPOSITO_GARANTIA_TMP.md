---
tipo: tabla
categoria: temp
owner: XXSIGEC
tags:
  - sigec-explorer
  - tabla
  - temp
  - documentada/negocio
aliases:
  - "XXCO_DEPOSITO_GARANTIA_TMP"
---

# ⏱️ XXCO_DEPOSITO_GARANTIA_TMP

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `DGT_FECHA_EMISION` | DATE | YES |  |  |
| `DGT_IMPORTE_DEPOSITO` | NUMBER | YES |  |  |
| `DGT_PENULTIMO_IMP_FACT` | NUMBER | YES |  |  |
| `DGT_ULTIMO_IMP_FACT` | NUMBER | YES |  |  |
