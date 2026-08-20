---
title: "2026-08-20 Ciencia de Datos — Integración de Estrategias de Ingeniería Inversa y Documentación TMDL / PBIP"
type: mejora
agente: "ciencia-de-datos"
tags:
  - #mejora
  - #ciencia-de-datos
  - #powerbi
  - #pbip
  - #tmdl
  - #dax
  - #protelem
created: 2026-08-20
---

# 📜 Registro de Mejora Continua: Ciencia de Datos — Ingeniería Inversa de Modelos TMDL y Documentación PBIP

- **Fecha**: 2026-08-20
- **Agente Responsable**: `ciencia-de-datos`
- **Archivo de Backup Preventivo**: `[[docs/Backups/2026-08-20_151500_ciencia-de-datos_SKILL.md.bak]]`
- **Skill Actualizado**: `[[.agents/skills/ciencia-de-datos/SKILL.md]]`
- **Proyecto Vinculado**: `[[docs/Proyectos/2026-08-20_protelem-indicadores-gerencia-comercial|PROTELEM - Indicadores Gerencia Comercial]]`

---

## 🎯 Contexto y Justificación

Durante la sesión de trabajo se requirió el análisis exhaustivo, desensamblado e ingeniería inversa del proyecto **`PROTELEM - Indicadores Gerencia Comercial.pbip`** y su modelo semántico TMDL, replicando el estándar y profundidad del documento de referencia **`Ordenativos_Todas_Zona_Informe (1).pdf`**.

Para asegurar que el agente mantenga esta capacidad avanzada en tareas futuras, se estructuraron y formalizaron las estrategias metodológicas aplicadas.

---

## 🛠️ Estrategias y Técnicas Incorporadas al Perfil

1. **Desensamblado Sistemático de Modelos Semánticos TMDL**:
   - Inspección y parseo recursivo de archivos `.tmdl` para extraer particiones de ingesta M, columnas nativas, columnas calculadas, jerarquías de medidas y metadatos.
2. **Auditoría de Orígenes Híbridos y Conexiones DirectQuery**:
   - Mapeo de endpoints de **Microsoft Fabric Data Warehouse** (`WH_FACTURACION`, `DW_INDICADORES`, `datos_generales`) combinados con ingestas programadas desde **SharePoint Online**.
3. **Identificación de Patrones de Claves Sintéticas Compuestas**:
   - Detección de claves de enlace como `KEY_ZON_LOC_SCF`, `KEY_TAR_CLA_TEN_TC_TG` y `KEY_ZON_PLAN_R_RF_GF` para cruzar hechos heterogéneos con dimensiones maestras `sigec_idx_*`.
4. **Análisis de Lógica Temporal y Desfases Contables**:
   - Interpretación de desfases relacionales en dimensiones calendario (`Año#Mes (-1)` y `Año#Mes (-2)`) para alinear ciclos comerciales y auditorías de facturación cerrada.
5. **Catálogo de Medidas DAX y Configuración de Semáforos**:
   - Desglose de fórmulas DAX operativas, ratios interanuales (`Ant Year`) y cuartetos de límites (Amarillo, Rojo, Límite Superior) para control de tacómetros (gauges).
6. **Auditoría de la Capa de Visualización (`.Report`)**:
   - Extracción de metadata de páginas (`page.json`) y definición de visuales (`visual.json`) para documentar tableros tipo Cockpit gerencial.
7. **Estructuración del Informe Técnico de Funcionamiento (Estilo Pedro Berecibar / PROTELEM)**:
   - Presentación estandarizada en 4 etapas secuenciales (Extracción, Consolidación, Enriquecimiento, Presentación) con diagnósticos de calidad técnica y catálogo de código fuente en anexos.

---

## 🔗 Referencias Relacionales
- [[00-Dashboard-MOC]]
- [[docs/Proyectos/2026-08-20_protelem-indicadores-gerencia-comercial|Ficha del Proyecto PROTELEM Indicadores Comercial]]
- [[docs/Agentes/02-Ciencia-de-Datos|Ficha Técnica del Agente de Ciencia de Datos]]
