---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 52
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "SUCURSALES"
---

# 📋 SUCURSALES

**Filas estimadas:** 52

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | NO | 🔑 PK |  |
| `SCF_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `ZON_CODIGO` | VARCHAR2 | NO | 🔗 → [[ZONAS]] |  |
| `SCF_C_POSTAL` | NUMBER | YES |  |  |
| `SCF_FAX` | VARCHAR2 | YES |  |  |
| `SCF_TELEFONO` | VARCHAR2 | YES |  |  |
| `SCF_DIRECCION` | VARCHAR2 | YES |  |  |
| `SCF_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO_DEBIAUT` | VARCHAR2 | YES |  |  |
| `SCF_NRO_CERTIFICADO` | NUMBER | YES |  |  |
| `SCF_CABECERA_ZONA` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **SCF_EN**: `ZON_CODIGO` → [[ZONAS]] (`ZON_CODIGO`)

## Tablas que referencian esta tabla

- [[AREAS_GEOGRAFICAS]] via `SCF_CODIGO`
- [[DIRECCIONES_MAIL]] via `SCF_CODIGO`
- [[IMPRESORAS]] via `SCF_CODIGO`
- [[PROCURADORES]] via `SCF_CODIGO`
- [[PROX_NROS_RECLAMO]] via `SCF_CODIGO`
- [[STOCK_EQUIPOS]] via `SCF_CODIGO`
- [[USUARIOS]] via `SCF_CODIGO`
- [[XXCO_LOTE_EQUIPO]] via `SCF_CODIGO_ASIGNACION`, `SCF_CODIGO_CREACION`
- [[XXCO_MOVIMIENTOS_EQUIPOS]] via `SCF_CODIGO_ASIGNADO`
- [[XXCO_SECTORES_EQUIPOS]] via `SCF_CODIGO_DESTINO`, `SCF_CODIGO_ORIGEN`
- [[XX_COLECTORAS]] via `SCF_CODIGO`

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
