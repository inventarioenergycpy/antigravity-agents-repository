---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 17856
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "CONSUMOS_DIARIOS_2"
---

# 📋 CONSUMOS_DIARIOS_2

**Filas estimadas:** 17,856

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `MED_NUMERO_EQUIPO` | NUMBER | YES |  |  |
| `LEC_FECHA_LECTURA` | DATE | YES |  |  |
| `LEC_VALOR_LEIDO` | NUMBER | YES |  |  |
| `LEC_FECHA_LECTURA_ANT` | DATE | YES |  |  |
| `LEC_VALOR_LEIDO_ANT` | NUMBER | YES |  |  |
| `CONSUMO` | NUMBER | YES |  |  |
| `DIAS` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `MED_NUMERO_EQUIPO` → [[XXCO_LECTURAS_TELEMEDIDAS]] _MED_NUMERO_EQUIPO es PK de XXCO_LECTURAS_TELEMEDIDAS_
- `LEC_FECHA_LECTURA` → [[XXCO_LECTURAS_TELEMEDIDAS]] _LEC_FECHA_LECTURA es PK de XXCO_LECTURAS_TELEMEDIDAS_
