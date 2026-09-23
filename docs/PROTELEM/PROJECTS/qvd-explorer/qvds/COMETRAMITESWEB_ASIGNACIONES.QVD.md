---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 12
scraped: 2026-07-17
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMETRAMITESWEB_ASIGNACIONES.QVD

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-17

## Campos

| Campo | Tipo inferido | Ejemplos |
|---|---|---|
| `NRO_TRAMITE` | integer | 122968 · 123050 |
| `ID_SERVICIO_WEB` | integer | 7 · 3 |
| `FECHA_MOVIMIENTO` | date | 22/07/2019 16:49:21 · 23/07/2019 15:59:58 · 30/07/2019 17:47:34 · 24/07/2019 10:27:36 |
| `FECHA_MOVIMIENTO_CORTA` | date | 22/07/2019 · 23/07/2019 · 30/07/2019 · 24/07/2019 |
| `HORA_MOVIMIENTO` | text | 16:49:21 · 15:59:58 · 17:47:34 · 10:27:36 |
| `ESTADO_MOVIMIENTO` | text | PENDIENTE · FINALIZADA · APROBADA |
| `NRO_ASIGNACION` | integer | 1 |
| `USUARIO_ASIGNACION` | unknown |  |
| `ORDEN_ESTADO` | integer | 1 · 7 · 6 |
| `MAX_NRO_ASIGNACION` | integer | 1 |
| `FALTA_ESTADO_FIN_AGENTE` | flag | NO |
| `SECUENCIA_ASIG_INCOMPLETA` | flag | NO |

## Posible origen SIGEC

- [[Projects/sigec-explorer/tablas/ASIGNACIONES\|ASIGNACIONES]] — match parcial de nombre
- [[Projects/sigec-explorer/tablas/TRAMITES\|TRAMITES]] — match parcial de nombre

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
