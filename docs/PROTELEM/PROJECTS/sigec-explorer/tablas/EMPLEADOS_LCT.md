---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: contratos
num_rows: 60704
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/contratos
  - documentada/negocio
aliases:
  - "EMPLEADOS_LCT"
---

# 📋 EMPLEADOS_LCT

**Prefijo `CNT_`:** Contrato / cuenta comercial (CONTRATOS)

**Filas estimadas:** 60,704

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `IVV_CODIGO` | NUMBER | NO |  |  |
| `LCT_FECHA_LECTURA` | DATE | NO |  | Fecha en que se tomó la lectura. |
| `CONSUMO` | NUMBER | YES |  |  |
| `DIAS` | NUMBER | YES |  |  |
| `IVA` | NUMBER | YES |  |  |
| `CFI` | NUMBER | YES |  |  |
| `ECO` | NUMBER | YES |  |  |
| `EBO` | NUMBER | YES |  |  |
| `IMPUESTO` | NUMBER | YES |  |  |
| `CNT_NUMERO_CUENTA` | VARCHAR2 | YES |  | NO es el número de contrato/cuenta comercial. Es el número de CUENTA BANCARIA o TARJETA para débito automático (VARCHAR2: 16 dígitos = tarjeta, 22 = CBU). Solo 122.016 de 3,74M filas de CONTRATOS lo tienen poblado (3,2%) y viene NULL en la mayoría de los suministros. En DOCUMENTOS también viene NULL. El identificador comercial es la PK (SRV_CODIGO, CNT_NUMERO). |
