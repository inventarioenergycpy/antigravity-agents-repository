---
tipo: arquitectura
estado: vigente
tags:
  - sigec-explorer
  - arquitectura
  - fastapi
---

# 🏗️ Arquitectura — SIGEC Explorer

## Dos fases de construcción

```
FASE 1 — Catálogo          FASE 2 — Chat
────────────────────        ─────────────────────────────────────
catalog_builder.py          schema_retriever.py
    ↓                           ↓
catalog.json  ←──────────── índice invertido + synonyms.json
    ↓                           ↓
FastAPI /catalog/*          LLM (Claude) + sql_validator.py
    ↓                           ↓
frontend/index.html         FastAPI /chat + /query/run
                                ↓
                            frontend/chat.html
```

## Fase 1 — Catálogo de esquema

### Objetivo
Un compañero puede explorar el esquema `XXSIGEC` completo sin tocar la base de datos.

### Componentes

| Archivo | Rol |
|---|---|
| `src/oracle_db.py` | Helper `OracleReadOnly` — conexión en modo solo lectura |
| `src/catalog_builder.py` | Consulta diccionario Oracle → genera `catalog.json` |
| `src/catalog.json` | Catálogo en disco, cargado en memoria al iniciar la API |
| `src/synonyms.json` | Diccionario usuario → esquema, editable manualmente |
| `src/main.py` | FastAPI: endpoints `/catalog/*` |
| `frontend/index.html` | Explorador de tablas con buscador y ego-graph de vecinos |

### Endpoints del catálogo

```
GET /catalog/tables                → lista tablas (filtros: ?category=base|all…)
GET /catalog/tables/{name}         → detalle: columnas, FK declaradas e inferidas
GET /catalog/search?q=medidor      → búsqueda (pasa por synonyms.json)
GET /catalog/graph/{table}         → ego-graph: tabla + vecinos rankeados por confianza
```

### Criterio de done
- Buscar "medidor" llega a tablas correctas vía sinónimos.
- El detalle de `LECTURAS` muestra FK declaradas e inferidas con dirección y confianza.
- `/catalog/graph/LECTURAS` devuelve `EQUIPOS`, `CUADRANTES`, `LECTURAS_TEMP` rankeados.
- Tablas `_TMP`/`_JN` no aparecen en búsqueda por defecto; `_H`/`_HIST` sí.

---

## Fase 2 — Chat Texto-a-SQL

### Objetivo
El usuario escribe en lenguaje natural y recibe el SELECT listo para ejecutar.

### Flujo completo

Ver [[Chat Texto-a-SQL]] para el flujo detallado paso a paso.

### Componentes adicionales

| Archivo | Rol |
|---|---|
| `src/schema_retriever.py` | Expansión de tokens + índice invertido + ranqueo de confianza |
| `src/sql_validator.py` | Validación en 4 capas (ver [[Seguridad]]) |
| `frontend/chat.html` | Interfaz: muestra SQL antes de ejecutar, tablas usadas, resultado |

### Criterio de done
- "necesito las medidas del medidor XXXXXX" → SELECT válido con JOIN a `LECTURAS`/`EQUIPOS`.
- El SQL siempre se muestra antes de ejecutar, sin excepción.
- `/query/run` rechaza cualquier SQL que no pase la validación, sin importar el origen.
- `synonyms.json` editable sin reiniciar la app.

---

## Stack técnico

| Capa | Elección |
|---|---|
| Conexión Oracle | `OracleReadOnly` (helper existente, modo Thick) |
| Backend | FastAPI + uvicorn |
| LLM | Claude Sonnet vía API Anthropic |
| Frontend | HTML + Vanilla JS (sin frameworks pesados) |
| Catálogo | `catalog.json` en disco (1 036 tablas, carga en memoria) |
| Sinónimos | `synonyms.json` editable |

## Árbol de archivos

```
mapeo-bd-sigec-oracle/
├── .env                         ← credenciales Oracle (no commitear)
├── DESIGN.md                    ← documento de diseño detallado
├── src/
│   ├── oracle_db.py             ← helper de conexión (ya existe ✅)
│   ├── catalog_builder.py       ← genera catalog.json (ya existe ✅)
│   ├── catalog.json             ← catálogo generado (ya existe ✅)
│   ├── synonyms.json            ← diccionario de sinónimos (ya existe ✅)
│   ├── schema_retriever.py      ← pendiente (Fase 2)
│   ├── sql_validator.py         ← pendiente (Fase 2)
│   └── main.py                  ← pendiente (Fase 1 API)
├── frontend/
│   ├── index.html               ← pendiente (Fase 1 UI)
│   └── chat.html                ← pendiente (Fase 2 UI)
└── requirements.txt             ← pendiente
```
