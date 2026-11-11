/* ==============================================================================================
   CONSULTA SQL DE CONVALIDACION: REQUERIMIENTO AFIP / ARCA - PICCININI MAXIMILIANO ALBERTO
   ==============================================================================================
   CONTRIBUYENTE : PICCININI MAXIMILIANO ALBERTO
   CUIT          : 20-26744618-1 (PRS_NUMERO: 1023878)
   REQUERIMIENTO : F. 8400/L N.º 0110002026045170002 (OI N.º 2465605)
   PERIODO       : Enero 2024 a Julio 2026 (01/01/2024 al 31/07/2026)
   MOTOR BD      : Oracle Database 19c Enterprise Edition (PRODEBS_SEE / EPEC)
   ESQUEMA       : XXSIGEC
   AUTOR         : Agente [02] Ciencia de Datos & Business Intelligence EPEC
   FECHA         : 2026-10-02
   ============================================================================================== */

WITH cliente_target AS (
    -- 1. Localización del titular por CUIT o ID de Persona
    SELECT 
        prs_numero,
        prs_razon_social,
        prs_cuit,
        prs_tipo_doc,
        prs_documento
    FROM 
        xxsigec.personas
    WHERE 
        prs_cuit = 20267446181
        OR prs_numero = 1023878
),
contratos_titular AS (
    -- 2. Suministros y contratos con actividad dentro del período solicitado
    SELECT 
        c.srv_codigo,
        c.cnt_numero,
        c.prs_numero,
        cli.prs_razon_social,
        cli.prs_cuit,
        c.cnt_estado,
        CASE WHEN c.cnt_estado = 'V' THEN 'VIGENTE' ELSE 'CADUCO' END AS estado_suministro,
        c.tcl_codigo,
        t.tcl_descripcion AS tarifa_descripcion,
        c.cnt_fecha_inicio,
        c.cnt_fecha_fin,
        s.srv_calle || CASE WHEN s.srv_nro IS NOT NULL THEN ' ' || s.srv_nro ELSE '' END AS domicilio_servicio,
        NVL(s.srv_direccion, '') AS datos_adicionales_dir,
        NVL(ag.agf_nombre, 'SIN LOCALIDAD') AS localidad
    FROM 
        xxsigec.contratos c
    JOIN 
        cliente_target cli ON c.prs_numero = cli.prs_numero
    JOIN 
        xxsigec.servicios s ON c.srv_codigo = s.srv_codigo
    LEFT JOIN 
        xxsigec.areas_geograficas ag ON s.agf_codigo = ag.agf_codigo
    LEFT JOIN 
        xxsigec.tarifas t ON c.tcl_codigo = t.tcl_codigo
    WHERE 
        c.srv_codigo IN (367193, 371771, 413593, 971255, 3071889, 3181200, 3197323, 3197328)
),
desglose_items AS (
    -- 3. Agregación analítica de ítems por documento para separar Neto, IVA y Otros Cargos
    SELECT 
        i.doc_tipo,
        i.doc_numero,
        SUM(CASE 
            WHEN ti.tit_iva = 'S' OR ti.gii_codigo IN ('IE', 'IT') THEN i.itm_importe 
            ELSE 0 
        END) AS neto_gravado_items,
        SUM(CASE 
            WHEN i.tit_clave IN ('IVI', 'IVO', 'IVC', 'IRP') OR ti.tit_descripcion LIKE '%IVA%' OR ti.tit_descripcion LIKE '%SNC%' 
            THEN i.itm_importe 
            ELSE 0 
        END) AS iva_items,
        SUM(CASE 
            WHEN (ti.tit_iva IS NULL OR ti.tit_iva <> 'S') 
             AND (ti.gii_codigo IS NULL OR ti.gii_codigo NOT IN ('IE', 'IT'))
             AND i.tit_clave NOT IN ('IVI', 'IVO', 'IVC', 'IRP')
             AND ti.tit_descripcion NOT LIKE '%IVA%' 
             AND ti.tit_descripcion NOT LIKE '%SNC%'
            THEN i.itm_importe 
            ELSE 0 
        END) AS otros_cargos_items
    FROM 
        xxsigec.items i
    LEFT JOIN 
        xxsigec.tipos_item ti ON i.tit_clave = ti.tit_clave
    WHERE 
        (i.doc_tipo, i.doc_numero) IN (
            SELECT d.doc_tipo, d.doc_numero
            FROM xxsigec.documentos d
            JOIN contratos_titular ct ON d.srv_codigo = ct.srv_codigo AND d.cnt_numero = ct.cnt_numero
            WHERE d.doc_fecha_emision BETWEEN TO_DATE('2024-01-01', 'YYYY-MM-DD') AND TO_DATE('2026-07-31', 'YYYY-MM-DD')
        )
    GROUP BY 
        i.doc_tipo, i.doc_numero
),
movimientos_comerciales AS (
    -- 4. Consolidación de documentos de facturación, pagos, cobranzas, notas y planes
    SELECT 
        ct.srv_codigo,
        ct.cnt_numero,
        ct.srv_codigo || '/' || LPAD(TO_CHAR(ct.cnt_numero), 2, '0') AS suministro_formato,
        ct.domicilio_servicio,
        ct.localidad,
        ct.estado_suministro,
        d.doc_fecha_emision AS fecha_emision,
        CASE 
            WHEN d.doc_tipo IN ('F', 'FA') THEN 'Factura'
            WHEN d.doc_tipo IN ('P', 'PA') THEN 'Pago'
            WHEN d.doc_tipo = 'RC' THEN 'Cobranza'
            WHEN d.doc_tipo = 'DT' THEN 'ND Interna'
            WHEN d.doc_tipo = 'CT' THEN 'NC Interna'
            WHEN d.doc_tipo = 'CF' THEN 'Plan de pago'
            WHEN d.doc_tipo = 'PG' THEN 'Cuota Plan'
            ELSE d.doc_tipo 
        END AS tipo_comprobante_descripcion,
        d.doc_tipo,
        d.doc_numero AS nro_comprobante,
        NVL(d.tce_codigo, 'A') AS letra_comprobante,
        CASE 
            WHEN d.tce_punto_venta IS NOT NULL AND d.tce_numero IS NOT NULL 
                THEN LPAD(TO_CHAR(d.tce_punto_venta), 5, '0') || '-' || LPAD(TO_CHAR(d.tce_numero), 8, '0')
            ELSE NULL 
        END AS nro_liq_serv_publicos,
        
        -- Importes desagregados
        CASE 
            WHEN d.doc_tipo IN ('F', 'FA') THEN NVL(di.neto_gravado_items, NVL(d.doc_importe_gravado, 0))
            ELSE 0 
        END AS importe_neto,
        CASE 
            WHEN d.doc_tipo IN ('F', 'FA') THEN NVL(di.iva_items, 0)
            ELSE 0 
        END AS importe_iva,
        CASE 
            WHEN d.doc_tipo IN ('F', 'FA') THEN NVL(di.otros_cargos_items, NVL(d.doc_importe_exento, 0))
            WHEN d.doc_tipo IN ('DT', 'CT') THEN NVL(d.doc_importe, 0)
            ELSE 0 
        END AS importe_otros_cargos,
        
        d.doc_importe AS importe_total,
        d.doc_saldo AS saldo_individual_documento,
        d.doc_consumo AS kwh_facturados,
        d.doc_anio AS anio_periodo,
        d.doc_periodo AS ciclo_periodo
    FROM 
        xxsigec.documentos d
    JOIN 
        contratos_titular ct ON d.srv_codigo = ct.srv_codigo AND d.cnt_numero = ct.cnt_numero
    LEFT JOIN 
        desglose_items di ON d.doc_tipo = di.doc_tipo AND d.doc_numero = di.doc_numero
    WHERE 
        d.doc_fecha_emision BETWEEN TO_DATE('2024-01-01', 'YYYY-MM-DD') AND TO_DATE('2026-07-31', 'YYYY-MM-DD')
        AND d.doc_estado = 'D' -- Filtro estricto de documentos definitivos
)
SELECT 
    m.suministro_formato,
    m.domicilio_servicio,
    m.localidad,
    m.estado_suministro,
    TO_CHAR(m.fecha_emision, 'DD/MM/YYYY') AS fecha_emision,
    m.tipo_comprobante_descripcion,
    m.doc_tipo || ' ' || TO_CHAR(m.nro_comprobante) AS comprobante_id,
    m.letra_comprobante,
    m.nro_liq_serv_publicos,
    m.importe_neto,
    m.importe_iva,
    m.importe_otros_cargos,
    m.importe_total,
    -- Cálculo de evolución cronológica de saldo en Cuenta Corriente
    SUM(m.importe_total) OVER (
        PARTITION BY m.srv_codigo, m.cnt_numero 
        ORDER BY m.fecha_emision ASC, m.nro_comprobante ASC
    ) AS saldo_acumulado_cta_cte
FROM 
    movimientos_comerciales m
ORDER BY 
    m.srv_codigo ASC, 
    m.cnt_numero ASC, 
    m.fecha_emision ASC, 
    m.nro_comprobante ASC;
