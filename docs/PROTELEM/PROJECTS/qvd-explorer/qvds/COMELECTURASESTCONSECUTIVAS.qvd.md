---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 18
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMELECTURASESTCONSECUTIVAS.qvd

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `AÑO_LECTURA` | integer | 2019 · 2024 · 2022 |
| `NRO_MES_LECTURA` | integer | 01 · 12 · 10 · 11 |
| `AÑO_MES_LECT` | integer | 201901 · 202412 · 202210 · 202211 |
| `ID_SUCURSAL` | integer | 18 |
| `ID_RUTA_LECTURA` | integer | 18060 · 18070 · 18030 |
| `ID_RUTA_FACTURACION` | integer | 4906 · 4901 · 4013 |
| `ID_GRUPO_CONTRATO` | text | GC |
| `ID_TIPO_LECTURA` | text | E |
| `ES_TELEMEDICION` | flag | NO |
| `FECHA_LECTURA` | date | 31/01/2019 · 16/12/2024 · 28/10/2022 · 29/11/2022 |
| `FECHA_LECTURA_NUM` | integer | 43496 · 45642 · 44862 · 44894 |
| `AÑO_CONTABLE` | integer | 2019 · 2024 · 2022 |
| `NRO_MES_CONTABLE` | integer | 1 · 12 · 10 · 11 |
| `CODIGO_SUMINISTRO` | integer | 100148 · 100178 · 100256 · 100257 |
| `NRO_EST_CONSECUTIVA` | integer | 2 · 3 |
| `CODIFICACION_CONSECUTIVA` | text | 100148E1 · 100178E1 · 100256E1 · 100257E1 |
| `EQUIPO_ORDEN` | integer | 3 · 2 |
| `PUNTO_MEDICION` | integer | 1 |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/LECTURAS\|LECTURAS]] — match parcial de nombre

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
