---
tipo: dominio
estado: vigente
sensibilidad: interna
tags:
  - sigec-explorer
  - dominio
  - oracle
  - epec
  - tarifas
aliases:
  - Tarifas y Clases
  - Cuadro tarifario SIGEC
  - TCL_CODIGO
  - CLA_CODIGO
  - Tarifas vigentes
  - Clases vigentes
fecha: 2026-08-24
---

# ⚡ Tarifas y clases vigentes — diccionario TCL/CLA

> [!abstract] Qué es esto
> El diccionario de **qué tarifas y clases están realmente en uso** en `XXSIGEC`,
> cómo se obtiene y qué significa cada campo. Verificado contra Oracle el
> **2026-08-24**: de un catálogo de 408 tarifas y 1.165 clases, sólo
> **77 tarifas / 143 pares tarifa-clase** tienen suministros vigentes, y esos 143
> pares cubren **1.206.074 suministros** — el 100 % del parque.
>
> Si vas a desarrollar algo que segmente clientes (dashboards, reportes, filtros,
> reglas de facturación), **este es el universo real**, no [[TARIFAS]] completa.

## 🧭 Respuesta corta

| | |
|---|---|
| Tarifas con uso real | **77** (de 408 en catálogo) |
| Pares tarifa-clase con uso real | **143** (de 1.165 clases en catálogo) |
| Suministros vigentes cubiertos | **1.206.074** |
| Con medición / sin medición | 1.180.693 / 25.381 |
| Con generación distribuida | 903 |

La identidad de una tarifa **no es `TCL_CODIGO` solo**: es el par
(`TCL_CODIGO`, `CLA_CODIGO`). La tarifa 140 («1.a/f RESIDENCIAL») contiene casas
de familia, consorcios CC, consorcios GC y usuarios-generadores, que se facturan
distinto. Segmentar sólo por `TCL_CODIGO` mezcla cosas que el negocio separa.

## 🗺️ El modelo: tres tablas

```
[[TARIFAS]]  ──1:N──▶  [[CLASES]]  ──1:N──▶  [[CONTRATOS]]
 TCL_CODIGO             TCL_CODIGO            TCL_CODIGO
 (408 filas)            CLA_CODIGO            CLA_CODIGO
 el "qué"               (1.165 filas)         CNT_ESTADO='V'
 TCL_GRUPO              la subdivisión        el uso real
```

- **[[TARIFAS]]** — el cuadro tarifario. PK `TCL_CODIGO`. Agrupa por `TCL_GRUPO` (1 a 8).
- **[[CLASES]]** — subdivide cada tarifa. PK compuesta (`TCL_CODIGO`, `CLA_CODIGO`).
  Acá viven las distinciones que cambian el cálculo: CC vs GC, BT/MT/AT,
  usuario-generador, clubes de barrio, tarifa social.
- **[[CONTRATOS]]** — el uso. Un contrato vigente (`CNT_ESTADO='V'`) apunta al par
  (`TCL_CODIGO`, `CLA_CODIGO`) con el que se le factura a ese suministro.

> [!important] La vigencia se demuestra por uso, no por un flag
> `TARIFAS.TCL_ESTADO` **no sirve** para saber qué está vigente. Verificado:
>
> - 159 tarifas marcadas `TCL_ESTADO='V'` **no tienen ningún contrato vigente**.
> - 28 tarifas con `TCL_ESTADO` **NULL** sí tienen contratos vigentes
>   (todo internet/transporte de datos 1300-1330 y alquiler de postes 1600-1603).
> - `TCL_ESTADO='N'` son 8 tarifas «Res. 90/2024 ZF», ninguna en uso.
>
> Por eso la consulta canónica define vigente como **«tiene al menos un suministro
> con contrato vigente»**. Es el único criterio que da un universo coherente.

## 🔍 La consulta canónica

Consulta de referencia. El `CASE` de medición y `CLA_ENERGIA_DIST` son los dos
atributos que casi siempre hacen falta junto al diccionario.

```sql
SELECT * FROM (
  SELECT
      cla.tcl_codigo,
      cla.cla_codigo,
      (SELECT tcl.tcl_descripcion FROM xxsigec.tarifas tcl
        WHERE tcl.tcl_codigo = cla.tcl_codigo)               tcl_descripcion,
      cla.cla_descripcion,
      (SELECT tcl.tcl_grupo FROM xxsigec.tarifas tcl
        WHERE tcl.tcl_codigo = cla.tcl_codigo)               tcl_grupo,
      (SELECT COUNT(DISTINCT cnt.srv_codigo)
         FROM xxsigec.contratos cnt
        WHERE cnt.cnt_numero = (SELECT MAX(cnt2.cnt_numero)
                                  FROM xxsigec.contratos cnt2
                                 WHERE cnt.srv_codigo  = cnt2.srv_codigo
                                   AND cnt2.cnt_estado = 'V'
                                   AND cla.tcl_codigo  = cnt2.tcl_codigo
                                   AND cla.cla_codigo  = cnt2.cla_codigo)
          AND cnt.cnt_estado = 'V'
          AND cla.tcl_codigo = cnt.tcl_codigo
          AND cla.cla_codigo = cnt.cla_codigo)               conteo_sumi,
      (CASE WHEN tcl_codigo IN (189,188,540,605,242)
            THEN 'SIN MEDICION' ELSE 'CON MEDICION' END)     con_sin_med,
      cla.cla_energia_dist                                   energia_dist
    FROM xxsigec.clases cla
   ORDER BY TO_NUMBER(cla.tcl_codigo), TO_NUMBER(cla.cla_codigo)
)
WHERE conteo_sumi > 0
```

### Equivalente simplificado

El `MAX(CNT_NUMERO)` es una defensa contra un caso que **no ocurre**: se verificó
que `CNT_ESTADO='V'` devuelve 1.206.074 filas para 1.206.074 suministros
distintos — hay **exactamente un contrato vigente por suministro**, y **cero**
suministros en más de una clase. Esta versión da el **mismo resultado** (143
pares, mismos conteos, 0 diferencias) y recorre [[CONTRATOS]] una sola vez:

```sql
SELECT c.tcl_codigo, c.cla_codigo,
       t.tcl_descripcion, cl.cla_descripcion, t.tcl_grupo,
       COUNT(DISTINCT c.srv_codigo)                          conteo_sumi,
       CASE WHEN c.tcl_codigo IN ('188','189','242','540','605')
            THEN 'SIN MEDICION' ELSE 'CON MEDICION' END      con_sin_med,
       cl.cla_energia_dist                                   energia_dist
  FROM xxsigec.contratos c
  JOIN xxsigec.clases  cl ON cl.tcl_codigo = c.tcl_codigo
                         AND cl.cla_codigo = c.cla_codigo
  JOIN xxsigec.tarifas t  ON t.tcl_codigo  = c.tcl_codigo
 WHERE c.cnt_estado = 'V'
 GROUP BY c.tcl_codigo, c.cla_codigo, t.tcl_descripcion,
          cl.cla_descripcion, t.tcl_grupo, cl.cla_energia_dist
 ORDER BY TO_NUMBER(c.tcl_codigo), TO_NUMBER(c.cla_codigo)
```

Usá la original si querés partir del catálogo (te deja ver también las clases con
0 suministros); la simplificada si querés el universo real y que sea rápida.

### Qué devuelve cada columna

| Columna | De dónde sale | Cómo leerla |
|---|---|---|
| `TCL_CODIGO` | `CLASES` / `CONTRATOS` | Código de tarifa. **VARCHAR2 con ceros a la izquierda** (`'010'`) |
| `CLA_CODIGO` | `CLASES` / `CONTRATOS` | Subdivisión. Sólo es único junto a `TCL_CODIGO` |
| `TCL_DESCRIPCION` | `TARIFAS` | Nombre del cuadro tarifario. **Se repite entre tarifas distintas** |
| `CLA_DESCRIPCION` | `CLASES` | El texto que realmente identifica al segmento |
| `TCL_GRUPO` | `TARIFAS` | Rubro contable 1-8 (ver tabla de grupos) |
| `CONTEO_SUMI` | `CONTRATOS` | Suministros distintos con contrato vigente en ese par |
| `CON_SIN_MED` | **hardcodeado** | Lista fija de 5 tarifas. No hay columna que lo diga |
| `ENERGIA_DIST` | `CLASES.CLA_ENERGIA_DIST` | `'S'` = clase de generación distribuida (usuario-generador) |

## ⚠️ Trampas para el desarrollo

> [!warning] 1. `TCL_CODIGO` es VARCHAR2 con ceros a la izquierda
> 6 tarifas del catálogo empiezan con `0`: `'010'`, `'011'`, `'032'`, `'033'`…
> `'010' = '10'` es **falso** como string. Por eso el `ORDER BY TO_NUMBER(...)`.
> Si comparás, hacelo con el string exacto (`= '010'`) o convertí ambos lados con
> `TO_NUMBER`. Nunca mezcles.
>
> El `IN (189,188,540,605,242)` de la consulta original funciona sólo porque
> Oracle convierte implícitamente la columna a `NUMBER` (verificado: los 408
> códigos son numéricos, así que hoy no rompe). Es frágil — en la versión
> simplificada se compara contra strings a propósito.

> [!warning] 2. «Sin medición» está hardcodeado
> No existe columna en [[TARIFAS]] ni [[CLASES]] que marque si el suministro se
> mide. La lista **`188, 189, 242, 540, 605`** es conocimiento de negocio embebido
> en la consulta:
>
> | TCL | Qué es | Suministros |
> |---:|---|---:|
> | `188` | Social Provincial sin medición (loteos) | 8.374 |
> | `189` | Residencial sin medición | 9.531 |
> | `242` | General y Servicios sin medición (CC + GC) | 2.128 |
> | `540` | Gobierno Nac./Prov./Mun. sin medición | 5.163 |
> | `605` | Alumbrado público con convenio, sin medición | 185 |
>
> Total **25.381** suministros (2,1 % del parque). Si aparece una tarifa nueva sin
> medición hay que **actualizar esta lista a mano**. Ojo con `1089` («Res. Sin
> Med. RG 25 - Art. 7», 35 suministros): dice «sin medición» en la descripción
> pero **no está en la lista**, así que la consulta la cuenta como *con* medición.
> Verificar con negocio antes de asumir cualquiera de las dos cosas.

> [!warning] 3. La descripción de la tarifa no identifica nada
> `TCL_DESCRIPCION` se repite entre tarifas distintas: `'1.a/f RESIDENCIAL'` es la
> 140 **y** la 1000; `'Resid TSP Indig Dto. 43/19'` es la 184, la 584 y la 587;
> `'5.2a USUARIOS ESPECIALES'` son la 542 y la 544. Para mostrarle algo a un
> usuario usá `CLA_DESCRIPCION`, o el par código + descripción de clase.

> [!warning] 4. El grupo 3 no es «industrial»
> `TCL_GRUPO=3` mezcla Grandes Consumos, Peaje (923), Uso Propio de EPEC (011,
> 032, 033) y **servicios que no son electricidad**: internet y transporte de
> datos (1300-1330) y alquiler de postes (1600-1603). Si tu reporte es de energía,
> esos ~430 suministros hay que excluirlos explícitamente.

> [!warning] 5. Generación distribuida: usá el flag, no el código de clase
> `CLA_CODIGO='9'` es la **convención** para el usuario-generador, pero no es
> regla: 6 clases con `CLA_CODIGO='9'` **no** son GD, y hay clases GD con código
> 1, 4, 5, 6, 7, 8, 10, 11, 12, 14, 15 y 17. El criterio correcto es
> **`CLA_ENERGIA_DIST = 'S'`** (903 suministros vigentes).

> [!tip] 6. Tarifa social: `CLA_SOCIAL_TIPO = 'SP'`
> 10 clases vigentes, **80.673** suministros — tarifas 180, 184, 188, 580, 584 y
> 587. La columna `CLA_PREPAGO` está **100 % NULL**: no hay prepago en SIGEC.

> [!note] 7. Los conteos de fila del catálogo están desactualizados
> [[TARIFAS]] y [[CLASES]] en este vault dicen 405 y 1.136 filas (vienen del
> `NUM_ROWS` estimado de Oracle). El conteo real al 2026-08-24 es **408** y
> **1.165**. No afecta a nada de esta nota, pero no uses `NUM_ROWS` como dato duro.

## 🏷️ Segmentos transversales (GD, movilidad eléctrica, social…)

> [!important] Son etiquetas, no una partición
> Estos segmentos **se solapan**: la clase `1410/9` es movilidad eléctrica **y**
> generación distribuida a la vez; `188/1` es tarifa social **y** sin medición.
> No sumes las filas de esta tabla esperando llegar al total del parque — para
> particionar usá `TCL_GRUPO`, que sí es excluyente.

### Sólo dos segmentos tienen flag real en la base

| Segmento | Criterio | Confiable |
|---|---|---|
| Generación distribuida | `CLA_ENERGIA_DIST = 'S'` | ✅ Sí |
| Tarifa social provincial | `CLA_SOCIAL_TIPO = 'SP'` | ✅ Sí |
| Cooperativas | `TCL_COOPERATIVAS_FLAG = 'S'` | ❌ **No — ver abajo** |

**Todo el resto hay que enumerarlo por `TCL_CODIGO`.** No existe columna de
categoría, rubro comercial ni «tipo de servicio» más allá de `TCL_GRUPO`.
`CLA_GRUPO` **no sirve**: vale `'AA'` en las 1.165 clases del catálogo.
`XX_TARIFAS_GRUPOS` tampoco: su contenido es de 2005 y apunta a tarifas
(`000`, `031`, `115`, `126`, `130`, `232`…) que hoy no tienen ni un contrato vigente.

> [!warning] `TCL_COOPERATIVAS_FLAG` no significa «es cooperativa»
> No coincide con el grupo 4. El flag `'S'` **incluye** tarifas que no son
> cooperativas y **excluye** una que sí lo es:
>
> | TCL/CLA | Grupo | Flag | Qué es |
> |---|:-:|:-:|---|
> | `355/1` | 3 | **S** | 3.1.2 c Parques Industriales |
> | `358/1` | 3 | **S** | 3.1.3 b EDESE S.A. |
> | `401/1` | **4** | **N** | 4.1 Coop. Electricidad ← es cooperativa y el flag dice que no |
> | `410`, `411` | 4 | S | 4.2 Coop. Eléctricas |
>
> Parece marcar «se factura como distribuidor mayorista», no «es cooperativa».
> Para cooperativas usá **`TCL_GRUPO = '4'`** (3 tarifas, 5 clases, 279 suministros).

### Tabla de segmentos

Foto de una única transacción de lectura (total 1.206.064 suministros en ese
instante; ver la nota sobre deriva al pie). **GD** = cuántas de esas clases son
además de generación distribuida.

| Segmento | Criterio | Clases | Suministros | GD |
|---|---|---:|---:|---:|
| Tarifa social provincial | `CLA_SOCIAL_TIPO='SP'` | 10 | 80.673 | 0 |
| Ex carenciados / indigentes | `TCL 1000` | 2 | 33.328 | 0 |
| Sin medición | `TCL 188,189,242,540,605` | 6 | 25.381 | 0 |
| Consorcios | descripción «Consorcio» | 3 | 9.186 | 0 |
| Alumbrado público | `TCL_GRUPO='6'` + `356` | 4 | 7.603 | 0 |
| Empleados / jubilados EPEC | `TCL 150, 1520` | 6 | 4.944 | 2 |
| Grandes consumos | `TCL 350,353,355,356,358` | 18 | 3.255 | 5 |
| Electrodependientes | `TCL 1800` | 1 | 1.231 | 0 |
| Entidades religiosas | descripción «Religiosas» | 6 | 1.162 | 2 |
| **Generación distribuida** | `CLA_ENERGIA_DIST='S'` | **24** | **903** | 24 |
| No eléctricos (internet + postes) | `TCL 1300-1330`, `1600-1603` | 26 | 855 | 0 |
| ├ Internet / transporte de datos | `TCL 1300-1330` | 22 | 728 | 0 |
| └ Alquiler de postes | `TCL 1600-1603` | 4 | 127 | 0 |
| **Movilidad eléctrica** | `TCL 1410, 1520, 2411` | **6** | **820** | 3 |
| Rural | `TCL_GRUPO='8'` | 3 | 619 | 1 |
| Uso propio EPEC | `TCL 010, 011, 032, 033` | 7 | 460 | 2 |
| Clubes de barrio | descripción «Clubes de Barrio» | 4 | 292 | 0 |
| Cooperativas | `TCL_GRUPO='4'` | 5 | 279 | 1 |
| Peaje (GUMEs / GUMAs) | `TCL 923` | 7 | 133 | 0 |
| Servicio de agua | `TCL_GRUPO='7'` | 2 | 64 | 0 |
| Bomberos voluntarios | descripción «Bom. Volunt» | 2 | 43 | 0 |
| Parques fotovoltaicos | `TCL 3550` | 1 | 3 | 1 |

> [!caution] Los segmentos por descripción son frágiles
> «Consorcios», «Religiosas», «Clubes de Barrio» y «Bomberos» salen de hacer
> `LIKE` sobre `CLA_DESCRIPCION`. Sirven para explorar, **no** para una regla de
> negocio: las descripciones tienen erratas (`'Conercial Discrimi.Gener Engia'`),
> abreviaturas inconsistentes y truncamientos a 30 caracteres. Si un segmento va a
> vivir en código, convertilo a **lista explícita de pares (TCL, CLA)** revisada
> con negocio, y dejá la lista versionada.

### Generación distribuida — las 24 clases

903 suministros. Es la única clase de segmento que se puede pedir con un
`WHERE` limpio: `cl.cla_energia_dist = 'S'`.

| TCL/CLA | Suministros | Clase | Segmento base |
|---|---:|---|---|
| `140/9` | 459 | Residencial Generador Energia | Residencial |
| `240/9` | 181 | 2 Comercial Generador Energia | Comercial |
| `241/9` | 68 | Conercial Discrimi.Gener Engia | Comercial discriminada |
| `350/9` | 60 | 3.1.1 BT Generador Energ | Grandes consumos |
| `350/12` | 41 | Gdes. Consumos Generador Energ | Grandes consumos |
| `1410/9` | 25 | Resid. Mov Elect / Gen.Energia | **Movilidad eléctrica** |
| `353/9` | 22 | Grandes Consumos Gdor Energia | Grandes consumos |
| `144/9` | 13 | Comercial con Base Gener. Ener | Residencial comercial |
| `150/9` | 5 | Generador de Energia | Empleados EPEC |
| `350/15` | 4 | MT/bt DA > 40 - Gen. Energia | Grandes consumos |
| `542/9` | 4 | GENERADOR DE ENERGIA | Usuarios especiales |
| `411/9` | 3 | Energia Inyectada (Autoconsumo | Cooperativas |
| `3550/1` | 3 | PARQUES FOTOVOLTAICOS | **Parques fotovoltaicos** |
| `541/9` | 2 | ENERGIA INYECTADA | Gobierno |
| `543/9` | 2 | ENERGIA INYECTADA | Gobierno |
| `547/9` | 2 | Ent. Religiosas - Gen. Ener. | Religiosas |
| `2411/9` | 2 | GENERACION DE ENERGIA | **Movilidad eléctrica comercial** |
| `010/9` | 1 | EPEC - U.P. Energia Inyectada | Uso propio |
| `032/9` | 1 | EPEC - U.P. Energia Inyectada | Uso propio |
| `350/8` | 1 | GUDI>300 Gen. Ener. Org. Pub. | Grandes consumos |
| `515/9` | 1 | Usuario Generador | Org. sindicales |
| `545/9` | 1 | Ent. Religiosas - Gen. Ener. | Religiosas |
| `832/9` | 1 | Rural Generador Energia | Rural |
| `1520/9` | 1 | Mov. Elec. Emp. - Gen. Energia | **Movilidad eléctrica empleados** |

`3550/1` («Parques Fotovoltaicos») es la única clase GD que **no** es la variante
«generador» de una tarifa de consumo: es una tarifa propia. Las otras 23 siempre
son el espejo de un segmento base — por eso GD se cruza con todo.

### Movilidad eléctrica — las 6 clases

820 suministros en 3 tarifas. No hay flag: **hay que enumerar**.

| TCL/CLA | Suministros | Tarifa | Clase |
|---|---:|---|---|
| `1410/1` | 774 | 1.j Res. Mov. Electrica | Resid. Movilidad Electrica |
| `1410/9` | 25 | 1.j Res. Mov. Electrica | Resid. Mov Elect / Gen.Energia ⚡ |
| `1520/1` | 12 | Mov. Electrica Empleados | Mov. Electrica Empleados |
| `1520/9` | 1 | Mov. Electrica Empleados | Mov. Elec. Emp. - Gen. Energia ⚡ |
| `2411/1` | 5 | Movilidad Electrica (c/DISC) | 2 MOV. ELECTRICA - COMERCIAL |
| `2411/9` | 2 | Movilidad Electrica (c/DISC) | GENERACION DE ENERGIA ⚡ |

El patrón se repite en los tres casos: clase `1` consumo, clase `9` usuario
generador. Es la convención, pero recordá la trampa 5 — no la uses como regla.


## 📊 El diccionario por grupo

Los 8 grupos particionan el parque de forma exacta: la suma da 1.206.074, sin
solapamiento ni huérfanos (0 contratos vigentes apuntan a una clase inexistente).

Leyenda: **Med.** ✓ con medición · — sin medición · **GD** ⚡ clase de generación
distribuida.

| Grupo | Rubro | Tarifas | Clases | Suministros |
|---:|---|---:|---:|---:|
| 1 | Residencial | 15 | 29 | 1.068.882 |
| 2 | Comercial / General y Servicios | 5 | 14 | 109.514 |
| 3 | Grandes Consumos, Peaje, Uso Propio, no eléctricos | 28 | 49 | 3.991 |
| 4 | Cooperativas | 3 | 5 | 279 |
| 5 | Oficial (Gobierno y Usuarios Especiales) | 19 | 38 | 15.133 |
| 6 | Alumbrado Público | 3 | 3 | 7.592 |
| 7 | Servicio de Agua | 2 | 2 | 64 |
| 8 | Rural | 2 | 3 | 619 |
| | **Total** | **77** | **143** | **1.206.074** |

### Grupo 1 — Residencial

15 tarifas · 29 clases · **1.068.882** suministros

| TCL | CLA | Tarifa (TCL_DESCRIPCION) | Clase (CLA_DESCRIPCION) | Suministros | Med. | GD |
|---:|---:|---|---|---:|:-:|:-:|
| `140` | `1` | 1.a/f RESIDENCIAL | 1 a-b-f Casas de familia | 915.012 | ✓ |  |
| `140` | `2` | 1.a/f RESIDENCIAL | 1 c   Consorcios C.C. | 9.044 | ✓ |  |
| `140` | `3` | 1.a/f RESIDENCIAL | 1 c   Gobierno-Viviendas | 26 | ✓ |  |
| `140` | `4` | 1.a/f RESIDENCIAL | 1 c   Consorcios G.C. | 28 | ✓ |  |
| `140` | `9` | 1.a/f RESIDENCIAL | Residencial Generador Energia | 459 | ✓ | ⚡ |
| `144` | `1` | 1.d RESID.COMERCIAL | 1.d Comercial con Base | 13.653 | ✓ |  |
| `144` | `9` | 1.d RESID.COMERCIAL | Comercial con Base Gener. Ener | 13 | ✓ | ⚡ |
| `146` | `1` | TARIFA CONSORCIO G.C. | 1C  CONSORCIOS G.C. | 114 | ✓ |  |
| `150` | `1` | 1.h   RESIDENCIAL | 1 a   Tar.Empleados EPEC | 2.448 | ✓ |  |
| `150` | `2` | 1.h   RESIDENCIAL | 1 a   Jubilados,pen.EPEC | 2.347 | ✓ |  |
| `150` | `4` | 1.h   RESIDENCIAL | 1 a   Trab.act.LyF-SUE-APSE | 130 | ✓ |  |
| `150` | `9` | 1.h   RESIDENCIAL | Generador de Energia | 5 | ✓ | ⚡ |
| `180` | `1` | Resid TSP Caren Dto. 43/19 | 1 a-b-f Casas de familia | 37.923 | ✓ |  |
| `180` | `2` | Resid TSP Caren Dto. 43/19 | Trf.Solidaria Serv. Res. | 1.281 | ✓ |  |
| `184` | `1` | Resid TSP Indig Dto. 43/19 | 1 a-b-f Casas de familia | 31.223 | ✓ |  |
| `184` | `2` | Resid TSP Indig Dto. 43/19 | Transf.Solidaria Residencial | 1.566 | ✓ |  |
| `187` | `1` | 1.a/f RES.SOCIAL PROV. INDIG. | 1 a-b-f Casas de familia | 6 | ✓ |  |
| `188` | `1` | Social Prov. sin medición | 1g LOTEOS SIN MED. SOC. PROV. | 8.374 | — |  |
| `189` | `1` | Residencial Sin Medicion | RESIDENCIAL SIN MEDICION | 9.531 | — |  |
| `1000` | `1` | 1.a/f RESIDENCIAL | Residencial - Ex. Carenciados | 20.118 | ✓ |  |
| `1000` | `2` | 1.a/f RESIDENCIAL | Residencial - Ex. Indigentes | 13.211 | ✓ |  |
| `1089` | `1` | Res. PRIEFU RG 25 D Art. 7 | Res. Sin Med. RG 25 - Art. 7 | 35 | ✓ |  |
| `1330` | `1` | Internet Residencial | Internet Abono Mensual 50 Mbs | 120 | ✓ |  |
| `1330` | `2` | Internet Residencial | Internet Abono Mensual 100 Mbs | 172 | ✓ |  |
| `1410` | `1` | 1.j Res. Mov. Electrica | Resid. Movilidad Electrica | 774 | ✓ |  |
| `1410` | `9` | 1.j Res. Mov. Electrica | Resid. Mov Elect / Gen.Energia | 25 | ✓ | ⚡ |
| `1520` | `1` | Mov. Electrica Empleados | Mov. Electrica Empleados | 12 | ✓ |  |
| `1520` | `9` | Mov. Electrica Empleados | Mov. Elec. Emp. - Gen. Energia | 1 | ✓ | ⚡ |
| `1800` | `1` | ELECTRODEPENDIENTE | RES. ELECTRODEPENDIENTE | 1.231 | ✓ |  |

### Grupo 2 — Comercial / General y Servicios

5 tarifas · 14 clases · **109.514** suministros

| TCL | CLA | Tarifa (TCL_DESCRIPCION) | Clase (CLA_DESCRIPCION) | Suministros | Med. | GD |
|---:|---:|---|---|---:|:-:|:-:|
| `010` | `1` | USO PROPIO - Mono-trif | EPEC - U.P. Monomica b.t. | 307 | ✓ |  |
| `010` | `9` | USO PROPIO - Mono-trif | EPEC - U.P. Energia Inyectada | 1 | ✓ | ⚡ |
| `240` | `1` | 2 GENERAL Y DE SERVICIOS | 2  Comercial  C.C | 101.512 | ✓ |  |
| `240` | `2` | 2 GENERAL Y DE SERVICIOS | 2  Industrial   C.C. | 1.218 | ✓ |  |
| `240` | `3` | 2 GENERAL Y DE SERVICIOS | 2  Comercial  GC | 1.849 | ✓ |  |
| `240` | `4` | 2 GENERAL Y DE SERVICIOS | 2  Industrial   GC | 6 | ✓ |  |
| `240` | `9` | 2 GENERAL Y DE SERVICIOS | 2 Comercial Generador Energia | 181 | ✓ | ⚡ |
| `241` | `1` | 2 GRAL.y SERV.(c/DISC) | 2 COMERCIAL G.C. DISCRIMINADA | 2.110 | ✓ |  |
| `241` | `2` | 2 GRAL.y SERV.(c/DISC) | 2 INDUSTRIAL G.C. DISCRIMINADA | 127 | ✓ |  |
| `241` | `9` | 2 GRAL.y SERV.(c/DISC) | Conercial Discrimi.Gener Engia | 68 | ✓ | ⚡ |
| `242` | `1` | 2 GENERAL Y DE SERVICIOS | 2 SIN MEDICION CC | 82 | — |  |
| `242` | `2` | 2 GENERAL Y DE SERVICIOS | 2 SIN MEDICION GC | 2.046 | — |  |
| `2411` | `1` | Movilidad Electrica (c/DISC) | 2 MOV. ELECTRICA - COMERCIAL | 5 | ✓ |  |
| `2411` | `9` | Movilidad Electrica (c/DISC) | GENERACION DE ENERGIA | 2 | ✓ | ⚡ |

### Grupo 3 — Grandes Consumos, Peaje, Uso Propio y no eléctricos

28 tarifas · 49 clases · **3.991** suministros

| TCL | CLA | Tarifa (TCL_DESCRIPCION) | Clase (CLA_DESCRIPCION) | Suministros | Med. | GD |
|---:|---:|---|---|---:|:-:|:-:|
| `011` | `1` | USO PROPIO Bº C/LIMIT. MED. SE | EPEC - U.P. Monomica b.t. | 84 | ✓ |  |
| `032` | `1` | EPEC - USO PROPIO | EPEC - U.P.  B.T. | 61 | ✓ |  |
| `032` | `2` | EPEC - USO PROPIO | EPEC - U.P.  M.T. | 4 | ✓ |  |
| `032` | `9` | EPEC - USO PROPIO | EPEC - U.P. Energia Inyectada | 1 | ✓ | ⚡ |
| `033` | `1` | EPEC USO PROPIO BARRIOS C/LIMIT. MED. SE | EPEC - U.P.   B.T. | 2 | ✓ |  |
| `350` | `1` | TARIFA 3-GDES.CONSUMOS | 3.1.1 a 40<= DA <=1000 | 2.035 | ✓ |  |
| `350` | `2` | TARIFA 3-GDES.CONSUMOS | 3.1.2 a/b MT/mt DA > 40 | 569 | ✓ |  |
| `350` | `4` | TARIFA 3-GDES.CONSUMOS | 3.1.2 a/b MT/bt DA > 40 | 67 | ✓ |  |
| `350` | `6` | TARIFA 3-GDES.CONSUMOS | 3.1.3 a/b DA > 40 AT | 5 | ✓ |  |
| `350` | `7` | TARIFA 3-GDES.CONSUMOS | GUDI>300 Kw Org. Pub. Sal/Edu | 21 | ✓ |  |
| `350` | `8` | TARIFA 3-GDES.CONSUMOS | GUDI>300 Gen. Ener. Org. Pub. | 1 | ✓ | ⚡ |
| `350` | `9` | TARIFA 3-GDES.CONSUMOS | 3.1.1 BT Generador Energ | 60 | ✓ | ⚡ |
| `350` | `10` | TARIFA 3-GDES.CONSUMOS | 3.1.1 a BT - Org. Pub Sal/Edu. | 2 | ✓ |  |
| `350` | `12` | TARIFA 3-GDES.CONSUMOS | Gdes. Consumos Generador Energ | 41 | ✓ | ⚡ |
| `350` | `13` | TARIFA 3-GDES.CONSUMOS | Clubes de Barrio Res. SE 742 | 8 | ✓ |  |
| `350` | `15` | TARIFA 3-GDES.CONSUMOS | MT/bt DA > 40 - Gen. Energia | 4 | ✓ | ⚡ |
| `353` | `2` | CONT.EN BAJA DA>100 | 3.1.1 b BT/bt DA > 100 | 394 | ✓ |  |
| `353` | `3` | CONT.EN BAJA DA>100 | Clubes de Barrio Res. SE 742 | 1 | ✓ |  |
| `353` | `7` | CONT.EN BAJA DA>100 | GUDI>300 Kw Org. Pub. Sal/Edu | 8 | ✓ |  |
| `353` | `9` | CONT.EN BAJA DA>100 | Grandes Consumos Gdor Energia | 22 | ✓ | ⚡ |
| `355` | `1` | 3.1.2 c PQUES INDUST. | 3.1.2 c PARQUES INDUSTRIALES | 4 | ✓ |  |
| `356` | `1` | Tarifa 3 - Gdes.Consumos | 3.1.1 a ALUMBRADO PUBLICO | 11 | ✓ |  |
| `358` | `1` | 3.1.3 b EDESE S.A. | 3.1.3 b EDESE S.A. | 1 | ✓ |  |
| `923` | `1` | 9 SERVICIO DE PEAJE | GUMES BT 40<= DA <= 1000 | 39 | ✓ |  |
| `923` | `2` | 9 SERVICIO DE PEAJE | GUMES BT DA > 100 S/SUBEST | 2 | ✓ |  |
| `923` | `3` | 9 SERVICIO DE PEAJE | GUMES/GUMAS MT | 74 | ✓ |  |
| `923` | `4` | 9 SERVICIO DE PEAJE | GUMES/GUMAS MT/BT (INTERMEDIA) | 8 | ✓ |  |
| `923` | `5` | 9 SERVICIO DE PEAJE | GUMAS AT | 7 | ✓ |  |
| `923` | `6` | 9 SERVICIO DE PEAJE | GUMAS MT B/JURIDIC. COOP. | 2 | ✓ |  |
| `923` | `7` | 9 SERVICIO DE PEAJE | GUMAS AT B/JURIDIC. COOP. | 1 | ✓ |  |
| `1300` | `1` | Transporte menos de 1Gb | Transporte menos de 1Gb | 43 | ✓ |  |
| `1301` | `1` | Transporte mas de 1 GB a  2 GB | Transporte entre 1 y 2 GB | 2 | ✓ |  |
| `1302` | `1` | Transporte de 1 GB o mas | Transporte de 1 GB o mas | 30 | ✓ |  |
| `1303` | `1` | Transporte menos de 1Gb | Transporte menos de 1Gb | 1 | ✓ |  |
| `1304` | `1` | Empresas menos de 100 Mbps. | Empresas menos de 100 Mbps. | 63 | ✓ |  |
| `1305` | `1` | Empresas - De 100 Mbps o Mas | Empresas - De 100 Mbps o Mas | 21 | ✓ |  |
| `1308` | `1` | ISP/Coop. Hasta 200 Mbps. | ISP/Coop. Hasta 200 Mbps. | 2 | ✓ |  |
| `1310` | `1` | ISP/Coop. - Menos de 1 GB | ISP/Coop. - Menos de 1 GB | 48 | ✓ |  |
| `1311` | `1` | ISP/Coop. - De 1 GB o Mas | ISP/Coop. - De 1 GB o Mas | 52 | ✓ |  |
| `1320` | `1` | Int. Din 30mb UP/50 Mb Down | Int. dina 30Mbs UP/50Mbs Down | 30 | ✓ |  |
| `1321` | `1` | Int Din 30 Mb UP/100 Mb Down | Int din 30 Mbs UP/100 Mbs Down | 6 | ✓ |  |
| `1322` | `1` | Int Din 30Mbs UP/300 Mbs Down | Int Din 30 Mbs UP/300 Mbs Down | 13 | ✓ |  |
| `1323` | `1` | Int Simet 4/4 Mb UP/50 Mb Down | Int Sim 4/4 50MbsUP/50Mbs Down | 9 | ✓ |  |
| `1326` | `1` | Int. Din 60mb UP/600 Mbs Down | Int. dina 60Mbs UP/600Mbs Down | 2 | ✓ |  |
| `1600` | `1` | Alquiler de postes hasta 10000 clientes | Alquiler Postes < 10.000 Cltes | 42 | ✓ |  |
| `1601` | `1` | Alq. Postes entre 10000 y 50000 Cltes. | Alq. Post. 10.000 y 50.000 clt | 24 | ✓ |  |
| `1602` | `1` | Alq. Postes  de mas de 50000 clientes | Alq. Postes > a 50.000 Cltes. | 18 | ✓ |  |
| `1603` | `1` | Alq. Postes Media Tension | Alquiler Post. - Media Tension | 43 | ✓ |  |
| `3550` | `1` | PARQUES FOTOVOLTAICOS | PARQUES FOTOVOLTAICOS | 3 | ✓ | ⚡ |

### Grupo 4 — Cooperativas

3 tarifas · 5 clases · **279** suministros

| TCL | CLA | Tarifa (TCL_DESCRIPCION) | Clase (CLA_DESCRIPCION) | Suministros | Med. | GD |
|---:|---:|---|---|---:|:-:|:-:|
| `401` | `1` | 4.1   COOP. ELECTRICIDAD | 4.1.a/b Sin med.potencia BT/MT | 7 | ✓ |  |
| `410` | `1` | 4.2 Coop.Electricas | 4.2.1 Coop.c/Fac.DP y DF | 36 | ✓ |  |
| `411` | `1` | 4.2 Coop.Electricas | 4.2.2a Coop.c/Fac.DP DF | 224 | ✓ |  |
| `411` | `3` | 4.2 Coop.Electricas | 4.2.3 Coop.c/Fac DP DF | 9 | ✓ |  |
| `411` | `9` | 4.2 Coop.Electricas | Energia Inyectada (Autoconsumo | 3 | ✓ | ⚡ |

### Grupo 5 — Oficial (Gobierno y Usuarios Especiales)

19 tarifas · 38 clases · **15.133** suministros

| TCL | CLA | Tarifa (TCL_DESCRIPCION) | Clase (CLA_DESCRIPCION) | Suministros | Med. | GD |
|---:|---:|---|---|---:|:-:|:-:|
| `515` | `1` | Org. Sind. Art. 77 CCT. | Clientes Comunes | 58 | ✓ |  |
| `515` | `2` | Org. Sind. Art. 77 CCT. | Grandes Clientes | 10 | ✓ |  |
| `515` | `9` | Org. Sind. Art. 77 CCT. | Usuario Generador | 1 | ✓ | ⚡ |
| `517` | `1` | Org. Sind. Art. 77 CCT. | Clientes Comunes | 1 | ✓ |  |
| `540` | `1` | 5.1 Gob. Nac. Prov. Muni. sin medición | 5.1 Gob. Prov. sin medición | 5.163 | — |  |
| `541` | `1` | GOBIERNO Nac/Prov./Mun/V. | 5.1 GOBIERNO Nac/Prov/Munic. | 4.793 | ✓ |  |
| `541` | `9` | GOBIERNO Nac/Prov./Mun/V. | ENERGIA INYECTADA | 2 | ✓ | ⚡ |
| `542` | `1` | 5.2a USUARIOS ESPECIALES | 5.2 a Ent.civiles CC | 1.773 | ✓ |  |
| `542` | `2` | 5.2a USUARIOS ESPECIALES | 5.2 a Ent.civiles GC | 685 | ✓ |  |
| `542` | `4` | 5.2a USUARIOS ESPECIALES | Clubes de Barrio Res. SE 742 | 246 | ✓ |  |
| `542` | `6` | 5.2a USUARIOS ESPECIALES | Ent. Sist. Nac. Bom. Volunt. | 41 | ✓ |  |
| `542` | `9` | 5.2a USUARIOS ESPECIALES | GENERADOR DE ENERGIA | 4 | ✓ | ⚡ |
| `543` | `1` | 5.1 GOBIERNO NAC/PROV/MUN | 5.1 GOBIERNO Nac/Prov/Munic. | 561 | ✓ |  |
| `543` | `7` | 5.1 GOBIERNO NAC/PROV/MUN | GUDI>300 Kw Org. Pub. Sal/Edu | 2 | ✓ |  |
| `543` | `9` | 5.1 GOBIERNO NAC/PROV/MUN | ENERGIA INYECTADA | 2 | ✓ | ⚡ |
| `544` | `1` | 5.2a USUARIOS ESPECIALES | 5.2 a Ent.civiles GC | 120 | ✓ |  |
| `544` | `2` | 5.2a USUARIOS ESPECIALES | 5.2 a Ent.civiles GC | 18 | ✓ |  |
| `544` | `3` | 5.2a USUARIOS ESPECIALES | Clubes de Barrio Res. SE 742 | 37 | ✓ |  |
| `544` | `5` | 5.2a USUARIOS ESPECIALES | Ent. Sist. Nac. Bom. Volunt. | 2 | ✓ |  |
| `545` | `1` | 5.2.b USUAR. ESPECIALES | 5.2     b   E.Religiosas  C.C. | 469 | ✓ |  |
| `545` | `2` | 5.2.b USUAR. ESPECIALES | 5.2     b   E.Religiosas  G.C. | 674 | ✓ |  |
| `545` | `9` | 5.2.b USUAR. ESPECIALES | Ent. Religiosas - Gen. Ener. | 1 | ✓ | ⚡ |
| `546` | `1` | 5.2.c USUAR. ESPECIALES | 5.2     c   Hogares grat. C.C. | 19 | ✓ |  |
| `546` | `2` | 5.2.c USUAR. ESPECIALES | 5.2     c   Hogares grat. G.C. | 13 | ✓ |  |
| `547` | `1` | 5.2.b USUAR. ESPECIALES | 5.2     b   E.Religiosas  C.C. | 5 | ✓ |  |
| `547` | `2` | 5.2.b USUAR. ESPECIALES | 5.2     b   E.Religiosas  G.C. | 11 | ✓ |  |
| `547` | `9` | 5.2.b USUAR. ESPECIALES | Ent. Religiosas - Gen. Ener. | 2 | ✓ | ⚡ |
| `580` | `1` | Resid TSP Caren Dto. 43/19 | Carenc.Ctro Jub/Pen.MDS 573/08 | 30 | ✓ |  |
| `584` | `1` | Resid TSP Indig Dto. 43/19 | Indig.Ctro Jub/Pen.MDS 573/08 | 267 | ✓ |  |
| `584` | `2` | Resid TSP Indig Dto. 43/19 | Indig. Centros Vec. MDS 496/09 | 3 | ✓ |  |
| `584` | `3` | Resid TSP Indig Dto. 43/19 | Indig. ONG y Otros MDS 196/10 | 4 | ✓ |  |
| `587` | `1` | Resid TSP Indig Dto. 43/19 | T. 5.2a con discr.energ/dem. | 2 | ✓ |  |
| `1312` | `1` | Transporte - Gobierno | Transporte Gobierno | 24 | ✓ |  |
| `1313` | `1` | Gobierno Nacional - Entes | Gobierno Nacional - Entes | 2 | ✓ |  |
| `1314` | `1` | Gobierno Municipal - Entes | Gobierno Municipal - Entes | 2 | ✓ |  |
| `1315` | `1` | Gobierno Provincial - Entes | Gobierno Provincial - Entes | 40 | ✓ |  |
| `1324` | `1` | Servicio Internet ACC | Servicio Internet ACC | 34 | ✓ |  |
| `1325` | `1` | Serv Transp de datos ACC | Serv. Transporte de datos ACC | 12 | ✓ |  |

### Grupo 6 — Alumbrado Público

3 tarifas · 3 clases · **7.592** suministros

| TCL | CLA | Tarifa (TCL_DESCRIPCION) | Clase (CLA_DESCRIPCION) | Suministros | Med. | GD |
|---:|---:|---|---|---:|:-:|:-:|
| `604` | `1` | 6.1   ALUMBRADO PUBLICO | 6           Alumb. c/medicion | 7.229 | ✓ |  |
| `605` | `1` | 6.2   ALUMBRADO PUBLICO | 6           Alumb.c/conv s/med | 185 | — |  |
| `606` | `1` | 6.1   ALUMBRADO PUBLICO | 6           Alumb.c/con lec/DR | 178 | ✓ |  |

### Grupo 7 — Servicio de Agua

2 tarifas · 2 clases · **64** suministros

| TCL | CLA | Tarifa (TCL_DESCRIPCION) | Clase (CLA_DESCRIPCION) | Suministros | Med. | GD |
|---:|---:|---|---|---:|:-:|:-:|
| `712` | `1` | 7     SERVICIO DE AGUA | 7           Serv.agua p/riego. | 56 | ✓ |  |
| `714` | `1` | Bom. Agua y Saneamiento | Servicio Urbano | 8 | ✓ |  |

### Grupo 8 — Rural

2 tarifas · 3 clases · **619** suministros

| TCL | CLA | Tarifa (TCL_DESCRIPCION) | Clase (CLA_DESCRIPCION) | Suministros | Med. | GD |
|---:|---:|---|---|---:|:-:|:-:|
| `832` | `1` | TARIFA RURAL | RESIDENCIAL RURAL | 609 | ✓ |  |
| `832` | `9` | TARIFA RURAL | Rural Generador Energia | 1 | ✓ | ⚡ |
| `833` | `1` | TARIFA RURAL | RESIDENCIAL RURAL C/DISCR. | 9 | ✓ |  |
## 🔎 Recetas para desarrollo

Consultas cortas listas para copiar, sobre el mismo criterio de vigencia.

**La tarifa y clase actual de un suministro**

```sql
SELECT c.tcl_codigo, c.cla_codigo, t.tcl_descripcion,
       cl.cla_descripcion, t.tcl_grupo, cl.cla_energia_dist
  FROM xxsigec.contratos c
  JOIN xxsigec.tarifas t ON t.tcl_codigo = c.tcl_codigo
  JOIN xxsigec.clases cl ON cl.tcl_codigo = c.tcl_codigo
                        AND cl.cla_codigo = c.cla_codigo
 WHERE c.srv_codigo = :suministro
   AND c.cnt_estado = 'V'
```

**Sólo suministros eléctricos** (excluye internet, datos y alquiler de postes)

```sql
   AND c.tcl_codigo NOT BETWEEN '1300' AND '1330'
   AND c.tcl_codigo NOT IN ('1600','1601','1602','1603')
```

> Cuidado: `BETWEEN` sobre VARCHAR2 es comparación **alfabética**. Funciona para
> este rango porque todos los códigos involucrados tienen 4 dígitos, pero si
> sumás códigos de otro largo, pasá a `TO_NUMBER(c.tcl_codigo) BETWEEN 1300 AND 1330`.

**Sólo usuarios-generadores (GD)**

```sql
   AND cl.cla_energia_dist = 'S'
```

**Sólo tarifa social**

```sql
   AND cl.cla_social_tipo = 'SP'
```

## ♻️ Cómo reproducir esta nota

Contra `XXSIGEC` en modo solo-lectura (ver [[Arquitectura]] y [[Seguridad]]).
Desde el repo `rediseño-factura-dashboard`, con `dashboard-clientes/backend` como
directorio de trabajo:

```python
import sys; sys.path.insert(0, "src")
from oracle_sigec.conexion import OracleReadOnly

with OracleReadOnly(timeout_ms=600_000) as db:
    filas = db.consultar_dicts(SQL)   # la consulta canónica de arriba
```

La consulta original tarda unos minutos (correlaciona [[CONTRATOS]] — 3,77 M
filas — dos veces por cada una de las 1.165 clases); por eso el `timeout_ms`
ampliado. La simplificada es un solo `GROUP BY` sobre el mismo universo.

> [!info] Encoding
> `TCL_DESCRIPCION` y `CLA_DESCRIPCION` traen caracteres Latin-1 (`º` en «USO
> PROPIO Bº», `ó` en «sin medición»). Si los ves como `?` o `�` es la consola,
> no el dato: escribí a archivo con `encoding='utf-8'` y verificá ahí.

## 🔗 Ver también

- [[TARIFAS]] · [[CLASES]] · [[CONTRATOS]] — fichas de tabla
- [[Modelo de Facturación]] — importe, kWh y período de una factura
- [[Glosario de Negocio]] — prefijos de columna y significado de tablas
- [[Hallazgos]] — bitácora de verificaciones contra Oracle

---

> [!caution] Los conteos derivan: SIGEC es producción
> El total de suministros vigentes cambia entre consultas corridas con minutos de
> diferencia (se observó 1.206.074 → 1.206.066 → 1.206.064 el mismo día): se dan
> altas y bajas de contrato todo el tiempo. Las diferencias son de unidades y no
> mueven ninguna conclusión, pero **si vas a comparar dos números entre sí,
> calculalos en la misma transacción de lectura** — un solo `with OracleReadOnly()`
> da un snapshot consistente. Comparar resultados de dos corridas distintas
> produce descuadres de un puñado de suministros que parecen bugs y no lo son.

---

*Verificado contra Oracle XXSIGEC el 2026-08-24. Los conteos son una foto de ese
día: el catálogo cambia con cada cuadro tarifario nuevo. Volvé a correr la
consulta canónica antes de fijar cualquier lista en código.*
