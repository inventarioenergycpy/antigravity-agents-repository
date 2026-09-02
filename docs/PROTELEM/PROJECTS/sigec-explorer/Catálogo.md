---
tipo: referencia
estado: vigente
sensibilidad: interna
tags:
  - sigec-explorer
  - catalogo
  - oracle
aliases:
  - catalog.json
---

# 📦 Catálogo de esquema — catalog.json

> [!abstract] Qué es esto
> `catalog.json` es el artefacto central del que depende todo: el explorador web y el chat texto-a-SQL. Se genera corriendo `catalog_builder.py` contra el diccionario de datos Oracle. No requiere acceso a la base de datos en runtime.

## Cómo generarlo

```bash
# Requiere red corporativa activa (epec2-scan2 debe ser alcanzable)
python -X utf8 src/catalog_builder.py
```

Tarda ~30 segundos. Al terminar imprime el reporte de validación en stdout.

## Fuentes de datos (diccionario Oracle)

| Vista Oracle | Qué aporta |
|---|---|
| `ALL_TABLES` | Lista de tablas + `NUM_ROWS` (estimado) |
| `ALL_TAB_COLUMNS` | Columnas, tipos, nullable, posición |
| `ALL_CONSTRAINTS` (tipo P) | Columnas PK por tabla |
| `ALL_CONSTRAINTS` (tipo R) + `ALL_CONS_COLUMNS` | FK declaradas resueltas a tabla y columna destino |
| `ALL_COL_COMMENTS` | Comentarios de columna (prácticamente vacío en XXSIGEC) |

## Estructura de una entrada en catalog.json

```json
{
  "DOCUMENTOS": {
    "category":    "base",
    "num_rows":    null,
    "comment":     "Created from Entity DOCUMENTO by CEIBO on 18-JUN-93",
    "pk":          ["DOC_NUMERO"],
    "columns": [
      {"name": "DOC_NUMERO",        "type": "NUMBER",  "nullable": false, "comment": null},
      {"name": "CNT_NUMERO_CUENTA", "type": "NUMBER",  "nullable": false, "comment": null},
      {"name": "DOC_FK_PRS",        "type": "NUMBER",  "nullable": true,  "comment": null}
    ],
    "fk_declared": [
      {
        "constraint_name": "DOC_FK_CNT",
        "local_cols":      ["CNT_NUMERO_CUENTA"],
        "ref_table":       "CONTRATOS",
        "ref_cols":        ["CNT_NUMERO_CUENTA"],
        "confidence":      "declared",
        "resolved":        true
      }
    ],
    "fk_inferred": [
      {
        "local_col":  "CNT_NUMERO_CUENTA",
        "ref_table":  "CONTRATOS",
        "ref_col":    "CNT_NUMERO_CUENTA",
        "direction":  "references",
        "confidence": "inferred_pk_match",
        "reason":     "CNT_NUMERO_CUENTA es PK de CONTRATOS"
      }
    ]
  }
}
```

## Tipos de FK inferidas y su confianza

| `confidence` | Lógica | Uso en retriever |
|---|---|---|
| `inferred_pk_match` | Columna es PK en tabla A, no-PK en tabla B → B referencia A | Alta: se usa en expansión de vecinos |
| `inferred_prefix` | Prefijo de columna mapea a tabla propietaria (ej. `CNT_` → CONTRATOS) | Media: se usa en expansión con menor prioridad |
| `inferred_name_only` | Columna compartida sin propietario identificable — dirección `unknown` | Baja: se excluye de la expansión automática |

> [!warning] NUNCA edge entre referenciadoras
> `CNT_NUMERO_CUENTA` en 39 tablas genera **38 edges hacia CONTRATOS**, no un clique de 741 pares. Las tablas referenciadoras no se conectan entre sí.

## Resultados de la última corrida (2026-07-01)

```
Tablas descargadas       : 1 036
Columnas                 : 23 998
Comentarios de columna   : 0 (vacío en XXSIGEC)

TABLAS POR CATEGORÍA:
  base      :   654
  custom    :   248
  hist      :     7
  temp      :    85
  journal   :    42
  archive   :     0  ← tablas "#" viven en ALL_OBJECTS, no en ALL_TABLES
  view      :     0  ← las vistas están en ALL_VIEWS
  TOTAL     : 1 036

FK DECLARADAS:
  Total constraints : 242
  Resueltas         : 242 (100%) ✅
  Sin resolver      :   0

FK INFERIDAS:
  inferred_pk_match  :   328
  inferred_prefix    : 5 116
  inferred_name_only : 1 991

Prefijos auto-descubiertos : 249 (además de los 27 del SEED_PREFIX_MAP)
Tablas huérfanas           : 112 (sin FK en ningún sentido)

SYNONYMS.JSON: todas las tablas y columnas/prefijos existen en el catálogo ✅
```

## Categorías y universo de recuperación

El campo `category` en cada tabla controla qué entra al chat por defecto:

```python
# En schema_retriever.py, filtro por defecto:
ACTIVE_CATEGORIES = {"base", "custom", "hist", "view"}
# Excluidos por defecto: temp, journal, archive
# Activable con: ?include_all=true
```

## Cuándo regenerar el catálogo

- Al agregar tablas nuevas al esquema XXSIGEC.
- Si se detectan FK declaradas nuevas.
- Si el reporte de validación muestra sinónimos rotos (tablas que ya no existen).
- Como máximo, una vez por sprint para mantenerlo fresco.
