---
tipo: roadmap
estado: vigente
sensibilidad: interna
tags:
  - sigec-explorer
  - sprints
  - roadmap
aliases:
  - Roadmap SIGEC Explorer
  - Estado del proyecto
---

# 🗺️ Sprints y estado del proyecto

## Estado general

```
Fase 0 — Reconocimiento    ██████████ 100% ✅
Fase 1 — Catálogo          ████░░░░░░  40%  En progreso
Fase 2 — Chat texto-a-SQL  ░░░░░░░░░░   0%  Pendiente
```

---

## Fase 0 — Reconocimiento ✅ Completa

**Objetivo:** entender el terreno antes de escribir código.

- [x] Identificar el owner real del esquema (`smunge` → `XXSIGEC`)
- [x] Contar tablas y clasificarlas por tipo (1 036 total)
- [x] Determinar cobertura de FK declaradas (242, escenario híbrido)
- [x] Evaluar comentarios (inutilizables como fuente semántica)
- [x] Mapear claves compartidas y convención de prefijos (`CNT_`, `SRV_`, `STE_`…)
- [x] Documentar hallazgos en DESIGN.md v1 y v2 (5 correcciones incorporadas)

**Artefactos generados:**
- `fase0_diagnostico.py` (script descartable, sirvió su propósito)
- `DESIGN.md` v2 (aprobado)

---

## Fase 1 — Catálogo 🔄 En progreso

**Objetivo:** cualquier compañero puede explorar el esquema sin tocar la base.

### Completado

- [x] `src/oracle_db.py` — helper de conexión (copia fiel del .md de referencia)
- [x] `src/synonyms.json` — sembrado con mapeos Fase 0 + conocimiento de dominio (SRV, STE)
- [x] `src/catalog_builder.py` — consulta diccionario Oracle, genera catalog.json con FK inferidas dirigidas
- [x] `src/catalog.json` — generado y validado (2026-07-01): 1 036 tablas, 242 FK declaradas, 5 444 FK inferidas

### Pendiente

- [ ] `src/main.py` — FastAPI con endpoints `/catalog/*`
  - `GET /catalog/tables` (con filtro `?category=`)
  - `GET /catalog/tables/{name}`
  - `GET /catalog/search?q=`
  - `GET /catalog/graph/{table}` (ego-graph)
- [ ] `frontend/index.html` — buscador + panel de detalle + ego-graph de vecinos
- [ ] `requirements.txt`
- [ ] Verificar privilegios del usuario `smunge` (Capa 1 de [[Seguridad]])

**Criterio de done Fase 1:**
- Buscar "medidor" → llega a tablas correctas vía sinónimos
- Detalle de `LECTURAS` muestra FK con dirección y confianza
- `/catalog/graph/LECTURAS` devuelve vecinos rankeados correctamente
- Tablas `_TMP`/`_JN` no aparecen en búsqueda por defecto; `_H`/`_HIST` sí

---

## Fase 2 — Chat Texto-a-SQL ⏳ Pendiente (post-aprobación Fase 1)

**Objetivo:** preguntas en lenguaje natural → SELECT validado → resultado en pantalla.

### Pendiente

- [ ] `src/schema_retriever.py` — índice invertido + expansión sinónimos + ranqueo de confianza
- [ ] `src/sql_validator.py` — validación en 4 capas
- [ ] Integración LLM (Claude Sonnet vía API Anthropic) en `src/main.py`
  - `POST /chat`
  - `POST /query/run`
- [ ] `frontend/chat.html` — SQL visible antes de ejecutar, tablas usadas con nivel de match, resultado paginado

**Criterio de done Fase 2:**
- "necesito las medidas del medidor XXXXXX" → SELECT válido + ejecutable
- `/query/run` rechaza SQL inválido sin importar el origen
- `synonyms.json` editable sin reiniciar

---

## Puntos abiertos (bloquean o afectan el diseño)

| # | Pregunta | Impacto | Estado |
|---|---|---|---|
| A | ¿`smunge` tiene privilegios de escritura en algún schema? | Capa 1 de seguridad | ⚠️ Pendiente verificar |
| B | ¿Cuáles son los 5 casos de uso más frecuentes del equipo? | Valida exclusión `_H`/`_HIST` y prioridad de sinónimos | ⚠️ Pendiente |
| C | ¿Existe tabla `LECTURAS` (o similar) con histórico de consumo? | Caso de uso estrella | ✅ Existen `LECTURAS` y `CABEZA_LECTURAS` en catálogo |
| D | ¿El límite de 8 tablas en contexto del LLM es suficiente? | Calidad del SQL generado | ⚠️ A validar en Fase 2 |
