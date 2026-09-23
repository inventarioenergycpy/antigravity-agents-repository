---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 97755
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "NOTIFICACIONES"
---

# 📋 NOTIFICACIONES

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 97,755

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_ESTADO` | VARCHAR2 | YES |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `SALDO_ACTUAL` | NUMBER | YES |  |  |
| `FECHA_CALCULO` | DATE | YES |  |  |
| `ENVIADO` | VARCHAR2 | YES |  |  |
