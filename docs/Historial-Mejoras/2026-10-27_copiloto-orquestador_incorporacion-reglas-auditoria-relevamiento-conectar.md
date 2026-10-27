---
type: historial-mejora
agente: "[[copiloto-orquestador-skills]] & [[ciencia-de-datos]]"
fecha: 2026-10-27
backup_asociado:
  - "[[docs/Backups/2026-10-27_160153_copiloto-orquestador-skills_SKILL.md.bak]]"
  - "[[docs/Backups/2026-10-27_160153_ciencia-de-datos_SKILL.md.bak]]"
tags:
  - #historial
  - #mejora
  - #conectar
  - #auditoria
  - #relevamiento
  - #sigec
  - #reglas-de-negocio
---

# Registro de Mejora: Incorporación de Reglas de Auditoría de Relevamientos CONECTAR y Normalización SIGEC

- **Fecha**: 2026-10-27
- **Agentes Actualizados**:
  * `copiloto-orquestador-skills` (Agente 11)
  * `ciencia-de-datos` (Agente 02)
- **Respaldos Preventivos Asociados**:
  * `docs/Backups/2026-10-27_160153_copiloto-orquestador-skills_SKILL.md.bak`
  * `docs/Backups/2026-10-27_160153_ciencia-de-datos_SKILL.md.bak`
- **Repositorio Dedicado Creado y Vinculado**: [https://github.com/PROTELEM-EPEC/auditoria-relevamiento-conectar](https://github.com/PROTELEM-EPEC/auditoria-relevamiento-conectar)

---

## 🎯 Descripción del Cambio y Contexto
A partir de la solicitud explícita del usuario (*"DOCUMENTAR Y GUARDAR"*), se activó el protocolo formal de auto-documentación y resguardo preventivo para formalizar en la base de habilidades de los agentes todo el conocimiento, lógica de cruces y catálogo de reglas de negocio desarrollados sobre la muestra de 1.348 medidores observados con error de la contratista CONECTAR.

---

## 🛠️ Reglas Incorporadas a las Habilidades

1. **Ampliación del Despacho Dinámico (`copiloto-orquestador-skills`)**:
   - Inclusión del nuevo dominio de *Auditoría de Relevamientos de Medidores CONECTAR y Normalización SIGEC* mapeado a `ciencia-de-datos` y al repositorio dedicado `PROTELEM-EPEC/auditoria-relevamiento-conectar`.

2. **Criterio de Validación Determinista (`ciencia-de-datos`)**:
   - Incorporación de las 19 tipologías de error de relevamiento (`MEDIDOR INEXISTENTE`, `LOCALIDAD/BARRIO INVALIDO`, `MEDIDOR RETIRADO`, `MEDIDOR NO COINCIDE`, etc.).
   - Algoritmo de chunking en lotes de $\le 900$ elementos para eludir el límite `ORA-01795` de Oracle y optimizar el rendimiento.
   - Heurística regex de detección de errores de tipeo sobre notas de PROTELEM.
   - Matriz de 7 estados deterministas (`CORREGIDO`, `CORREGIDO_REEMPLAZO`, `CORREGIDO_TIPEO`, `NORMALIZADO_OTRO_SUMI`, `DIVERGENCIA`, `ACTUALIZADO_RECIENTE`, `PENDIENTE`).
   - Diferenciación de cohortes temporales (casos viejos 2022-2023 vs. recientes 2024-2026).

---

## 📈 Impacto y Beneficio
- **Trazabilidad Absoluta**: Cualquier agente de IA que atienda una consulta sobre relevamientos de CONECTAR o inconsistencias de medidores activará de inmediato las reglas deterministas de resolución sin alucinaciones (*Zero Vibes QA*).
- **Escalabilidad y Replicabilidad**: El procedimiento queda blindado con scripts testeados, diccionarios de datos estructurados en JSON y documentación didáctica completa para la inducción de nuevos profesionales humanos o agentes en EPEC.
