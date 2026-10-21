---
title: "Metodología de Conteo Histórico en SIGEC: Facturas Impresas al Correo, F-218 y Liquidación de Órdenes de Provisión"
proyecto: "sigec-liquidacion-correo"
fecha: 2026-10-16
agentes:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Agente 02 - Ciencia de Datos]]"
  - "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Agente 06 - Arquitecto de Sistemas EPEC]]"
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Agente 11 - Copiloto Orquestador]]"
tags:
  - #sigec
  - #facturacion
  - #correo-del-interior
  - #ocasa
  - #f218
  - #orden-de-provision
  - #epec
---

# 📬 Metodología de Conteo Histórico en SIGEC: Facturas Impresas Enviadas al Correo, F-218 y Liquidación de Órdenes de Provisión (OP)

> [!WARNING]
> **ESTADO DE LA INVESTIGACIÓN: NO CONCLUYENTE / EN CURSO (CONTINUIDAD A FUTURO)**
> El análisis comparativo preliminar entre las planillas de liquidación de la F-218 y la tabla `XXSIGEC.DOCUMENTOS` no se considera cerrado ni concluyente. Requiere contrastación empírica directa sobre la instancia productiva de Oracle (`PRODEBS_SEE`), evaluación de desfasajes de corte y análisis de casos de refacturación/anulación.


## 1. El Problema Operativo y Diagnóstico de Negocio

En el sistema comercial SIGEC de EPEC, la tabla maestra de contratos (`xxsigec.contratos`) contiene la columna `CNT_TIPO_IMPRESION`, la cual categoriza la modalidad de emisión y entrega de la factura:
- `EST` (4): **Estándar** (Factura impresa en papel y distribuida por correo postal).
- `SIM` (0): **Sin Impresión** (Factura Digital adherida por el usuario).
- `SEN` (0): **Sin Envío** (Oficina Virtual).
- `BR` (1): **Braille**.
- `EMP` (2): **Empleado EPEC**.
- `REC` (3): **Reparto Recomendado**.
- `ADJ` (5): **Adjunta Nota** (No usar).

### La Trampa de la Foto Actual:
Ejecutar la consulta:
```sql
SELECT * FROM xxsigec.contratos WHERE cnt_tipo_impresion = 'EST';
```
muestra únicamente el estado **hoy**. Si un cliente estuvo recibiendo factura papel durante 2024 y se adhirió a Factura Digital (`SIM`) en 2025, sus facturas de 2024 quedan indebidamente excluidas si se filtran por el contrato actual. Esto produce un desfasaje con las piezas que efectivamente la contratista de correo imprimió, transportó y rindió en su momento.

---

## 2. Marco Contractual: Órdenes de Provisión (OP) y Formulario F-218

- **Orden de Provisión (OP)**: Instrumento contractual que formaliza la adjudicación a la empresa postal (históricamente Correo del Interior S.A. y actualmente Organización Courier Argentina S.A. - OCASA, bajo las O.P. 21942, 22673, 23100, 25238 y 26211). Fija el plazo de vigencia, presupuesto máximo y **precios unitarios por ítem**:
  - **Ítem 1**: Impresión de Facturas y Notificaciones.
  - **Ítem 2**: Braille.
  - **Ítem 3**: Distribución de Facturas.
  - **Ítem 4**: Distribución de Notificaciones.
- **Formulario F-218 (Certificación de Trabajos Realizados)**: Documento mensual emitido para certificar la cantidad de servicios efectivamente cumplidos por la contratista. Cada ítem rendido se multiplica por su precio unitario en la OP para liquidar el subtotal, más IVA (21%), deducciones y emisión de la orden de pago.
- **Planilla de Control de Gestión**: `\\srvfs01\Control_de_Gestion\DEPARTAMENTO FACTURACION\CORREO DEL INTERIOR\LIQUIDACION_CORREO_2025.xls`, donde se audita el saldo de piezas contratadas vs. acumuladas de cada OP.

---

## 3. Solución Técnica en Oracle SIGEC: Estrategias de Conteo Histórico

### Estrategia A: Transaccional Directa vía `XXSIGEC.DOCUMENTOS` (Recomendada)
La tabla `XXSIGEC.DOCUMENTOS` registra cada documento de facturación con sus marcas de ejecución:
1. `DOC_ENVIADO_CORREO` (DATE): Si está poblada, la factura fue enviada físicamente al lote de correo para su impresión y entrega postal. Si es `NULL`, fue procesada por canales sin correo físico (Factura Digital / Oficina Virtual).
2. `CODIGO_MODELO_IMPRESION_XML`: Registra la plantilla de impresión física asignada al documento.
3. `DOC_FECHA_EMISION`: Permite agrupar las facturas en el mes de devengamiento exacto de la F-218.
4. Filtros obligatorios de sanidad de datos: `DOC_TIPO = 'F'` (Factura) y `DOC_GRUPO = 'N'` (Circuito normal de energía).

### Estrategia B: Reconstrucción Temporal con `XXSIGEC.CONTRATOS_JN` (Journal Histórico)
Para auditorías donde se requiera demostrar qué condición legal/contractual tenía el cliente al instante de facturarle:
- Se realiza un join temporal entre `DOCUMENTOS` y `CONTRATOS_JN` con la condición `jn.jn_fecha <= d.doc_fecha_emision`.
- Se selecciona mediante función de ventana analítica (`ROW_NUMBER()`) el último registro previo a la emisión.

---

## 4. Scripts y Archivos Entregables
- Script SQL maestro: [`scripts/consulta_sigec_historico_facturas_correo_f218.sql`](file:///D:/Proyectos/antigravity-agents-repository/scripts/consulta_sigec_historico_facturas_correo_f218.sql).
- Planillas de conciliación verificadas en red: `\\srvfs01\Control_de_Gestion\DEPARTAMENTO FACTURACION\CORREO DEL INTERIOR\LIQUIDACION_CORREO_2025.xls` y `Resumen_Detalle_F218.xlsx`.

---

## 5. Conciliación Específica del Ítem 4: Notificaciones e Intimaciones

En el Formulario F-218 y en las Órdenes de Provisión, el **Ítem 4** remunera la *"Distribución de Notificaciones"*.

### Fuente de Información en SIGEC: `XXSIGEC.SEGUIMIENTO_IMP_VARIOS`
A diferencia de las facturas que nacen en `DOCUMENTOS`, los lotes de intimaciones y notificaciones de deuda procesados para envío postal se registran en `XXSIGEC.SEGUIMIENTO_IMP_VARIOS`:
- **`SIV_FECHA_PROCESADO`**: Fecha string en formato `ddmmyyyy` correspondiente a la corrida del lote.
- **`SIV_TIPO_IMPRESION`**: Código clasificador de la pieza postal:
  - `IN`: Intimaciones Normales de Clientes Comunes (~98% del volumen).
  - `IA`: Intimaciones por Aforos / Recupero de Energía.
  - `IG`: Intimaciones a Grandes Clientes.
  - `NE`: Notificaciones Especiales institucionales.
  - `ND`: Notificaciones Diversas de Deuda.
  - `NO`: Notificaciones Oficiales / Otras dependencias.
  - `NC`: Notificaciones de Corte / Suspensión de Suministro.
- **`SIV_CANT_EMISION`**: Cantidad física real despachada a la contratista para reparto. Esta es la cifra exacta que se certifica en el **Ítem 4 de la F-218**.
- **`SIV_IMP_EMISION`**: Deuda total intimada en los lotes.

### Matriz Integral de Liquidación (F-218):
$$\text{Monto F-218} = (\text{Cant. Facturas Papel} \times P_{\text{distrib\_fact}}) + (\text{Cant. Notificaciones} \times P_{\text{distrib\_notif}}) + (\text{Total Piezas} \times P_{\text{impresion}})$$

---

## 6. Puntos Críticos Abiertos y Hoja de Ruta para Continuidad Futura

1. **Ejecución y Extracción en Base Viva (Oracle PRODEBS_SEE)**:
   - Correr las consultas elaboradas sobre la base productiva para validar si el campo `DOC_ENVIADO_CORREO` se puebla de forma unívoca o si existen excepciones en lotes de facturación manual / contingencia.
2. **Desfasaje Temporal Emisión vs. Despacho Físico (Efecto Corte Contable)**:
   - Analizar las facturas emitidas en los últimos días del mes ($M$) cuya entrega efectiva al correo y certificación en F-218 ocurre los primeros días del mes subsiguiente ($M+1$).
3. **Casuística de Documentos No Normales y Refacturaciones**:
   - Evaluar el impacto de notas de crédito (`DOC_TIPO = 'C'`), refacturaciones y facturas retenidas (`DOCUMENTOS_RTS_RETENIDOS`) sobre el recuento de piezas físicas.
4. **Cierre de Ciclo Anual 2026**:
   - Incorporar los meses restantes de 2026 (Octubre, Noviembre y Diciembre) a medida que se emitan y firmen las respectivas F-218 bajo la OP 26211.
