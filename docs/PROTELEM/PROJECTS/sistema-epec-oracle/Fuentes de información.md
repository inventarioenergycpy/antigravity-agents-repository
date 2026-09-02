---
tipo: referencia
estado: vigente
sensibilidad: interna
tags:
  - sistema-epec-oracle
  - referencia
  - fuentes
  - epec
aliases:
  - Fuentes de información
  - Pliegos CIS (carpeta de red)
  - Origen del material sistema-epec-oracle
fecha: 2026-08-04
---

# 📥 Fuentes de información — Sistema EPEC Oracle

> [!abstract] Qué es esto
> De dónde sale todo el material de este proyecto: una carpeta de red que **no es un depósito de archivos sueltos**, sino un vault de Obsidian autónomo con su propio pipeline de procesamiento y un wiki mantenido por LLM. Esta nota documenta su ubicación, su estructura y las reglas para leerla sin romperla.

## 📍 Ubicación

```
\\srvfs01\ProyectoTelemedicion\42- Pliegos CIS
```

> [!warning] Solo lectura — innegociable
> En esa carpeta **no se escribe nada**: ni notas, ni archivos temporales, ni correcciones, ni salidas de análisis. Es material compartido de una licitación en curso y su carpeta `documentos/` es lo único irreproducible de todo el conjunto.
> Para trabajar sobre un archivo, se copia al staging propio: `d:\Usuarios\pberecibar\Desktop\proyectos\my-brain\projects\sistema-epec-oracle\`.

## 🧭 Qué es esa carpeta

Un vault de Obsidian completo, con `CLAUDE.md`, `README.md`, plantillas, scripts de extracción y un wiki de **65 artículos**. Sigue el patrón de base de conocimiento mantenida por LLM: el humano aporta las fuentes originales, el LLM extrae, resume y mantiene el wiki, y las preguntas se responden contra el wiki en vez de reabrir planillas de 11 MB.

```
documentos/  →   raw/   →  raw/consolidado/  →   wiki/   →  outputs/
(originales)   (texto)    (cruce de versiones)  (artículos) (respuestas)
```

| Carpeta | Qué hay | Quién escribe |
|---|---|---|
| `documentos/` | Las 9 fuentes originales (`.xlsx`, `.pdf`, `.pptx`, `.txt`) tal como llegaron | Solo el humano. **Intocable** |
| `raw/` | Las mismas fuentes volcadas a CSV/TXT en UTF-8 — 19 CSV + 3 TXT | Generado; se regenera entero con `scripts/extraer.py` |
| `raw/consolidado/` | `requerimientos.csv` / `.json` — una fila por requerimiento con estado, motivo, numeral de marzo y responsable | Generado por `scripts/consolidar.py` |
| `scripts/` | `extraer.py`, `consolidar.py`, `gen_articulos.py`, `gen_indices.py` | — |
| `wiki/` | Los 65 artículos organizados en 12 temas | Solo el LLM |
| `outputs/` | Respuestas y reportes generados | Vacía al 2026-08-04 |
| `templates/` | `wiki-articulo.md` | — |

**La carpeta intocable es `documentos/`, no `raw/`**: `raw/` se llama así porque es la materia prima que el wiki consume, pero es derivada y se reconstruye en un comando. Al revés no.

## 📚 Las fuentes originales

Nueve archivos en `documentos/`, en orden de prioridad. **La versión más nueva manda**; lo viejo queda como historial.

| # | Archivo | Fecha | Qué aporta |
|---|---|---|---|
| 0 | `Bill Factors_ORACLE.txt` | 2026-08-03 | Nota de proveedor sobre los *bill factors* de Oracle C2M/CCS. No compite con el Anexo: complementa el motor tarifario |
| 1 | `RFP Funcional EPEC_Ajustado0612_1143_OPEN.xlsx` | 2026-08-03 | **Versión vigente del Anexo I**: 35 grupos, 929 requerimientos, columna `Acción` (83 Eliminar / 10 Ajustar / 27 Incluir) con el motivo de cada recorte |
| 2 | `PliegoEPEC_v3_1337.pdf` | 2026-08-03 | El pliego: ecosistema y alcance objetivo, requerimientos por componente, fuera de alcance, faltantes |
| 3 | `Comparativa precios JB.xlsx` | 2026-04-08 | Precios PRETECO (cloud vs. híbrida), ESC Partners por etapa, gestión del cambio |
| 4 | `Propuesta nuevo sistema comercial.pptx` | 2026-04-08 | Propuestas PRETECO/ESC y OPEN, plazos (18 meses de proyecto / 20 de gestión del cambio) |
| 5 | `ppt_JB.pptx` | 2026-04-08 | Ídem + desafíos comerciales, indicadores estratégicos y objetivos 2026 |
| 6 | `Anexo I ..._TRABAJADO_12032026.xlsx` | 2026-03-19 | Anexo trabajado: `Cumplimiento`, `Novedad`, observaciones, responsables por sector, hojas `omnicanalidad` y `mdm` |
| 7 | `Puntos Omnicanalidad.xlsx` | 2026-03-19 | Numerales de omnicanalidad (grupos 29, 31, 32, 33, 35) |
| 8 | `Anexo I_Alance Funcional_CIS CRM WFM.xlsx` | 2026-03-12 | Línea base original del Anexo I |

Hay además dos archivos auxiliares en `documentos/`: `Cuadro_Plataforma_Vision360.md` (diagrama Mermaid que propone reemplazar el bloque *Portal de autogestión* del pliego por un bloque *Visión 360*) y su render en `.png`.

> [!info] La fecha del archivo en Windows no sirve
> Copiar un archivo resetea su `mtime`. El orden se mantiene **a mano** en la tabla de prioridad de `CLAUDE.md` y `README.md` de la fuente. Cuando llega un archivo nuevo, hay que ubicarlo explícitamente en esa tabla.

## ⚠️ Reglas de lectura

Cuatro reglas que la fuente documenta y que hay que aplicar en cualquier análisis:

1. **Nunca cruzar versiones por numeral.** Entre marzo y agosto de 2026, 489 de los 701 requerimientos identificables en ambas versiones cambiaron de numeral, y los grupos se renumeraron a partir del 25. El cruce se hace normalizando el texto. Es la regla más importante del corpus.
2. **El pliego cita la numeración vieja** (marzo), no la vigente. Al citarlo, verificar el texto.
3. **La hoja de responsables (`SECTOR POR FUNCIONALIDAD`) también usa la numeración vieja**: leerla por número directo asigna mal el responsable de once grupos.
4. **Los 27 requerimientos `Incluir` no tienen numeral** en la fuente. El wiki les asigna identificadores `N.s/n-K` que son **convención propia** y no deben citarse hacia afuera como si fueran del Anexo.

## 🚪 Puntos de entrada

Para responder cualquier pregunta, la ruta corta es:

| Archivo | Para qué |
|---|---|
| `wiki/INDEX.md` | Índice maestro por tema — empezar acá |
| `wiki/mapa-numerales.md` | Los 35 grupos con conteo de requerimientos, estado y artículo que los documenta |
| `wiki/gobernanza/cambios-entre-versiones.md` | **Leer antes de citar cualquier numeral** |
| `wiki/90-deuda-tecnica.md` | Duplicados, contradicciones y defectos de las fuentes |
| `wiki/91-preguntas-abiertas.md` | Lo que las fuentes no responden |
| `wiki/log.md` | Registro cronológico append-only de todo lo que se hizo |

## 📝 Observaciones sobre el estado de la carpeta

Detectadas al 2026-08-04, no corregidas (la carpeta es de solo lectura):

- **`Analisis Pliego EPEC - Oracle vs OPEN.html`** está en la raíz del vault, no en `outputs/`. Es un informe autocontenido que compara el pliego contra las propuestas de Oracle y OPEN (SmartFlex), agrupando los 902 requisitos de la hoja `entregable 12032026` en tres módulos (CIS, Visión 360, Trabajo en Campo). Es el archivo más reciente y **no figura en la tabla de prioridad** de la fuente.
- **`~$Anexo I_Alance Funcional_CIS CRM WFM _TRABAJADO_12032026.xlsx`** es un archivo de bloqueo de Excel que quedó huérfano en `documentos/`.
- **`documentos/Version 2026/`** y **`outputs/`** están vacías.

## Temas relacionados

- [[_index|MOC del proyecto]]
- [[Seguridad]]
- [[Fuentes de verdad]] — por qué esta nota **explica y enlaza** el wiki de red en vez de copiarlo

## Fuente

`\\srvfs01\ProyectoTelemedicion\42- Pliegos CIS` — `README.md`, `CLAUDE.md`, `wiki/INDEX.md`, `wiki/mapa-numerales.md` y `wiki/log.md`. Relevada el 2026-08-04.
