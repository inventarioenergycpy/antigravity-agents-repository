---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 32417
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_ARCHIVOS"
---

# 🔧 XXCO_ARCHIVOS

> [!info] Significado de negocio
> Registro de archivos procesados (32.417 filas). Es EXCLUSIVAMENTE de cobranza/medios de pago (ARC_ORIGEN: RAPIPAGO, PAGO FACIL, BANELCO, COBRO EXPRESS, DA-VISA/MASTER/NARANJA, bancos, municipios). No registra interfaces legales ni de ilicitos.

**Filas estimadas:** 32,417

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ARC_NUMERO` | NUMBER | NO | 🔑 PK |
| `ARC_NOMBRE_ARCHIVO` | VARCHAR2 | NO |  |
| `ARC_ORIGEN` | VARCHAR2 | NO |  |
| `USR_NUMERO_ALTA` | NUMBER | NO | 🔗 → [[USUARIOS]] |
| `ARC_FECHA_ALTA` | DATE | NO |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `ARC_OBSERVACIONES` | VARCHAR2 | YES |  |
| `ARC_ERROR_PROCESAMIENTO` | VARCHAR2 | YES |  |
| `ARC_NUMERO_REPROCESO` | NUMBER | YES | 🔗 → [[XXCO_ARCHIVOS]] |
| `ARC_NUMERO_PADRE` | NUMBER | YES |  |
| `ARC_TARJETA` | VARCHAR2 | YES |  |
| `ARC_METODO_PAGO` | VARCHAR2 | YES |  |
| `ARC_ESTADO` | VARCHAR2 | YES |  |
| `USR_NUMERO_PROCESO` | NUMBER | YES |  |
| `ARC_FECHA_PROCESO` | DATE | YES |  |
| `USR_NUMERO_ANULA` | NUMBER | YES |  |
| `ARC_FECHA_ANULACION` | DATE | YES |  |
| `ARP_NUMERO` | NUMBER | YES |  |

## FK declaradas → otras tablas

- **ARC_REPROCESO_FK**: `ARC_NUMERO_REPROCESO` → [[XXCO_ARCHIVOS]] (`ARC_NUMERO`)
- **USUARIO_FK**: `USR_NUMERO_ALTA` → [[USUARIOS]] (`USR_NUMERO`)

## Tablas que referencian esta tabla

- [[XXCO_ARCHIVOS]] via `ARC_NUMERO_REPROCESO`
