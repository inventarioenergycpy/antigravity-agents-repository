---
title: "Creación e Integración del Agente 11: Copiloto Orquestador y Selector Dinámico de Habilidades"
tags:
  - #historial-mejoras
  - #agente
  - #copiloto
  - #orquestador
  - #google-standards
  - #skills
created: 2026-10-05
---

# 📜 Registro Histórico: Creación del Agente 11 (Copiloto Orquestador de Skills)

- **Fecha de Implementación**: 2026-10-05
- **Identificador de Habilidad**: `copiloto-orquestador-skills`
- **Ubicación de Habilidad**: `.agents/skills/copiloto-orquestador-skills/SKILL.md`
- **Ficha Técnica**: `docs/Agentes/11-Copiloto-Orquestador-de-Skills.md`
- **Backup Preventivo**: `docs/Backups/2026-10-05_072900_copiloto-orquestador-skills_SKILL.md.bak`

---

## 🎯 Contexto y Justificación
Se requería dotar al entorno Antigravity IDE de un **Copiloto Orquestador Central** capaz de:
1. Evaluar semánticamente la naturaleza de cualquier consulta o requerimiento.
2. Seleccionar y despachar de forma dinámica la habilidad especialista idónea del catálogo existente (Agentes 01 al 10 y habilidades satélite).
3. Ante consultas sobre dominios inéditos o no cubiertos, activar un protocolo de investigación en estándares oficiales de **Google** (`agy-customizations`, Google AI / DeepMind framework) y de desarrolladores reconocidos (Anthropic, OpenAI, Microsoft AutoGen/Semantic Kernel, LangChain), para concebir, diseñar y validar una nueva habilidad bajo la **Metodología en 6 Etapas**.

---

## 🔬 Metodología Aplicada

1. **Fase 1 (Investigación)**: Revisión de directivas en `agy-customizations`, patrones de *Dynamic Dispatching*, *Tool Use Orchestration* y *Progressive Disclosure*.
2. **Fase 2 (Diseño Pre-Implementación)**: Definición de la arquitectura de decisión en 2 vías (Enrutamiento vs. Creación de Skills basada en estándares Google/Expertos).
3. **Fase 3 (Diagramación & Pruebas)**: Flujo de enrutamiento en Mermaid, matrices de clasificación temática y mapeo de fuentes de referencia.
4. **Fase 4 (Prueba Piloto)**: Generación de la especificación técnica completa, validación de sintaxis YAML frontmatter y presentación al usuario.
5. **Fase 5 (Pruebas Finales)**: Validación de permisos, trazabilidad en el workspace y coherencia relacional en Obsidian.
6. **Fase 6 (Auto-Documentación)**: Creación de ficha técnica en `docs/Agentes/`, actualización del tablero maestro `docs/00-Dashboard-MOC.md`, respaldo preventivo en `docs/Backups/` y este registro histórico.

---

## 🔗 Referencias Relacionales
- [[00-Dashboard-MOC]]
- [[Agentes/11-Copiloto-Orquestador-de-Skills|Ficha Técnica Agente 11]]
- [[docs/Backups/README|Bóveda de Backups]]
