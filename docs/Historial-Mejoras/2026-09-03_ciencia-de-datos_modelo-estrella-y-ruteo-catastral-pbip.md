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

# Registro de Mejora: Modelo Estrella en Power Query M y ReorganizaciÃ³n Catastral de Rutas PBIP

## ðŸ“Œ Contexto y DiagnÃ³stico
A requerimiento del usuario, se analizÃ³ el proyecto Power BI en modo desarrollador (`.pbip`) ubicado en `\\srvfs01\ProyectoTelemedicion\SQL\4_Power_BI_listos\Control de rutas de lecturas - Nuevas Rutas - proyecto.pbip`. Se identificÃ³ un modelo plano no normalizado en `GEOREF_VM_SUMINISTROS` (66 columnas) y limitaciones algorÃ­tmicas en la tabla de ruteo `TABLA_RUTAS_NUEVAS` que dejaba suministros huÃ©rfanos y dividÃ­a manzanas.

---

## ðŸ› ï¸ Implementaciones Realizadas

1. **IngenierÃ­a Dimensional en Lenguaje M**:
   - GeneraciÃ³n de 7 tablas de dimensiones normalizadas en Power Query M (`Dim_Red_Electrica`, `Dim_Tarifa`, `Dim_Geografia`, `Dim_Medidor`, `Dim_Catastro_Manzana`, `Dim_Ruta_Actual`, `Dim_Estado_Servicio`).
   - AplicaciÃ³n estricta del comentario del usuario: `Dim_Red_Electrica` compuesta exclusivamente por `DISTRIBUIDOR`, `SUBESTACION`, `SEA` (sin `PCT` ni `ORIGEN`).
   - Reemplazo de columnas textuales en la tabla de hechos por claves enteras `Int64` (`ID_*_KEY`), reduciendo la huella de memoria en VertiPaq.

2. **Algoritmo de Ruteo Geo-Catastral con Nomenclatura DC**:
   - UtilizaciÃ³n de la estructura catastral oficial completa (16 dÃ­gitos) tomando `LEFT(DC, LEN(DC) - 3)` como clave atÃ³mica de manzana.
   - Cobertura total de suministros (`CANT_SUMI >= 1`), eliminando casos huÃ©rfanos.
   - AgrupaciÃ³n ordenada por manzana dentro de cada `GRUPO_LECTURA` acotada a **180 suministros por ruta**.

3. **Mapeo de Relaciones TMDL y SincronizaciÃ³n**:
   - ActualizaciÃ³n de `relationships.tmdl` y `model.tmdl` con relaciones 1 a N unidireccionales activas.
   - Backup de seguridad de las definiciones previas en `scratch/definition_backup/`.
