---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 2104237
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "PERSONAS"
---

# 📋 PERSONAS

> [!info] Significado de negocio
> Clientes y personas físicas/jurídicas (~2,1M filas). PK PRS_NUMERO. Identidad del titular: PRS_RAZON_SOCIAL (nombre), PRS_TIPO_DOC + PRS_DOCUMENTO (DNI), PRS_CUIT. Se llega desde CONTRATOS.PRS_NUMERO.

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 2,104,237

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_NUMERO` | NUMBER | NO | 🔑 PK | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | NO |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `PRS_TIPO_DOC` | VARCHAR2 | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `PRS_DIRECCION` | VARCHAR2 | YES |  |  |
| `PRS_NRO` | VARCHAR2 | YES |  |  |
| `PRS_DEPTO` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `PRS_CATEGORIA` | VARCHAR2 | YES |  |  |
| `PRS_CALLE` | VARCHAR2 | YES |  |  |
| `PRS_C_POSTAL` | NUMBER | YES |  |  |
| `PRS_TELEFONOS` | VARCHAR2 | YES |  |  |
| `PRS_FAX` | VARCHAR2 | YES |  |  |
| `PRS_ESTADO` | VARCHAR2 | YES |  |  |
| `PRS_PISO` | VARCHAR2 | YES |  |  |
| `PRS_NUMERO_REGISTRO` | NUMBER | YES |  |  |
| `IMP_CODIGO` | NUMBER | YES |  |  |
| `IVV_CODIGO` | NUMBER | YES |  |  |
| `PRS_DATO_IMPOSITIVO` | VARCHAR2 | YES |  |  |
| `PRS_FORMULARIO_IMPOSITIVO` | VARCHAR2 | YES |  |  |
| `PRS_SUB_TYPE` | VARCHAR2 | YES |  |  |
| `GPE_GRUPO` | VARCHAR2 | YES |  |  |
| `PRS_FECHA_CUIT` | DATE | YES |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `PRS_E_MAIL` | VARCHAR2 | YES |  |  |
| `PRS_NRO_JUBIL` | VARCHAR2 | YES |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES | 🔗 → [[ENTES]] | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `PRS_NRO_SOBRE` | NUMBER | YES |  |  |
| `PRS_TEL_CELULAR` | VARCHAR2 | YES |  |  |
| `PRS_INSCRIPCION_IB` | NUMBER | YES |  |  |
| `PRS_CONVENIO_IB` | VARCHAR2 | YES |  |  |
| `PRS_PLAN_PAGO` | VARCHAR2 | YES |  |  |
| `USU_ID` | NUMBER | YES |  |  |
| `PRS_TORRE` | VARCHAR2 | YES |  |  |
| `PRS_LOCAL` | VARCHAR2 | YES |  |  |
| `PRS_OFICINA` | VARCHAR2 | YES |  |  |
| `GAR_SEG_CAUCION` | VARCHAR2 | YES |  |  |
| `GAR_FECHA_INICIO` | DATE | YES |  |  |
| `GAR_FECHA_VIGENCIA` | DATE | YES |  |  |
| `PRS_IMPRESION_BRAILLE` | VARCHAR2 | YES |  |  |
| `PRS_TIENE_VERAZ` | VARCHAR2 | YES |  |  |
| `PRS_CUIT_VALIDO` | VARCHAR2 | YES |  |  |
| `PRS_FECHA_VERAZ` | DATE | YES |  |  |
| `PRS_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
| `PRS_CONC_QUIEB` | VARCHAR2 | YES |  |  |
| `PRS_FECHA_CONC_QUIEB` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **PRS_MIN_FK**: `MIN_CODIGO` → [[ENTES]] (`MIN_CODIGO`)

## Tablas que referencian esta tabla

- [[CONTRATOS]] via `PRS_NUMERO`
- [[DATOS_RESULTADOS]] via `PRS_NUMERO`
- [[DOCUMENTOS]] via `PRS_NUMERO`
- [[INTERFAZ_MED_ORD]] via `PRS_NUMERO`
- [[LIQUIDACIONES_ILICITOS]] via `PRS_NUMERO`
- [[ORDENATIVOS]] via `PRS_NUMERO`
- [[RECLAMOS]] via `PRS_NUMERO_DENUNCIADO`
- [[XX_CALIFICACIONES]] via `PRS_NUMERO`
- [[XX_CONTRIBUCIONES_PROYECTOS]] via `PRS_NUMERO`

## FK inferidas (alta confianza)

- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
- `GPE_GRUPO` → [[GRUPOS_PERSONA]] _GPE_GRUPO es PK de GRUPOS_PERSONA_
