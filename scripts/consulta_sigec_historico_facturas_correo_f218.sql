/* ==============================================================================================
SUITE SQL: HISTORICO DE FACTURAS IMPRESAS Y DISTRIBUIDAS POR CORREO (SIGEC EPEC)
==============================================================================================
OBJETIVO       : Reconstruir la condición histórica de envío a correo al momento de facturación,
                 superando la limitación de la foto actual en CONTRATOS.CNT_TIPO_IMPRESION,
                 para conciliar las cantidades certificadas en la F-218 contra las O.P. de liquidación
                 (LIQUIDACION_CORREO_2025.xls / O.P. 23100 / O.P. 25238 / O.P. 26211).
MOTOR BD       : Oracle Database 19c Enterprise Edition (Instancia: PRODEBS_SEE / EPEC)
ESQUEMA        : XXSIGEC
TABLAS CLAVE   : XXSIGEC.DOCUMENTOS, XXSIGEC.CONTRATOS, XXSIGEC.CONTRATOS_JN,
                 XXSIGEC.SEGUIMIENTO_IMP_VARIOS, XXSIGEC.XXCO_DOC_CORREO_XML
AUTOR          : Agente [02] Ciencia de Datos & Agente [11] Copiloto Orquestador
FECHA          : 2026-10-16
============================================================================================== */

-- ==============================================================================================
-- CONSULTA 1: CONTEO HISTÓRICO TRANSACCIONAL DESDE XXSIGEC.DOCUMENTOS
-- ==============================================================================================
-- Proposito: Contar mes a mes cuántas facturas normales definitivas de energía (DOC_TIPO='F',
--            DOC_GRUPO='N') tuvieron marca efectiva de despacho a correo (DOC_ENVIADO_CORREO),
--            segregando por modelo de impresión XML y contrastando con las digitales.
-- ==============================================================================================

SELECT
    TO_CHAR(d.doc_fecha_emision, 'YYYY-MM')                      AS anio_mes_emision,
    d.doc_anio                                                   AS ciclo_anio,
    d.doc_periodo                                                AS ciclo_periodo,
    -- Marca de despacho a correo postal
    CASE 
        WHEN d.doc_enviado_correo IS NOT NULL THEN 'IMPRESA_ENVIADA_CORREO'
        ELSE 'DIGITAL_SIN_CORREO_POSTAL'
    END                                                          AS condicion_envio_historica,
    NVL(d.codigo_modelo_impresion_xml, 'SIN_MODELO_XML')         AS modelo_impresion_xml,
    NVL(d.ivv_tipo_formulario, 'SIN_FORMULARIO')                 AS tipo_formulario,
    COUNT(*)                                                     AS total_casos_facturas,
    COUNT(DISTINCT d.srv_codigo || '-' || d.cnt_numero)          AS contratos_unicos_facturados,
    SUM(d.doc_importe)                                           AS importe_total_facturado,
    MIN(d.doc_enviado_correo)                                    AS primer_despacho_correo,
    MAX(d.doc_enviado_correo)                                    AS ultimo_despacho_correo
FROM
    xxsigec.documentos d
WHERE
    d.doc_tipo = 'F'               -- Factura normal
    AND d.doc_grupo = 'N'          -- Circuito normal de energía eléctrica
    AND d.doc_fecha_emision >= TO_DATE('2024-01-01', 'YYYY-MM-DD')
GROUP BY
    TO_CHAR(d.doc_fecha_emision, 'YYYY-MM'),
    d.doc_anio,
    d.doc_periodo,
    CASE 
        WHEN d.doc_enviado_correo IS NOT NULL THEN 'IMPRESA_ENVIADA_CORREO'
        ELSE 'DIGITAL_SIN_CORREO_POSTAL'
    END,
    NVL(d.codigo_modelo_impresion_xml, 'SIN_MODELO_XML'),
    NVL(d.ivv_tipo_formulario, 'SIN_FORMULARIO')
ORDER BY
    anio_mes_emision DESC,
    ciclo_periodo DESC,
    condicion_envio_historica;


-- ==============================================================================================
-- CONSULTA 2: RECONSTRUCCIÓN POINT-IN-TIME DE CNT_TIPO_IMPRESION VIA JOURNAL (CONTRATOS_JN)
-- ==============================================================================================
-- Proposito: Determinar con exactitud qué valor de CNT_TIPO_IMPRESION tenía el contrato AL MOMENTO
--            EXACTO de la emisión de cada factura, independientemente de si hoy el cliente
--            se adhirió a Factura Digital (SIM) o cambió a Oficina Virtual (SEN).
-- ==============================================================================================

WITH facturas_periodo AS (
    SELECT /*+ INDEX(d DOC_FECHA_EMISION_IDX) */
        d.doc_tipo,
        d.doc_numero,
        d.srv_codigo,
        d.cnt_numero,
        d.doc_fecha_emision,
        d.doc_enviado_correo,
        d.doc_anio,
        d.doc_periodo
    FROM
        xxsigec.documentos d
    WHERE
        d.doc_tipo = 'F'
        AND d.doc_grupo = 'N'
        AND d.doc_fecha_emision >= TO_DATE('2025-01-01', 'YYYY-MM-DD')
        AND d.doc_fecha_emision <  TO_DATE('2025-02-01', 'YYYY-MM-DD')  -- Mes testigo de prueba
),
estado_contrato_historico AS (
    SELECT
        f.doc_tipo,
        f.doc_numero,
        f.srv_codigo,
        f.cnt_numero,
        f.doc_fecha_emision,
        f.doc_enviado_correo,
        -- Obtenemos el último CNT_TIPO_IMPRESION anterior o igual a la fecha de emision de la factura
        jn.cnt_tipo_impresion AS tipo_impresion_historico,
        ROW_NUMBER() OVER (
            PARTITION BY f.doc_tipo, f.doc_numero 
            ORDER BY jn.jn_fecha DESC, jn.jn_secuencia_cnt DESC
        ) AS rn
    FROM
        facturas_periodo f
        INNER JOIN xxsigec.contratos_jn jn
            ON jn.srv_codigo = f.srv_codigo
            AND jn.cnt_numero = f.cnt_numero
            AND jn.jn_fecha <= f.doc_fecha_emision
)
SELECT
    NVL(tipo_impresion_historico, 'SIN_REGISTRO_JN') AS tipo_impresion_al_facturar,
    CASE NVL(tipo_impresion_historico, 'EST')
        WHEN 'EST' THEN 'ESTANDAR (Papel / Correo Postal)'
        WHEN 'BR'  THEN 'BRAILLE (Especial Correo)'
        WHEN 'REC' THEN 'REPARTO RECOMENDADO (Correo)'
        WHEN 'EMP' THEN 'EMPLEADO EPEC'
        WHEN 'SEN' THEN 'SIN ENVIO (Oficina Virtual)'
        WHEN 'SIM' THEN 'SIN IMPRESION (Factura Digital)'
        WHEN 'ADJ' THEN 'ADJUNTA NOTA'
        ELSE 'OTRO / INDETERMINADO'
    END                                              AS descripcion_tipo,
    CASE 
        WHEN doc_enviado_correo IS NOT NULL THEN 'SI_DESPACHADO'
        ELSE 'NO_DESPACHADO'
    END                                              AS estado_despacho_doc,
    COUNT(*)                                         AS cantidad_facturas_f218
FROM
    estado_contrato_historico
WHERE
    rn = 1
GROUP BY
    tipo_impresion_historico,
    CASE 
        WHEN doc_enviado_correo IS NOT NULL THEN 'SI_DESPACHADO'
        ELSE 'NO_DESPACHADO'
    END
ORDER BY
    cantidad_facturas_f218 DESC;


-- ==============================================================================================
-- CONSULTA 3: TOTALIZADOR MENSUAL CONCILIABLE CON LA F-218 Y PLANILLA OP (LIQUIDACION_CORREO)
-- ==============================================================================================
-- Proposito: Generar exactamente la matriz mensual de cantidades de 'Facturas Distribuidas' (Item 3)
--            e 'Impresión de Facturas' (Item 1) para cotejar contra la F-218 y el Excel de la red.
-- ==============================================================================================

SELECT
    TO_CHAR(d.doc_fecha_emision, 'YYYY-MM') AS anio_mes_liquidacion,
    COUNT(CASE WHEN d.doc_enviado_correo IS NOT NULL THEN 1 END) AS cantidad_facturas_impresas_correo,
    COUNT(CASE WHEN d.doc_enviado_correo IS NULL THEN 1 END)     AS cantidad_facturas_digitales,
    COUNT(*)                                                     AS total_facturas_emitidas,
    ROUND(
        COUNT(CASE WHEN d.doc_enviado_correo IS NOT NULL THEN 1 END) * 100.0 / COUNT(*), 
        2
    )                                                            AS porcentaje_papel_correo,
    ROUND(
        COUNT(CASE WHEN d.doc_enviado_correo IS NULL THEN 1 END) * 100.0 / COUNT(*), 
        2
    )                                                            AS porcentaje_digital
FROM
    xxsigec.documentos d
WHERE
    d.doc_tipo = 'F'
    AND d.doc_grupo = 'N'
    AND d.doc_fecha_emision >= TO_DATE('2024-01-01', 'YYYY-MM-DD')
GROUP BY
    TO_CHAR(d.doc_fecha_emision, 'YYYY-MM')
ORDER BY
    anio_mes_liquidacion DESC;
