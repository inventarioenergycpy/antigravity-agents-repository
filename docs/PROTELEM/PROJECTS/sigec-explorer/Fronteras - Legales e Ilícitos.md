---
tipo: arquitectura
estado: vigente
sensibilidad: interna
tags:
  - sigec-explorer
  - arquitectura
  - oracle
  - epec
  - ilicitos
  - legales
aliases:
  - Fronteras Legales e Ilícitos
  - Frontera SIGEC Legales
  - Fraude e Ilícitos
  - Gestión Judicial SIGEC
  - INCORE
fecha: 2026-08-05
---

# ⚖️ Fronteras de SIGEC con Legales e Ilícitos

> [!abstract] Qué es esto
> Mapa de las fronteras entre `XXSIGEC` y los dominios de **Fraude e Ilícitos** y
> **Legales**: qué módulos existen, cuáles siguen vivos, por dónde salen y entran
> los datos, y qué caminos son arqueología. Todo verificado contra Oracle el
> 2026-08-05. Rastro completo en el cuaderno de investigación del repo
> (`investigaciones/2026-08-05-fronteras-legales-ilicitos/`).

## 🧭 Respuesta corta

**Ilícitos no es un sistema externo: es un módulo interno de XXSIGEC**, vivo y de
alto volumen. **Legales sí vive afuera**, pero su frontera no es una tabla de
staging: es una **marca de estado** (`DETALLE_SALDO.FECHA_PASE_GJ`) más una
**interfaz de archivo de oficios judiciales** hacia un schema `XXLG` que
`smunge` no puede leer.

Y el resultado más contraintuitivo: **los dos dominios casi no se tocan**.

## 🏢 Las tres áreas, nombradas

De [[SECTORES]] (103 filas, árbol por `SEC_CODIGO_PADRE`):

| `SEC_CODIGO` | Descripción | Padre | Actividad |
|---|---|---|---|
| `FRAU` | Fraude e Ilicitos | `COM` Comercial | 215.433 órdenes recibidas en 2025 |
| `LEGALES` | Legales | **raíz** (sin padre) | solo **emite**: ~480 órdenes |
| `COBJUDIC` | Cobranzas Judiciales | `ADM` Administración | **cero** órdenes |

> [!important] Legales no recibe trabajo: lo emite
> `SEC_CODIGO_DESTINO = 'LEGALES'` es **cero en los 38M de [[ORDENATIVOS]]**.
> Como origen sí aparece (2022: 52 · 2023: 95 · 2024: 158 · 2025: 100). Legales
> **interviene sobre** el sistema comercial; no es destinatario de derivaciones.

`SEC_TIPO = 'SX'` marca **terceros externos** modelados como sectores: CONECTAR
SRL, COOP. DE LYF, EMA, IEMCO, INGENIA, LOZA, ROWING, NAXOS, TECNORED.
Contratistas que ejecutan trabajos de campo sobre medidores — aparecen en la
vista de ilícitos por su actividad de **telemedición**, no por el circuito de
fraude (ver abajo).

## 🔥 Ilícitos — módulo interno y vivo

```
ORDENATIVOS  (TOR: II · GF · NF · FL · IF · RF  →  SEC_DESTINO = FRAU)
     │
     └─ RECLAMOS  (TRO_GRUPO_RECLAMO = 'FR')  ──OPE_NUMERO──▶ OPERATIVOS
          ├─ DATOS_RESULTADOS   ← acta de constatación (PK DRE_NUMERO)
          │     └─ ACTA_AUD · ACTIVIDADES_ACTA · LECTURAS_ACTA · PRECINTOS_ACTA
          └─ LIQUIDACIONES_ILICITOS  ← el cargo al cliente
                └─ ITEMS_LIQUIDACIONES · TMP_PRELIQ_ILICITOS
```

**Volumen 2025:** 215.433 órdenes a `FRAU` · 186.759 reclamos de fraude ·
33.696 actas · 34.746 liquidaciones.

Órdenes históricas a `FRAU`: `II` Inspeccion Ilicitos 1.241.508 · `GF` Gestion de
Fraude 222.657 · `NF` Notificacion por Fraude 155.123 · `FL` 87.902 · `IF` 45.969
· `RF` Retiro Por Fraude 19.504.

> [!tip] El disparador es una orden de trabajo, no una denuncia
> [[TIPOS_ORDENATIVO]] tiene `TOR_ESTADO_ILICITO` y `TOR_RESULTADO_ILICITO`:
> cualquier orden (lectura, corte, verificación) puede **volver del campo marcada
> como ilícito** y abrir el caso.

[[TIPOS_RECLAMO]] grupo `FR` = **57 tipologías** en árbol de dos niveles:
`F` POSIBLE FRAUDE → `F1` conexión directa · `F2` fraude con retiro · `F3` no
fraude · `F4` cesión de energía · `F5` fraude sin retiro → hojas (`11`–`13`,
`21`–`38`, `40`–`42`, `51`–`79`).

La vista operativa del área es **`GEOREF.VW_ILICITOS`** (61 columnas, 13.157
filas, actualizada al día): `INCORE`, `DEUDA_NORMAL` vs `DEUDA_JUDICIAL`, `ACTA`,
`PRELIQUIDACION`, `MONTO`, `FRAUDE`, `ESTADO`, catastro y GPS. No toca `XXLG`; se
arma sobre XXSIGEC + funciones `GEOREF.FC_*`, y filtra
`WHERE Fc_actas(...) IS NOT NULL` → **solo suministros con acta**.

> [!warning] Tres trampas de esta vista
> 1. **`SECTOR_EJECUTANTE`, `ASIGNADO` y las tres `FECHA_*` vienen de
>    `Fc_protelem_*`** — órdenes de **telemedición**, no del circuito de fraude.
> 2. **`DEUDA_JUDICIAL` es un parámetro de `Fc_deuda`**, y hay **cuatro**
>    categorías: `NORMAL` (243.549 suministros · $124.985M), `PPC` (23.619 ·
>    $3.649M), `OTRAS` (489 · $4.756M) y `JUDICIAL` (**91** · $2.706M, ~$29,7M
>    cada uno: grandes deudores). Ese stock vigente **no** es comparable con los
>    1.805 suministros del pase a GJ de 2025, que son eventos históricos.
> 3. **Para análisis masivo no usarla**: cada columna es una llamada PL/SQL por
>    fila. Usar **`GEOREF.VM_SUMINISTROS`**, que es **tabla materializada** (91
>    columnas, 1,2M suministros) con los mismos indicadores.

`GEOREF.VW_INSP_ILICITOS` es una **bandeja de trabajo pendiente**, no un universo
completo: filtra `TOR_CODIGO='II'`, `ORD_ESTADO='D'`, **`SCF_CODIGO_DESTINO=1`
(solo Córdoba capital)**, `ORD_RESULTADO IS NULL` y deuda vencida.

## ⚖️ Legales — la frontera real: `FECHA_PASE_GJ`

**GJ = Gestión Judicial.** Columna 57 de [[DETALLE_SALDO]] (5,19M documentos):
**158.883 con pase a GJ**, del 1997-10-28 a **hoy**.

| Año | Documentos | Suministros | Saldo |
|---|---|---|---|
| 2023 | 21.474 | 885 | $126.493.443 |
| 2024 | 13.301 | 686 | $326.374.955 |
| **2025** | **22.497** | **1.805** | **$4.548.326.866** |
| 2026 (parcial) | 10.533 | 999 | $2.209.097.227 |

**El certificado de deuda es el instrumento del pase:** de 104.681
[[CERTIFICADOS_DEUDA]] cruzables, **97.543 (93,2 %)** tienen `FECHA_PASE_GJ`.
Son el mismo flujo visto desde dos tablas.

### Lo que sale hacia afuera

| Interfaz (`XXTIPOS_TRANSFER_ARCHIVOS`) | Qué mueve | Ruta |
|---|---|---|
| `XXLG_OFICIOS_JUDICIAL_DE_BD_A_WIN` | **oficios judiciales** | `vmprodcon1` → `srv3594` |
| `TRANSFER_INTIMACIONES` | intimaciones | `Ebs12-prod-n1` → `srv3594` |
| `TRANS_INTIMACIONES_DOC` | intimaciones | `srv3594` → `Ebs12-prod-n1` |
| `TRANS_INTIMACIONES_CORTES` | cortes | `srv3594` → `Ebs12-prod-n1` |

El prefijo **`XXLG` = LeGales**. Existe el schema (`XXLG_TIPOS_JUICIOS_SEQ`,
vía synonym público) pero **`smunge` no tiene acceso a sus tablas**: es el único
lugar donde podría estar el registro de juicios.

> [!warning] `XXSIRE` NO es Legales
> Pese a `XXSIRE_SEC_EMBARGO` y `XXSIRE_CTA_ALIMENTARIA`, ese schema es de
> **nómina/RRHH** (convive con `SEC_ADELANTO_SUELDO`, `XXRH_LIQ_SAL`). Son
> embargos de **haberes de empleados**, no deuda de clientes.

## 🔌 INCORE = `IN` · `CO` · `RE`

El acrónimo son literalmente los `TOR_CODIGO` de [[TIPOS_ORDENATIVO]]:

| Código | Descripción | Grupo |
|---|---|---|
| `IN` | Ordenativo de **In**timacion | `INT` |
| `CO` | Ordenativo de **Co**rte Operativo | `COR` |
| `RE` | Ordenativo de **Re**tiro de Medidor | `MD` |
| `IA` | Intimacion a Servicio Activo | `INT` |
| `NE` | Notificacion de Deuda Gdes. Clientes | `NT` |

Estado por contrato en `XXCO_DETALLE_DEUDA_USR_TMP`: `ULTIMO_INCORE_GENERADO` /
`ULTIMO_INCORE_EJECUTADO` + sus fechas. Elegibilidad en
[[CONTRATOS]] `CNT_COND_INTIMACION` (`S` 3.705.652 / `N` 53.615).

En `GEOREF` la codificación es `I1`–`I3`, `O1`–`O3`, `R1`–`R3`. El cruce contra
`ESTADO_SERVICIO` confirma que **la letra es la etapa**:

| Etapa | Casos | Servicio cortado | Lectura |
|---|---|---|---|
| `I` intimación | 55.080 | 4,3 % | el servicio sigue normal |
| `O` orden de corte | 3.977 | 4,1 % | emitida, **aún no ejecutada** |
| `R` retiro | 658 | **96,5 %** | el corte **ya se ejecutó** |

Contra una línea base de **1,2 %** de servicios cortados en todo el padrón
(14.601 de 1.203.584). El **número** (1/2/3) **no** quedó resuelto: escala con la
deuda en `O` y `R`, pero no decrece de forma monótona en `I` (`I2`=53.017 vs
`I1`=2.062). Pendiente de confirmar con el negocio.

## ⛔ Desconectados por documento, superpuestos por cliente

**Por documento — no se tocan.** Cruce de [[LIQUIDACIONES_ILICITOS]] contra
[[DETALLE_SALDO]] por (`DOC_TIPO`, `DOC_NUMERO`): 646 documentos de ilícito en el
saldo, de los cuales **solo 23 pasaron a gestión judicial**. La liquidación del
fraude **no se judicializa**: se cobra por vía administrativa (liquidación →
factura).

**Por suministro — fuerte superposición.**

| | Suministros | Con reclamo de fraude 2020+ | % |
|---|---|---|---|
| Línea base (todos) | 1.556.839 | 451.595 | 29,0 % |
| Pasados a GJ en 2025 | 1.805 | 1.323 | **73,3 %** |

**2,5× la línea base.** No se judicializa *el cargo del fraude*, pero **los
mismos clientes terminan judicializados por su deuda común**. Es asociación, no
causalidad demostrada: parte puede ser sesgo de selección (el cliente muy
endeudado recibe tanto inspección de ilícito como acción judicial).

> [!note] El pase a GJ no tiene vuelta
> Los 158.883 documentos tienen **todos** `DOC_SITUACION = 'G'` (correlación 1:1
> con `FECHA_PASE_GJ` — es el indicador equivalente y más simple). De ellos,
> 157.751 siguen con saldo pendiente, 1.132 sin `SALDO_ACTUAL` y **cero
> saldados**. Saldo total en gestión judicial: **$7.447.380.666**. El resultado
> del juicio no vuelve a SIGEC.

## 📊 El embudo INCORE y el perfil de la deuda judicial

Medido sobre `GEOREF.VM_SUMINISTROS` (1,2M suministros, tabla materializada).

| Etapa | Suministros | % padrón | Deuda involucrada |
|---|---|---|---|
| Sin proceso | 1.143.869 | 95,04 % | $118.147 M |
| `I` intimación | 55.080 | 4,57 % | $13.551 M |
| `O` orden de corte | 3.977 | 0,33 % | $1.402 M |
| `R` retiro ejecutado | 658 | 0,05 % | $290 M |

De cada 100 intimados, **7 llegan a orden de corte y 1 a retiro**.

> [!warning] Dato accionable
> **3.977 órdenes de corte vigentes**, de las cuales **3.816 (96 %) tienen el
> servicio todavía activo**: **$1.402 millones** en órdenes emitidas y no
> ejecutadas.

**La deuda judicial es industrial y concentrada:** 17 suministros del grupo
tarifario 3 (Grandes Consumos) son el **93,3 %** de los $2.706 M, y los 10
mayores el **96,2 %**. Córdoba capital reúne 46 de los 91 casos.

> [!important] Al gran cliente no se lo corta: se lo demanda
> El **99,97 %** de la deuda judicial está en suministros con **servicio activo**.
> Los cortados acumulan deuda *normal* ($4.489 M), no judicial. Corte e
> intimación son la vía **masiva** para deuda común; el juicio es la vía
> **excepcional** para pocos deudores muy grandes. Son dos políticas distintas,
> no dos etapas del mismo proceso.

## 🪦 Lo que está muerto (no perder tiempo acá)

| Camino | Evidencia |
|---|---|
| Módulo judicial de SIGEC ([[PROCURADORES]] · `ASIGNACIONES` · `ACCIONES`) | **piloto de 1999**: 412 asignaciones todas del 1999-08-30 a un solo procurador; 2 acciones; `MOVIMIENTOS_MONETARIOS`, `ACCIONES_PARAMETROS` y `CONCURSOS_QUIEBRAS` en cero |
| [[ACTA_TMP]] (staging legacy de Ilícitos) | archivo **1993-1998**; dump dBase/FoxPro con filas de encabezado cargadas como datos |
| Derivación "ZA" (`ACTA_TMP.TRANSZA`) | **17 filas**, 1992-1996; único lugar del esquema con ese token |
| `ORDENATIVOS.EXP_NUMERO` (nº expediente) | **0 usos** en 17,9M órdenes desde 2020 |
| `XXCO_AMPAROS_MEMO_INCORE` | 772 contratos, todos con `FECHA_TOPE` 2019-09-06, **cero vigentes** |
| `ERSEP_CNT_NO_INTIMA` | oficios del ente regulador **2000-2010** |

> [!note] Corrección de lectura sobre `ACTA_TMP`
> `TRANSCOB` / `TRANSZA` / `TRANSLEGAL` **no son flags: son fechas** (texto
> `D/M/YY`) de transferencia. `CAR_TRACOB` / `CAR_TRANZA` / `CAR_TRALEG` **no son
> "fecha de carga": son nombres de la persona a cargo** (`CAR_` = "a cargo de").
> Esas tres columnas contienen **nombres de empleados** → no se transcriben acá.

## 🔒 Seguridad

Tres puntos detectados en esta investigación, todos **excluidos** de consultas y
del vault (ver [[Modelo de seguridad]] regla 1 y [[Seguridad]]):

- `XXSERVIDORES.SER_PASSWORD` / `SER_USUARIO` — credenciales de servidores.
- `PROCURADORES.PRO_CONTRASEA` / `PRO_USUARIO` — credenciales de abogados externos.
- `ACTA_TMP.CAR_TRACOB` / `CAR_TRANZA` / `CAR_TRALEG` — nombres de empleados.

## 🔗 Ver también

- [[Esquema XXSIGEC]] — hallazgos generales del esquema
- [[Glosario de Negocio]] — semántica acumulada (incluye lo de esta nota)
- [[Hallazgos]] — log de hallazgos semánticos
- [[_index|MOC SIGEC Explorer]]
