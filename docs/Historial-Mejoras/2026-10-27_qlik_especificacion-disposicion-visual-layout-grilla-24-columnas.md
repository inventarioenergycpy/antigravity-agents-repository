---
title: "Historial de Mejoras: Especificación y Codificación de Disposición Visual Qlik Sense (Equivalencia Power BI)"
tags:
  - #historial
  - #qlik-sense
  - #power-bi
  - #layout
  - #grid-24
  - #wireframe
  - #automation
created: 2026-10-27
updated: 2026-10-27
---

# 📜 Historial de Mejoras: Especificación y Codificación de Disposición Visual en Qlik Sense
**Fecha**: 2026-10-27  
**Proyecto**: Migración Power BI a Qlik Sense - Tablero MI Zona A  
**Squad Responsable**: Copiloto Orquestador (Agente 11 / PM) & Especialista en Ciencia de Datos (Agente 02)

---

## 🎯 1. Objetivo de la Intervención
Establecer un método determinista y automatizado para codificar la disposición visual de los gráficos en Qlik Sense de forma 100% equivalente al reporte nativo de Power BI (`Tablero MI - Zona A.pbip`), resolviendo la colocación de más de 80 componentes visuales distribuidos en 7 páginas corporativas.

---

## ⚙️ 2. Acciones y Desarrollos Ejecutados

1. **Ingeniería Inversa de Coordenadas PBIP**:
   - Inspección y extracción automática de las 7 páginas en `Tablero MI - Zona A.Report/definition/pages/*`.
   - Conversión matemática de coordenadas cartesianas de Power BI (`x`, `y`, `width`, `height`) a la grilla nativa de **24 columnas** de Qlik Sense (`col`, `row`, `colspan`, `rowspan`).

2. **Entregables de Codificación y Automatización**:
   - [`scripts/extraer_layout_pbip_a_qlik.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/extraer_layout_pbip_a_qlik.py): Motor Python de extracción y mapeo.
   - [`D:\Usuarios\jidiaz\Downloads\qlik_sense_sheets_layout_specification.json`](file:///D:/Usuarios/jidiaz/Downloads/qlik_sense_sheets_layout_specification.json): Catálogo JSON con los metadatos completos por visual y hoja.
   - [`scripts/aplicar_layout_qlik_engine.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/aplicar_layout_qlik_engine.py): Conector QIX Engine API vía WebSocket para inyección automática en `.qvf`.
   - [`D:\Usuarios\jidiaz\Downloads\qlik_sense_app_sheets_bundle.json`](file:///D:/Usuarios/jidiaz/Downloads/qlik_sense_app_sheets_bundle.json): Bundle Qlik GenericObjects de todas las hojas.
   - [`D:\Usuarios\jidiaz\Downloads\viewer_layout_qlik.html`](file:///D:/Usuarios/jidiaz/Downloads/viewer_layout_qlik.html): Visor web interactivo de la grilla de 24 columnas con selector de hojas, inspección de tiles y descarga.

3. **Documentación Técnica Maestra**:
   - Creado el blueprint con matrices ASCII y tablas de correspondencia en [`docs/Proyectos/2026-10-27_especificacion-disposicion-visual-qlik-sense.md`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Proyectos/2026-10-27_especificacion-disposicion-visual-qlik-sense.md).
