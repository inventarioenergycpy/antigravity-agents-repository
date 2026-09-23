---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: contratos
num_rows: 743
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/contratos
  - documentada/negocio
aliases:
  - "XXCO_TMP_MED_DUPLICADOS"
---

# 🔧 XXCO_TMP_MED_DUPLICADOS

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 743

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `STE_NUMERO` | NUMBER | YES |  | Número de medidor (identificador del equipo físico). Es LA clave de medidor del esquema: aparece en 29 tablas y es PK de STOCK_EQUIPOS junto con STE_TIPO. |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
