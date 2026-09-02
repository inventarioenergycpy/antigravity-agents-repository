---
tipo: tabla
categoria: journal
owner: XXSIGEC
dominio: contratos
num_rows: 28198140
tags:
  - sigec-explorer
  - tabla
  - journal
  - dominio/contratos
  - documentada/negocio
aliases:
  - "CONTRATOS_JN"
---

# 📝 CONTRATOS_JN

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 28,198,140

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `JN_SECUENCIA_CNT` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | YES |  |  |
| `TEN_CODIGO` | VARCHAR2 | YES |  |  |
| `IVV_CODIGO` | NUMBER | YES |  |  |
| `IMP_CODIGO` | NUMBER | YES |  |  |
| `AGF_CODIGO_OIM` | NUMBER | YES |  |  |
| `OIM_TIPO` | VARCHAR2 | YES |  |  |
| `CNT_COND_CORTE` | VARCHAR2 | YES |  |  |
| `CNT_COND_INTIMACION` | VARCHAR2 | YES |  | Flag S/N en CONTRATOS: si el contrato es intimable. S=3.705.652, N=53.615. CNT_FECHA_TOPE_INTIMAC casi no se usa (20 filas). |
| `CNT_COND_RETIRO` | VARCHAR2 | YES |  |  |
| `URC_CODIGO` | NUMBER | YES |  |  |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_NUMERO_CUENTA` | VARCHAR2 | YES |  | NO es el número de contrato/cuenta comercial. Es el número de CUENTA BANCARIA o TARJETA para débito automático (VARCHAR2: 16 dígitos = tarjeta, 22 = CBU). Solo 122.016 de 3,74M filas de CONTRATOS lo tienen poblado (3,2%) y viene NULL en la mayoría de los suministros. En DOCUMENTOS también viene NULL. El identificador comercial es la PK (SRV_CODIGO, CNT_NUMERO). |
| `JN_USR_NUMERO` | NUMBER | YES |  |  |
| `JN_FECHA` | DATE | YES |  |  |
| `CNT_ESTADO` | VARCHAR2 | YES |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `CNT_CALLE_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_NRO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_PISO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_DEPTO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_DIRECCION_PAGO` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO_PAGO` | NUMBER | YES |  |  |
| `SRV_CODIGO_PADRE` | NUMBER | YES |  |  |
| `CNT_CODIGO_PADRE` | NUMBER | YES |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `CNT_FECHA_INICIO` | DATE | YES |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `CNT_FECHA_TOPE_CORTE` | DATE | YES |  |  |
| `CNT_FECHA_REQUISITOS` | DATE | YES |  |  |
| `CNT_TIPO` | VARCHAR2 | YES |  |  |
| `CNT_CIIU` | NUMBER | YES |  |  |
| `CNT_PROPIETARIO` | VARCHAR2 | YES |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `PRS_NUMERO_APODERADO` | NUMBER | YES |  |  |
| `CNT_FECHA_VIGENCIA` | DATE | YES |  |  |
| `TFA_CODIGO` | VARCHAR2 | YES |  |  |
| `OBSERVACION` | VARCHAR2 | YES |  |  |
| `CNT_COND_COSENO_FI` | VARCHAR2 | YES |  |  |
| `CNT_COND_EXCESO_DEM` | VARCHAR2 | YES |  |  |
| `CNT_GUDI` | VARCHAR2 | YES |  |  |
| `CNT_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `CNT_PERIODO_GRACIA_COS_FI` | VARCHAR2 | YES |  |  |
| `CIB_CODIGO` | NUMBER | YES |  |  |
| `CNT_FECHA_TOPE_EXENTO_IB` | DATE | YES |  |  |
| `CNT_CONDICION_SUBSIDIO` | VARCHAR2 | YES |  |  |
| `CNT_COEF_RECUPERO_SUBSIDIO` | NUMBER | YES |  |  |
| `CNT_CODIGO_ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `CNT_FECHA_CBIO_COND_SUB` | DATE | YES |  |  |
| `CNT_TIPO_IMPRESION` | VARCHAR2 | YES |  |  |
| `USR_UNIX` | VARCHAR2 | YES |  |  |
| `USR_ORACLE` | VARCHAR2 | YES |  |  |
| `SERVIDOR` | VARCHAR2 | YES |  |  |
| `CNT_DURACION` | NUMBER | YES |  |  |
| `CNT_PORCENTAJE_TCL_REC_BON` | NUMBER | YES |  |  |
| `CNT_FECHA_TOPE_INTIMAC` | DATE | YES |  |  |

## FK inferidas (alta confianza)

- `JN_FECHA` → [[APLICACIONES_JN]] _JN_FECHA es PK de APLICACIONES_JN_
- `MPA_TIPO_MEDIO_PAGO` → [[MEDIOS_PAGO]] _MPA_TIPO_MEDIO_PAGO es PK de MEDIOS_PAGO_
- `CNT_CIIU` → [[CODIGOS_CIIU]] _CNT_CIIU es PK de CODIGOS_CIIU_
- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
- `CNT_GUDI` → [[XX_GUDI_MAIL]] _CNT_GUDI es PK de XX_GUDI_MAIL_
