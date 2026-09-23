---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 766959430
tags:
  - sigec-explorer
  - tabla
  - custom
  - documentada/negocio
aliases:
  - "XXCO_LECTURAS_TELEMEDIDAS"
---

# 🔧 XXCO_LECTURAS_TELEMEDIDAS

> [!info] Significado de negocio
> Índices diarios de facturación de medidores inteligentes vía MDM (~817M filas). LEC_FECHA_LECTURA es DATE siempre a las 00:00:00 (un registro por día). NO contiene perfiles de 15 minutos — es el acumulado diario para facturación. Incluye marcas NSEN, CLOU, HEXIN, ITRON. Columnas: MED_NUMERO_EQUIPO, CDR_CODIGO, LEC_FECHA_LECTURA, LEC_VALOR, LTE_ORIGEN (MDM/MDC).

**Filas estimadas:** 766,959,430

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `MED_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `MED_NOMBRE` | VARCHAR2 | YES |  |
| `MED_NUMERO_EQUIPO` | NUMBER | NO | 🔑 PK |
| `CDR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `CDR_UNIDAD` | VARCHAR2 | YES |  |
| `LEC_FECHA_LECTURA` | DATE | NO | 🔑 PK |
| `LEC_FECHA_LECTURA_ANT` | DATE | YES |  |
| `LEC_VALOR_LEIDO` | NUMBER | YES |  |
| `LEC_VALOR_LEIDO_ANT` | NUMBER | YES |  |
| `LEC_FECHA_CARGA` | DATE | YES |  |
| `CRM_NUMERO` | NUMBER | NO | 🔑 PK |
| `LTE_FECHA_PROCESO` | DATE | YES |  |
| `LTE_FECHA_CARGA` | DATE | YES |  |
| `CRM_PROGRAMADO` | DATE | YES |  |
| `CRM_INICIO` | DATE | YES |  |
| `CRM_FIN` | DATE | YES |  |
| `TM_CODIGO` | VARCHAR2 | YES |  |
| `LTE_ORIGEN` | VARCHAR2 | YES |  |
