---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 61911
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "CONSUMOS_DIARIOS"
---

# 📋 CONSUMOS_DIARIOS

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 61,911

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `MED_NUMERO_EQUIPO` | NUMBER | YES |  |  |
| `LEC_FECHA_LECTURA` | DATE | YES |  |  |
| `CDR_UNIDAD_SIGEC` | VARCHAR2 | YES |  |  |
| `LEC_VALOR_LEIDO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `MED_NUMERO_EQUIPO` → [[XXCO_LECTURAS_TELEMEDIDAS]] _MED_NUMERO_EQUIPO es PK de XXCO_LECTURAS_TELEMEDIDAS_
- `LEC_FECHA_LECTURA` → [[XXCO_LECTURAS_TELEMEDIDAS]] _LEC_FECHA_LECTURA es PK de XXCO_LECTURAS_TELEMEDIDAS_
