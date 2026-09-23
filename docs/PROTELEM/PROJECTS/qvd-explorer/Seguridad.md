---
tipo: seguridad
estado: vigente
sensibilidad: interna
tags:
  - qvd-explorer
  - seguridad
---

# 🔒 Seguridad — qvd-explorer

> [!important] Default de sensibilidad de la colección `qvds/`
> **confidencial** — las fichas incluyen filas de ejemplo con datos reales de clientes
> (suministros, contratos, actas, marcas de fraude). Aplica el default de colección
> masiva de [[Convenciones]]: no se repite `sensibilidad` nota por nota; solo se
> marcaría una excepción más restrictiva.

- No compartir fichas de `qvds/` fuera del equipo sin regenerarlas sin ejemplos:
  `python main.py vault --no-samples` (la variante sin ejemplos puede tratarse
  como `interna`).
- El diccionario completo con ejemplos vive además en `data/` del repo
  `qs-scrapping`, que está fuera de git.

*Actualizado: 2026-07-17.*
