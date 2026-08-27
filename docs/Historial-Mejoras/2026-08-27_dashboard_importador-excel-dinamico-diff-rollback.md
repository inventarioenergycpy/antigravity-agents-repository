---
title: "Registro de Mejora: Plantillas Excel Dinámicas Adaptables, Motor de Diff Visual, Cargas Parciales y Rollback"
tags:
  - #historial
  - #dashboard
  - #excel
  - #diff
  - #rollback
  - #desarrollador-web-showroom
fecha: 2026-08-27
agente: "desarrollador-web-showroom"
---

# 📜 Registro de Mejora: Plantillas Excel Adaptables y Motor de Carga Inteligente con Diff y Rollback

## 🎯 Contexto y Necesidad
Para la administración ágil y masiva del [Dashboard de Gestión de Proyectos e Intermediación Financiera](https://inventarioenergycpy.github.io/dashboard-gestion-intermediacion/), los consultores requerían un sistema para:
1. Descargar plantillas en formato Excel estructuradas que representen fielmente el esquema vivo del sistema (oferta, demanda, deals y compliance), excluyendo fechas dinámicas de agenda pero incluyendo fechas contractuales clave (vigencias, vencimientos, *Tail Periods*).
2. Que la plantilla se auto-adapte de forma dinámica ante futuras modificaciones de campos o entidades sin necesidad de reescribir plantillas estáticas.
3. Analizar cualquier archivo `.xlsx` o `.csv` cargado, presentando un **Diff Visual** detallado que resalte altas, modificaciones y datos previos que serán sobrescritos.
4. Permitir **cargas parciales** mediante selección granular por checkboxes.
5. Garantizar resguardo total mediante **Snapshots Automáticos** previos a la aplicación de cambios y capacidad de **Rollback inmediato**.

---

## 🛠️ Acciones y Componentes Implementados

1. **Esquema Dinámico (`DATA_SCHEMA` en `js/store.js`)**:
   - Definición unificada de metadatos para `projects`, `interlocutors` y `deals`.
   - Método `getDynamicSchema()` para alimentar dinámicamente al generador de plantillas y al parser.

2. **Generador Dinámico de Plantillas (`js/modules/templateManager.js`)**:
   - Construcción automatizada de libros de trabajo Excel (`.xlsx`) con 4 hojas:
     - `1_PROYECTOS_OFERTA`
     - `2_INTERLOCUTORES_FONDOS`
     - `3_SUBGESTIONES_DEALS`
     - `INSTRUCCIONES_Y_CATALOGOS`

3. **Motor de Importación y Diff Visual (`js/modules/smartImporter.js`)**:
   - Parseo sintáctico mediante SheetJS.
   - Algoritmo de comparación campo por campo:
     - Identifica `[NUEVO]` (altas en verde).
     - Identifica `[MODIFICADO]` (alertas en ámbar con tabla comparativa de *Valor Anterior vs. Nuevo Valor*).
     - Identifica `[SIN CAMBIOS]`.
   - Modal interactivo `#modalSmartImport` con selección granular para cargas parciales.
   - Confirmación explícita previa al impacto.

4. **Motor de Snapshots y Rollback (`js/store.js` & `js/modules/settings.js`)**:
   - Guardado automático de puntos de restauración históricos con estadísticas.
   - Botón de reversión inmediata en Toast Notification y panel de historial de Snapshots.

---

## 🔗 Enlaces Relacionados
* [[00-Dashboard-MOC|Dashboard Principal MOC]]
* [[Proyectos/2026-08-23_dashboard-gestion-intermediacion|Ficha Técnica del Dashboard en Obsidian]]
* [Repositorio GitHub del Dashboard](https://github.com/inventarioenergycpy/dashboard-gestion-intermediacion)
