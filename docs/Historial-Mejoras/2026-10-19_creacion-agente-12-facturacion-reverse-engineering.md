---
title: "Creación e Integración del Agente 12: Especialista en Reverse Engineering de Facturación EPEC"
tags:
  - #historial-mejoras
  - #agente
  - #facturacion
  - #reverse-engineering
  - #epec
  - #sigec
  - #tarifas
  - #simulador
  - #protelem
created: 2026-10-19
---

# 📜 Registro Histórico: Creación del Agente 12 (Facturación Reverse Engineering)

- **Fecha de Implementación**: 2026-10-19
- **Identificador de Habilidad**: `facturacion-reverse-engineering`
- **Ubicación de Habilidad**: `.agents/skills/facturacion-reverse-engineering/SKILL.md`
- **Ficha Técnica en Obsidian**: `docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering.md`
- **Ficha de Proyecto Dedicado**: `docs/Proyectos/2026-10-19_facturacion-reverse-engineering.md`
- **Repositorio Remoto Upstream**: `https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering.git`
- **Backup Preventivo**: `docs/Backups/2026-10-19_160800_facturacion-reverse-engineering_SKILL.md.bak`

---

## 🎯 Contexto y Justificación
Se requería formalizar un perfil de agente altamente especializado para la **ingeniería inversa, auditoría y simulación exacta de la facturación comercial SIGEC de EPEC**.  
Para asegurar que este agente mantenga su validez técnica y precisión matemática **para la posteridad**, se implementó un **protocolo mandatorio de arranque (Fase 0)** que comprueba y sincroniza de forma automática el repositorio local con el último commit del repositorio upstream oficial de GitHub (`PROTELEM-EPEC/facturacion-reverse-engineering`, rama `main`).

---

## 🔬 Metodología Estandarizada en 6 Etapas

1. **Fase 1 (Investigación en Fuentes Confiables)**:
   - Análisis de la arquitectura del repositorio `D:\Proyectos\facturacion-reverse-engineering`, su aislamiento de dependencias (`CLAUDE.md`, `DESIGN.md`), el motor JS puro (`web/motor.js`), las 31 tablas de SIGEC (`docs/glosario_tablas.md`) y la suite de 13 consultas maestras SQL (`docs/modelo_factura_documentado.sql`).
2. **Fase 2 (Diseño Pre-Implementación & Protocolo de Sincronización)**:
   - Diseño del hook de control de arranque que ejecuta `git fetch origin main`, verifica los hashes de commit (`HEAD` vs `origin/main`) y previene el uso de cuadros tarifarios obsoletos.
3. **Fase 3 (Diagramación & Scripting de Sincronización)**:
   - Programación de `.agents/skills/facturacion-reverse-engineering/scripts/sync_upstream.py` con soporte para validación silenciosa (`--quiet`) y actualización automática fast-forward (`--pull`).
4. **Fase 4 (Prueba Piloto & Ejecución Real)**:
   - Ejecución del script de sincronización contra `D:\Proyectos\facturacion-reverse-engineering`, confirmando coincidencia exacta en el commit `1bf97d8fb1` del upstream remoto.
5. **Fase 5 (Validación del Modelo Final)**:
   - Verificación de enlaces, integridad de rutas relativas y compatibilidad con el entorno multi-repositorio.
6. **Fase 6 (Auto-Documentación e Histórico en Obsidian)**:
   - Generación de `SKILL.md`, ficha técnica del agente en `docs/Agentes/`, ficha de proyecto en `docs/Proyectos/`, actualización del tablero maestro `docs/00-Dashboard-MOC.md`, backup preventivo `.bak` y este registro cronológico.

---

## 🔗 Referencias Relacionales
* [[00-Dashboard-MOC|Dashboard Central MOC]]
* [[docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering|Ficha Técnica Agente 12]]
* [[docs/Proyectos/2026-10-19_facturacion-reverse-engineering|Proyecto Dedicado: Facturación Reverse Engineering]]
* [[docs/Backups/README|Bóveda de Backups]]
