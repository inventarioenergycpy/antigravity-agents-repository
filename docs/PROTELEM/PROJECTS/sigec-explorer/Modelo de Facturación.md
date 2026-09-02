---
tipo: dominio
estado: vigente
sensibilidad: interna
tags:
  - sigec-explorer
  - dominio
  - oracle
  - epec
  - facturacion
aliases:
  - Modelo de Facturación
  - Factura SIGEC
  - Período de facturación
  - Importe facturado
  - kWh facturados
fecha: 2026-08-06
---

# 🧾 Modelo de facturación — importe, kWh y período

> [!abstract] Qué es esto
> Cómo se lee **una factura** en `XXSIGEC`: de dónde salen el importe que se le
> cobró a un cliente, los kWh que entraron en esa factura y los días que
> comprende el período. Verificado contra Oracle el 2026-08-06 sobre 2025
> completo (14,09 M facturas). Rastro en el cuaderno del repo
> (`investigaciones/2026-08-06-facturacion-cliente-periodo/`).

## 🧭 Respuesta corta

Las tres cosas están en **una sola fila de [[DOCUMENTOS]]**. Una fila = una
factura de un contrato en un período. No hace falta tocar [[LECTURAS]] (223 M
filas) ni [[ITEMS]] (4.157 M).

| Lo que se pregunta | Columna |
|---|---|
| Cuánto se le facturó | `DOC_IMPORTE` — total **con impuestos** |
| Cuánto de eso es energía | `DOC_IMPORTE_GRAVADO` (neto) |
| Cuánto son impuestos | `DOC_IMPORTE_EXENTO` |
| kWh facturados | `DOC_CONSUMO` |
| Días del período | `DOC_FECHA_HASTA` − `DOC_FECHA_DESDE` |

```sql
SELECT d.DOC_IMPORTE, d.DOC_CONSUMO,
       d.DOC_FECHA_DESDE, d.DOC_FECHA_HASTA,
       (d.DOC_FECHA_HASTA - d.DOC_FECHA_DESDE) AS dias
  FROM XXSIGEC.DOCUMENTOS d
 WHERE d.SRV_CODIGO = :suministro
   AND d.DOC_ANIO   = :anio
   AND d.DOC_TIPO = 'F' AND d.DOC_GRUPO = 'N' AND d.DOC_ESTADO = 'D'
```

## ⚠️ La trampa: el «período» no es el mes que consumís

`DOC_ANIO` / `DOC_PERIODO` es la **etiqueta del ciclo de facturación**, no el mes
consumido. En 2025 el período es el mes de fin de consumo **+1** en el **97,3 %**
de las facturas; solo el 0,97 % tiene el `DOC_FECHA_HASTA` dentro del mes que
lleva de etiqueta.

```
período 2025/1  ─▶  consume del 13/11/2024 al 12/12/2024  ─▶  se emite 19/12/2024
    (etiqueta)              (DOC_FECHA_DESDE/HASTA)            (DOC_FECHA_EMISION)
```

> [!important] «El mes» hay que elegirlo a propósito
> Tres fechas distintas conviven en la misma factura y para «enero 2025» dan
> conjuntos **distintos**:
>
> | Criterio | Columnas | Responde |
> |---|---|---|
> | Ciclo de la boleta | `DOC_ANIO`, `DOC_PERIODO` | «la factura del período 01/2025» |
> | Cuándo se facturó | `DOC_FECHA_EMISION` | «lo emitido en enero 2025» |
> | Días consumidos | `DOC_FECHA_DESDE/HASTA` | «el consumo de los días de enero» |
>
> Desfasaje etiqueta ↔ fin de consumo (2025): **+1 mes** 13.702.593 · +2 meses
> 239.079 · 0 · 137.398. Contra la emisión el reparto es ~mitad y mitad.

**Ninguna factura calza con el mes calendario**: los cortes de lectura caen a
mitad de mes. Responder «el consumo de enero» exige **prorratear**.

## 📅 Los días del período encadenan

`DOC_FECHA_DESDE` = `DOC_FECHA_HASTA` de la factura anterior del mismo contrato
en el **99,4 %** de los casos: el día frontera **se comparte**.

> [!warning] Los días son `HASTA − DESDE`, sin `+1`
> Sumar 1 (el reflejo habitual con rangos inclusivos) cuenta dos veces el día de
> corte y rompe la continuidad entre facturas consecutivas.

Duración en 2025: 31 días (4,25 M docs) · 30 (3,62 M) · 29 (2,86 M) · 32
(1,54 M) · 28 (0,99 M) → ciclo **mensual**. `DOC_FRECUENCIA` **no sirve**: viene
100 % NULL.

## 📆 Vencimiento: hay uno solo

`DOC_FECHA_VENC_1` está poblada al 100%. **`DOC_FECHA_VENC_2` y `_VENC_3` están
vacías** (0 filas), igual que `DOC_RECARGO_VENC_2/3`: el modelo prevé segundo y
tercer vencimiento, pero **los datos no los tienen**. `DOC_FECHA_VENC` es
redundante (= `VENC_1` en el 99,99%).

Tiempos medios: emisión → vencimiento **27,4 días**; fin del período leído →
vencimiento **47,7 días**. `DOC_VENC_NRO` no es una fecha sino el número de
vencimiento aplicado; su NULL marca al impago (saldo promedio $82.112 contra
$150 cuando vale 1).

> [!warning] El rango que ve el cliente corre un día
> La boleta oficial presenta el período como **`DOC_FECHA_DESDE + 1` … `DOC_FECHA_HASTA`**
> — corre el inicio para no solapar con la factura anterior, que comparte ese día
> frontera. Verificado contra la API pública de EPEC: su `hasta` es
> `DOC_FECHA_HASTA` exacto y su `desde` es `DOC_FECHA_DESDE + 1`. **La cantidad de
> días no cambia**: sigue siendo `HASTA − DESDE`.

## 📈 Comparar contra el mismo período del año anterior

Self-join de `DOCUMENTOS` por `(SRV_CODIGO, CNT_NUMERO, DOC_ANIO−1, DOC_PERIODO)`.
Tres reglas no negociables:

1. **Normalizar por día.** Solo el 20,4% de los pares dura lo mismo. Comparando
   kWh crudos, **el 6,1% de los casos cambia de signo** (la flecha apunta al
   revés) y el 25,1% se desvía más de 5 pp.
   ```
   kwh_dia = DOC_CONSUMO / (DOC_FECHA_HASTA − DOC_FECHA_DESDE)
   ```
2. **Unir por contrato, no por suministro.** El **12,3%** de los suministros
   cambió de titular entre 2024 y 2025: unir solo por `SRV_CODIGO` muestra el
   consumo del **ocupante anterior**. Cuesta 6 pp de cobertura (92,5% vs 98,7%) y
   es requisito de privacidad.
3. **Comparar kWh, no importe.** El importe mezcla consumo con aumentos
   tarifarios e impuestos: interanual daría un número dominado por la inflación.

> [!bug] `ORDER BY DOC_ANIO DESC` elige basura
> En Oracle los `NULL` ordenan **primero** en `DESC`, y hay facturas con
> `DOC_ANIO` NULL que **se siguen emitiendo** (2.118 en 2026). Sin `NULLS LAST`
> más guardas `IS NOT NULL`, **el 48,9% de los contratos** elige como «última
> factura» un documento sin período, sin fechas y sin consumo.

## 💰 Cómo se compone el importe

`DOC_IMPORTE` = `DOC_IMPORTE_GRAVADO` + `DOC_IMPORTE_EXENTO` (99,27 % de las
facturas 2025).

> [!note] `DOC_IMPORTE_EXENTO` no significa «exento de IVA»
> Es el **bloque de impuestos y cargos**. Verificado ítem por ítem contra
> [[ITEMS]]: IVA Cons. Final 21 % + Ordenanza impositiva municipal 9,90 % +
> Dto. 2298 0,40 % + ERSeP Ley 10281 R.27 0,10 % + Fondo de Desarrollo
> Energético Provincial 10 % + redondeo.

Estructura de una factura residencial típica (ejemplo anonimizado, 29 días):

```
CFI  Cargo Fijo         17 días  ┐
EE1..EE4  Energía por escalón    ├─ vigencia de tarifa V.01/11/24
CFI  Cargo Fijo         12 días  ┐
EE1..EE4  Energía por escalón    ├─ vigencia de tarifa V.01/12/24
                                 ─────────────────────────────────
                                 = DOC_IMPORTE_GRAVADO   (≈ 71 %)
IVC · OIM · DTO · R27 · FDE · RED
                                 = DOC_IMPORTE_EXENTO    (≈ 29 %)
                                 ─────────────────────────────────
                                 = DOC_IMPORTE
```

Dos observaciones que se repiten:

- **[[ITEMS]] cuadra al centavo**: `SUM(ITM_IMPORTE)` por `(DOC_TIPO,
  DOC_NUMERO)` reproduce `DOC_IMPORTE` en el **100 %** de la muestra.
- **El cargo fijo lleva los días**: el ítem `CFI` tiene `ITM_UNIDAD = 'Días'` y
  su cantidad son los días prorrateados por **vigencia de tarifa** (17 + 12 = 29
  = `HASTA − DESDE`). Es la vía para ver el período partido por tarifa.

> [!tip] Para kWh usar `DOC_CONSUMO`, no `ITEMS`
> Los ítems marcados `TIPOS_ITEM.TIT_CONSUMO = 'S'` reproducen `DOC_CONSUMO`
> solo en el 81,5 %. `DOC_CONSUMO` sí cubre la banda horaria completa: coincide
> con `CONS_ENERGIA+PICO+VALLE+RESTO` de [[AUDITORIA_CAMMESA]] en el 99,92 %
> (solo el 0,56 % de las facturas tiene banda horaria).

## 🔗 Del cliente a sus facturas

> [!danger] `DOCUMENTOS.PRS_NUMERO` está vacía
> Existe como columna pero tiene **2 filas pobladas de 14,09 M** facturas 2025.
> Quien la use para llegar al cliente obtiene un resultado vacío sin error.

```
PERSONAS ──PRS_NUMERO──▶ CONTRATOS ──(SRV_CODIGO, CNT_NUMERO)──▶ DOCUMENTOS
```

Un suministro tiene un contrato **por cada titular sucesivo** (ver
[[CONTRATOS]]): para el histórico de lo que se le facturó a alguien **cuando era
titular**, no filtrar por `CNT_ESTADO='V'`. El número de contrato de 10 dígitos
que ve el cliente se **arma**, no se almacena (ver [[Glosario de Negocio]]).

## 🎚️ Filtros obligatorios

```sql
DOC_TIPO   = 'F'   -- factura definitiva
DOC_GRUPO  = 'N'   -- circuito normal de energía
DOC_ESTADO = 'D'   -- definitivo
```

| Sigla | Qué es | Qué hacer |
|---|---|---|
| `F` | Factura definitiva | la base |
| `FP` | Factura **provisoria** (estimada, sin lectura) | **excluir** — duplica consumo (202.948 en 2025) |
| `C` | Nota de crédito | importe y consumo vienen **positivos** → **negar** |
| `D` | Nota de débito | sumar (casi sin consumo) |

Para el facturado **neto** de un período:

```sql
SUM(CASE WHEN DOC_TIPO = 'C' THEN -DOC_IMPORTE ELSE DOC_IMPORTE END)
-- con DOC_TIPO IN ('F','C','D')
```

> [!note] El grano no es único
> 1 factura `F` por contrato-período en el 99,8 %, pero **30.285 contratos
> tuvieron 2** en 2025 (refacturaciones) y 821 tuvieron 3. No asumir unicidad al
> agregar.

## 🚫 Dos falsos amigos

| Objeto | Qué parece | Qué es |
|---|---|---|
| [[CABEZA_LECTURAS]] | Cabecera histórica de lecturas por suministro y período | **Tabla de trabajo**: 11.845 filas, todas con `CLC_ANIO = 1`, una por suministro. Inútil para reconstruir períodos |
| `DOC_IMPORTE_BASICO` | El neto de la factura | Coincide con `DOC_IMPORTE_GRAVADO` solo en el 70,6 % y es menor en el 28,2 %. Usar `GRAVADO` |
| `DOC_PERCEPCION` | Un importe de percepción | **Flag `'S'`/NULL**. Sumarlo tira `ORA-01722` |
| `DOC_SALDO` | Lo facturado | Lo que queda **pendiente de cobro** (cero en el 97,3 %) |

## 🔭 Puntas abiertas

- **Cobranza**: `DOC_SALDO` dice cuánto falta, pero *cuándo y cómo* se pagó está
  en `MOVIMIENTOS_COBRANZA` / `APLICACIONES` — sin verificar.
- **Refacturaciones**: los 30.285 casos con 2 facturas en el mismo período no se
  analizaron.

---
- [[_index|← MOC SIGEC Explorer]] · [[Glosario de Negocio]] · [[Hallazgos]]
- Relacionado: [[Esquema XXSIGEC]] · [[Fronteras - Legales e Ilícitos]]
