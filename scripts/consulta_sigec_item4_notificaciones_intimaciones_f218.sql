/* ==============================================================================================
SUITE SQL: CONCILIACIÓN ÍTEM 4 - DISTRIBUCIÓN DE NOTIFICACIONES E INTIMACIONES (F-218 / OP)
==============================================================================================
OBJETIVO       : Conciliar y auditar las cantidades de piezas postales de Notificaciones e
                 Intimaciones liquidadas a la contratista de correo (OCASA / Correo del Interior)
                 en el Formulario F-218 contra la tabla de control XXSIGEC.SEGUIMIENTO_IMP_VARIOS.
VINCULACIÓN    : Planilla en red:
                 \\srvfs01\Control_de_Gestion\DEPARTAMENTO FACTURACION\CORREO DEL INTERIOR\LIQUIDACION_CORREO_2025.xls
                 (Hojas: O.P. 23100 / O.P. 25238 / O.P. 26211 - Ítem 4 'Distribución de Notificaciones')
MOTOR BD       : Oracle Database 19c Enterprise Edition (Instancia: PRODEBS_SEE / EPEC)
ESQUEMA        : XXSIGEC
TABLA FUENTE   : XXSIGEC.SEGUIMIENTO_IMP_VARIOS
AUTOR          : Agente [02] Ciencia de Datos & Agente [06] Arquitecto de Sistemas EPEC
FECHA          : 2026-10-16
============================================================================================== */

-- ==============================================================================================
-- CONSULTA 1: CONCILIACIÓN MENSUAL PIVOTADA DEL ÍTEM 4 (F-218) POR TIPO DE INTIMACIÓN
-- ==============================================================================================
-- Proposito: Reproducir exactamente el total mensual de notificaciones de la F-218 desglosando
--            por cada tipología de pieza postal emitida en el período.
-- ==============================================================================================

WITH lotes_normalizados AS (
    SELECT
        -- Parseo seguro de fecha string 'ddmmyyyy' a fecha calendario
        TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy')              AS fecha_proceso,
        TO_CHAR(TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy'), 'YYYY-MM') AS periodo_liquidacion,
        UPPER(TRIM(siv.siv_tipo_impresion))                       AS tipo_impresion,
        NVL(siv.siv_cant_emision, 0)                              AS cant_emision,
        NVL(siv.siv_cant_generada, 0)                             AS cant_generada,
        -- Conversión segura del importe intimado
        NVL(TO_NUMBER(REPLACE(siv.siv_imp_emision, ',', '.')), 0) AS importe_deuda_intimada,
        siv.siv_distrito_origen                                   AS distrito_origen,
        siv.cpr_numero                                            AS corrida_proceso
    FROM
        xxsigec.seguimiento_imp_varios siv
    WHERE
        siv.siv_fecha_procesado IS NOT NULL
        AND LENGTH(TRIM(siv.siv_fecha_procesado)) = 8
        AND TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy') >= TO_DATE('2024-01-01', 'YYYY-MM-DD')
)
SELECT
    periodo_liquidacion,
    -- Desglose por tipología de notificación / intimación
    SUM(CASE WHEN tipo_impresion = 'IN' THEN cant_emision ELSE 0 END) AS cant_in_intimaciones_normales,
    SUM(CASE WHEN tipo_impresion = 'IA' THEN cant_emision ELSE 0 END) AS cant_ia_aforos_irregularidades,
    SUM(CASE WHEN tipo_impresion = 'IG' THEN cant_emision ELSE 0 END) AS cant_ig_grandes_clientes,
    SUM(CASE WHEN tipo_impresion = 'NE' THEN cant_emision ELSE 0 END) AS cant_ne_notificaciones_especiales,
    SUM(CASE WHEN tipo_impresion = 'ND' THEN cant_emision ELSE 0 END) AS cant_nd_notificaciones_deuda,
    SUM(CASE WHEN tipo_impresion = 'NO' THEN cant_emision ELSE 0 END) AS cant_no_notificaciones_oficiales,
    SUM(CASE WHEN tipo_impresion = 'NC' THEN cant_emision ELSE 0 END) AS cant_nc_notificaciones_corte,
    -- TOTAL CERTIFICADO PARA EL ÍTEM 4 EN EL FORMULARIO F-218
    SUM(cant_emision)                                                 AS total_item_4_notificaciones_f218,
    -- Importe total de deuda intimada en las piezas postales
    SUM(importe_deuda_intimada)                                       AS importe_total_deuda_intimada,
    COUNT(DISTINCT corrida_proceso)                                   AS total_corridas_batch,
    MIN(fecha_proceso)                                                AS primer_despacho_mes,
    MAX(fecha_proceso)                                                AS ultimo_despacho_mes
FROM
    lotes_normalizados
GROUP BY
    periodo_liquidacion
ORDER BY
    periodo_liquidacion DESC;


-- ==============================================================================================
-- CONSULTA 2: DISTRIBUCIÓN TERRITORIAL DEL ÍTEM 4 POR SUCURSAL / DISTRITO COMERCIAL
-- ==============================================================================================
-- Proposito: Auditar geográficamente la procedencia de las notificaciones e intimaciones
--            despachadas en un período mensual específico.
-- ==============================================================================================

SELECT
    siv.siv_distrito_origen                                          AS codigo_distrito,
    NVL(suc.scf_descripcion, 'DISTRITO ' || siv.siv_distrito_origen) AS nombre_sucursal_distrito,
    TO_CHAR(TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy'), 'YYYY-MM') AS periodo_liquidacion,
    SUM(CASE WHEN UPPER(TRIM(siv.siv_tipo_impresion)) = 'IN' THEN NVL(siv.siv_cant_emision,0) ELSE 0 END) AS cant_intimaciones_normales,
    SUM(CASE WHEN UPPER(TRIM(siv.siv_tipo_impresion)) = 'IG' THEN NVL(siv.siv_cant_emision,0) ELSE 0 END) AS cant_grandes_clientes,
    SUM(CASE WHEN UPPER(TRIM(siv.siv_tipo_impresion)) IN ('NE','ND','NO','NC') THEN NVL(siv.siv_cant_emision,0) ELSE 0 END) AS cant_otras_notificaciones,
    SUM(NVL(siv.siv_cant_emision, 0))                                AS total_piezas_distrito
FROM
    xxsigec.seguimiento_imp_varios siv
    LEFT JOIN xxsigec.sucursales suc
        ON suc.scf_codigo = siv.siv_distrito_origen
WHERE
    siv.siv_fecha_procesado IS NOT NULL
    AND LENGTH(TRIM(siv.siv_fecha_procesado)) = 8
    AND TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy') >= TO_DATE('2025-01-01', 'YYYY-MM-DD')
GROUP BY
    siv.siv_distrito_origen,
    suc.scf_descripcion,
    TO_CHAR(TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy'), 'YYYY-MM')
ORDER BY
    periodo_liquidacion DESC,
    total_piezas_distrito DESC;


-- ==============================================================================================
-- CONSULTA 3: MATRIZ INTEGRAL UNIFICADA F-218 (ÍTEM 1 + ÍTEM 3 + ÍTEM 4 + VALORIZACIÓN OP)
-- ==============================================================================================
-- Proposito: Consolidar en una única fila mensual la totalidad de servicios postales facturados:
--            - Ítem 1: Impresión de Facturas y Notificaciones
--            - Ítem 3: Distribución de Facturas
--            - Ítem 4: Distribución de Notificaciones e Intimaciones
--            - Cálculo económico liquidable según precios unitarios de la Orden de Provisión
-- ==============================================================================================

WITH facturas_mensuales AS (
    SELECT
        TO_CHAR(d.doc_fecha_emision, 'YYYY-MM') AS periodo,
        COUNT(CASE WHEN d.doc_enviado_correo IS NOT NULL THEN 1 END) AS cant_facturas_correo,
        COUNT(CASE WHEN d.doc_enviado_correo IS NULL THEN 1 END)     AS cant_facturas_digitales,
        COUNT(*) AS cant_total_facturas
    FROM
        xxsigec.documentos d
    WHERE
        d.doc_tipo = 'F'
        AND d.doc_grupo = 'N'
        AND d.doc_fecha_emision >= TO_DATE('2024-01-01', 'YYYY-MM-DD')
    GROUP BY
        TO_CHAR(d.doc_fecha_emision, 'YYYY-MM')
),
notificaciones_mensuales AS (
    SELECT
        TO_CHAR(TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy'), 'YYYY-MM') AS periodo,
        SUM(NVL(siv.siv_cant_emision, 0)) AS cant_notificaciones_correo
    FROM
        xxsigec.seguimiento_imp_varios siv
    WHERE
        siv.siv_fecha_procesado IS NOT NULL
        AND LENGTH(TRIM(siv.siv_fecha_procesado)) = 8
        AND TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy') >= TO_DATE('2024-01-01', 'YYYY-MM-DD')
    GROUP BY
        TO_CHAR(TO_DATE(siv.siv_fecha_procesado, 'ddmmyyyy'), 'YYYY-MM')
)
SELECT
    f.periodo,
    -- Ítem 3 F-218: Distribución de Facturas
    f.cant_facturas_correo                                    AS item3_distribucion_facturas,
    -- Ítem 4 F-218: Distribución de Notificaciones
    NVL(n.cant_notificaciones_correo, 0)                      AS item4_distribucion_notificaciones,
    -- Ítem 1 F-218: Impresión Física Total (Facturas Papel + Notificaciones)
    (f.cant_facturas_correo + NVL(n.cant_notificaciones_correo, 0)) AS item1_impresion_total_piezas,
    -- Facturación Digital EPEC (Ahorro postal / no liquidable a contratista)
    f.cant_facturas_digitales                                 AS facturas_digitales_sin_correo,
    f.cant_total_facturas                                     AS total_facturas_emitidas_sistema,
    -- Estimación Liquidación Neta (Valores de referencia OP 26211: Fact=$236.98, Notif=$377.01, Imp=$39.57)
    ROUND(
        (f.cant_facturas_correo * 236.98) +
        (NVL(n.cant_notificaciones_correo, 0) * 377.01) +
        ((f.cant_facturas_correo + NVL(n.cant_notificaciones_correo, 0)) * 39.57),
        2
    )                                                         AS subtotal_estimado_op_s_iva,
    -- Total estimado con IVA 21% para el legajo F-218
    ROUND(
        ((f.cant_facturas_correo * 236.98) +
        (NVL(n.cant_notificaciones_correo, 0) * 377.01) +
        ((f.cant_facturas_correo + NVL(n.cant_notificaciones_correo, 0)) * 39.57)) * 1.21,
        2
    )                                                         AS total_estimado_op_con_iva
FROM
    facturas_mensuales f
    LEFT JOIN notificaciones_mensuales n
        ON n.periodo = f.periodo
ORDER BY
    f.periodo DESC;
