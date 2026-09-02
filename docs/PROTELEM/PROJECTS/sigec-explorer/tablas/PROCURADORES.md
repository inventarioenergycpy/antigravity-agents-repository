---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 10
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "PROCURADORES"
---

# 📋 PROCURADORES

> [!info] Significado de negocio
> Abogados externos de cobro judicial (10 filas, todos PRO_ESTADO='A', sucursal 1 / Cordoba capital). Cabeza del modulo judicial de SIGEC, que es un PILOTO DE 1999 NUNCA USADO: ASIGNACIONES 412 filas todas del 1999-08-30 al procurador 1; ACCIONES 2 filas (sep-1999); MOVIMIENTOS_MONETARIOS, ACCIONES_PARAMETROS y CONCURSOS_QUIEBRAS en CERO. ETAPAS = 1 EXTRAJUDICIAL, 2 JUDICIAL. OJO: PRO_CONTRASEA / PRO_USUARIO son credenciales.

**Filas estimadas:** 10

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRO_ID` | NUMBER | NO | 🔑 PK |  |
| `AGF_CODIGO` | NUMBER | NO | 🔗 → [[AREAS_GEOGRAFICAS]] | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `SCF_CODIGO` | NUMBER | NO | 🔗 → [[SUCURSALES]] |  |
| `PRO_NOMBRE` | VARCHAR2 | NO |  |  |
| `PRO_CUIT` | NUMBER | NO |  |  |
| `PRO_CALLE` | VARCHAR2 | NO |  |  |
| `PRO_NUMERO` | VARCHAR2 | NO |  |  |
| `PRO_ESTADO` | VARCHAR2 | NO |  |  |
| `PRO_PISO` | VARCHAR2 | YES |  |  |
| `PRO_DEPTO` | VARCHAR2 | YES |  |  |
| `PRO_MAIL` | VARCHAR2 | YES |  |  |
| `PRO_TELEFONOS` | VARCHAR2 | YES |  |  |
| `PRO_FAX` | VARCHAR2 | YES |  |  |
| `PRO_USUARIO` | VARCHAR2 | YES |  |  |
| `PRO_CONTRASEA` | VARCHAR2 | YES |  |  |

## FK declaradas → otras tablas

- **PRO_AGF_FK**: `AGF_CODIGO` → [[AREAS_GEOGRAFICAS]] (`AGF_CODIGO`)
- **PRO_SCF_FK**: `SCF_CODIGO` → [[SUCURSALES]] (`SCF_CODIGO`)

## Tablas que referencian esta tabla

- [[ACCIONES]] via `PRO_ID`
- [[ASIGNACIONES]] via `PRO_ID`
- [[MOVIMIENTOS_MONETARIOS]] via `PRO_ID`
