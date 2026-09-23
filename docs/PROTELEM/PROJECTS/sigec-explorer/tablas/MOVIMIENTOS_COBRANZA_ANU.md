---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: cobranza
num_rows: 22165
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/cobranza
  - documentada/negocio
aliases:
  - "MOVIMIENTOS_COBRANZA_ANU"
---

# 📋 MOVIMIENTOS_COBRANZA_ANU

**Prefijo `MOV_`:** Movimientos de cobranza (MOVIMIENTOS_COBRANZA)

**Filas estimadas:** 22,165

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MOV_NUMERO` | NUMBER | NO |  |  |
| `CPR_NUMERO` | NUMBER | NO |  |  |
| `URC_CODIGO` | NUMBER | NO |  |  |
| `MOV_TRANSACCION` | NUMBER | NO |  |  |
| `MOV_FECHA` | DATE | NO |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `MOV_IMPORTE` | NUMBER | NO |  |  |
| `MOV_ERROR` | VARCHAR2 | YES |  |  |
| `MOV_PLAN` | NUMBER | YES |  |  |
| `MOV_ZONA` | NUMBER | YES |  |  |
| `MOV_LOCALIDAD` | NUMBER | YES |  |  |
| `MOV_RUTA` | NUMBER | YES |  |  |
| `MOV_SUMINISTRO` | NUMBER | YES |  |  |
| `MOV_SECUENCIA` | NUMBER | YES |  |  |
| `MOV_ANIO` | NUMBER | YES |  |  |
| `MOV_PERIODO` | NUMBER | YES |  |  |
| `MOV_FECHA_ANTERIOR` | DATE | YES |  |  |
| `URC_CODIGO_ANTERIOR` | NUMBER | YES |  |  |
| `MOV_CPR_ANTERIOR` | NUMBER | YES |  |  |
| `MOV_WARN` | VARCHAR2 | YES |  |  |
| `MOV_DIFERENCIA` | NUMBER | YES |  |  |
| `MOV_NUMERO_CUENTA` | VARCHAR2 | YES |  |  |
| `MOV_TIPO_MEDIO_PAGO` | VARCHAR2 | YES |  |  |
