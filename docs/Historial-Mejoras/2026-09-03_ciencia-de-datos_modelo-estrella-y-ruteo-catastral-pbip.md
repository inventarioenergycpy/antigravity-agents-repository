---
type: historial-mejora
agente: "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
fecha: 2026-09-03
proyecto_asociado: "[[docs/Proyectos/2026-09-03_control-rutas-lecturas-nuevas-rutas|Control de Rutas de Lecturas - Nuevas Rutas]]"
tags:
  - #historial
  - #mejora
  - #powerbi
  - #pbip
  - #modelo-estrella
  - #ciencia-de-datos
---

# Registro de Mejora: Ajuste de Dimensiones y Ruteo por Distrito, Grupo y Manzana DC

## ðŸ“Œ Modificaciones Confirmadas
1. **Descarte de `Dim_Catastro_Manzana`**: Se mantuvo la informaciÃ³n parcelaria y catastral directamente en la tabla de hechos `GEOREF_VM_SUMINISTROS`.
2. **`Dim_Red_Electrica` Depurada**: Exclusivamente contiene `DISTRIBUIDOR`, `SUBESTACION` y `SEA`. Los campos `PCT` y `ORIGEN` permanecen en la tabla de hechos.
3. **`TABLA_RUTAS_NUEVAS`**: AgrupaciÃ³n canÃ³nica por `DISTRITO`, `GRUPO_LECTURA` y `DESCRIPCION_MANZANAS_CATASTRAL`, ordenamiento jerÃ¡rquico y particiÃ³n en rutas de hasta 180 suministros sin exclusiones (`CANT_SUMI >= 1`).
