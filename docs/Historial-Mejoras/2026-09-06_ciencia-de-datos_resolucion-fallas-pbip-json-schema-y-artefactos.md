---
type: historial-mejora
agente: "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
fecha: 2026-09-06
proyecto_asociado: "[[docs/Proyectos/2026-09-03_control-rutas-lecturas-nuevas-rutas|Control de Rutas de Lecturas - Nuevas Rutas]]"
backup_asociado: "[[docs/Backups/2026-09-06_121400_ciencia-de-datos_SKILL.md.bak|Backup Ciencia de Datos 2026-09-06]]"
tags:
  - #historial
  - #mejora
  - #powerbi
  - #pbip
  - #tmdl
  - #json-schema
  - #ciencia-de-datos
---

# 📋 Registro de Aprendizaje & Resolución de Fallas en Proyectos Power BI (`.pbip` / TMDL)

**Fecha**: 2026-09-06  
**Agente Responsable**: [[docs/Agentes/02-Ciencia-de-Datos|02 - Ciencia de Datos & Analytics BI]]  
**Proyecto Asociado**: [[docs/Proyectos/2026-09-03_control-rutas-lecturas-nuevas-rutas|Control de Rutas de Lecturas - Nuevas Rutas]]  
**Backup Preventivo**: [`docs/Backups/2026-09-06_121400_ciencia-de-datos_SKILL.md.bak`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Backups/2026-09-06_121400_ciencia-de-datos_SKILL.md.bak)

---

## 🛠️ Diagnóstico y Análisis Completo de Fallas Resueltas

Durante la inicialización y reconstrucción del proyecto Power BI Project (`.pbip` / TMDL) **Control de rutas de lecturas - Nuevas Rutas**, se identificaron y resolvieron **4 patrones de error sintáctico y estructural** en la especificación de Power BI Desktop (Release Abril 2026):

### 🔴 Incidente 1: `RequiredArtifactMissing: Path: definition.pbir`
- **Causa**: Al extraer el modelo semántico `.Dataset`, faltaba la carpeta `.Report` y el archivo manifestador `definition.pbir`.
- **Solución**: Se desempaquetó la estructura visual `Report/` desde el `.pbix` y se creó `definition.pbir` vinculando la carpeta del reporte con el conjunto de datos.

### 🔴 Incidente 2: `UnrecognizedSchemaVersion: Path: definition.pbir / definition.pbism`
- **Causa**: Incompatibilidad de URLs en `$schema`. Power BI Desktop Abril 2026 requiere patrones específicos:
  - `definition.pbir`: `https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/1.0.0/schema.json`
  - `definition.pbism`: `https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json` (respetando la **M** mayúscula en `semanticModel`).
- **Solución**: Ajuste de URLs canónicas con la nomenclatura exacta en los manifiestos JSON.

### 🔴 Incidente 3: `Property 'semanticModel' has not been defined and the schema does not allow additional properties`
- **Causa**: En el archivo raíz `.pbip`, se agregó por error la propiedad `"semanticModel"` dentro del arreglo `artifacts`. El esquema local `.pbip` sólo permite la propiedad `report` (`artifacts[0].report`).
- **Solución**: Estandarización del archivo raíz `.pbip` conteniendo únicamente la propiedad `report`.

### 🔴 Incidente 4: `Cannot read ... \model.bim. Missing required artifact 'model.bim'`
- **Causa**: Cuando la carpeta `.Dataset\` carecía del archivo descriptor `definition.pbi-dataset`, Power BI Desktop asumía un modelo legacy (TMSL/BIM) y buscaba `model.bim`.
- **Solución**: Creación del manifiesto `definition.pbi-dataset` dentro de `.Dataset\`, indicando que el modelo utiliza la especificación **TMDL** en la subcarpeta `definition/`.

### 🔴 Incidente 5: `Property '' has not been defined ... line 2, position 5`
- **Causa**: Clave de propiedad `$schema` escrita como cadena vacía `""` por reemplazos automáticos de formateadores JSON.
- **Solución**: Reescritura estricta de la clave `"$schema"` en todos los manifiestos.

### 🔴 Incidente 6: `DatasetDefinition: Required artifact is missing in ...\definition.pbism`
- **Causa**: En la versión de Power BI Desktop, la validación de artefactos de Fabric exige `definition.pbism` para el modelo semántico.
- **Solución**: Se creó `definition.pbism` con la especificación `semanticModel/definitionProperties/1.0.0/schema.json`.

### 🔴 Incidente 7: `Cannot read ... \model.bim. Missing required artifact 'model.bim'`
- **Causa**: Al remover `definition.pbi-dataset`, el componente `PBIProjectShredder` de Power BI Desktop no detectaba que la carpeta correspondía a un modelo TMDL y realizaba fallback buscando el archivo único legacy `model.bim`.
- **Solución**: Implementación de la **Estrategia Dual de Coexistencia de Manifiestos**: mantener de forma simultánea `definition.pbi-dataset` (usado por el *PBIProjectShredder* para identificar TMDL) y `definition.pbism` (usado por la validación de ítems de Fabric), sumado a la creación de un enlace unión de directorio (`mklink /J`) entre `.Dataset` y `.SemanticModel`.

### 🔴 Incidente 8: `Missing required artifact 'model.bim'` (Persistencia en Agosto 2026)
- **Causa**: El validador estricto `PBIProjectShredder.CheckRequiredArtifactAsync` verifica la existencia física de `model.bim` en `.Dataset\` antes de delegar la resolución al motor TMDL.
- **Solución**: Adición del manifiesto sintáctico `model.bim` con compatibilidad `1567` (`powerBI_V3`), conviviendo con `definition.pbism`, `definition.pbi-dataset` y la carpeta modular TMDL `definition/`.

### 🔴 Incidente 9: `FilePathTooLongError: La ruta de acceso especificada o el nombre de archivo son demasiado largos`
- **Causa**: `PBIProjectUtils.EnsureNotLong` valida que las rutas absolutas no excedan 260 caracteres. El nombre de proyecto original `Control de rutas de lecturas - Nuevas Rutas - proyecto.Report` concatenado con las subcarpetas profundas de visuales personalizados (`CustomVisuals\massFilter2E7137AC...\resources\massFilter2E7137AC....pbiviz.json`) alcanzaba 263 caracteres, provocando un desbordamiento de ruta.
- **Solución**: Refactorización de nombres a identificadores cortos y limpios (`Control_Rutas.pbip`, `Control_Rutas.Report`, `Control_Rutas.Dataset`), reduciendo la ruta máxima a 205 caracteres.

---

## 🏛️ Reglas Preventivas Incorporadas a la Habilidad del Agente

1. **Estructura Canónica Local PBIP**:
   - `root.pbip` ➔ Contiene únicamente el artefacto `report`.
   - `.Report\definition.pbir` ➔ Puntero `byPath` hacia `../<nombre>.Dataset`.
   - `.Dataset\definition.pbi-dataset` ➔ Esquema `pbimProperties` que activa el modo TMDL en `definition/`.
2. **Auditoría Sintáctica JSON**:
   - Verificar siempre que las claves de los objetos manifiestos contengan la cadena exacta `"$schema"`.

---

## 🔗 Referencias Cruzadas
- [[00-Dashboard-MOC]]
- [[docs/Agentes/02-Ciencia-de-Datos]]
- [[docs/Proyectos/2026-09-03_control-rutas-lecturas-nuevas-rutas]]
