---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 3705
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "UNIDADES_RECAUDADORAS"
---

# 📋 UNIDADES_RECAUDADORAS

**Filas estimadas:** 3,705

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `URC_CODIGO` | NUMBER | NO | 🔑 PK |
| `URC_DESCRIPCION` | VARCHAR2 | NO |  |
| `URC_TIPO` | VARCHAR2 | NO |  |
| `URC_GRUPO` | VARCHAR2 | YES |  |
| `URC_PLAZO_PAGO` | NUMBER | YES |  |
| `URC_CODIGO_MADRE` | NUMBER | YES | 🔗 → [[UNIDADES_RECAUDADORAS]] |
| `SCF_CODIGO` | NUMBER | YES | 🔗 → [[AGENCIAS]] |
| `URC_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |
| `URC_TIPO_LOTE` | VARCHAR2 | YES |  |
| `SCF_CODIGO_CONTABLE` | NUMBER | YES |  |
| `URC_NUMERO` | NUMBER | YES |  |
| `URC_MONEDA` | VARCHAR2 | YES |  |
| `URC_NRO_CTA` | NUMBER | YES |  |
| `URC_FILIAL` | VARCHAR2 | YES |  |
| `AGE_CODIGO` | VARCHAR2 | YES | 🔗 → [[AGENCIAS]] |
| `CUENTA_BANCARIA_CE` | NUMBER | YES |  |
| `URC_CAJA_EPEC` | VARCHAR2 | YES |  |
| `URC_CODIGO_DEPOSITO` | NUMBER | YES |  |
| `URC_HORA_CORRIDA` | VARCHAR2 | YES |  |
| `URC_CUIT` | NUMBER | YES |  |
| `URC_RAZON_SOCIAL` | VARCHAR2 | YES |  |
| `URC_CLASIFICACION_ENTE` | VARCHAR2 | YES |  |
| `URC_PRESENCIAL` | VARCHAR2 | YES |  |
| `URC_MEDIO_RECAUDADOR` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **URC_DEPENDIENTE_DE**: `URC_CODIGO_MADRE` → [[UNIDADES_RECAUDADORAS]] (`URC_CODIGO`)
- **URC_POSEE**: `SCF_CODIGO`, `AGE_CODIGO` → [[AGENCIAS]] (`SCF_CODIGO`, `AGE_CODIGO`)

## Tablas que referencian esta tabla

- [[ASIENTOS_CONTABLES]] via `URC_CODIGO`
- [[DOCUMENTOS]] via `URC_CODIGO`
- [[FORMAS_PAGO]] via `URC_CODIGO`
- [[UNIDADES_RECAUDADORAS]] via `URC_CODIGO_MADRE`

## FK inferidas (alta confianza)

- `AGE_CODIGO` → [[AGENCIAS]] _AGE_CODIGO es PK de AGENCIAS_
