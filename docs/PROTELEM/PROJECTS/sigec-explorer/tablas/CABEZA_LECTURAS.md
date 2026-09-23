---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: lecturas
num_rows: 11845
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/lecturas
  - documentada/negocio
aliases:
  - "CABEZA_LECTURAS"
---

# 📋 CABEZA_LECTURAS

> [!info] Significado de negocio
> CORRECCIÓN (2026-08-06): NO es la cabecera histórica de lecturas por suministro y período, pese al nombre y a la PK (CLC_ANIO, CLC_PERIODO, SRV_CODIGO). Tiene solo 11.845 filas, TODAS con CLC_ANIO=1 y una por suministro: es una TABLA DE TRABAJO del proceso de lectura, no un histórico. Inútil para reconstruir los días de un período facturado — para eso usar DOCUMENTOS.DOC_FECHA_DESDE/HASTA.

**Prefijo `LCT_`:** Lecturas de medidores (LECTURAS)

**Filas estimadas:** 11,845

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CLC_ANIO` | NUMBER | NO | 🔑 PK |  |
| `CLC_PERIODO` | NUMBER | NO | 🔑 PK |  |
| `CLC_FECHA_LECTURA` | DATE | YES |  |  |
| `CLC_FECHA_LECTURA_ANTERIOR` | DATE | YES |  |  |
| `CLC_CITACION` | VARCHAR2 | YES |  |  |
| `CLC_COS_FI` | NUMBER | YES |  |  |
| `CLC_DEMANDA_EXCESO` | NUMBER | YES |  |  |
| `CLC_DEMANDA_CORREGIDA` | NUMBER | YES |  |  |
| `CLC_ESTADO` | VARCHAR2 | YES |  |  |
