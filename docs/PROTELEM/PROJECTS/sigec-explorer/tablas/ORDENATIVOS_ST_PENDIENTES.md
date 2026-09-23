---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 486
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "ORDENATIVOS_ST_PENDIENTES"
---

# 📋 ORDENATIVOS_ST_PENDIENTES

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 486

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ORD_NUMERO` | NUMBER | NO |  |  |
| `ORD_FECHA_GENERACION` | DATE | NO |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | NO |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
