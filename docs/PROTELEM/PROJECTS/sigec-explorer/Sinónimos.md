---
tipo: referencia
estado: vigente
tags:
  - sigec-explorer
  - sinonimos
  - vocabulario
aliases:
  - synonyms.json
  - Diccionario de dominio
---

# 📖 Diccionario de sinónimos — synonyms.json

> [!abstract] Por qué existe
> El vocabulario del usuario no coincide con el del esquema. El usuario dice "medida", el esquema dice "lectura" / prefijo `LCT_`. Sin este diccionario, el chat fallaría en el caso de uso estrella ("necesito las medidas del medidor XXXXXX"). Ver [[Esquema XXSIGEC#Convención de prefijos de columna]].

## Archivo

```
src/synonyms.json
```

Editable manualmente por cualquier compañero. Cambios toman efecto sin reiniciar la app (el retriever lo lee en cada petición).

## Estructura de una entrada

```json
"medidor": {
  "tables":  ["STOCK_EQUIPOS", "EQUIPOS"],
  "columns": ["MEDIDOR", "NCW_MEDIDOR", "LEL_CODIGO_MEDIDOR", "STE_"]
}
```

- `tables` → tablas que se agregan al contexto de búsqueda cuando el usuario usa este término.
- `columns` → columnas que se buscan en el índice invertido del catálogo.
- Valores terminados en `_` son **prefijos**: `"STE_"` matchea cualquier columna que empiece con `STE_`.

## Mapeos actuales (sembrados en Fase 0)

### Medición y medidor

| Término usuario | Tablas | Columnas / prefijos |
|---|---|---|
| medida, medicion, consumo | LECTURAS, CABEZA_LECTURAS | MEDIDOR, LTM_ACCESO_MEDIDOR |
| lectura | LECTURAS, CABEZA_LECTURAS, LECTURAS_TEMP | MEDIDOR, LCT_ |
| medidor | STOCK_EQUIPOS, EQUIPOS | MEDIDOR, NCW_MEDIDOR, LEL_CODIGO_MEDIDOR, LTM_ACCESO_MEDIDOR, STE_ |
| numero de medidor, nro medidor | STOCK_EQUIPOS | MEDIDOR, STE_ |
| equipo | EQUIPOS, STOCK_EQUIPOS | — |

> [!note] SRV y STE — conocimiento de dominio validado por el equipo
> - `SRV_` = prefijo de **suministro** → tabla `SERVICIOS`
> - `STE_` = prefijo de **número de medidor** → tabla `STOCK_EQUIPOS`
> No siempre se usan estas terminologías; hay variantes en el esquema.

### Contrato y suministro

| Término usuario | Tablas | Columnas / prefijos |
|---|---|---|
| suministro, punto de suministro | SERVICIOS | SUMINISTRO, SRV_SUMINISTRO_ORIGINAL, MOV_SUMINISTRO, SRV_ |
| servicio | SERVICIOS, CONTRATOS | — |
| cuenta, nro cuenta, numero de cuenta | CONTRATOS | CNT_NUMERO_CUENTA, MOV_NUMERO_CUENTA |
| contrato | CONTRATOS | CNT_ |

### Clientes y personas

| Término usuario | Tablas | Columnas |
|---|---|---|
| cliente | PERSONAS | NRO_CLIENTE |
| persona | PERSONAS | — |

### Facturación y cobranza

| Término usuario | Tablas | Columnas / prefijos |
|---|---|---|
| factura, boleta, documento | DOCUMENTOS, BOLETAS | DOC_ |
| pago | MOVIMIENTOS_COBRANZA, APLICACIONES | — |
| cobranza, movimiento | MOVIMIENTOS_COBRANZA | MOV_ |
| aplicacion | APLICACIONES | APL_ |

### Tarifas e infraestructura

| Término usuario | Tablas | Columnas |
|---|---|---|
| tarifa, categoria | TARIFAS, CATEGORIAS, CONCEPTOS_TARIFAS | — |
| escalon | ESCALONES | — |
| usuario | USUARIOS | — |
| sector | SECTORES | — |
| sucursal | SUCURSALES | — |
| zona | ZONAS | — |

## Cómo agregar un sinónimo nuevo

1. Identificar qué tabla/columna de `XXSIGEC` corresponde (buscando en `/catalog/search`).
2. Agregar la entrada en `src/synonyms.json`.
3. Verificar que el nombre de tabla exista corriendo `catalog_builder.py` (sección de validación de sinónimos).
4. El cambio toma efecto inmediatamente (no requiere reinicio).

## Cuándo agregar sinónimos

Cada vez que el chat devuelva una tabla incorrecta o no encuentre la tabla correcta para una pregunta real de un compañero, agregar el mapeo que faltaba. El diccionario crece con el uso real del equipo.
