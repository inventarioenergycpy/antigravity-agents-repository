---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 4157179227
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "ITEMS"
---

# 📋 ITEMS

> [!info] Significado de negocio
> Detalle de ítems de factura (~4.157M filas, 19x LECTURAS, SIN PK). Es el DESGLOSE EXACTO del importe: SUM(ITM_IMPORTE) por (DOC_TIPO, DOC_NUMERO) reproduce DOCUMENTOS.DOC_IMPORTE al centavo en el 100% de la muestra (1.660/1.660 facturas). Ítems típicos de una factura de energía: CFI cargo fijo, EE1..EE4 energía por escalón, IVC IVA 21%, OIM ord. imp. municipal 9,90%, DTO Dto.2298, R27 ERSeP Ley 10281, FDE Fdo.Des.Ene.Prov 10%, RED redondeo; se repiten por cada VIGENCIA DE TARIFA dentro del período (ITM_DETALLE_IMPRESO = 'V.01/11/24'). El ítem CFI viene con ITM_UNIDAD='Días' y su ITM_CANTIDAD son los DÍAS FACTURADOS prorrateados por vigencia (suman HASTA-DESDE). Tiene la tarifa histórica exacta vía TIPOS_ITEM.TCL_CODIGO. CORRECCIÓN (2026-08-06): DOC_FECHA_EMISION viene 100% NULL (0 de 121.107 ítems de la muestra) — NO sirve como filtro pese a estar desnormalizada; el acceso barato es por (DOC_TIPO, DOC_NUMERO). Para kWh NO sumar los ítems TIT_CONSUMO='S' (solo reproducen DOC_CONSUMO en 81,5%): usar DOC_CONSUMO. TIPOS_ITEM (866 filas) tiene los flags TIT_CONSUMO, TIT_CAMMESA, TIT_BANDA_HORARIA, ITM_UNIDAD, TCL_CODIGO. NOTA: no ayuda a reproducir la imagen CAMMESA porque el desvío dominante (alumbrado) es de inclusión de documentos, no de tarifa.

**Prefijo `DOC_`:** Documentos de facturación (DOCUMENTOS)

**Filas estimadas:** 4,157,179,227

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `ITM_NUMERO` | NUMBER | NO |  |
| `DOC_TIPO` | VARCHAR2 | NO |  |
| `DOC_NUMERO` | NUMBER | NO |  |
| `DOC_TIPO_ORIGEN_1` | VARCHAR2 | YES |  |
| `DOC_NUMERO_ORIGEN_1` | NUMBER | YES |  |
| `TIT_CLAVE` | VARCHAR2 | NO |  |
| `ITM_DETALLE` | VARCHAR2 | YES |  |
| `ITM_CANTIDAD` | NUMBER | YES |  |
| `ITM_PRECIO_UNIT` | NUMBER | YES |  |
| `ITM_IMPORTE` | NUMBER | NO |  |
| `ITM_SALDO` | NUMBER | YES |  |
| `ITM_MES_CONTABLE` | NUMBER | YES |  |
| `ITM_ESTADO` | VARCHAR2 | YES |  |
| `DOC_NUMERO_ORIGEN` | NUMBER | YES |  |
| `DOC_TIPO_ORIGEN` | VARCHAR2 | YES |  |
| `ITM_VENC_NRO` | VARCHAR2 | YES |  |
| `ITM_SALDO_CANTIDAD` | NUMBER | YES |  |
| `ITM_DETALLE_IMPRESO` | VARCHAR2 | YES |  |
| `DOC_FECHA_EMISION` | DATE | YES |  |
| `CPR_NUMERO` | NUMBER | YES |  |
| `TAB_NUMERO` | NUMBER | YES |  |
| `ITM_SECCION` | NUMBER | YES |  |
| `ITM_PRECIO_POR_IVA` | NUMBER | YES |  |
| `ITM_BASE_CALCULO` | NUMBER | YES |  |
| `ITM_PORCENTAJE` | NUMBER | YES |  |
| `ITM_ULTIMA_ACTUALIZACION` | DATE | YES |  |

## FK inferidas (alta confianza)

- `ITM_NUMERO` → [[XX_INFORMES_PROCESOS_ITEMS]] _ITM_NUMERO es PK de XX_INFORMES_PROCESOS_ITEMS_
