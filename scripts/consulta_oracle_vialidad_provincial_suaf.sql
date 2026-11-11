-- ========================================================================
-- REPORTE DE AUDITORÍA Y CONTROL: VIALIDAD PROVINCIAL vs. SISTEMA SUAF
-- SCHEMA: XXSIGEC | INSTANCIA: PRODEBS_SEE (Oracle 19c)
-- COLUMNA IDENTIFICADORA DE SUMINISTRO: c.srv_codigo / s.srv_codigo
-- ========================================================================

SELECT 
    c.srv_codigo                                              AS suministro,
    c.cnt_numero                                              AS nro_contrato,
    LPAD(c.srv_codigo, 8, '0') || LPAD(c.cnt_numero, 2, '0') AS stro_cnt_completo,
    c.prs_numero                                              AS prs_numero_cliente,
    p.prs_razon_social                                        AS razon_social_titular,
    c.min_codigo                                              AS codigo_ente,
    NVL(e.min_descripcion, 'SIN ENTE')                         AS descripcion_ente,
    CASE 
        WHEN c.min_codigo = '02' OR c.prs_numero = 336080 OR UPPER(p.prs_razon_social) LIKE '%VIALIDAD%'
        THEN 'SI - VIALIDAD PROVINCIAL'
        ELSE 'NO - OTRO ENTE / NO DPV'
    END                                                       AS marca_vialidad_provincial,
    suc.zon_codigo                                            AS letra_zona,
    z.zon_descripcion                                         AS zona_descripcion,
    suc.scf_descripcion                                       AS sucursal_epec,
    c.tcl_codigo                                              AS tarifa_codigo,
    t.tcl_descripcion                                         AS tarifa_descripcion,
    c.cnt_estado                                              AS estado_contrato,
    TO_CHAR(c.cnt_fecha_inicio, 'DD/MM/YYYY')                 AS fecha_inicio_contrato,
    TO_CHAR(c.cnt_fecha_fin, 'DD/MM/YYYY')                    AS fecha_fin_contrato,
    eq.ste_numero                                             AS medidor_activo,
    ag.agf_nombre                                             AS localidad
FROM xxsigec.contratos c
LEFT JOIN xxsigec.personas p 
  ON c.prs_numero = p.prs_numero
LEFT JOIN xxsigec.servicios s 
  ON c.srv_codigo = s.srv_codigo
LEFT JOIN xxsigec.areas_geograficas ag 
  ON s.agf_codigo = ag.agf_codigo
LEFT JOIN xxsigec.sucursales suc 
  ON s.scf_codigo = suc.scf_codigo
LEFT JOIN xxsigec.zonas z 
  ON suc.zon_codigo = z.zon_codigo
LEFT JOIN xxsigec.entes e 
  ON c.min_codigo = e.min_codigo
LEFT JOIN xxsigec.tarifas t 
  ON c.tcl_codigo = t.tcl_codigo
LEFT JOIN xxsigec.equipos eq 
  ON s.srv_codigo = eq.srv_codigo 
 AND eq.eqp_estado IS NULL
WHERE c.cnt_estado = 'A'
ORDER BY suc.zon_codigo, c.srv_codigo, c.cnt_numero;
