---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 11
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMESUCURSALES.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `SCF_CODIGO` | integer | 1 · 2 · 3 · 4 · 5 |
| `SCF_DESCRIPCION` | text | CORDOBA · LA FALDA · COSQUIN · LA CUMBRE · CAPILLA DEL MONTE |
| `AGF_CODIGO` | integer | 1000 · 2000 · 2100 · 2150 · 2200 |
| `ZON_CODIGO` | text | A · B |
| `SCF_C_POSTAL` | integer | 5000 · 5172 · 5166 ·  |
| `SCF_FAX` | text |  · 423584 · 452022 Reclamos · 451567 · 481002 |
| `SCF_TELEFONO` | text | 0800-777-0000 · 423466 · 451672 Of.Comerc. · 451567 · 481002 |
| `SCF_DIRECCION` | text | LA TABLADA 350 · Av.EDEN Pje. CAPDEVILA · SAN MARTIN 836 · 25 DE MAYO Esq. RIVADAVIA · SAN LUIS Esq. MITRE |
| `SCF_DEFINICION_CONTABLE` | integer | 3101 · 3211 · 3231 · 3241 · 3221 |
| `SCF_CODIGO_DEBIAUT` | flag | S · N |
| `SCF_NRO_CERTIFICADO` | integer | 13618 · 381 · 326 · 116 · 80 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/SUCURSALES\|SUCURSALES]] — match parcial de nombre + 11 columnas en comun
- [[Projects/sigec-explorer/tablas/XXCO_XML_ORD_NF_TMP\|XXCO_XML_ORD_NF_TMP]] — 4 columnas en comun
- [[Projects/sigec-explorer/tablas/DETALLE_SALDO\|DETALLE_SALDO]] — 3 columnas en comun

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
