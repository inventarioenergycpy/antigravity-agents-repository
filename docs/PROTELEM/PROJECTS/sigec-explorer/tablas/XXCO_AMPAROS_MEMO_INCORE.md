---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: servicios
num_rows: 772
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_AMPAROS_MEMO_INCORE"
---

# 🔧 XXCO_AMPAROS_MEMO_INCORE

> [!info] Significado de negocio
> Contratos con amparo judicial que el proceso INCORE no puede cortar (772 filas). CONGELADA: todas con FECHA_TOPE = 2019-09-06, cero vigentes hoy. Fue un memo puntual, no un proceso vivo.

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 772

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `FECHA_TOPE` | DATE | YES |  |  |
