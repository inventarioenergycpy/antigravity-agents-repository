---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 97
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "TIPOS_ORDENATIVO"
---

# 📋 TIPOS_ORDENATIVO

> [!info] Significado de negocio
> Catalogo de tipos de orden de trabajo (97 filas). TOR_ESTADO_ILICITO / TOR_RESULTADO_ILICITO marcan las ordenes que pueden volver del campo detectando un ilicito (CO, GF, NF, RE, RF): el disparador de Ilicitos es una orden de trabajo, no una denuncia. Los codigos de INCORE son TOR: IN intimacion, CO corte, RE retiro.

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 97

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TOR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TOR_DESCRIPCION` | VARCHAR2 | NO |  |
| `TOR_GRUPO` | VARCHAR2 | YES |  |
| `TOR_ESTADO_ILICITO` | VARCHAR2 | YES |  |
| `TOR_RESULTADO_ILICITO` | VARCHAR2 | YES |  |
| `TOR_GENERACION` | VARCHAR2 | NO |  |
| `GOR_CODIGO` | VARCHAR2 | NO | 🔗 → [[GRUPOS_ORDENATIVOS]] |
| `IMO_CODIGO` | VARCHAR2 | YES | 🔗 → [[IMPRESORES_ORDENATIVOS]] |
| `TOR_OBSERVACIONES` | VARCHAR2 | YES |  |
| `TOR_TIPO_TITULAR_ASOCIADO` | VARCHAR2 | NO |  |
| `TOR_REPETIBLE` | VARCHAR2 | NO |  |
| `TOR_VISTA_ASOCIADA` | VARCHAR2 | YES |  |
| `TOR_VISTA_ASOC_REQUERIDA` | VARCHAR2 | YES |  |
| `TOR_ESTADO` | VARCHAR2 | NO |  |
| `TOR_CODIGO_BARRA` | NUMBER | NO |  |
| `TOR_MULTI_SUCURSAL` | VARCHAR2 | YES |  |
| `TOR_PROC_CORREO` | VARCHAR2 | YES |  |
| `TOR_CNT_VIGENTES` | VARCHAR2 | YES |  |
| `TOR_CNT_CADUCOS` | VARCHAR2 | YES |  |
| `TOR_CNT_TA` | VARCHAR2 | YES |  |
| `TOR_CNT_TB` | VARCHAR2 | YES |  |
| `TOR_GENERA_RCL` | VARCHAR2 | YES |  |
| `TOR_PERM_CBIO_DISTRITO` | VARCHAR2 | YES |  |
| `TOR_SOLICITAR_IAF` | VARCHAR2 | YES |  |
| `TOR_REQUIERE_EQUIPO` | VARCHAR2 | YES |  |
| `TOR_COLOR_STANDARD` | VARCHAR2 | YES |  |
| `IMO_CODIGO_ALTERNATIVO` | VARCHAR2 | YES |  |
| `MDM_TYPEWORK` | VARCHAR2 | YES |  |
| `TOR_CIERRE_MANUAL_HABILITADO` | VARCHAR2 | YES |  |

## FK declaradas → otras tablas

- **TOR_IMO_FK**: `IMO_CODIGO` → [[IMPRESORES_ORDENATIVOS]] (`IMO_CODIGO`)
- **TO_1_GOR_FK**: `GOR_CODIGO` → [[GRUPOS_ORDENATIVOS]] (`GOR_CODIGO`)

## Tablas que referencian esta tabla

- [[ACCIONES_ORDENATIVOS]] via `TOR_CODIGO_ACCION`
- [[ORDENATIVOS]] via `TOR_CODIGO`
- [[ORDENATIVOS_AUTORIZADOS]] via `TOR_CODIGO`
- [[TOR_DOC_PLAZOS]] via `TOR_CODIGO`
- [[XXCO_MOTIVOS_RECLAMOS]] via `TOR_CODIGO`

## FK inferidas (alta confianza)

- `GOR_CODIGO` → [[GRUPOS_ORDENATIVOS]] _GOR_CODIGO es PK de GRUPOS_ORDENATIVOS_
- `IMO_CODIGO` → [[IMPRESORES_ORDENATIVOS]] _IMO_CODIGO es PK de IMPRESORES_ORDENATIVOS_
