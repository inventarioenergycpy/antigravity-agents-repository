---
tipo: decisiones
estado: vigente
tags:
  - sigec-explorer
  - decisiones
  - adr
aliases:
  - ADRs SIGEC Explorer
---

# ⚖️ Decisiones técnicas

## DEC-001 — Escenario FK: híbrido, no puro

**Fecha:** 2026-07-01
**Contexto:** La pregunta central de Fase 0 era si las relaciones estaban declaradas a nivel motor o solo en convención de nombres.
**Hallazgo:** 242 FK declaradas cubriendo 143 tablas (~14 %). El 86 % restante usa convención de prefijo de 3 letras.
**Decisión:** Arquitectura híbrida: FK declaradas como grafo base + inferencia dirigida por prefijo/PK como enriquecimiento. FK `name_only` se registran pero no se usan en expansión automática de vecinos.
**Consecuencia:** El catálogo tiene dos tipos de edges (`fk_declared` y `fk_inferred`) con niveles de confianza explícitos. El retriever los rankea por separado.

---

## DEC-002 — FK inferidas: siempre con dirección, nunca clique

**Fecha:** 2026-07-01
**Contexto:** `CNT_NUMERO_CUENTA` aparece en 39 tablas. Tratarlas como todas-relacionadas-entre-sí generaría 741 edges y reventaría el límite de 8 tablas en el contexto del LLM.
**Decisión:** La inferencia tiene dirección. La tabla donde la columna es PK es la dueña; las demás la referencian. Se generan 38 edges hacia `CONTRATOS`, no un clique.
**Reglas de precedencia:**
1. `inferred_pk_match` — columna es PK en exactamente 1 tabla
2. `inferred_prefix` — prefijo de columna mapea a tabla propietaria por convención
3. `inferred_name_only` — dirección desconocida, se registra pero no se usa en expansión

---

## DEC-003 — Sinónimos en Fase 1, no embeddings diferidos

**Fecha:** 2026-07-01
**Contexto:** El caso estrella falla con token-match puro. El usuario dice "medida", el esquema dice "lectura"/`LCT_`.
**Decisión:** `synonyms.json` editable manualmente, cargado en Fase 1, no diferido a una hipotética "Fase 2.5" con embeddings. Más barato, explicable, y captura exactamente el conocimiento de dominio que los compañeros no tienen.
**Trade-off aceptado:** Requiere mantenimiento manual cuando aparecen términos nuevos. Se mitiga documentando el proceso en [[Sinónimos]].

---

## DEC-004 — `_H`/`_HIST` incluidas en el universo de recuperación por defecto

**Fecha:** 2026-07-01
**Contexto:** Las tablas históricas estaban planificadas para exclusión por defecto.
**Cambio:** El caso estrella ("medidas del medidor") probablemente necesita el histórico de lecturas. Excluirlas puede eliminar la respuesta correcta.
**Decisión:** `_H`/`_HIST` se incluyen por defecto. `_TMP`, `_JN` y `#` siguen excluidos.
**Punto abierto:** Validar contra los 5 casos de uso reales del equipo antes de cambiar esto.

---

## DEC-005 — `/catalog/graph` como ego-graph bajo demanda, no grafo global

**Fecha:** 2026-07-01
**Contexto:** 634+ nodos no se pueden renderizar en pantalla de forma útil.
**Decisión:** `GET /catalog/graph/{table}` devuelve una tabla + sus vecinos directos rankeados por confianza. El cliente llama este endpoint al seleccionar una tabla, no al cargar la app.

---

## DEC-006 — `/query/run` siempre re-valida

**Fecha:** 2026-07-01
**Contexto:** Si `/query/run` acepta SQL arbitrario del cliente sin validar, cualquier llamada directa al endpoint es un agujero.
**Decisión:** `/query/run` aplica las mismas 4 capas de validación que `/chat`, sin importar el origen. No existe "SQL de confianza pre-validado".

---

## DEC-007 — catalog.json en disco, cargado en memoria al iniciar

**Fecha:** 2026-07-01
**Contexto:** 1 036 tablas, ~24K columnas. Alternativas: re-consultar Oracle en cada petición, usar una DB intermedia (SQLite), o JSON en memoria.
**Decisión:** JSON en disco, cargado en memoria al arrancar la app. 1 036 tablas caben fácil en RAM (~10-50 MB estimado). Sin dependencia de DB adicional. Se regenera con `catalog_builder.py` cuando cambia el esquema.
