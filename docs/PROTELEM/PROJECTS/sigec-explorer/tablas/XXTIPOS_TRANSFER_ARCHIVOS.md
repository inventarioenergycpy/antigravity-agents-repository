---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 160
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "XXTIPOS_TRANSFER_ARCHIVOS"
---

# 📋 XXTIPOS_TRANSFER_ARCHIVOS

> [!info] Significado de negocio
> Registro de las interfaces de archivo de SIGEC (160 filas): TTA_NOMBRE, TTA_DESCRIPCION, path origen/destino, SER_NOMBRE_ORIGEN/DESTINO -> XXSERVIDORES, TCA_CODIGO -> XXTIPOS_CARGA_ARCHIVOS (loader SQL*Loader), TTA_FECHA_BAJA. Es el INVENTARIO DE FRONTERAS de SIGEC. Baja masiva en jul-2019 (migracion a EBS12). Servidores: Ebs12-prod-n1 (concurrentes, primario), srv3594, vmprodcon1, vdebitos.

**Filas estimadas:** 160

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TTA_NOMBRE` | VARCHAR2 | NO | 🔑 PK |
| `TTA_DESCRIPCION` | VARCHAR2 | YES |  |
| `TTA_PATH_ORIGEN` | VARCHAR2 | YES |  |
| `TTA_PATH_DESTINO` | VARCHAR2 | YES |  |
| `TTA_OBSERVACION` | VARCHAR2 | YES |  |
| `SER_NOMBRE_ORIGEN` | VARCHAR2 | YES | 🔗 → [[XXSERVIDORES]] |
| `SER_NOMBRE_DESTINO` | VARCHAR2 | YES | 🔗 → [[XXSERVIDORES]] |
| `TCA_CODIGO` | VARCHAR2 | YES | 🔗 → [[XXTIPOS_CARGA_ARCHIVOS]] |
| `TTA_FECHA_BAJA` | DATE | YES |  |

## FK declaradas → otras tablas

- **TTA_FK_SER_DEST**: `SER_NOMBRE_DESTINO` → [[XXSERVIDORES]] (`SER_NOMBRE`)
- **TTA_FK_SER_ORIG**: `SER_NOMBRE_ORIGEN` → [[XXSERVIDORES]] (`SER_NOMBRE`)
- **TTA_FK_TCA_LOADER**: `TCA_CODIGO` → [[XXTIPOS_CARGA_ARCHIVOS]] (`TCA_CODIGO`)
