---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: documentos
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/documentos
  - documentada/negocio
aliases:
  - "XXCO_ORD_TMP"
---

# ⏱️ XXCO_ORD_TMP

**Prefijo `TOR_`:** Tipo de ordenativo (TIPOS_ORDENATIVO, 97 filas). PK TOR_CODIGO. Agrupado por GOR_CODIGO (GRUPOS_ORDENATIVOS: COR corte, INT intimaciones, FR fraude, MD medidores, NT notificacion...).

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TRT_NUMERO` | NUMBER | YES |  |  |
| `TOR_CODIGO` | VARCHAR2 | YES |  |  |
| `ORD_NUMERO` | NUMBER | YES |  |  |
| `SRV_CODIGO` | NUMBER | YES |  | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | YES |  | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `ORD_FECHA_GENERACION` | DATE | YES |  |  |
| `SCF_CODIGO_ORIGEN` | NUMBER | YES |  |  |
| `SEC_CODIGO_ORIGEN` | VARCHAR2 | YES |  |  |
| `SEC_CODIGO_DESTINO` | VARCHAR2 | YES |  | Sector destino del ordenativo (-> SECTORES). Es el mecanismo de derivacion entre areas. FRAU (Fraude e Ilicitos) recibe 1,77M ordenes historicas; LEGALES recibe CERO. |
| `SCF_CODIGO_DESTINO` | NUMBER | YES |  |  |
| `ORD_FECHA_INICIO` | DATE | YES |  |  |
| `ORD_FECHA_FIN` | DATE | YES |  |  |
| `ORD_FECHA_VENCIMIENTO` | DATE | YES |  |  |
| `ORD_RESULTADO` | VARCHAR2 | YES |  |  |
| `ORD_SITUACION` | VARCHAR2 | YES |  |  |
| `ORD_ESTADO` | VARCHAR2 | YES |  |  |
| `SRV_CODIGO_ORIGEN` | NUMBER | YES |  |  |
| `CNT_NUMERO_ORIGEN` | NUMBER | YES |  |  |
| `TRT_NUMERO_ORIGEN` | NUMBER | YES |  |  |
| `CPR_NUMERO` | NUMBER | YES |  |  |
| `TOR_CODIGO_ORIGEN` | VARCHAR2 | YES |  |  |
