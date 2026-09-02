---
tipo: tabla
categoria: journal
owner: XXSIGEC
num_rows: 74250
tags:
  - sigec-explorer
  - tabla
  - journal
  - documentada/negocio
aliases:
  - "EDIFICIOS_JN"
---

# 📝 EDIFICIOS_JN

**Filas estimadas:** 74,250

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `JN_SECUENCIA_EDI` | NUMBER | YES |  |  |
| `EDI_NUMERO` | NUMBER | YES |  |  |
| `EDI_FECHA_CONEX` | DATE | YES |  |  |
| `EDI_FECHA_DESPACHO` | DATE | YES |  |  |
| `EDI_NOMBRE` | VARCHAR2 | YES |  |  |
| `EDI_CALLE` | VARCHAR2 | YES |  |  |
| `EDI_NRO` | NUMBER | YES |  |  |
| `EDI_DIRECCION` | VARCHAR2 | YES |  |  |
| `JN_USR_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `JN_OBSERVACION` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `EDI_FECHA_ALTA` | DATE | YES |  |  |
| `EDI_FECHA_CONEXION` | DATE | YES |  |  |
| `EDI_CANT_TORRES` | NUMBER | YES |  |  |
| `EDI_CANT_PISOS` | NUMBER | YES |  |  |
| `EDI_CANT_DEPTOS` | NUMBER | YES |  |  |
| `EDI_CANT_OFICINAS` | NUMBER | YES |  |  |
| `EDI_CANT_LOCALES` | NUMBER | YES |  |  |
| `EDI_CANT_SRV_GENERALES` | NUMBER | YES |  |  |
| `EDI_SUBESTACIONES` | VARCHAR2 | YES |  |  |
| `EDI_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `EDI_CORR_PCP` | VARCHAR2 | YES |  |  |
| `EDI_PAGO_PCP` | VARCHAR2 | YES |  |  |
| `EDI_CORR_PCT` | VARCHAR2 | YES |  |  |
| `EDI_PAGO_PCT` | VARCHAR2 | YES |  |  |
| `EDI_OBSERVACIONES_TEC` | VARCHAR2 | YES |  |  |
| `EDI_DOCUMENTID_THUBAN` | VARCHAR2 | YES |  |  |
| `EDI_EXPTE_SUME` | VARCHAR2 | YES |  |  |
| `EDI_TELEMEDIBLE` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
