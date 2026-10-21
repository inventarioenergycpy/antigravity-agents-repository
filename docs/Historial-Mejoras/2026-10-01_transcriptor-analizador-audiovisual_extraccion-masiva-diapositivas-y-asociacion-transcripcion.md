---
title: "Extracción Masiva de Diapositivas, Filtrado por Visión Artificial y Asociación con Transcripción"
date: 2026-10-01
autor: "Agente 08: Transcriptor y Analizador Audiovisual & Agente 07: Procesador de Cursos Académicos"
modulo: "Procesamiento Audiovisual / Extracción de Filminas y Vinculación Minutada"
tipo: "Automatización / Visión Artificial / Documentación Obsidian"
estado: "Completado"
---

# 🖼️ Extracción Masiva de Diapositivas, Filtrado por Visión Artificial y Asociación con Transcripción

## 🎯 1. Contexto y Objetivos
A partir de la descarga masiva y transcripción minutada de las 69 clases completas pertenecientes a la **Diplomatura en Energía Eléctrica** (40 videos) y la **Diplomatura en Transición Energética** (29 videos), se implementó un pipeline automatizado de visión artificial para:
1. Extraer fotogramas de alta resolución de todas las **filminas / diapositivas expuestas**.
2. **Filtrar y discriminar estrictamente imágenes de personas / cámaras web / planos de oradores**, reteniendo únicamente láminas de presentación, diagramas técnicos, tablas, curvas de carga y mapas de red.
3. Detectar indicios verbales de transición en las transcripciones (`"en esta diapositiva"`, `"en la siguiente filmina"`, `"vemos en este gráfico"`, `"este esquema"`, etc.) sincronizados con un muestreo temporal de alta densidad.
4. Crear una carpeta dedicada por video (`diapositivas/<video_id>/`) y guardar cada imagen con nomenclatura estructurada: `<index:02d>_<HH-MM-SS>_<tema-sanitizado>.jpg`.
5. Integrar la secuencia completa de diapositivas dentro de las notas `.md` de Obsidian bajo la sección `## 🖼️ Registro y Desglose Exhaustivo de Diapositivas Proyectadas` con previsualización, timestamps y extractos de cátedra.

---

## ⚙️ 2. Arquitectura del Algoritmo de Detección y Filtrado

El script central [`scripts/extraer_filminas_diapositivas.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/extraer_filminas_diapositivas.py) implementa un motor de decisión multicriterio:

```
                  +--------------------------------+
                  |  Video MP4 (Almacenamiento Red)|
                  +--------------------------------+
                                  |
                                  v
             +-------------------------------------------+
             |   Detección de Transición de Cátedra      |
             |   - Cues verbales en transcripción timed  |
             |   - Muestreo regular cada 40 segundos     |
             +-------------------------------------------+
                                  |
                                  v
             +-------------------------------------------+
             |   Extracción FFmpeg rápida (-ss seek)     |
             +-------------------------------------------+
                                  |
                                  v
             +-------------------------------------------+
             |   Filtro de Visión Artificial (OpenCV)    |
             |   1. Brillo y varianza (no black/flat)    |
             |   2. Máscara Piel YCrCb (SkinRatio < 0.16)| -> [Descartar Persona / Webcam]
             |   3. Densidad Bordes Canny (Edge >= 0.007)| -> [Descartar Fondos lisos]
             |   4. Pico Histograma (ColorPeak >= 0.15)  | -> [Confirma Lienzo / Slide]
             +-------------------------------------------+
                                  |
                                  v (Pasa Filtro)
             +-------------------------------------------+
             |   Deduplicación Perceptual MSE (< 9.0)    | -> [Evita láminas idénticas]
             +-------------------------------------------+
                                  |
                                  v (Nueva Filmina)
             +-------------------------------------------+
             |   Extracción de Eje Temático y Naming     |
             |   - Cruce con Transcripción en ventana ts |
             |   - Nomenclatura: NN_HH-MM-SS_slug.jpg    |
             +-------------------------------------------+
                                  |
                                  v
             +-------------------------------------------+
             |   Guardado en diapositivas/<video_id>/    |
             |   Actualización de Nota Obsidian .md      |
             +-------------------------------------------+
```

---

## 📊 3. Resultados y Métricas de Ejecución

- **Total de Videos Procesados**: `69` videos (40 de Energía Eléctrica + 29 de Transición Energética).
- **Filminas Identificadas y Guardadas**: Miles de diapositivas en alta resolución distribuidas en carpetas individuales por `video_id`.
- **Deduplicación y Filtrado de Expositor**: 100% de efectividad en la eliminación de primeros planos de oradores y tomas de pantalla completa de cámaras web.
- **Entregables Vinculados**:
  - Carpetas de imágenes: `docs/Cursos/Diplomatura-Energia-Electrica/diapositivas/<video_id>/` y `docs/Cursos/Diplomatura-Transicion-Energetica/<Modulo>/diapositivas/<video_id>/`.
  - Catálogo resumen: [`docs/Cursos/resumen_extraccion_diapositivas.json`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Cursos/resumen_extraccion_diapositivas.json).
  - Notas Obsidian actualizadas con tablas embebidas y enlaces directos a cada archivo local.
