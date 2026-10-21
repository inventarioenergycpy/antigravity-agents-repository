-- ============================================================================
-- CONSULTA ORACLE SIGEC: CASUÍSTICA DE CAUSAS DE RECLAMO (VE vs RO / RC 2026)
-- Ecosistema Antigravity IDE - Agente 02: Ciencia de Datos (EPEC / SIGEC)
-- ============================================================================

WITH
-- 1. Universo de Órdenes VE del año 2026
ORDENATIVOS_VE AS (
    SELECT /*+ INDEX(ve ORD_FECHA_GEN_IDX) */
        ve.ORD_NUMERO                               AS ORD_NUMERO_VE,
        ve.SRV_CODIGO                               AS SUMINISTRO,
        ve.CNT_NUMERO                               AS CONTRATO,
        ve.TOR_CODIGO                               AS TIPO_ORDEN_VE,
        ve.TRT_NUMERO                               AS TRT_NUMERO_VE,
        ve.ORD_ESTADO                               AS ESTADO_VE,
        ve.ORD_RESULTADO                            AS RESULTADO_VE,
        ve.ORD_FECHA_GENERACION                     AS FECHA_GEN_VE,
        ve.ORD_FECHA_FIN                            AS FECHA_FIN_VE,
        ve.ORD_DATOS_ADICIONALES                    AS DATOS_ADICIONALES_VE,
        ve.ORD_DATOS_RESULTADOS                     AS DATOS_RESULTADOS_VE,
        ve.SEC_CODIGO_ORIGEN                        AS SEC_ORIGEN_VE,
        ve.SEC_CODIGO_DESTINO                       AS SEC_DESTINO_VE,
        ve.SCF_CODIGO_ORIGEN                        AS SUC_ORIGEN_VE,
        ve.STE_NUMERO                               AS MEDIDOR_VE
    FROM XXSIGEC.ORDENATIVOS ve
    WHERE ve.TOR_CODIGO = 'VE'
      AND ve.ORD_FECHA_GENERACION >= TO_DATE('2026-01-01', 'YYYY-MM-DD')
),

-- 2. Universo de Reclamos Operativos / Comerciales (RO, RC, ER, RN)
ORDENATIVOS_RECLAMO AS (
    SELECT /*+ INDEX(rec ORD_FECHA_GEN_IDX) */
        rec.ORD_NUMERO                              AS ORD_NUMERO_RECLAMO,
        rec.SRV_CODIGO                              AS SUMINISTRO,
        rec.CNT_NUMERO                              AS CONTRATO,
        rec.TOR_CODIGO                              AS TIPO_RECLAMO,
        rec.TRT_NUMERO                              AS TRT_NUMERO_RECLAMO,
        rec.ORD_ESTADO                              AS ESTADO_RECLAMO,
        rec.ORD_RESULTADO                           AS RESULTADO_RECLAMO,
        rec.ORD_FECHA_GENERACION                    AS FECHA_GEN_RECLAMO,
        rec.ORD_FECHA_FIN                           AS FECHA_FIN_RECLAMO,
        rec.ORD_DATOS_ADICIONALES                   AS DATOS_ADICIONALES_RECLAMO,
        rec.ORD_DATOS_RESULTADOS                    AS DATOS_RESULTADOS_RECLAMO,
        rec.SEC_CODIGO_ORIGEN                       AS SEC_ORIGEN_RECLAMO
    FROM XXSIGEC.ORDENATIVOS rec
    WHERE rec.TOR_CODIGO IN ('RO', 'RC', 'ER', 'RN')
      AND rec.ORD_FECHA_GENERACION >= TO_DATE('2025-12-01', 'YYYY-MM-DD')
),

-- 3. Cruce y Ponderación de Vinculación entre VE y Reclamo
CRUCE_VE_RECLAMO AS (
    SELECT
        ve.ORD_NUMERO_VE,
        ve.SUMINISTRO,
        ve.CONTRATO,
        ve.TIPO_ORDEN_VE,
        ve.TRT_NUMERO_VE,
        ve.ESTADO_VE,
        ve.RESULTADO_VE,
        ve.FECHA_GEN_VE,
        ve.FECHA_FIN_VE,
        ve.DATOS_ADICIONALES_VE,
        ve.DATOS_RESULTADOS_VE,
        ve.SEC_DESTINO_VE,
        ve.MEDIDOR_VE,
        
        rec.ORD_NUMERO_RECLAMO,
        rec.TIPO_RECLAMO,
        rec.TRT_NUMERO_RECLAMO,
        rec.ESTADO_RECLAMO,
        rec.RESULTADO_RECLAMO,
        rec.FECHA_GEN_RECLAMO,
        rec.FECHA_FIN_RECLAMO,
        rec.DATOS_ADICIONALES_RECLAMO,
        rec.DATOS_RESULTADOS_RECLAMO,
        
        -- Mecanismo de Enlace
        CASE 
            WHEN ve.TRT_NUMERO_VE = rec.TRT_NUMERO_RECLAMO THEN '1. MISMO TRAMITE (TRT_NUMERO)'
            WHEN ve.DATOS_ADICIONALES_VE LIKE '%' || TO_CHAR(rec.ORD_NUMERO_RECLAMO) || '%' THEN '2. MENCION DIRECTA EN VE'
            WHEN rec.DATOS_ADICIONALES_RECLAMO LIKE '%' || TO_CHAR(ve.ORD_NUMERO_VE) || '%' THEN '3. MENCION DIRECTA EN RECLAMO'
            ELSE '4. MISMO SUMINISTRO EN VENTANA +/- 30 DIAS'
        END AS TIPO_VINCULACION,
        
        ROUND(ve.FECHA_GEN_VE - rec.FECHA_GEN_RECLAMO, 1) AS DIAS_DIF_GEN,
        
        ROW_NUMBER() OVER (
            PARTITION BY ve.ORD_NUMERO_VE
            ORDER BY 
                CASE 
                    WHEN ve.TRT_NUMERO_VE = rec.TRT_NUMERO_RECLAMO THEN 1
                    WHEN ve.DATOS_ADICIONALES_VE LIKE '%' || TO_CHAR(rec.ORD_NUMERO_RECLAMO) || '%' THEN 2
                    WHEN rec.DATOS_ADICIONALES_RECLAMO LIKE '%' || TO_CHAR(ve.ORD_NUMERO_VE) || '%' THEN 3
                    ELSE 4
                END,
                ABS(ve.FECHA_GEN_VE - rec.FECHA_GEN_RECLAMO) ASC
        ) AS RN_MATCH
    FROM ORDENATIVOS_VE ve
    JOIN ORDENATIVOS_RECLAMO rec
      ON (ve.TRT_NUMERO_VE = rec.TRT_NUMERO_RECLAMO OR (ve.SUMINISTRO = rec.SUMINISTRO AND ABS(ve.FECHA_GEN_VE - rec.FECHA_GEN_RECLAMO) <= 30))
),

-- 4. Motor de Clasificación Taxonómica de Causas de Reclamo (NLP / Regex en Oracle SQL)
CLASIFICACION_CASUISTICA AS (
    SELECT
        c.*,
        CASE
            -- 1. Inmueble deshabitado / Vacío
            WHEN REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(vacio|vacío|deshabitad|desocupad|baldio|baldío|sin habitante|no vive nadie|sin uso)') 
              OR REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(dpto|casa|local|inmueble)\s+(est[aá]\s+)?(cerrad|desocupad|sin habit)')
            THEN '1. INMUEBLE DESHABITADO / VACÍO CON CONSUMO FACTURADO'
            
            -- 2. Aporta foto / video / lectura real inferior
            WHEN REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(foto|video|filmaci[oó]n|imagen\s+de\s+lectura|trae\s+lectura|aporta\s+lectura|presenta\s+lectura|adjunta\s+foto|con\s+foto)')
            THEN '2. DISCREPANCIA CON LECTURA REAL (APORTA FOTO / VIDEO / LECTURA)'
            
            -- 3. Consumos Estimados / Falta de toma de lectura
            WHEN REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(estimad|sin\s+tomar\s+lectura|no\s+toman\s+lectura|no\s+pasaron\s+a\s+leer|no\s+pas[oó]\s+el\s+tomador|sin\s+lectura\s+real|per[ií]odos\s+estimados)')
            THEN '3. RECLAMO POR CONSUMOS ESTIMADOS / FALTA DE LECTURA'
            
            -- 4. Error de Lectura / Dígito Erróneo
            WHEN REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(error\s+de\s+lectura|mal\s+le[ií]d|mal\s+tomada|d[ií]gito|error\s+tomador|le[ií]do\s+de\s+m[aá]s|lectura\s+err[oó]nea)')
            THEN '4. ERROR DE LECTURA / DÍGITO ERRÓNEO POR EL TOMADOR'
            
            -- 5. Medidor Cruzado / Discrepancia N° de Medidor / Sin Medidor
            WHEN REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(cruzad|otro\s+medidor|no\s+coincide\s+medidor|medidor\s+equivocado|medidor\s+distinto|cambiaron\s+medidor|sin\s+medidor|robo\s+de\s+medidor)')
              OR REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(medidor\s+instalado\s+\d+|tiene\s+medidor\s+\d+)')
            THEN '5. MEDIDOR CRUZADO / DISCREPANCIA N° DE MEDIDOR / SIN MEDIDOR'
            
            -- 6. Medidor Defectuoso / Trabado / Display Apagado / Quemado
            WHEN REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(trabad|clavad|frenad|no\s+gira|display\s+apagado|pantalla\s+apagada|rot[oa]|quemad|chispea|chispas|defectuoso|averiad)')
            THEN '6. MEDIDOR DEFECTUOSO / TRABADO / DISPLAY APAGADO / QUEMADO'
            
            -- 7. Exceso de Consumo Habitual / Disconformidad
            WHEN REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(exceso|elevado\s+consumo|consumo\s+elevado|alto\s+consumo|consumo\s+muy\s+alto|salto\s+de\s+consumo|mucho\s+consumo|consumo\s+excesivo|desproporcionado|no\s+tengo\s+artefactos|no\s+hay\s+artefactos|imposible\s+ese\s+consumo)')
            THEN '7. EXCESO DE CONSUMO HABITUAL / DISCONFORMIDAD CON FACTURA'
            
            -- 8. Reclamo Web (RO)
            WHEN LOWER(NVL(DATOS_ADICIONALES_RECLAMO, '')) LIKE '%observaciones usuario:%' 
              OR LOWER(NVL(DATOS_ADICIONALES_RECLAMO, '')) LIKE '%verificar el consumo del contrato:%'
              OR LOWER(NVL(DATOS_ADICIONALES_RECLAMO, '')) LIKE '%reclamo web%'
            THEN '8. RECLAMO COMERCIAL WEB (OFICINA VIRTUAL / APP EPEC)'
            
            -- 9. Reclamo Comercial Sucursal (RC)
            WHEN REGEXP_LIKE(LOWER(NVL(DATOS_ADICIONALES_VE, '') || ' ' || NVL(DATOS_ADICIONALES_RECLAMO, '')), '(factura|periodo|período|tarifa|no\s+recibio|no\s+llega|corte|intimacion|intimación|debito|duplicada|ajuste|ersep|sume)')
            THEN '9. RECLAMO COMERCIAL SUCURSAL / TARIFA / FACTURACIÓN'
            
            -- 10. Validación Automática MDM
            WHEN LOWER(NVL(DATOS_ADICIONALES_VE, '')) LIKE '%validacion mdm%'
            THEN '10. VALIDACIÓN AUTOMÁTICA MDM (TELEMEDICIÓN)'
            
            ELSE '11. VERIFICACIÓN GENERAL DE LECTURA EN TERRENO'
        END AS CATEGORIA_CAUSA
    FROM CRUCE_VE_RECLAMO c
    WHERE RN_MATCH = 1
)

-- 5. Reporte Consolidado Final de Casuística
SELECT
    SUMINISTRO,
    CONTRATO,
    ORD_NUMERO_VE,
    TIPO_ORDEN_VE,
    ESTADO_VE,
    RESULTADO_VE,
    TO_CHAR(FECHA_GEN_VE, 'YYYY-MM-DD')         AS FECHA_VE,
    TO_CHAR(FECHA_FIN_VE, 'YYYY-MM-DD')         AS FECHA_FIN_VE,
    
    TIPO_RECLAMO,
    ORD_NUMERO_RECLAMO,
    ESTADO_RECLAMO,
    RESULTADO_RECLAMO,
    TO_CHAR(FECHA_GEN_RECLAMO, 'YYYY-MM-DD')    AS FECHA_RECLAMO,
    
    TIPO_VINCULACION,
    DIAS_DIF_GEN                                AS DIAS_ENTRE_RECLAMO_Y_VE,
    
    CATEGORIA_CAUSA,
    DATOS_ADICIONALES_VE                        AS OBSERVACIONES_VE,
    DATOS_ADICIONALES_RECLAMO                   AS OBSERVACIONES_RECLAMO,
    DATOS_RESULTADOS_VE                         AS RESULTADOS_VE
FROM CLASIFICACION_CASUISTICA
ORDER BY 
    FECHA_GEN_VE DESC, 
    ORD_NUMERO_VE DESC;
