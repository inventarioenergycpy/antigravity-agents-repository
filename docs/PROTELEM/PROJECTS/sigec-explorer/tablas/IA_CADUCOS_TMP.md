---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 0
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "IA_CADUCOS_TMP"
---

# ⏱️ IA_CADUCOS_TMP

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 0

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `NRO_ORDEN` | NUMBER | YES |  |  |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `NRO_ORDEN_A_VERIF` | NUMBER | YES |  |  |
| `IAC_SALDO_DEBE` | NUMBER | YES |  |  |
| `IAC_SALDO_HABER` | NUMBER | YES |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `ESTADO` | VARCHAR2 | YES |  |  |
| `FECHA_DESDE` | DATE | YES |  |  |
| `FECHA_HASTA` | DATE | YES |  |  |
| `FECHA_DESDE_CC_PG` | DATE | YES |  |  |

## FK inferidas (alta confianza)

- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
