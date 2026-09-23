---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
num_rows: 34620
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "ACTA_TMP"
---

# ⏱️ ACTA_TMP

> [!info] Significado de negocio
> Staging legacy de Ilicitos (35.219 filas, 100 columnas TODAS VARCHAR2, sin PK, nombres truncados a 10 chars = origen dBase/FoxPro). ARCHIVO HISTORICO DE LOS 90 (1993-1998), no una frontera viva. Incluye filas de encabezado cargadas como datos. Workflow: acta -> preliquidacion -> consolidacion -> carta documento -> plan de pago -> 3 derivaciones (TRANSCOB cobranzas, TRANSZA via muerta, TRANSLEGAL legales). NRO_SIGEC guarda el numero que devuelve SIGEC. CAR_TRACOB/CAR_TRANZA/CAR_TRALEG contienen NOMBRES DE EMPLEADOS: dato sensible.

**Filas estimadas:** 34,620

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `NRO` | VARCHAR2 | YES |  |  |
| `PLAN` | VARCHAR2 | YES |  |  |
| `RUTA` | VARCHAR2 | YES |  |  |
| `SUMINISTRO` | VARCHAR2 | YES |  | Clave de punto de suministro con nombre corto sin prefijo (7 tablas de integración/TMP). |
| `SUMI_NUEVO` | VARCHAR2 | YES |  |  |
| `CONTRATO` | VARCHAR2 | YES |  |  |
| `CLIENTE` | VARCHAR2 | YES |  |  |
| `CATEGORIA` | VARCHAR2 | YES |  |  |
| `NOMBRE` | VARCHAR2 | YES |  |  |
| `TITULAR` | VARCHAR2 | YES |  |  |
| `ACTIVIDAD` | VARCHAR2 | YES |  |  |
| `CALLE` | VARCHAR2 | YES |  |  |
| `ALTURA` | VARCHAR2 | YES |  |  |
| `PISO` | VARCHAR2 | YES |  |  |
| `DPTO` | VARCHAR2 | YES |  |  |
| `BARRIO` | VARCHAR2 | YES |  |  |
| `SECC` | VARCHAR2 | YES |  |  |
| `DOC_TIPO` | VARCHAR2 | YES |  |  |
| `DOC_NRO` | VARCHAR2 | YES |  |  |
| `CARACTER` | VARCHAR2 | YES |  |  |
| `INFRACCION` | VARCHAR2 | YES |  |  |
| `INSPECTOR` | VARCHAR2 | YES |  |  |
| `SUMARIO` | VARCHAR2 | YES |  |  |
| `NROSUM` | VARCHAR2 | YES |  |  |
| `SECUESTRO` | VARCHAR2 | YES |  |  |
| `LUGAR` | VARCHAR2 | YES |  |  |
| `ACTANOTA` | VARCHAR2 | YES |  |  |
| `OFICIAL` | VARCHAR2 | YES |  |  |
| `MEDIDOR` | VARCHAR2 | YES |  | Número de medidor, pero SOLO en 4 tablas de carga/TMP (ACTA_TMP, XXCO_XML_*). La clave real y extendida de medidor es STE_NUMERO. No existe columna NRO_MEDIDOR. |
| `ESTADO` | VARCHAR2 | YES |  |  |
| `FORM466` | VARCHAR2 | YES |  |  |
| `FORM471` | VARCHAR2 | YES |  |  |
| `HORA` | VARCHAR2 | YES |  |  |
| `FECHA` | VARCHAR2 | YES |  |  |
| `FECHA_CARG` | VARCHAR2 | YES |  |  |
| `NRO1` | VARCHAR2 | YES |  |  |
| `NRO2` | VARCHAR2 | YES |  |  |
| `MED_CON` | VARCHAR2 | YES |  |  |
| `OBSERVA` | VARCHAR2 | YES |  |  |
| `CARGO_ACTA` | VARCHAR2 | YES |  |  |
| `MODIF_ACTA` | VARCHAR2 | YES |  |  |
| `CONSUMO` | VARCHAR2 | YES |  |  |
| `CARG_CONSU` | VARCHAR2 | YES |  |  |
| `MODI_CONSU` | VARCHAR2 | YES |  |  |
| `EMISION1` | VARCHAR2 | YES |  |  |
| `GESTION1` | VARCHAR2 | YES |  |  |
| `PLAZO1` | VARCHAR2 | YES |  |  |
| `CAR_GEST1` | VARCHAR2 | YES |  |  |
| `EMISION2` | VARCHAR2 | YES |  |  |
| `GESTION2` | VARCHAR2 | YES |  |  |
| `PLAZO2` | VARCHAR2 | YES |  |  |
| `CAR_GEST2` | VARCHAR2 | YES |  |  |
| `FE_EMISION` | VARCHAR2 | YES |  |  |
| `PLAZO` | VARCHAR2 | YES |  |  |
| `NRO_CARTA` | VARCHAR2 | YES |  |  |
| `YEAR` | VARCHAR2 | YES |  |  |
| `CAR_EMISIO` | VARCHAR2 | YES |  |  |
| `FE_RECIBIO` | VARCHAR2 | YES |  |  |
| `CAR_RESIBO` | VARCHAR2 | YES |  |  |
| `ACLARACION` | VARCHAR2 | YES |  |  |
| `PRESENTO` | VARCHAR2 | YES |  |  |
| `IMPORTE` | VARCHAR2 | YES |  |  |
| `ICONSUMO` | VARCHAR2 | YES |  |  |
| `GASTOS` | VARCHAR2 | YES |  |  |
| `NOTARIAL` | VARCHAR2 | YES |  |  |
| `SEGURIDAD` | VARCHAR2 | YES |  |  |
| `FACTURAS` | VARCHAR2 | YES |  |  |
| `CONTADO` | VARCHAR2 | YES |  |  |
| `ENTREGA` | VARCHAR2 | YES |  |  |
| `ENTREGA1` | VARCHAR2 | YES |  |  |
| `ENTREGA2` | VARCHAR2 | YES |  |  |
| `CUOTAS` | VARCHAR2 | YES |  |  |
| `NRO_SIGEC` | VARCHAR2 | YES |  |  |
| `NRO_CONTRA` | VARCHAR2 | YES |  |  |
| `PAGADOR` | VARCHAR2 | YES |  |  |
| `MITIPO` | VARCHAR2 | YES |  |  |
| `MINRO` | VARCHAR2 | YES |  |  |
| `CAR_PRELIQ` | VARCHAR2 | YES |  |  |
| `MOD_PRELIQ` | VARCHAR2 | YES |  |  |
| `CONSOLIDA` | VARCHAR2 | YES |  |  |
| `DEBITO` | VARCHAR2 | YES |  |  |
| `RECIBO` | VARCHAR2 | YES |  |  |
| `FACTU_CONS` | VARCHAR2 | YES |  |  |
| `FACTU_GAST` | VARCHAR2 | YES |  |  |
| `RECIBO_SIG` | VARCHAR2 | YES |  |  |
| `CARG_CONSO` | VARCHAR2 | YES |  |  |
| `MODI_CONSO` | VARCHAR2 | YES |  |  |
| `TRANSCOB` | VARCHAR2 | YES |  |  |
| `CAR_TRACOB` | VARCHAR2 | YES |  |  |
| `TRANSZA` | VARCHAR2 | YES |  |  |
| `CAR_TRANZA` | VARCHAR2 | YES |  |  |
| `TRANSLEGAL` | VARCHAR2 | YES |  | En ACTA_TMP: FECHA (texto D/M/YY) de transferencia del acta al area Legales, 1996-1998. Su par CAR_TRALEG es el NOMBRE de la persona a cargo (CAR_ = 'a cargo de'), no una fecha de carga. Archivo historico: no es una frontera viva. |
| `PRIORIDAD` | VARCHAR2 | YES |  |  |
| `CAR_TRALEG` | VARCHAR2 | YES |  |  |
| `OBSERVA1` | VARCHAR2 | YES |  |  |
| `OBSERVA2` | VARCHAR2 | YES |  |  |
| `OBSERVA3` | VARCHAR2 | YES |  |  |
| `OBSERVA4` | VARCHAR2 | YES |  |  |
| `OBSERVA5` | VARCHAR2 | YES |  |  |
| `OBSERVA6` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `DOC_NRO` → [[XXCO_DOC_CORREO_XML]] _DOC_NRO es PK de XXCO_DOC_CORREO_XML_
- `FECHA` → [[XXCO_ACTIVIDADES_ANEXOS]] _FECHA es PK de XXCO_ACTIVIDADES_ANEXOS_
