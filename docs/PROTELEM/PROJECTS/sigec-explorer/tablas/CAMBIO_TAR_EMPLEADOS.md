---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 5810
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "CAMBIO_TAR_EMPLEADOS"
---

# 📋 CAMBIO_TAR_EMPLEADOS

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 5,810

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `PRS_NUMERO` | NUMBER | NO |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `GRF_CODIGO` | VARCHAR2 | YES |  |  |
| `TCL_CODIGO` | VARCHAR2 | NO |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `CLA_CODIGO` | VARCHAR2 | NO |  |  |
| `CNT_NUMERO_CUENTA` | VARCHAR2 | YES |  | NO es el número de contrato/cuenta comercial. Es el número de CUENTA BANCARIA o TARJETA para débito automático (VARCHAR2: 16 dígitos = tarjeta, 22 = CBU). Solo 122.016 de 3,74M filas de CONTRATOS lo tienen poblado (3,2%) y viene NULL en la mayoría de los suministros. En DOCUMENTOS también viene NULL. El identificador comercial es la PK (SRV_CODIGO, CNT_NUMERO). |
| `FECHA_CARGA` | DATE | YES |  |  |
| `ORDEN_CARGA` | NUMBER | YES |  |  |
| `PRS_RAZON_SOCIAL` | VARCHAR2 | YES |  | Razón social / nombre del cliente en PERSONAS. Buscar organismos por LIKE (ej. Municipalidad de Córdoba, TAMSE). Prefijo PRS_ = Personas. |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `CNT_FECHA_FIN` | DATE | YES |  |  |
| `MPA_TIPO_MEDIO_PAGO` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `MPA_TIPO_MEDIO_PAGO` → [[MEDIOS_PAGO]] _MPA_TIPO_MEDIO_PAGO es PK de MEDIOS_PAGO_
