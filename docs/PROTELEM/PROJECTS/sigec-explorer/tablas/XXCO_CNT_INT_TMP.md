---
tipo: tabla
categoria: temp
owner: XXSIGEC
dominio: servicios
tags:
  - sigec-explorer
  - tabla
  - temp
  - dominio/servicios
  - documentada/negocio
aliases:
  - "XXCO_CNT_INT_TMP"
---

# ⏱️ XXCO_CNT_INT_TMP

**Prefijo `SRV_`:** Suministro / punto de suministro (SERVICIOS)

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `SRV_CODIGO` | NUMBER | NO | 🔑 PK | Código del punto de suministro. Clave que enlaza SERVICIOS ↔ PUNTOS_MEDICION ↔ EQUIPOS ↔ LECTURAS. |
| `CNT_NUMERO` | NUMBER | NO | 🔑 PK | Número de contrato dentro de un suministro (1, 2, 3…): cada titular sucesivo del mismo punto de suministro abre un CNT_NUMERO nuevo. Junto con SRV_CODIGO forma la PK real de CONTRATOS y los 2 últimos dígitos del número de contrato de 10 dígitos que ve el cliente. |
| `TCL_CODIGO` | VARCHAR2 | YES |  | Código de tarifa/clase tarifaria (PK de TARIFAS, 405 filas). TCL_DESCRIPCION es granular; el rubro de venta se toma de TCL_GRUPO. |
| `GRL_CODIGO` | VARCHAR2 | YES |  |  |
| `SCF_CODIGO` | NUMBER | YES |  |  |
| `TCL_GRUPO` | VARCHAR2 | YES |  | Grupo/rubro tarifario en TARIFAS. Mapea al sector de venta: 1=Residencial, 2=Comercial(Gral y Serv), 3=Industrial(Grandes Consumos), 4=Cooperativas, 5=Oficial(Gob y Us.Esp.), 6=Alumbrado Público, 7=Servicio de Agua, 8=Rural. Peaje y Uso Propio viven dentro del grupo 3 (identificar por TCL_DESCRIPCION). |
| `ZON_CODIGO` | VARCHAR2 | YES |  |  |
| `AGE_CODIGO` | VARCHAR2 | YES |  |  |
| `BAR_CODIGO` | VARCHAR2 | YES |  |  |

## FK inferidas (alta confianza)

- `AGE_CODIGO` → [[AGENCIAS]] _AGE_CODIGO es PK de AGENCIAS_
- `ZON_CODIGO` → [[ZONAS]] _ZON_CODIGO es PK de ZONAS_
- `BAR_CODIGO` → [[XXCO_BARRIOS]] _BAR_CODIGO es PK de XXCO_BARRIOS_
