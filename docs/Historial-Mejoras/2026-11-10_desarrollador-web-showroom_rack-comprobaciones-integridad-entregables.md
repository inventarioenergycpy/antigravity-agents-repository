---
title: "Mejora: Incorporación del Rack de Comprobaciones de Integridad de Entregables Web (Zero-Undefined Guardrail)"
fecha: 2026-11-10
agente: "desarrollador-web-showroom"
arquetipo: "Arquetipo C (Finanzas / Showrooms / Web Apps)"
tipo_mejora: "QA y Blindaje Técnico de Entregables"
backups:
  - "docs/Backups/2026-11-10_114300_desarrollador-web-showroom_SKILL.md.bak"
  - "docs/Backups/2026-11-10_114300_03-Desarrollador-Web-Showroom.md.bak"
  - "docs/Backups/2026-11-10_114300_Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md.bak"
---

# 🛡️ Historial de Mejora: Rack de Comprobaciones de Integridad de Entregables Web

## 1. Contexto de la Falla Detectada y Causa Raíz
Durante la sesión de trabajo con el **Squad Ágil de Arquetipo C**, tras actualizar la cartera de inversiones a 25 proyectos e integrar el proyecto minero *Mina San Antonio*, se detectó una falla visual crítica en la tabla de proyectos del Dashboard (`#view-projects`) y en el Showroom Web:
- Todos los proyectos mostraban `undefined` en lugar de su título y descripción (excepto *Mina San Antonio*).
- **Causa Raíz:** En `projects-master.json`, los proyectos tenían `title` y `description` anidados únicamente dentro de `es: { title, ... }`, sin existir a nivel raíz. Al invocarse `store.js`, la asignación `existing.title = dp.title` sobreescribió la caché del navegador (`localStorage`) con `undefined`. Además, los renderizadores de la UI no contaban con fallbacks defensivos en cascada.

## 2. Pautas y Reglas Incorporadas al Agente 03 (`desarrollador-web-showroom`)

Se formalizó de manera mandatoria en la habilidad [`.agents/skills/desarrollador-web-showroom/SKILL.md`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/.agents/skills/desarrollador-web-showroom/SKILL.md), en la ficha técnica [`docs/Agentes/03-Desarrollador-Web-Showroom.md`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Agentes/03-Desarrollador-Web-Showroom.md) y en el rector [`docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md) el **Rack de 5 Comprobaciones Técnicas de Control**:

1. **Zero-Undefined Guardrail (Fallbacks Defensivos en Cascada):**
   - Prohibición estricta de interpolar `${item.prop}` sin fallback defensivo multinivel:
     `item.title || (item.es && item.es.title) || (item.en && item.en.title) || item.id || 'Sin título'`
   - Barrido post-build sobre `bundle.js`, `main.js` y el DOM asegurando cero ocurrencias literales de `"undefined"` o `"NaN"`.
2. **Contrato de Esquemas y Dualidad Raíz/Bilingüe (SSOT):**
   - Garantía de que todo catálogo o entidad JSON conserve los atributos primarios (`title`, `description`, `status`, `category`) tanto en la raíz como dentro de bloques idiomáticos específicos (`es`/`en`).
3. **Resiliencia de Persistencia y Auto-Sanación (`localStorage` Self-Healing):**
   - Rutina obligatoria en `loadData()` que detecte valores corruptos o nulos en la caché del navegador del cliente y los cure reactivamente contra los datos semilla actualizados.
4. **Sincronización Multicanal y Mapeo Biunívoco de Estados:**
   - Mapeo biunívoco riguroso entre emisor y receptor (ej. `bloqueado_por_gestion` -> `tramite` 🟡), con propagación simultánea por `BroadcastChannel` y `window.onstorage`.
5. **Batería de Pruebas Deterministas Automatizadas (Pre-Deploy Test Suite):**
   - Script ejecutable (`test_sync_integrity.py` o suite de test) obligatorio previo a cualquier commit o despliegue con validación estricta de `Exit Code 0`.

## 3. Impacto en la Operación de Entregables Futuros
- **Prevención Absoluta de Regresiones:** Ningún entregable web podrá pasar a producción si presenta inconsistencias de datos, renderizado de `undefined` o discrepancias matemáticas de cartera.
- **Estandarización del Control de Calidad:** Tanto el Project Manager (PM) como los Operadores 1 y 3 del Squad contarán con este rack normativo como criterio de aceptación (Definition of Done) en la Instancia 1 (Técnica) e Instancia 3 (UX) del Triple QA.

## 4. Archivos de Respaldo Preventivo (Rollback Protection)
- [`docs/Backups/2026-11-10_114300_desarrollador-web-showroom_SKILL.md.bak`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Backups/2026-11-10_114300_desarrollador-web-showroom_SKILL.md.bak)
- [`docs/Backups/2026-11-10_114300_03-Desarrollador-Web-Showroom.md.bak`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Backups/2026-11-10_114300_03-Desarrollador-Web-Showroom.md.bak)
- [`docs/Backups/2026-11-10_114300_Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md.bak`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Backups/2026-11-10_114300_Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md.bak)
