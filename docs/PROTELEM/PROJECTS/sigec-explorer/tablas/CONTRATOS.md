---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 3743553
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "CONTRATOS"
---

# 📋 CONTRATOS

> [!info] Significado de negocio
> Contratos comerciales — entidad central del dominio (~3,74M filas). PK COMPUESTA (SRV_CODIGO, CNT_NUMERO): un suministro tiene un contrato por cada titular sucesivo. Titular = PRS_NUMERO → PERSONAS. Vigente = CNT_ESTADO='V'. OJO: CNT_NUMERO_CUENTA NO es el número de cuenta comercial (es CBU/tarjeta de débito automático).

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 3,743,553

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | NO | 🔗 → [[PERSONAS]] | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `PRS_NUMERO_APODERADO` | NUMBER | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `TEN_CODIGO` | VARCHAR2 | NO | 🔗 → [[TENSIONES]] |  |
| `CAT_CODIGO` | VARCHAR2 | NO | 🔗 → [[CATEGORIAS]] |  |
| `OBT_PROPIETARIO` | VARCHAR2 | YES |  |  |
| `CNT_FECHA_INICIO` | DATE | NO |  |  |
| `IVV_CODIGO` | NUMBER | NO |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `CNT_TENSION` | NUMBER | YES |  |  |
| `CNT_TIPO` | VARCHAR2 | NO |  |  |
| `CNT_COND_CORTE` | VARCHAR2 | NO |  |  |
| `CNT_COND_INTIMACION` | VARCHAR2 | NO |  | Flag S/N en CONTRATOS: si el contrato es intimable. S=3.705.652, N=53.615. CNT_FECHA_TOPE_INTIMAC casi no se usa (20 filas). |
| `CNT_COND_RETIRO` | VARCHAR2 | NO |  |  |
| `CNT_DIRECCION_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_CALLE_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_NRO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_PISO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_DEPTO_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_C_POSTAL_PAGO` | NUMBER | YES |  |  |
| `AGF_CODIGO_PAGO` | NUMBER | NO |  |  |
| `MIN_CODIGO` | VARCHAR2 | YES |  | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `CNT_ANIO` | NUMBER | YES |  |  |
| `CNT_PERIODO` | NUMBER | YES |  |  |
| `CNT_TASA` | VARCHAR2 | YES |  |  |
| `CNT_CONSUMO_PROMEDIO_ANUAL` | NUMBER | YES |  |  |
| `CNT_NUMERO_SOBRE` | VARCHAR2 | YES |  |  |
| `CNT_CONSUMO_PROMEDIO_VERANO` | NUMBER | YES |  |  |
| `CNT_NUMERO_REPARTO` | VARCHAR2 | YES |  |  |
| `CNT_CONSUMO_PROMEDIO_INVIERNO` | NUMBER | YES |  |  |
| `CNT_LEGAJO` | VARCHAR2 | YES |  |  |
| `CNT_CONSUMO_MAXIMO` | NUMBER | YES |  |  |
| `CNT_CONTRIBUCION` | VARCHAR2 | YES |  |  |
| `CNT_CIIU` | NUMBER | YES |  |  |
| `URC_CODIGO` | NUMBER | NO |  |  |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | NO |  |  |
| `CNT_NUMERO_CUENTA` | VARCHAR2 | YES |  | NO es el número de contrato/cuenta comercial. Es el número de CUENTA BANCARIA o TARJETA para débito automático (VARCHAR2: 16 dígitos = tarjeta, 22 = CBU). Solo 122.016 de 3,74M filas de CONTRATOS lo tienen poblado (3,2%) y viene NULL en la mayoría de los suministros. En DOCUMENTOS también viene NULL. El identificador comercial es la PK (SRV_CODIGO, CNT_NUMERO). |
| `CNT_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO_OIM` | NUMBER | NO | 🔗 → [[OIM]] |  |
| `OIM_TIPO` | VARCHAR2 | NO | 🔗 → [[OIM]] |  |
| `CNT_ESTADO` | VARCHAR2 | NO |  | Estado del contrato: 'V' = vigente (el titular actual), 'C' = cerrado/cesado (titular anterior, con CNT_FECHA_FIN). Para 'el titular de hoy' filtrar CNT_ESTADO='V' (o CNT_FECHA_FIN IS NULL). |
| `CNT_PROPIETARIO` | VARCHAR2 | YES |  |  |
| `CNT_SECUENCIA_ORIGINAL` | NUMBER | YES |  |  |
| `TLY_CODIGO` | NUMBER | YES |  |  |
| `IMP_CODIGO` | NUMBER | NO |  |  |
| `USR_NUMERO` | NUMBER | YES |  |  |
| `GCO_GRUPO` | VARCHAR2 | YES |  |  |
| `CNT_FECHA_TOPE_CORTE` | DATE | YES |  |  |
| `CNT_TFA_CODIGO` | VARCHAR2 | YES |  |  |
| `TFA_CODIGO` | VARCHAR2 | NO |  |  |
| `CNT_TIPO_DOMICILIO` | VARCHAR2 | YES |  |  |
| `CNT_FACTURABLE` | VARCHAR2 | YES |  |  |
| `EID_NUMERO` | NUMBER | YES |  |  |
| `CNT_TORRE_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_LOCAL_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_OFICINA_PAGO` | VARCHAR2 | YES |  |  |
| `CNT_TIPO_SUMINISTRO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO_PADRE` | NUMBER | YES |  |  |
| `CNT_NUMERO_PADRE` | NUMBER | YES |  |  |
| `CNT_VALIDADO` | VARCHAR2 | YES |  |  |
| `CNT_SERVICIO` | NUMBER | YES |  |  |
| `CNT_INSTITUCION` | NUMBER | YES |  |  |
| `CNT_CANT_DESC_CONTR` | NUMBER | YES |  |  |
| `CNT_FECHA_DESC_CONTR` | DATE | YES |  |  |
| `CNT_FECHA_REQUISITOS` | DATE | YES |  |  |
| `SEC_CODIGO` | VARCHAR2 | YES |  |  |
| `CNT_FECHA_DEBIAUT` | DATE | YES |  |  |
| `CNT_FECHA_VIGENCIA` | DATE | YES |  |  |
| `CNT_COND_EXCESO_DEM` | VARCHAR2 | YES |  |  |
| `CNT_COND_COSENO_FI` | VARCHAR2 | YES |  |  |
| `CNT_AGENTE` | VARCHAR2 | YES |  |  |
| `CNT_GUDI` | VARCHAR2 | YES |  |  |
| `CNT_PERIODO_GRACIA_COS_FI` | VARCHAR2 | YES |  |  |
| `CNT_PRORRATEA` | VARCHAR2 | YES |  |  |
| `CNT_CNT_RESPALDO` | VARCHAR2 | YES |  |  |
| `CNT_ENERGIA_PLUS` | VARCHAR2 | YES |  |  |
| `CNT_FECHA_INICIO_COMPLETA` | DATE | YES |  |  |
| `LEY_9121` | VARCHAR2 | YES |  |  |
| `CNT_PLAN_PAGO` | VARCHAR2 | YES |  |  |
| `CIB_CODIGO` | NUMBER | YES |  |  |
| `CNT_FECHA_TOPE_EXENTO_IB` | DATE | YES |  |  |
| `CNT_CONDICION_SUBSIDIO` | VARCHAR2 | YES |  |  |
| `CNT_COEF_RECUPERO_SUBSIDIO` | NUMBER | YES |  |  |
| `CNT_CODIGO_ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `CNT_FECHA_CBIO_COND_SUB` | DATE | YES |  |  |
| `ADR_CODIGO` | NUMBER | YES |  |  |
| `CNT_FECHA_TOPE_IB` | DATE | YES |  |  |
| `CNT_FECHA_BAJA_ADM` | DATE | YES |  |  |
| `CNT_TIPO_IMPRESION` | VARCHAR2 | YES |  |  |
| `CNT_PROPIEDAD` | VARCHAR2 | YES |  |  |
| `NCW_NUMERO_CONSTANCIA` | NUMBER | YES |  |  |
| `CNT_MATRICULA` | VARCHAR2 | YES |  |  |
| `CNT_ULTIMA_ACTUALIZACION` | DATE | YES |  |  |
| `CNT_PORCENTAJE_TCL_REC_BON` | NUMBER | YES |  |  |
| `CNT_DURACION` | NUMBER | YES |  |  |
| `CNT_DOC_FECHA_VENC_ULTIMA` | DATE | YES |  |  |
| `CNT_ULTIMA_ACTUALIZACION_MDM` | DATE | YES |  |  |
| `CNT_FECHA_TOPE_INTIMAC` | DATE | YES |  |  |

## FK declaradas → otras tablas

- **CNT_FK_CAT**: `CAT_CODIGO` → [[CATEGORIAS]] (`CAT_CODIGO`)
- **CNT_FK_OIM**: `AGF_CODIGO_OIM`, `OIM_TIPO` → [[OIM]] (`AGF_CODIGO`, `OIM_TIPO`)
- **CNT_FK_PRS**: `PRS_NUMERO` → [[PERSONAS]] (`PRS_NUMERO`)
- **CNT_FK_TEN**: `TEN_CODIGO` → [[TENSIONES]] (`TEN_CODIGO`)

## Tablas que referencian esta tabla

- [[DOCUMENTOS]] via `CNT_NUMERO`, `SRV_CODIGO`
- [[EXCESOS_A_FACTURAR]] via `CNT_NUMERO`, `SRV_CODIGO`
- [[INTERFAZ_MED_ORD]] via `CNT_NUMERO`, `SRV_CODIGO`
- [[ITEMS_A_FACTURAR]] via `CNT_NUMERO`, `SRV_CODIGO`
- [[LIQUIDACIONES_ILICITOS]] via `CNT_NUMERO`, `SRV_CODIGO`
- [[PAGOS_TEMPRANOS]] via `CNT_NUMERO`, `SRV_CODIGO`
- [[XX_CALIFICACIONES]] via `CNT_NUMERO`, `SRV_CODIGO`
- [[XX_CONTRIBUCIONES_PROYECTOS]] via `CNT_NUMERO`, `SRV_CODIGO`
- [[XX_INTERFASE_PROYECTOS]] via `CNT_NUMERO`, `SRV_CODIGO`

## FK inferidas (alta confianza)

- `MPA_TIPO_MEDIO_PAGO` → [[MEDIOS_PAGO]] _MPA_TIPO_MEDIO_PAGO es PK de MEDIOS_PAGO_
- `CNT_CIIU` → [[CODIGOS_CIIU]] _CNT_CIIU es PK de CODIGOS_CIIU_
- `MIN_CODIGO` → [[ENTES]] _MIN_CODIGO es PK de ENTES_
- `CNT_GUDI` → [[XX_GUDI_MAIL]] _CNT_GUDI es PK de XX_GUDI_MAIL_
- `ADR_CODIGO` → [[XXCO_ACTIVIDADES_DGR]] _ADR_CODIGO es PK de XXCO_ACTIVIDADES_DGR_
