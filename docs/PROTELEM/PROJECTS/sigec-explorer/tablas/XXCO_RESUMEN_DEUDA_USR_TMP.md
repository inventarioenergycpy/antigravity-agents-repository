---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
num_rows: 4
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_RESUMEN_DEUDA_USR_TMP"
---

# ⏱️ XXCO_RESUMEN_DEUDA_USR_TMP

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 4

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `PRS_RAZON_SOCIAL` | VARCHAR2 | NO |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `TMI_CODIGO` | VARCHAR2 | YES |  | Tipo de ente (PK de TIPOS_ENTE, en ENTES): 1 Nacional, 2 Provincial, 3 Municipal, 4 Cooperativas, 5 Particulares, 6 Prov. No Autárq., 7 EPEC, 8 Barrios. Se guarda como VARCHAR ('1'...'8'). |
| `MIN_CODIGO` | VARCHAR2 | NO |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `MIN_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `CANT_DOC` | NUMBER | YES |  |  |
| `DEUDA` | NUMBER | YES |  |  |
| `DOC_SALDO_ACTUALIZADO` | NUMBER | YES |  |  |
| `DOC_SALDO_ACTUALIZADO_S_I` | NUMBER | YES |  |  |
| `DOC_INTERESES` | NUMBER | YES |  |  |
| `DOC_PUNIT_INTERESES` | NUMBER | YES |  |  |
| `DOC_FECHA_VENC_MIN` | DATE | YES |  |  |
| `DOC_FECHA_VENC_MAX` | DATE | YES |  |  |
| `DOC_SALDO_NO_VENC` | NUMBER | YES |  |  |
| `DOC_SALDO_VENC` | NUMBER | YES |  |  |
| `GESTION_JUDICIAL` | NUMBER | YES |  |  |
| `TIENE_GARANTE` | CHAR | YES |  |  |
| `RC_CREDITOS` | NUMBER | YES |  |  |
| `DEP_EN_GARANTIA` | NUMBER | YES |  |  |
| `FACTURACION_ULTIMOS_3_MESES` | NUMBER | YES |  |  |
| `ULTIMO_PAGO_30_DIAS` | DATE | YES |  |  |
| `IMPORTE_TOTAL_PAGO_30_DIAS` | NUMBER | YES |  |  |
| `ZON_CODIGO` | VARCHAR2 | NO |  |  |
| `SCF_CODIGO` | NUMBER | NO |  |  |
| `SCF_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `CNT_COND_INTIMACION` | VARCHAR2 | NO |  | Flag S/N en CONTRATOS: si el contrato es intimable. S=3.705.652, N=53.615. CNT_FECHA_TOPE_INTIMAC casi no se usa (20 filas). |
| `CNT_COND_CORTE` | VARCHAR2 | NO |  |  |
| `CNT_COND_RETIRO` | VARCHAR2 | NO |  |  |
| `CNT_FECHA_TOPE_CORTE` | DATE | YES |  |  |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `RG_FECHA_ACTUALIZACION` | DATE | YES |  |  |
| `DOC_SALDO_ERSEP` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
