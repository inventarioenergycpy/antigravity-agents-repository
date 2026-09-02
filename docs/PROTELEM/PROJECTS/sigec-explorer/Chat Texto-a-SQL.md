---
tipo: arquitectura
estado: vigente
tags:
  - sigec-explorer
  - chat
  - llm
  - sql
aliases:
  - Texto a SQL
  - Chat SQL
---

# 💬 Chat Texto-a-SQL — Fase 2

> [!abstract] Objetivo
> El usuario escribe en lenguaje natural y recibe el SELECT listo para ejecutar contra `XXSIGEC`. El SQL **siempre** se muestra antes de ejecutar; nunca se ejecuta de forma silenciosa.

## Flujo completo de una consulta

### Ejemplo: _"necesito las medidas del medidor XXXXXX"_

```
Usuario: "necesito las medidas del medidor XXXXXX"
         │
         ▼
[1] EXPANSIÓN DE TOKENS — schema_retriever.py + synonyms.json
    "medidas"  → {tables: [LECTURAS, CABEZA_LECTURAS], columns: [MEDIDOR, LCT_]}
    "medidor"  → {tables: [STOCK_EQUIPOS, EQUIPOS],    columns: [MEDIDOR, STE_]}
    "XXXXXX"   → literal para el WHERE
         │
         ▼
[2] RECUPERACIÓN DE TABLAS — índice invertido sobre catalog.json
    Candidatas directas : LECTURAS, CABEZA_LECTURAS, STOCK_EQUIPOS, EQUIPOS
    FK expansion        : vecinos declared + inferred_pk_match de esas tablas
    Corte               : máx 8 tablas, ordenadas por confianza (ver tabla abajo)
         │
         ▼
[3] GENERACIÓN SQL — LLM Claude Sonnet
    Prompt: instrucción de solo-lectura + schema snippet ≤8 tablas + pregunta
    Reglas en prompt:
      - FETCH FIRST {limit} ROWS ONLY obligatorio
      - Prefijo XXSIGEC. en cada tabla
      - Solo SELECT o WITH … SELECT
         │
         ▼
[4] VALIDACIÓN — sql_validator.py (ver [[Seguridad]])
    - Empieza con SELECT o WITH
    - Un solo statement (no múltiples `;`)
    - Contiene FETCH FIRST o ROWNUM (si no, se agrega automáticamente)
    - Keywords DML/DDL como señal secundaria
         │
         ▼
[5] RESPUESTA AL USUARIO
    a) Tablas usadas + nivel de match (directo / sinónimo / vecino)
    b) SQL generado — siempre visible ANTES de ejecutar
    c) Botón "Ejecutar" → POST /query/run (re-valida server-side)
    d) Resultado paginado (máx 200 filas en UI)
```

## Ranqueo de tablas candidatas

| Nivel | Fuente | Prioridad |
|---|---|---|
| `direct` | Nombre de tabla/columna aparece en la pregunta | 1 (máxima) |
| `synonym` | Token expandido desde `synonyms.json` | 2 |
| `neighbor_declared` | Vecino por FK declarada de tabla ya seleccionada | 3 |
| `neighbor_inferred_pk` | Vecino por `inferred_pk_match` | 4 |
| `neighbor_inferred_prefix` | Vecino por `inferred_prefix` | 5 |

Corte duro en 8 tablas. Si hay más candidatas, ganan las de mayor prioridad.

## API

```
POST /chat
  body:     {"question": "necesito las medidas del medidor XXXXXX", "limit": 50}
  response: {
    "sql": "SELECT l.* FROM XXSIGEC.LECTURAS l ...",
    "tables_used": [
      {"table": "LECTURAS",      "match": "synonym"},
      {"table": "STOCK_EQUIPOS", "match": "synonym"},
      {"table": "EQUIPOS",       "match": "neighbor_declared"}
    ],
    "warning": null
  }

POST /query/run
  body:     {"sql": "SELECT ...", "limit": 200}
  response: {"columns": [...], "rows": [...], "row_count": N, "truncated": bool}
```

> [!warning] /query/run re-valida siempre
> El endpoint `/query/run` aplica la misma validación de seguridad que `/chat`, sin importar el origen del SQL. No existe "SQL de confianza pre-validado".

## Prompt al LLM (estructura)

```
[SYSTEM]
Eres un experto en SQL Oracle para el sistema SIGEC de EPEC.
SOLO generas consultas SELECT. Nunca DML ni DDL.
Todas las tablas llevan el prefijo XXSIGEC.
Toda consulta incluye FETCH FIRST {limit} ROWS ONLY.
El esquema relevante para esta consulta es:

{schema_snippet — columnas y FK de las ≤8 tablas recuperadas}

[USER]
{pregunta original del usuario}
```

El schema snippet incluye columnas con tipos, FK declaradas y FK inferred_pk_match (no inferred_name_only para no contaminar el contexto con relaciones de baja confianza).

## Componentes pendientes de implementar (Fase 2)

- [ ] `src/schema_retriever.py` — índice invertido + expansión sinónimos + ranqueo
- [ ] `src/sql_validator.py` — validación en 4 capas (ver [[Seguridad]])
- [ ] Endpoints `/chat` y `/query/run` en `src/main.py`
- [ ] `frontend/chat.html` — UI con SQL visible, tablas usadas, resultado paginado
