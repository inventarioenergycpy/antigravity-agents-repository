---
tipo: tabla
categoria: custom
owner: XXSIGEC
dominio: contratos
num_rows: 3351
tags:
  - sigec-explorer
  - tabla
  - custom
  - dominio/contratos
  - documentada/negocio
aliases:
  - "XXCO_AFECTADOS_POR_NOVEDAD_FM"
---

# 🔧 XXCO_AFECTADOS_POR_NOVEDAD_FM

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 3,351

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `RTA_CODIGO` | NUMBER | NO |  |  |
| `FECHA_CARGA` | DATE | YES |  |  |
| `CNT_COND_INTIMACION` | VARCHAR2 | NO |  | Flag S/N en CONTRATOS: si el contrato es intimable. S=3.705.652, N=53.615. CNT_FECHA_TOPE_INTIMAC casi no se usa (20 filas). |
| `CNT_COND_CORTE` | VARCHAR2 | NO |  |  |
| `CNT_COND_RETIRO` | VARCHAR2 | NO |  |  |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | YES |  |  |
| `URC_CODIGO` | NUMBER | YES |  |  |
| `CNT_NUMERO_CUENTA` | NUMBER | YES |  | NO es el número de contrato/cuenta comercial. Es el número de CUENTA BANCARIA o TARJETA para débito automático (VARCHAR2: 16 dígitos = tarjeta, 22 = CBU). Solo 122.016 de 3,74M filas de CONTRATOS lo tienen poblado (3,2%) y viene NULL en la mayoría de los suministros. En DOCUMENTOS también viene NULL. El identificador comercial es la PK (SRV_CODIGO, CNT_NUMERO). |
| `CNT_TIPO_IMPRESION` | VARCHAR2 | YES |  |  |
| `IGNORAR` | NUMBER | YES |  |  |

## FK inferidas (alta confianza)

- `MPA_TIPO_MEDIO_PAGO` → [[MEDIOS_PAGO]] _MPA_TIPO_MEDIO_PAGO es PK de MEDIOS_PAGO_
