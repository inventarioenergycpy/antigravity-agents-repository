---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 83
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TIPOS_RECLAMO"
---

# 📋 TIPOS_RECLAMO

> [!info] Significado de negocio
> Catalogo de tipos de reclamo (83 filas). El grupo TRO_GRUPO_RECLAMO='FR' son las 57 tipologias de ilicito, en arbol de 2 niveles: F POSIBLE FRAUDE -> F1 CONEXION DIRECTA, F2 FRAUDE CON RETIRO, F3 NO FRAUDE, F4 CESION ENERGIA, F5 FRAUDE SIN RETIRO -> hojas 11-13, 21-38, 40-42, 51-79.

**Filas estimadas:** 83

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TRO_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TRO_CODIGO_RECL_ENARGAS` | VARCHAR2 | YES |  |
| `TRO_DESCRIPCION` | VARCHAR2 | YES |  |
| `TRO_CANT_DIAS_RESOLUCION` | VARCHAR2 | YES |  |
| `TRO_GRUPO_RECLAMO` | VARCHAR2 | YES |  |
| `TRO_PRIORIDAD_RESOLUCION` | VARCHAR2 | YES |  |
| `TRO_CODIGO_PADRE` | VARCHAR2 | YES |  |
| `TRO_CODIGO_INFORME` | VARCHAR2 | YES |  |
| `FUN_SHORT_NAME` | VARCHAR2 | YES |  |
| `TIT_CLAVE` | VARCHAR2 | YES |  |

## Tablas que referencian esta tabla

- [[RECLAMOS_ORDENATIVO]] via `TRO_CODIGO`
- [[RECLAMOS_ORDENATIVOS]] via `TRO_CODIGO`
