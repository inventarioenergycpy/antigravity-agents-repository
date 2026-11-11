/* ==============================================================================================
SUITE SQL: CONTROL Y CONCILIACIÓN 2026 - ÍTEM 3: DISTRIBUCIÓN DE FACTURAS (F-218 vs SIGEC)
==============================================================================================
OBJETIVO       : Comparar mes a mes las cantidades de facturas físicas enviadas al correo en 2026
                 desde la tabla transaccional XXSIGEC.DOCUMENTOS frente a lo certificado en los
                 Formularios F-218 y liquidado en la Orden de Provisión OP 26211 (OCASA) en la planilla:
                 \\srvfs01\Control_de_Gestion\DEPARTAMENTO FACTURACION\CORREO DEL INTERIOR\LIQUIDACION_CORREO_2025.xls
MOTOR BD       : Oracle Database 19c Enterprise Edition (Instancia: PRODEBS_SEE / EPEC)
ESQUEMA        : XXSIGEC
TABLA FUENTE   : XXSIGEC.DOCUMENTOS
AUTOR          : Agente [02] Ciencia de Datos & Agente [06] Arquitecto de Sistemas EPEC
FECHA          : 2026-10-16
============================================================================================== */

-- ==============================================================================================
-- CONTROL MENSUAL AÑO 2026: TABLA DOCUMENTOS vs FORMULARIO F-218 (OP 26211)
-- ==============================================================================================

WITH facturas_2026 AS (
    SELECT
        TO_CHAR(d.doc_fecha_emision, 'YYYY-MM') AS periodo_emision,
        -- Marca de despacho a correo postal
        CASE 
            WHEN d.doc_enviado_correo IS NOT NULL THEN 'POSTAL'
            ELSE 'DIGITAL'
        END AS canal_envio,
        d.doc_numero,
        d.srv_codigo,
        d.cnt_numero
    FROM
        xxsigec.documentos d
    WHERE
        d.doc_tipo = 'F'               -- Factura normal
        AND d.doc_grupo = 'N'          -- Circuito normal de energía
        AND d.doc_fecha_emision >= TO_DATE('2026-01-01', 'YYYY-MM-DD')
        AND d.doc_fecha_emision <  TO_DATE('2026-10-01', 'YYYY-MM-DD')
),
conteo_sigec AS (
    SELECT
        periodo_emision,
        COUNT(CASE WHEN canal_envio = 'POSTAL' THEN 1 END)  AS facturas_postales_sigec,
        COUNT(CASE WHEN canal_envio = 'DIGITAL' THEN 1 END) AS facturas_digitales_sigec,
        COUNT(*)                                            AS total_facturas_emitidas_sigec
    FROM
        facturas_2026
    GROUP BY
        periodo_emision
),
f218_control_excel AS (
    -- Valores certificados en los Formularios F-218 de la planilla LIQUIDACION_CORREO_2025.xls (Hoja OP 26211)
    SELECT '2026-01' AS periodo, 27288 AS nro_f218, 689933 AS cant_f218_item3, 13 AS cant_braille_item2, 163500322.34 AS importe_neto_op FROM DUAL UNION ALL
    SELECT '2026-02' AS periodo, 27597 AS nro_f218, 649707 AS cant_f218_item3, 10 AS cant_braille_item2, 153967564.86 AS importe_neto_op FROM DUAL UNION ALL
    SELECT '2026-03' AS periodo, 27956 AS nro_f218, 641292 AS cant_f218_item3,  9 AS cant_braille_item2, 151973378.16 AS importe_neto_op FROM DUAL UNION ALL
    SELECT '2026-04' AS periodo, 28385 AS nro_f218, 681401 AS cant_f218_item3, 13 AS cant_braille_item2, 161478408.98 AS importe_neto_op FROM DUAL UNION ALL
    SELECT '2026-05' AS periodo, 28716 AS nro_f218, 649076 AS cant_f218_item3, 11 AS cant_braille_item2, 153818030.48 AS importe_neto_op FROM DUAL UNION ALL
    SELECT '2026-06' AS periodo, 29101 AS nro_f218, 693615 AS cant_f218_item3,  6 AS cant_braille_item2, 164372882.70 AS importe_neto_op FROM DUAL UNION ALL
    SELECT '2026-07' AS periodo, 29453 AS nro_f218, 705105 AS cant_f218_item3, 13 AS cant_braille_item2, 167095782.90 AS importe_neto_op FROM DUAL UNION ALL
    SELECT '2026-08' AS periodo, 29857 AS nro_f218, 596084 AS cant_f218_item3, 13 AS cant_braille_item2, 141259986.32 AS importe_neto_op FROM DUAL UNION ALL
    SELECT '2026-09' AS periodo, 30136 AS nro_f218, 683200 AS cant_f218_item3, 13 AS cant_braille_item2, 161904736.00 AS importe_neto_op FROM DUAL
)
SELECT
    f.periodo,
    f.nro_f218                                          AS formulario_f218,
    -- 1. Cantidad de Facturas Estándar certificadas en F-218 (Ítem 3)
    f.cant_f218_item3                                   AS f218_item3_facturas,
    f.cant_braille_item2                                AS f218_item2_braille,
    (f.cant_f218_item3 + f.cant_braille_item2)          AS f218_total_piezas_factura,
    -- 2. Conteo transaccional en XXSIGEC.DOCUMENTOS
    s.facturas_postales_sigec                           AS sigec_doc_enviado_correo,
    s.facturas_digitales_sigec                          AS sigec_facturas_digitales,
    s.total_facturas_emitidas_sigec                     AS sigec_total_emitidas,
    -- 3. Diferencia y Validación
    (s.facturas_postales_sigec - (f.cant_f218_item3 + f.cant_braille_item2)) AS diferencia_piezas,
    CASE 
        WHEN (s.facturas_postales_sigec - (f.cant_f218_item3 + f.cant_braille_item2)) = 0 
        THEN 'IGUALDAD EXACTA (100%)'
        ELSE 'DIFERENCIA MENOR'
    END AS estado_conciliacion,
    -- 4. Valorización económica en la OP 26211 ($ 236,98 s/iva)
    f.importe_neto_op                                   AS importe_neto_item3_op,
    ROUND(f.importe_neto_op * 1.21, 2)                  AS importe_total_con_iva
FROM
    f218_control_excel f
    LEFT JOIN conteo_sigec s
        ON s.periodo_emision = f.periodo
ORDER BY
    f.periodo ASC;
