---
tipo: referencia
estado: vigente
sensibilidad: interna
tags:
  - sigec-explorer
  - seguridad
  - oracle
aliases:
  - Modelo de seguridad SIGEC
  - Seguridad SIGEC
---

# 🔒 Seguridad — Modelo en 4 capas

> [!abstract] Principio
> La seguridad no descansa en un solo mecanismo. Cada capa es independiente de las demás. Si una falla, las otras siguen activas. La capa 1 es la única que importa realmente; las demás son refuerzo.

> [!info] Dos seguridades distintas
> Esta nota cubre la **seguridad de las queries** (que nadie escriba ni ejecute SQL peligroso). La **clasificación de datos y el manejo de secretos** a nivel cerebro están en [[Modelo de seguridad]] (global). El resumen para este proyecto está abajo.

## Clasificación de datos y default de sensibilidad (sigec-explorer)

> [!note] Default del proyecto: `interna`
> `sigec-explorer` documenta el **esquema interno** de la base de facturación de EPEC (nombres de tablas y columnas), **no** datos de clientes. Default de sensibilidad del proyecto: **`interna`** — incluidas las 1036 fichas de `tablas/`, que no repiten el campo (ver [[Convenciones#Default de sensibilidad en colecciones masivas]]).
> - Ninguna ficha contiene valores personales reales: `NRO_DOCUMENTO`/`CUIT` aparecen solo como **nombres de columna**.
> - **Secretos:** credenciales Oracle solo en `.env` (gitignored), nunca en el vault. Conexión en [[Oracle EPEC - Conexión y convenciones]].

## Capa 1 — Privilegios del usuario Oracle ⚠️ ACCIÓN PENDIENTE

**La pared real.** Si el motor rechaza a nivel de privilegios, ningún SQL malformado puede causar daño, independientemente de lo que haga la aplicación.

**Acción pendiente:** verificar que `smunge` tenga **exclusivamente** privilegio `SELECT` sobre `XXSIGEC.*` y ningún `INSERT`/`UPDATE`/`DELETE`/`DDL` en ningún esquema accesible.

```sql
-- Verificar privilegios del usuario smunge
SELECT PRIVILEGE, OWNER, TABLE_NAME, GRANTABLE
FROM DBA_TAB_PRIVS
WHERE GRANTEE = 'SMUNGE'
ORDER BY OWNER, TABLE_NAME;
```

Si hay privilegios de escritura → conseguir un usuario dedicado de solo lectura antes de abrir la herramienta a más compañeros.

## Capa 2 — `SET TRANSACTION READ ONLY` ✅ Ya implementado

El helper `OracleReadOnly` en `src/oracle_db.py` ejecuta `SET TRANSACTION READ ONLY` al abrir cada conexión. Cualquier intento de escritura dentro de esa sesión es rechazado por el motor Oracle, independientemente del SQL.

```python
# oracle_db.py — __enter__
conn.autocommit = False
with conn.cursor() as cur:
    cur.execute("SET TRANSACTION READ ONLY")
```

## Capa 3 — Validación estructural del SQL ✅ En sql_validator.py

Se aplica **por separado** en `/chat` y en `/query/run`. El SQL recibido debe cumplir las 3 reglas:

| Regla | Qué verifica | Si falla |
|---|---|---|
| Solo SELECT/WITH | `strip().upper()` empieza con `SELECT` o `WITH` | Rechazar con error |
| Un único statement | No más de un `;` en el SQL | Rechazar (previene stacked queries) |
| Límite de filas | Contiene `FETCH FIRST` o `ROWNUM` | Auto-agregar `FETCH FIRST {limit} ROWS ONLY` + `warning` |

## Capa 4 — Blacklist de keywords (señal secundaria)

Buscar `INSERT`, `UPDATE`, `DELETE`, `DROP`, `CREATE`, `ALTER`, `EXEC`, `MERGE` como palabras completas con regex `\bKEYWORD\b` (case-insensitive).

> [!warning] Limitaciones de esta capa
> - **Falsos positivos**: columnas como `FECHA_UPDATE` o `LOG_DELETE` contienen keywords pero son identificadores. El word boundary `\b` ayuda pero no es perfecto.
> - **No es la defensa principal**: un SQL malicioso bien construido puede evadir un blacklist. Esta capa **solo refuerza** las capas 1-3, no las reemplaza.

## Regla sobre /query/run

```
/query/run SIEMPRE re-valida el SQL recibido.
No existe "SQL de confianza pre-validado" aunque venga de /chat.
```

Esto previene que alguien llame directamente a `/query/run` con un SQL arbitrario, saltando el paso de generación del LLM.

## Puntos abiertos

- [ ] Verificar privilegios reales del usuario `smunge` (Capa 1)
- [ ] Implementar `src/sql_validator.py` con las capas 3 y 4
