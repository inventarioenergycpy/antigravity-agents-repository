---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 8
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "TIPOS_ENTE"
---

# 📋 TIPOS_ENTE

> [!info] Significado de negocio
> Catálogo de tipos de ente (TMI_CODIGO→TMI_DESCRIPCION): 1 Nacional, 2 Provincial, 3 Municipal, 4 Cooperativas de Electricidad, 5 Particulares, 6 Provincial No Autárq.(Reparto), 7 Empresa Provincial de Energía (EPEC), 8 Barrios c/Limitadores. Clave para distinguir organismos municipales (TMI 3) de no municipales.

**Filas estimadas:** 8

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `TMI_CODIGO` | VARCHAR2 | NO |  | Tipo de ente (PK de TIPOS_ENTE, en ENTES): 1 Nacional, 2 Provincial, 3 Municipal, 4 Cooperativas, 5 Particulares, 6 Prov. No Autárq., 7 EPEC, 8 Barrios. Se guarda como VARCHAR ('1'...'8'). |
| `TMI_DESCRIPCION` | VARCHAR2 | NO |  |  |
| `TMI_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |  |
