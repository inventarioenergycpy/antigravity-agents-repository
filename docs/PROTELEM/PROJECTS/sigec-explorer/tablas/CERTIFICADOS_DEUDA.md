---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 155747
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "CERTIFICADOS_DEUDA"
---

# 📋 CERTIFICADOS_DEUDA

> [!info] Significado de negocio
> Titulo ejecutivo de deuda (155.747 filas, vivo: 24.043 en 2025). Es el INSTRUMENTO del pase a gestion judicial: de 104.681 certificados cruzables con DETALLE_SALDO, 97.543 (93,2%) tienen FECHA_PASE_GJ.

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 155,747

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `CER_NUMERO` | NUMBER | NO |  |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CER_DOC_SALDO_TOTAL` | NUMBER | NO |  |  |
| `CER_FECHA_GENERACION` | DATE | NO |  |  |
| `G_PRS_NUMERO` | NUMBER | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
