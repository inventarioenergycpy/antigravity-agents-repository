---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 889
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "CONTRATOS_CHQ_RECH"
---

# 📋 CONTRATOS_CHQ_RECH

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 889

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SESION` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `IMPORTE` | NUMBER | YES |  |  |
| `DOC_NUMERO_INTIMA` | NUMBER | YES |  |  |
| `DOC_TIPO_INTIMA` | VARCHAR2 | YES |  |  |
