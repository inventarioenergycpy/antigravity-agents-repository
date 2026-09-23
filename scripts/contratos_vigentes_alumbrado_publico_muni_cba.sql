/* =========================================================================
   CONSULTA : Contratos Vigentes de Alumbrado Público - Municipalidad de Córdoba
   ESQUEMA  : XXSIGEC (Oracle Database 19c / PRODEBS_SEE)
   OBJETIVO : Extraer todos los suministros vigentes de Alumbrado Público
              pertenecientes a la Municipalidad de Córdoba (incluyendo 
              todas las localidades y áreas geográficas).
   CAMPOS   : Razón Social, Suministro, Contrato, Calle, Nro, Dir Adicional,
              Localidad, Medidor, Fecha Instalación, Tarifa, Ente, Criterio.
   AUTOR    : Agente [02] Ciencia de Datos & BI EPEC
   FECHA    : 2026-09-23
   ========================================================================= */

SELECT
    p.prs_razon_social                                  AS razon_social,
    c.srv_codigo                                        AS suministro,
    c.cnt_numero                                        AS contrato,
    s.srv_calle                                         AS calle,
    s.srv_nro                                           AS nro_calle,
    s.srv_direccion                                     AS datos_adicionales_direccion,
    NVL(ag.agf_nombre, 'SIN LOCALIDAD')                 AS localidad,
    eq.ste_numero                                       AS medidor,
    TO_CHAR(eq.eqp_fecha_instal, 'DD/MM/YYYY')          AS fecha_instalacion_medidor,
    c.tcl_codigo || ' - ' || t.tcl_descripcion          AS tarifa,
    NVL(c.min_codigo || ' - ' || e.min_descripcion, 'SIN ENTE') AS ente_descripcion,
    
    -- Trazabilidad del Criterio de Selección (Camino 1 vs Camino 2)
    CASE 
        WHEN c.tcl_codigo IN ('604', '605', '606') AND c.min_codigo IN ('3004', '3005', '3104', '3105') 
            THEN 'Cumple Camino 1 y Camino 2'
        WHEN c.tcl_codigo IN ('604', '605', '606') 
            THEN 'Solo Camino 1 (Tarifa AP / Ente distinto)'
        ELSE 'Solo Camino 2 (Ente AP / Tarifa distinta)'
    END                                                 AS criterio_inclusion

FROM
    xxsigec.contratos c

-- 1. Vinculación con Personas (Razón Social Municipalidad de Córdoba sin restringir jurisdicción)
INNER JOIN xxsigec.personas p 
    ON c.prs_numero = p.prs_numero

-- 2. Vinculación con Servicios (Datos físicos de localización del suministro)
INNER JOIN xxsigec.servicios s 
    ON c.srv_codigo = s.srv_codigo

-- 3. Vinculación con Áreas Geográficas (Localidad)
LEFT JOIN xxsigec.areas_geograficas ag 
    ON s.agf_codigo = ag.agf_codigo

-- 4. Vinculación con Tarifas (Descripción de Tarifa)
LEFT JOIN xxsigec.tarifas t 
    ON c.tcl_codigo = t.tcl_codigo

-- 5. Vinculación con Entes Estatales (Descripción de Ente)
LEFT JOIN xxsigec.entes e 
    ON c.min_codigo = e.min_codigo

-- 6. Vinculación con Medidores Físicos Activos (eqp_estado IS NULL)
LEFT JOIN xxsigec.equipos eq 
    ON s.srv_codigo = eq.srv_codigo 
    AND eq.eqp_estado IS NULL

WHERE
    -- Filtro de Contrato Vigente ('V')
    c.cnt_estado = 'V'
    
    -- Filtro de Razón Social (Municipalidad de Córdoba)
    AND (
        UPPER(p.prs_razon_social) LIKE '%MUNICIPALIDAD%CORDOBA%'
        OR UPPER(p.prs_razon_social) LIKE '%MUNICIP%C%RDOBA%'
    )
    
    -- Condición Combinada de Alumbrado Público (Camino 1 + Camino 2)
    AND (
        c.tcl_codigo IN ('604', '605', '606')
        OR c.min_codigo IN ('3004', '3005', '3104', '3105')
    )

ORDER BY
    ag.agf_nombre ASC,
    c.tcl_codigo ASC,
    c.srv_codigo ASC;
