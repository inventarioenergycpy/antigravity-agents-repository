---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: servicios
num_rows: 1222337
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/servicios
  - documentada/negocio
aliases:
  - "RANGO_DETALLE"
---

# 📋 RANGO_DETALLE

**Prefijo `PRS_`:** Personas / clientes (PERSONAS)

**Filas estimadas:** 1,222,337

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `PRS_TIPO_DOC` | VARCHAR2 | YES |  |  |
| `PRS_DOCUMENTO` | NUMBER | YES |  | Número de documento del titular en PERSONAS (NUMBER), con PRS_TIPO_DOC ('DNI', 'LC', 'LE', 'CI'…). Distinto de PRS_CUIT (que a veces está y a veces no). Es el 'número de documento del titular' de una consulta comercial. |
| `PRS_CUIT` | NUMBER | YES |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `CNT_ESTADO` | VARCHAR2 | YES |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `SALDO_DEBE` | NUMBER | YES |  |  |
| `SALDO_HABER` | NUMBER | YES |  |  |
| `SALDO_CC_PG` | NUMBER | YES |  |  |
| `CANT_DEBE` | NUMBER | YES |  |  |
| `CANT_HABER` | NUMBER | YES |  |  |
| `CANT_CC_PG` | NUMBER | YES |  |  |
| `TFA_CODIGO` | VARCHAR2 | YES |  |  |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | YES |  |  |
| `SALDO_F_VENCIDO` | NUMBER | YES |  |  |
| `CANT_F_VENCIDO` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `MPA_TIPO_MEDIO_PAGO` → [[MEDIOS_PAGO]] _MPA_TIPO_MEDIO_PAGO es PK de MEDIOS_PAGO_
- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
