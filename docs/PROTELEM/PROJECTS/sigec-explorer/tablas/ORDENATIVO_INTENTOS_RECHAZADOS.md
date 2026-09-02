---
tipo: tabla
categoria: base
owner: XXSIGEC
dominio: documentos
num_rows: 1024167
tags:
  - sigec-explorer
  - tabla
  - base
  - dominio/documentos
  - documentada/negocio
aliases:
  - "ORDENATIVO_INTENTOS_RECHAZADOS"
---

# 📋 ORDENATIVO_INTENTOS_RECHAZADOS

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

**Filas estimadas:** 1,024,167

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `OIR_NUMERO` | NUMBER | NO | 🔑 PK |  |
| `OIR_FECHA` | DATE | NO |  |  |
| `TOR_CODIGO` | VARCHAR2 | NO |  |  |
| `ORD_NUMERO` | NUMBER | NO |  |  |
| `TOR_CODIGO_INTENTO` | VARCHAR2 | YES |  |  |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `PRS_NUMERO` | NUMBER | YES |  | PK de PERSONAS (número interno de cliente, no visible al usuario). CONTRATOS.PRS_NUMERO apunta al titular del contrato; PRS_NUMERO_APODERADO al apoderado si lo hay. |
| `OIR_OBSERVACIONES` | VARCHAR2 | YES |  |  |
| `USR_CODIGO` | VARCHAR2 | YES |  |  |
