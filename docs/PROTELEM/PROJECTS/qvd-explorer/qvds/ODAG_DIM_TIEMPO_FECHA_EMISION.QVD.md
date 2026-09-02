---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 13
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 ODAG_DIM_TIEMPO_FECHA_EMISION.QVD

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `FE_ANIO` | integer | 2010 |
| `Año_Emision` | integer | 2010 |
| `PERIODO_EMISION` | integer | 201003 · 201004 |
| `Mes_Emision` | integer | 03 · 04 |
| `FE_ID_PERIODO_CONTABLE` | text | 03/2010 · 04/2010 |
| `FE_DIA` | integer | 30 · 31 · 1 · 2 · 3 |
| `FECHA_EMISION` | date | 2010-03-30 00:00:00.000000 · 2010-03-31 00:00:00.000000 · 2010-04-01 00:00:00.000000 · 2010-04-02 00:00:00.000000 · 2010-04-03 00:00:00.000000 |
| `FE_ID_MES` | integer | 3 · 4 |
| `FE_ID_SEMESTRE` | integer | 1 |
| `FE_ID_TRIMESTRE` | integer | 1 · 2 |
| `FE_MES_DESCRIPCION` | text | MARZO · ABRIL |
| `FE_SEMESTRE_DESCRIPCION` | text | 2010- 01 - PRIMER |
| `FE_TRIMESTRE_DESCRIPCION` | text | 2010- 01 - ENE/FEB/MAR · 2010- 02 - ABR/MAY/JUN |

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
