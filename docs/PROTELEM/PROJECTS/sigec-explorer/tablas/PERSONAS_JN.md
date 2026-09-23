---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: servicios
num_rows: 3857260
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/servicios
  - documentada/negocio
aliases:
  - "PERSONAS_JN"
---

# 📝 PERSONAS_JN

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 3,857,260

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `JN_SECUENCIA` | NUMBER | YES |  |  |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `PRS_TIPO_DOC` | VARCHAR2 | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `JN_USR_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `JN_USR_AUTORIZA` | NUMBER | YES |  |  |
| `PRS_CALLE` | VARCHAR2 | YES |  |  |
| `PRS_NRO` | VARCHAR2 | YES |  |  |
| `PRS_PISO` | VARCHAR2 | YES |  |  |
| `PRS_DEPTO` | VARCHAR2 | YES |  |  |
| `PRS_C_POSTAL` | NUMBER | YES |  |  |
| `PRS_DIRECCION` | VARCHAR2 | YES |  |  |
| `PRS_TELEFONOS` | VARCHAR2 | YES |  |  |
| `PRS_FAX` | VARCHAR2 | YES |  |  |
| `IVV_CODIGO` | NUMBER | YES |  |  |
| `GPE_GRUPO` | VARCHAR2 | YES |  |  |
| `JN_COD_MOVIM` | VARCHAR2 | YES |  |  |
| `OBSERVACION` | VARCHAR2 | YES |  |  |
| `PRS_NRO_JUBIL` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `PRS_INSCRIPCION_IB` | NUMBER | YES |  |  |
| `PRS_CONVENIO_IB` | VARCHAR2 | YES |  |  |
| `PRS_TIENE_VERAZ` | VARCHAR2 | YES |  |  |
| `USR_UNIX` | VARCHAR2 | YES |  |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |  |
| `SERVIDOR` | VARCHAR2 | YES |  |  |
| `PRS_E_MAIL` | VARCHAR2 | YES |  |  |
| `PRS_CUIT_VALIDO` | VARCHAR2 | YES |  |  |
| `PRS_FECHA_VERAZ` | DATE | YES |  |  |
| `PRS_CONC_QUIEB` | VARCHAR2 | YES |  |  |
| `PRS_FECHA_CONC_QUIEB` | DATE | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `GPE_GRUPO` → [[GRUPOS_PERSONA]] _GPE_GRUPO es PK de GRUPOS_PERSONA_
