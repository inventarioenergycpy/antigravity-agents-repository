---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: servicios
num_rows: 11554047
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/servicios
  - documentada/negocio
aliases:
  - "SERVICIOS_JN"
---

# 📝 SERVICIOS_JN

> [!info] Significado de negocio
> Journal de cambios de SERVICIOS. SÍ incluye AGF_CODIGO (sirve para detectar re-zonificaciones de localidad) además de dirección, ruta, GRL, etc. Verificado: la re-zonificación de/hacia Córdoba (AGF 1000) es marginal (~6M kWh/año, 0,2% del total de la ciudad). No existe columna 'datos_adicionales_domicilio' en SERVICIOS.

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

**Filas estimadas:** 11,554,047

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `JN_SECUENCIA_SRV` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `RTA_CODIGO` | NUMBER | YES |  |  |
| `SRV_ORDEN_LECTURA` | NUMBER | YES |  |  |
| `SRV_ORDEN_LECTURA_ANTERIOR` | NUMBER | YES |  |  |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `SRV_CALLE` | VARCHAR2 | YES |  |  |
| `SRV_NRO` | NUMBER | YES |  |  |
| `SRV_PISO` | VARCHAR2 | YES |  |  |
| `SRV_DEPTO` | VARCHAR2 | YES |  |  |
| `SRV_DIRECCION` | VARCHAR2 | YES |  |  |
| `OBSERVACION` | VARCHAR2 | YES |  |  |
| `RTL_CODIGO` | NUMBER | YES |  |  |
| `EDI_NUMERO` | NUMBER | YES |  |  |
| `SRV_DISTRITO_CATA` | NUMBER | YES |  |  |
| `SRV_ZONA_CATA` | NUMBER | YES |  |  |
| `SRV_MANZANA_CATA` | NUMBER | YES |  |  |
| `SRV_LOTE_CATA` | NUMBER | YES |  |  |
| `SRV_PH_CATA` | NUMBER | YES |  |  |
| `GSE_GRUPO` | VARCHAR2 | YES |  |  |
| `BAR_CODIGO` | VARCHAR2 | YES |  |  |
| `USR_UNIX` | VARCHAR2 | YES |  |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |  |
| `SERVIDOR` | VARCHAR2 | YES |  |  |
| `SRV_TELEMEDIBLE` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `BAR_CODIGO` → [[XXCO_BARRIOS]] _BAR_CODIGO es PK de XXCO_BARRIOS_
- `GSE_GRUPO` → [[GRUPOS_SERVICIO]] _GSE_GRUPO es PK de GRUPOS_SERVICIO_
