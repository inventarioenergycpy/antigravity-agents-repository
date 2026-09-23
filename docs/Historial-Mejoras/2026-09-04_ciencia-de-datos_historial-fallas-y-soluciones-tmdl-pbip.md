---
type: historial-mejora
agente: "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
fecha: 2026-09-04
proyecto_asociado: "[[docs/Proyectos/2026-09-03_control-rutas-lecturas-nuevas-rutas|Control de Rutas de Lecturas - Nuevas Rutas]]"
tags:
  - #historial
  - #fallas
  - #soluciones
  - #powerbi
  - #pbip
  - #tmdl
  - #utf8
  - #ciencia-de-datos
---

# 📋 Historial de Fallas, Diagnósticos y Soluciones Técnicas (TMDL / PBIP)

**Proyecto Asociado**: [[docs/Proyectos/2026-09-03_control-rutas-lecturas-nuevas-rutas|Control de Rutas de Lecturas - Nuevas Rutas (Power BI PBIP)]]  
**Agente Responsable**: [[docs/Agentes/02-Ciencia-de-Datos|02 - Ciencia de Datos & Ingeniero de Analytics BI]]  
**Ruta del PBIP**: `\\srvfs01\ProyectoTelemedicion\SQL\4_Power_BI_listos\Control de rutas de lecturas - Nuevas Rutas - proyecto.pbip`

---

## 🛠️ Registro Cronológico de Incidentes

### 🔴 Incidente 1: Rechazo de Deserialización por Detección de UTF-8 BOM
* **Fecha**: 2026-09-03 (16:30 ART)
* **Estado**: ✅ **RESUELTO**
* **Mensaje de Error**:
  ```text
  Cannot read '\\...\definition\model.tmdl'. Only text with UTF8 encoding without BOM (byte order marks) is supported. Detected BOM: 'UTF-8'
  ```
* **Diagnóstico y Causa Raíz**:
  El cmdlet `Set-Content -Encoding UTF8` de PowerShell añade por defecto el preámbulo Byte Order Mark (BOM: `0xEF 0xBB 0xBF`). El parser nativo de TMDL de Power BI Desktop (versión Julio 2026) requiere estrictamente texto UTF-8 sin BOM (UTF-8 No BOM).
* **Solución Propuesta & Ajuste**:
  Se implementó la persistencia de archivos mediante el ensamblado .NET `[System.IO.File]::WriteAllBytes` con un codificador `System.Text.UTF8Encoding($false)`, eliminando cualquier preámbulo BOM de los archivos `.tmdl`.

---

### 🔴 Incidente 2: Error de Resolución en Jerarquía de Fechas de Variación
* **Fecha**: 2026-09-03 (16:32 ART)
* **Estado**: ✅ **RESUELTO**
* **Mensaje de Error**:
  ```text
  La propiedad DefaultHierarchy del objeto variación Variacion en la columna FECHA_INICIO de la tabla GEOREF_VM_SUMINISTROS hace referencia a un objeto que no se puede encontrar
  ```
* **Diagnóstico y Causa Raíz**:
  En la tabla calculada local `LocalDateTable_2e2ab0a2-e80e-4686-9c9d-8fb43057a58c.tmdl`, la jerarquía automática estaba declarada con tilde (`hierarchy 'Jerarquía de fechas'`). En la tabla de hechos `GEOREF_VM_SUMINISTROS.tmdl`, la referencia fue escrita sin tilde (`'Jerarquia de fechas'`). TMDL es sensible a mayúsculas, minúsculas y caracteres diacríticos, provocando una falla de puntero en el deserializador.
* **Solución Propuesta & Ajuste**:
  Se estandarizó la referencia en `GEOREF_VM_SUMINISTROS.tmdl` a `variation Variación` y `defaultHierarchy: LocalDateTable_2e2ab0a2-e80e-4686-9c9d-8fb43057a58c.'Jerarquía de fechas'`.

---

### 🔴 Incidente 3: Falla de Deserialización por Doble Codificación UTF-8 (*Mojibake*)
* **Fecha**: 2026-09-04 (07:19 ART)
* **Estado**: ✅ **RESUELTO**
* **Mensaje de Error**:
  ```text
  La propiedad DefaultHierarchy del objeto variación VariaciÃ³n en la columna FECHA_INICIO de la tabla GEOREF_VM_SUMINISTROS hace referencia a un objeto que no se puede encontrar
  ```
* **Diagnóstico y Causa Raíz**:
  Durante la manipulación previa de cadenas con conversiones implícitas de terminal, los caracteres diacríticos (`ó`, `í`) sufrieron doble codificación UTF-8:
  * `ó` (`0xC3 0xB3`) se transformó en `0xC3 0x83 0xC2 0xB3` (`"Ã³"`).
  * `í` (`0xC3 0xAD`) se transformó en `0xC3 0x83 0xC2 0xAD` (`"Ã­"`).
  Al deserializar el archivo, Power BI interpretaba literalmente el nombre `VariaciÃ³n` y la jerarquía `JerarquÃ­a de fechas`, perdiendo la concordancia con la tabla de fechas.
* **Solución Propuesta & Ajuste**:
  1. Se programó un escáner binario que recorrió los 22 archivos `.tmdl` identificando secuencias `0xC3 0x83` y `0xC3 0x82`.
  2. Se reparó `GEOREF_VM_SUMINISTROS.tmdl` y comentarios en `TABLA_RUTAS_NUEVAS.tmdl`, reescribiendo los bytes limpios correspondientes a UTF-8 nativo.
  3. Se validó la igualdad binaria exacta entre la definición de la jerarquía en `LocalDateTable_2e2ab0a2...` y la referencia en `GEOREF_VM_SUMINISTROS`.
  4. Se creó copia de respaldo limpia y verificada en `scratch/definition_clean`.

---

## 🛡️ Medidas Preventivas Establecidas
1. **Regla de Persistencia TMDL**: Todo archivo `.tmdl` debe crearse y modificarse exclusivamente mediante `System.Text.UTF8Encoding($false)` sin BOM.
2. **Validación Pre-Despliegue**: Antes de notificar al usuario, ejecutar script de verificación binaria que audite la ausencia de BOM (`0xEF 0xBB 0xBF`) y ausencia de doble codificación (`0xC3 0x83`).
