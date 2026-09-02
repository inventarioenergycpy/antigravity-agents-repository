---
tipo: referencia
estado: vigente
sensibilidad: interna
tags:
  - sigec-explorer
  - oracle
  - esquema
aliases:
  - Esquema Oracle SIGEC
---

# 🗄️ Esquema XXSIGEC — Reconocimiento (Fase 0)

> [!abstract] Contexto
> El usuario de conexión es `smunge` (sin tablas propias). El esquema real es `XXSIGEC`, propiedad del sistema comercial de EPEC. Proveniencia: Oracle Forms/Designer, entidades creadas 1993-1995.

## Resumen ejecutivo

| Métrica | Valor |
|---|---|
| Total tablas | **1 036** |
| FK declaradas a nivel motor | **242** (todas resueltas) |
| Tablas con FK salientes | 143 (~14 %) |
| Tablas referenciadas como destino FK | 105 |
| Comentarios de tabla útiles | ~158 (mayormente auto-generados, siglo pasado) |
| Comentarios de columna | **0 útiles** |
| Total columnas | 23 998 |

> [!warning] Comentarios inutilizables
> Los comentarios existentes son strings auto-generados tipo `"Created from Entity CONTRATO by CEIBO on 18-JUN-93"`. El sistema infiere significado **exclusivamente** desde nombres de tabla/columna + [[Sinónimos]].

## Categorías de tablas

| Categoría | Total | En universo de recuperación por defecto |
|---|---|---|
| `base` — tablas sin sufijo especial | 654 | ✅ Incluidas |
| `custom` — prefijo `XXCO_` | 248 | ✅ Incluidas |
| `hist` — sufijo `_H` / `_HIST` | 7 | ✅ Incluidas ¹ |
| `temp` — sufijo `_TMP` / `_TEMP` | 85 | ❌ Excluidas |
| `journal` — sufijo `_JN` | 42 | ❌ Excluidas |
| `archive` — sufijo `#` | ~22 (en ALL_OBJECTS, no en ALL_TABLES) | ❌ Excluidas |

> ¹ Las `_H`/`_HIST` se mantienen incluidas porque el caso de uso estrella ("medidas del medidor X") probablemente requiere el histórico.

## Escenario FK — HÍBRIDO

242 FK declaradas cubren 143 tablas (~14 %). El **86 % de las relaciones viven en convención de nombres de columna** (prefijo de 3 letras). Esto define la arquitectura del [[Catálogo]]:
- FK declaradas → grafo base confiable
- FK inferidas por prefijo/PK → enriquecen el grafo con dirección
- FK name-only → baja confianza, se excluyen de la expansión automática de vecinos

## Tablas hub (más referenciadas como destino FK)

| Tabla | Veces referenciada |
|---|---|
| `TIPOS_ITEM` | 14 |
| `SUCURSALES` | 13 |
| `USUARIOS` | 13 |
| `SECTORES` | 10 |
| `CONTRATOS` | 9 |
| `PERSONAS` | 9 |
| `OPERATIVOS` | 7 |
| `CLASES` / `TARIFAS` | 6 |

## Claves de join más extendidas

| Columna | # Tablas | Significado de dominio |
|---|---|---|
| `CNT_NUMERO_CUENTA` | 39 | Número de contrato/cuenta — join key principal |
| `SRV_SUMINISTRO_ORIGINAL` | 12 | Clave del suministro propagada a lectura/facturación |
| `NRO_CLIENTE` | 12 | Número de cliente (tablas `EXT_VKO_*`) |
| `SUMINISTRO` | 11 | Punto de suministro (nombre corto sin prefijo) |
| `MEDIDOR` | 9 | Identificador del medidor (⚠ no existe `NRO_MEDIDOR`) |

## Convención de prefijos de columna

El esquema usa prefijos de 2-4 letras en nombres de columna al estilo Oracle Apps. Ejemplos validados:

| Prefijo | Tabla propietaria | Nota de dominio |
|---|---|---|
| `CNT_` | `CONTRATOS` | |
| `SRV_` | `SERVICIOS` | SRV = **suministro** |
| `STE_` | `STOCK_EQUIPOS` | STE = **número de medidor** |
| `MOV_` | `MOVIMIENTOS_COBRANZA` | |
| `DOC_` | `DOCUMENTOS` | |
| `APL_` | `APLICACIONES` | |
| `LCT_` | `LECTURAS` | |
| `LTM_` | `LECTURAS_TEMP` | |
| `EQP_` | `EQUIPOS` | |
| `PRS_` | `PERSONAS` | |

> [!note] Auto-descubrimiento
> El `catalog_builder.py` descubrió **249 prefijos adicionales** desde columnas PK reales del esquema. Ver [[Catálogo]] para el detalle.
