---
type: historial-mejora
agente: "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto de Sistemas EPEC]]"
fecha: 2026-10-21
tags:
  - #historial
  - #proyecto
  - #ami
  - #protelem
  - #subestaciones
  - #cronograma
---

# Registro de Proyecto: Creación del Repositorio Dedicado `PROTELEM-EPEC/despliegue-medidores-inteligentes-ami`

## 📝 Descripción del Hito
- **Contexto**: Aprobación de la planificación estratégica y cronograma con Verificación Primitiva (`VP 20d`) para el despliegue de **400.000 medidores inteligentes**, **6.000 concentradores de subestación** y **188.000 USE de mano de obra** adjudicados en la Licitación Pública N° 5573 (Resolución N° 0653/2026).
- **Acción Realizada**:
  1. Creación del nuevo repositorio dedicado bajo la organización **`PROTELEM-EPEC`**:
     - URL: `https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami`
     - Ruta local: `D:\Proyectos\despliegue-medidores-inteligentes-ami` (con enlace junction en el scratchpad del IDE).
  2. Generación de la estructura integral del proyecto:
     - `README.md`: Memoria técnica maestra de la licitación y reglas de compatibilidad.
     - `index.html`, `style.css`, `app.js`: Tablero ejecutivo interactivo con visualización de Gantt, simulador de capacidad de cuadrillas y diagnóstico por plan.
     - `data/`: Datasets JSON estructurados (`cronograma_entregas_ami.json`, `diagnostico_planes_capital.json`, `relevamiento_interior.json`).
     - `docs/`: 4 informes de ingeniería y resguardo digital de las OPs (27131, 27132, 27133, 27134) y PET de Mano de Obra en PDF.
     - `assets/img/`: Cartografía GIS de planes Zona A de Córdoba Capital y diagrama Gantt de Verificación Primitiva.
  3. Registro cruzado en la Bóveda Central de Obsidian:
     - Ficha técnica: `docs/Proyectos/2026-10-21_despliegue-medidores-inteligentes-ami.md`.
     - Actualización de índices en `docs/00-Dashboard-MOC.md` y `docs/PROTELEM/00-Indice-PROTELEM-EPEC.md`.

## 🎯 Impacto Operativo
- Establece la **Regla de Oro Operativa ("SET OK")**: Ninguna acometida se instala sin concentrador activo y reportando al Headend en la subestación asociada.
- Define el arranque escalonado: **Sanxing en Febrero 2027 (Plan 18 y San Francisco)** y **CLOU en Abril 2027 (Plan 6 y continuidad con Plan 4)**.
- Demuestra matemáticamente que con 50 cuadrillas contratistas (~16.000 medidores/mes) se garantiza stock continuo sin quiebres durante todo el ciclo 2027-2028.

## 🔗 Referencias
- [[00-Dashboard-MOC]]
- [[docs/PROTELEM/00-Indice-PROTELEM-EPEC|Índice PROTELEM-EPEC]]
- [[docs/Proyectos/2026-10-21_despliegue-medidores-inteligentes-ami|Ficha Técnica del Proyecto AMI]]
