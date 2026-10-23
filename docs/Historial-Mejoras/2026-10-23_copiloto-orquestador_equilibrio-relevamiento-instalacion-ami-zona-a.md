---
type: historial-mejora
fecha: 2026-10-23
agente: "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]]"
agentes_colaboradores:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
  - "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto de Sistemas EPEC]]"
proyecto: "[[docs/Proyectos/2026-10-21_despliegue-medidores-inteligentes-ami|Plan Maestro Despliegue AMI]]"
repositorio: "https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami"
tags:
  - #historial
  - #ami
  - #telemedicion
  - #relevamiento
  - #protelem
---

# 2026-10-23 · Equilibrio Relevamiento vs. Instalación vs. Stock AMI (Zona A)

## Contexto
Solicitud: medir la tasa real de instalación (Nov-2025..Abr-2026) y la tasa de relevamiento en Zona A (`georef.relevamiento`, SET `1000-%`), y evaluar el equilibrio con el stock de entregas de la Lic. 5573 con reserva de almacén del 10%.

## Fuentes (Oracle, snapshot 23/10/2026)
- Instalación: `XXSIGEC.EQUIPOS.EQP_FECHA_INSTAL` ⨝ `XXSIGEC.STOCK_EQUIPOS` (marcas `CLOU`, `NSEN`, validadas contra `srv_telemedible` SI/SN) ⨝ `SUCURSALES.ZON_CODIGO`.
- Relevamiento: `GEOREF.RELEVAMIENTO` · `COUNT(DISTINCT REL_MEDIDOR_ID)` por mes de `REL_FECHA_ALTA`.
- Backlog: relevados Zona A cuyo `SERVICIOS.SRV_TELEMEDIBLE` ∉ (SI, SN).

## Resultados
| Indicador | Valor |
|---|---:|
| Instalación MI Zona A | 7.559/mes |
| Relevamiento Zona A (misma ventana) | 3.620/mes |
| Backlog relevado pendiente | 162.156 |
| Stock neto Zona A (90%) | 316.980 |
| Cierre al ritmo histórico | Jul-2030 |
| Ritmo requerido (cierre Ene-2028) | 26.400 inst/mes · 12.900 relev/mes |

## Impacto
- Identifica la **mano de obra** como restricción dominante y un pico de **~234k medidores ociosos** en Dic-2027.
- Anticipa quiebres de stock (Feb/Ago/Nov-2027) si se alcanza el ritmo requerido.

## Supuestos pendientes de validación
Prorrateo SF 28k entre Sanxing E1/E2; no se modela consumo del backlog previo a Feb-2027 ni la regla SET OK.

## Artefactos
- Repo proyecto: `docs/05_equilibrio_relevamiento_instalacion_stock_zona_a.md`, `scripts/analisis_tasas_instalacion_relevamiento.py`, `scripts/simulacion_equilibrio_zona_a.py`, `data/simulacion_equilibrio_zona_a.csv`.
- Backups: `docs/Backups/2026-10-23_151127_despliegue-medidores-inteligentes-ami.md.bak`, `docs/Backups/2026-10-23_151127_00-Dashboard-MOC.md.bak`.

[[00-Dashboard-MOC]]
