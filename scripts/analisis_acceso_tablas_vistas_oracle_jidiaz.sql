/* ==============================================================================================
   SUITE DE ANALISIS DE ACCESIBILIDAD A TABLAS Y VISTAS EN ORACLE DATABASE
   ==============================================================================================
   USUARIO TARGET : jidiaz (y roles asignados)
   DICCIONARIO BD : SYS.ALL_TABLES, SYS.ALL_VIEWS, SYS.ALL_TAB_PRIVS, SYS.ALL_TAB_COMMENTS, 
                    SYS.ALL_TAB_COLS, SYS.ALL_SYNONYMS, USER_ROLE_PRIVS, SESSION_ROLES
   MOTOR COMPAT.  : Oracle Database 11g / 12c / 18c / 19c / 21c Enterprise Edition (PRODEBS_SEE / EPEC)
   AUTOR          : Agente [02] Ciencia de Datos & BI (Ecosistema Antigravity IDE)
   FECHA          : 2026-10-08
   METODOLOGIA    : Desarrollo e Ingenieria de Datos en 6 Etapas
   ============================================================================================== */

-- ==============================================================================================
-- MODULO 1: RESUMEN EJECUTIVO Y DISTRIBUCION DE OBJETOS ACCESIBLES POR ESQUEMA (OWNER)
-- ==============================================================================================
-- Proposito: Identificar cuantitativamente a que esquemas tiene acceso el usuario jidiaz,
--            separando esquemas de negocio operacional (XXSIGEC, EPEC, etc.) de esquemas de sistema.
-- ==============================================================================================

WITH inventario_unificado AS (
    -- 1. Tablas fisicas accesibles
    SELECT 
        owner,
        table_name AS object_name,
        'TABLE' AS object_type,
        num_rows,
        tablespace_name,
        status,
        last_analyzed
    FROM sys.all_tables
    
    UNION ALL
    
    -- 2. Vistas logicas accesibles
    SELECT 
        owner,
        view_name AS object_name,
        'VIEW' AS object_type,
        NULL AS num_rows,
        NULL AS tablespace_name,
        'VALID' AS status,
        NULL AS last_analyzed
    FROM sys.all_views
),
clasificacion_esquemas AS (
    SELECT 
        owner,
        object_name,
        object_type,
        num_rows,
        CASE 
            WHEN owner IN ('SYS', 'SYSTEM', 'DBSNMP', 'OUTLN', 'XDB', 'WMSYS', 'CTXSYS', 
                           'MDSYS', 'ORDSYS', 'AUDSYS', 'GSMADMIN_INTERNAL', 'OJVMSYS', 
                           'APEX_040000', 'APEX_050000', 'APEX_190000', 'LBACSYS', 'DVSYS') 
                THEN 'SISTEMA_ORACLE_INTERNO'
            WHEN owner LIKE 'APEX%' OR owner LIKE 'FLOWS_%' 
                THEN 'FRAMEWORK_APEX'
            WHEN owner IN ('XXSIGEC', 'SIGEC', 'EPEC', 'COMMERCIAL', 'GIS', 'CATASTRO', 'PROTELEM')
                THEN 'NEGOCIO_CORE_OPERACIONAL'
            ELSE 'APLICATIVO_EXTERNO_O_USUARIO'
        END AS categoria_esquema
    FROM inventario_unificado
)
SELECT 
    categoria_esquema,
    owner,
    COUNT(CASE WHEN object_type = 'TABLE' THEN 1 END) AS total_tablas,
    COUNT(CASE WHEN object_type = 'VIEW' THEN 1 END) AS total_vistas,
    COUNT(1) AS total_objetos_accesibles,
    NVL(SUM(num_rows), 0) AS total_filas_estimadas_tablas
FROM clasificacion_esquemas
GROUP BY categoria_esquema, owner
ORDER BY 
    CASE 
        WHEN categoria_esquema = 'NEGOCIO_CORE_OPERACIONAL' THEN 1
        WHEN categoria_esquema = 'APLICATIVO_EXTERNO_O_USUARIO' THEN 2
        WHEN categoria_esquema = 'FRAMEWORK_APEX' THEN 3
        ELSE 4 
    END,
    total_objetos_accesibles DESC;


-- ==============================================================================================
-- MODULO 2: INVENTARIO MAESTRO DETALLADO DE TABLAS Y VISTAS DE NEGOCIO
-- ==============================================================================================
-- Proposito: Listado completo de tablas y vistas accesibles excluyendo catalogos internos de SYS,
--            incorporando conteo de columnas, fecha de analisis estadistico y comentarios.
-- ==============================================================================================

WITH catalogo_objetos AS (
    SELECT 
        t.owner,
        t.table_name AS nombre_objeto,
        'TABLA' AS tipo_objeto,
        t.num_rows AS filas_estimadas,
        t.blocks,
        t.last_analyzed AS ultima_fecha_analisis,
        t.partitioned AS es_particionada,
        t.status AS estado_objeto
    FROM sys.all_tables t
    
    UNION ALL
    
    SELECT 
        v.owner,
        v.view_name AS nombre_objeto,
        'VISTA' AS tipo_objeto,
        NULL AS filas_estimadas,
        NULL AS blocks,
        NULL AS ultima_fecha_analisis,
        'NO' AS es_particionada,
        'VALID' AS estado_objeto
    FROM sys.all_views v
),
conteo_columnas AS (
    SELECT 
        owner,
        table_name AS nombre_objeto,
        COUNT(1) AS total_columnas
    FROM sys.all_tab_cols
    GROUP BY owner, table_name
),
comentarios_tabla AS (
    SELECT 
        owner,
        table_name AS nombre_objeto,
        comments AS descripcion_funcional
    FROM sys.all_tab_comments
)
SELECT 
    c.owner AS esquema_propietario,
    c.nombre_objeto,
    c.tipo_objeto,
    NVL(col.total_columnas, 0) AS cant_columnas,
    c.filas_estimadas,
    c.es_particionada,
    TO_CHAR(c.ultima_fecha_analisis, 'YYYY-MM-DD HH24:MI:SS') AS fecha_estadisticas,
    com.descripcion_funcional
FROM catalogo_objetos c
LEFT JOIN conteo_columnas col 
  ON c.owner = col.owner AND c.nombre_objeto = col.nombre_objeto
LEFT JOIN comentarios_tabla com 
  ON c.owner = com.owner AND c.nombre_objeto = com.nombre_objeto
WHERE c.owner NOT IN (
    'SYS', 'SYSTEM', 'DBSNMP', 'OUTLN', 'XDB', 'WMSYS', 'CTXSYS', 
    'MDSYS', 'ORDSYS', 'AUDSYS', 'GSMADMIN_INTERNAL', 'OJVMSYS'
)
ORDER BY c.owner ASC, c.tipo_objeto ASC, c.nombre_objeto ASC;


-- ==============================================================================================
-- MODULO 3: AUDITORIA DE PRIVILEGIOS EXPLICITOS Y ROLES DE ACCESO (SECURITY MATRIX)
-- ==============================================================================================
-- Proposito: Determinar con exactitud que tipo de operaciones (SELECT, INSERT, UPDATE, DELETE)
--            puede realizar jidiaz sobre cada tabla o vista, y mediante que via (Directa o Rol).
-- ==============================================================================================

WITH privilegios_recibidos AS (
    -- Privilegios otorgados a jidiaz, roles activos o asignados a PUBLIC
    SELECT 
        grantee,
        owner,
        table_name,
        privilege,
        grantable,
        grantor,
        CASE 
            WHEN grantee = USER THEN 'PRIVILEGIO_DIRECTO_USUARIO'
            WHEN grantee = 'PUBLIC' THEN 'ASIGNACION_GLOBAL_PUBLIC'
            ELSE 'ROL_ASIGNADO'
        END AS tipo_otorgamiento
    FROM sys.all_tab_privs_recd
    WHERE grantee IN (USER, 'PUBLIC')
       OR grantee IN (SELECT granted_role FROM user_role_privs)
       OR grantee IN (SELECT role FROM session_roles)
)
SELECT 
    owner AS esquema_tabla,
    table_name AS nombre_tabla_vista,
    tipo_otorgamiento,
    grantee AS beneficiario_permiso,
    LISTAGG(privilege, ', ') WITHIN GROUP (ORDER BY privilege) AS privilegios_disponibles,
    grantor AS otorgado_por
FROM privilegios_recibidos
WHERE owner NOT IN ('SYS', 'SYSTEM', 'XDB', 'WMSYS', 'MDSYS')
GROUP BY 
    owner,
    table_name,
    tipo_otorgamiento,
    grantee,
    grantor
ORDER BY owner, table_name;


-- ==============================================================================================
-- MODULO 4: MOTOR DE BUSQUEDA Y DESCUBRIMIENTO POR ENTIDADES DE NEGOCIO CORE
-- ==============================================================================================
-- Proposito: Localizar instantaneamente tablas y vistas asociadas a entidades operativas clave
--            (Contratos, Clientes/Personas, Medidores/Equipos, Facturas, Cobranzas, Reclamos, etc.)
-- ==============================================================================================

SELECT 
    CASE 
        WHEN UPPER(o.nombre_objeto) LIKE '%CNT%' OR UPPER(o.nombre_objeto) LIKE '%CONTRAT%' 
            THEN '1. CONTRATOS_Y_SUMINISTROS'
        WHEN UPPER(o.nombre_objeto) LIKE '%PRS%' OR UPPER(o.nombre_objeto) LIKE '%PERSON%' OR UPPER(o.nombre_objeto) LIKE '%CLI%' 
            THEN '2. CLIENTES_Y_PERSONAS'
        WHEN UPPER(o.nombre_objeto) LIKE '%DOC%' OR UPPER(o.nombre_objeto) LIKE '%FACT%' OR UPPER(o.nombre_objeto) LIKE '%ITM%' OR UPPER(o.nombre_objeto) LIKE '%ITEM%' 
            THEN '3. FACTURACION_Y_DOCUMENTOS'
        WHEN UPPER(o.nombre_objeto) LIKE '%MED%' OR UPPER(o.nombre_objeto) LIKE '%EQP%' OR UPPER(o.nombre_objeto) LIKE '%EQUIP%' OR UPPER(o.nombre_objeto) LIKE '%STE%' 
            THEN '4. MEDIDORES_Y_EQUIPOS'
        WHEN UPPER(o.nombre_objeto) LIKE '%PAG%' OR UPPER(o.nombre_objeto) LIKE '%COB%' OR UPPER(o.nombre_objeto) LIKE '%MOV%' OR UPPER(o.nombre_objeto) LIKE '%CTA%' 
            THEN '5. PAGOS_Y_CUENTA_CORRIENTE'
        WHEN UPPER(o.nombre_objeto) LIKE '%REC%' OR UPPER(o.nombre_objeto) LIKE '%CLM%' OR UPPER(o.nombre_objeto) LIKE '%CAS%' OR UPPER(o.nombre_objeto) LIKE '%CXI%' 
            THEN '6. RECLAMOS_Y_ATENCION_CX'
        WHEN UPPER(o.nombre_objeto) LIKE '%GEO%' OR UPPER(o.nombre_objeto) LIKE '%CAT%' OR UPPER(o.nombre_objeto) LIKE '%SRV%' OR UPPER(o.nombre_objeto) LIKE '%LOC%' OR UPPER(o.nombre_objeto) LIKE '%ZON%' 
            THEN '7. CATASTRO_Y_GEOGRAFIA'
        WHEN UPPER(o.nombre_objeto) LIKE '%TAR%' OR UPPER(o.nombre_objeto) LIKE '%TCL%' OR UPPER(o.nombre_objeto) LIKE '%PRE%' 
            THEN '8. TARIFAS_Y_PRECIOS'
        ELSE '9. OTROS_MODULOS'
    END AS dominio_funcional,
    o.owner AS esquema,
    o.nombre_objeto,
    o.tipo_objeto,
    NVL(t.num_rows, 0) AS filas_estimadas,
    c.comments AS descripcion_comentario
FROM (
    SELECT owner, table_name AS nombre_objeto, 'TABLA' AS tipo_objeto FROM sys.all_tables
    UNION ALL
    SELECT owner, view_name AS nombre_objeto, 'VISTA' AS tipo_objeto FROM sys.all_views
) o
LEFT JOIN sys.all_tables t 
  ON o.owner = t.owner AND o.nombre_objeto = t.table_name
LEFT JOIN sys.all_tab_comments c 
  ON o.owner = c.owner AND o.nombre_objeto = c.table_name
WHERE o.owner NOT IN ('SYS', 'SYSTEM', 'XDB', 'WMSYS', 'MDSYS', 'CTXSYS', 'AUDSYS')
ORDER BY dominio_funcional ASC, o.owner ASC, o.nombre_objeto ASC;


-- ==============================================================================================
-- MODULO 5: DICCIONARIO DE COLUMNAS PARA UN ESQUEMA O TABLA ESPECIFICA
-- ==============================================================================================
-- Proposito: Inspeccionar la estructura interna, tipos de datos y nulabilidad de cualquier tabla
--            accesible (ej. XXSIGEC.CONTRATOS, XXSIGEC.DOCUMENTOS, XXSIGEC.SERVICIOS, etc.)
-- ==============================================================================================

SELECT 
    c.owner AS esquema,
    c.table_name AS tabla_o_vista,
    c.column_id AS nro_orden,
    c.column_name AS nombre_columna,
    c.data_type || 
        CASE 
            WHEN c.data_type IN ('VARCHAR2', 'CHAR') THEN '(' || c.data_length || ')'
            WHEN c.data_type = 'NUMBER' AND c.data_precision IS NOT NULL AND c.data_scale IS NOT NULL 
                THEN '(' || c.data_precision || ',' || c.data_scale || ')'
            WHEN c.data_type = 'NUMBER' AND c.data_precision IS NOT NULL 
                THEN '(' || c.data_precision || ')'
            ELSE '' 
        END AS tipo_dato_formateado,
    CASE WHEN c.nullable = 'N' THEN 'NOT NULL' ELSE 'NULLABLE' END AS obligatoriedad,
    com.comments AS comentario_columna
FROM sys.all_tab_cols c
LEFT JOIN sys.all_col_comments com 
  ON c.owner = com.owner 
 AND c.table_name = com.table_name 
 AND c.column_name = com.column_name
WHERE c.owner = 'XXSIGEC' -- Reemplazar por el esquema a auditar (ej. 'XXSIGEC', 'EPEC')
  -- AND c.table_name IN ('CONTRATOS', 'DOCUMENTOS', 'PERSONAS', 'SERVICIOS', 'ITEMS')
ORDER BY c.table_name ASC, c.column_id ASC;


-- ==============================================================================================
-- MODULO 6: MAPEO DE SINONIMOS PUBLICOS Y PRIVADOS ACCESIBLES
-- ==============================================================================================
-- Proposito: Identificar nombres cortos o alias (sinonimos) que permiten consultar tablas
--            sin necesidad de anteponer el nombre del esquema (ej. SELECT * FROM CONTRATOS).
-- ==============================================================================================

SELECT 
    s.owner AS tipo_sinonimo, -- 'PUBLIC' o nombre de usuario
    s.synonym_name AS nombre_sinonimo,
    s.table_owner AS esquema_objeto_real,
    s.table_name AS tabla_objeto_real,
    s.db_link
FROM sys.all_synonyms s
WHERE s.table_owner NOT IN ('SYS', 'SYSTEM', 'XDB', 'WMSYS', 'MDSYS')
  AND (s.owner = 'PUBLIC' OR s.owner = USER)
ORDER BY s.table_owner ASC, s.synonym_name ASC;