---
title: "Ficha Técnica: Planificador y Diseñador de Agentes AI"
type: agente
agente: "planificador-agentes"
tags:
  - #agente
  - #planificador
  - #arquitectura
  - #investigacion
  - #pruebas-piloto
  - #wbs
  - #clarification-gate
  - #stage-gate
created: 2026-08-14
updated: 2026-10-28
---

# 📐 Ficha Técnica: Planificador y Diseñador de Agentes AI

- **Identificador de Skill**: `planificador-agentes`
- **Ubicación de Habilidad**: [`.agents/skills/planificador-agentes/SKILL.md`](file:///D:/Proyectos/antigravity-agents-repository/.agents/skills/planificador-agentes/SKILL.md)
- **Rol Principal**: Investigación de fuentes verídicas, diseño pre-implementación, estructuración jerárquica WBS (Etapas, Tareas y Subtareas), formulación de compuertas de clarificación interactiva y validación continua Stage-Gate con Triple QA para proyectos complejos y nuevos agentes.

---

## 🧭 Capacidades Clave

1. **Investigación en Fuentes Confiables del Estado del Arte**:
   - Evaluación rigurosa de documentación oficial (Google DeepMind, Anthropic, Microsoft AutoGen, PMI Agile) para respaldar el diseño de sistemas y flujos de trabajo.
2. **Compuerta de Clarificación e Inception**:
   - Formulación de cuestionarios de descubrimiento (preguntas de planificación y verificación) para fijar el *Definition of Ready (DoR)*.
3. **Diagramación Jerárquica WBS y Contratos Tipados**:
   - Desglose modular de objetivos en Etapas, Tareas y Subtareas atómicas con precondiciones, postcondiciones y contratos Blackboard.
4. **Compuertas de Validación Stage-Gate (Triple QA)**:
   - Configuración de compuertas obligatorias de paso (Técnico determinista, Negocio/Dominio y UX) asegurando el *Definition of Done (DoD)*.
5. **Documentación Holística y Auto-Documentación**:
   - Registro automático de cada proceso, backup preventivo `.bak` en `docs/Backups/` y notas históricas en `docs/Historial-Mejoras/`.

---

## 🔗 Referencias Relacionales
- [[00-Dashboard-MOC]]
- [[docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores|Protocolo Rector Multi-Agente PM y 3 Operadores]]
- [[docs/Proyectos/README|Índice de Proyectos]]
- [[docs/Backups/README|Bóveda de Backups]]
- [[docs/Historial-Mejoras/README|Historial de Mejoras]]