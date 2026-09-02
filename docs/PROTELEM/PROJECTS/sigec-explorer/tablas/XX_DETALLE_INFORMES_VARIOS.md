---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1178581943
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XX_DETALLE_INFORMES_VARIOS"
---

# 📋 XX_DETALLE_INFORMES_VARIOS

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 1,178,581,943

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `DIE_NUMERO` | NUMBER | YES | 🔑 PK |  |
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `DOC_TIPO` | VARCHAR2 | NO |  |  |
| `DOC_NUMERO` | NUMBER | NO |  |  |
| `INV_NUMERO` | NUMBER | NO |  |  |
| `TIT_CLAVE` | VARCHAR2 | NO |  |  |
| `TIV_CODIGO` | VARCHAR2 | NO |  |  |
| `DIE_IMPORTE` | NUMBER | NO |  |  |
| `SCF_CODIGO` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | YES |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `TIV_SIGNO` | VARCHAR2 | NO |  |  |
| `OIM_TIPO` | VARCHAR2 | YES |  |  |
| `TIV_TIPO` | VARCHAR2 | YES |  |  |
| `DIE_MES_EMISION` | NUMBER | YES |  |  |
| `ENE_VENDOR_ID` | NUMBER | YES |  |  |
| `APL_FECHA` | DATE | YES |  |  |
| `VENDOR_SITE_ID` | NUMBER | YES |  |  |
| `URC_CODIGO_DEPO` | NUMBER | YES |  |  |
| `APL_VENC_NRO` | NUMBER | YES |  |  |
| `ITM_NUMERO` | NUMBER | YES |  |  |
| `ALI_CUOTA` | NUMBER | YES |  |  |
| `BASE_CALCULO` | NUMBER | YES |  |  |
| `ASI_NUMERO` | NUMBER | YES |  |  |
| `CPR_NUMERO_INFORME_GL` | NUMBER | YES |  |  |
| `DBO_ORDEN` | NUMBER | YES |  |  |
| `DIE_BASE_CALCULO` | NUMBER | YES |  |  |
| `DOC_CONSUMO` | NUMBER | YES |  | Consumo facturado (kWh) en la cabecera de DOCUMENTOS: LA columna de kWh de una factura. Cubre la banda horaria completa — coincide con CONS_ENERGIA+PICO+VALLE+RESTO de la VM en 99,65% de las filas (revalidado 2026-08: 99,92% en el período 2025/6, y solo 0,56% de las facturas tiene banda horaria). En notas de crédito (DOC_TIPO='C') viene POSITIVO: negar para restar. Es la forma de obtener kWh cuando se usa DOCUMENTOS (la VM AUDITORIA_CAMMESA solo tiene 2022 desde dic-2022). Para kWh preferirla SIEMPRE sobre sumar ITEMS (que solo la reproduce en 81,5%). |

## FK inferidas (alta confianza)

- `ITM_NUMERO` → [[XX_INFORMES_PROCESOS_ITEMS]] _ITM_NUMERO es PK de XX_INFORMES_PROCESOS_ITEMS_
- `TIV_SIGNO` → [[XX_TOTALES_INFORMES_VARIOS]] _TIV_SIGNO es PK de XX_TOTALES_INFORMES_VARIOS_
- `TIV_TIPO` → [[XX_TOTALES_INFORMES_VARIOS]] _TIV_TIPO es PK de XX_TOTALES_INFORMES_VARIOS_
