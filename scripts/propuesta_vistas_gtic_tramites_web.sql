/* ==============================================================================================
   PROPUESTA TÉCNICA DE VISTAS SANITIZADAS Y ROLES PARA GTIC - EPEC
   ==============================================================================================
   OBJETIVO       : Facilitar a la GTIC la implementación de accesos de sólo lectura (SELECT)
                    sobre trámites web (Oficina Virtual) y su vinculación con SIGEC.
   SEGURIDAD      : Principio de Mínimo Privilegio, exclusión de BLOBs pesados, hash SHA-256 en BD.
   ESQUEMA SUGERIDO: XXSIGEC / OVP_GATEWAY / ESQUEMA_AUDITORIA
   ============================================================================================== */

-- 1. CREACIÓN DEL ROL DE CONSULTA (Sólo Lectura)
CREATE ROLE RO_AUDITORIA_TRAMITES_WEB;

-- Asignación sugerida al usuario analista:
-- GRANT RO_AUDITORIA_TRAMITES_WEB TO JIDIAZ;


-- 2. VISTA 1: MAESTRO Y TRAZABILIDAD DE SOLICITUDES WEB CON VÍNCULO SIGEC
CREATE OR REPLACE VIEW VW_AUDITORIA_SOLICITUDES_WEB AS
SELECT 
    s.sol_id                        AS solicitud_id,
    s.fecha_creacion                AS fecha_alta,
    s.tipo_solicitud_id             AS tipo_solicitud_codigo,
    ts.descripcion                  AS tipo_solicitud_desc,
    s.estado_id                     AS estado_actual_codigo,
    es.descripcion                  AS estado_actual_desc,
    s.usuario_id                    AS usuario_cuenta_id,
    s.srv_codigo                    AS suministro_nis,
    s.cnt_numero                    AS contrato_numero,
    s.oficina_id                    AS oficina_asignada_codigo,
    ofc.descripcion                 AS oficina_asignada_desc,
    -- Vínculo formal con SIGEC
    s.ordenativo_nro                AS ordenativo_sigec,
    s.reclamo_nro                   AS reclamo_sigec,
    s.fecha_envio_sigec             AS fecha_interfaz_sigec
FROM xxww_solicitudes_new s
LEFT JOIN xxww_tipos_solicitud ts  ON s.tipo_solicitud_id = ts.tipo_solicitud_id
LEFT JOIN xxww_estados_solicitud es ON s.estado_id = es.estado_id
LEFT JOIN xxww_oficinas ofc         ON s.oficina_id = ofc.oficina_id;

GRANT SELECT ON VW_AUDITORIA_SOLICITUDES_WEB TO RO_AUDITORIA_TRAMITES_WEB;


-- 3. VISTA 2: HISTORIAL DE TRANSICIONES Y OBSERVACIONES DE SOLICITUDES
CREATE OR REPLACE VIEW VW_AUDITORIA_SOLICITUDES_HIST AS
SELECT 
    h.sol_id                        AS solicitud_id,
    h.hist_id                       AS secuencia_evento,
    h.fecha_cambio                  AS fecha_transicion,
    h.estado_anterior_id            AS estado_anterior,
    h.estado_nuevo_id               AS estado_nuevo,
    h.usuario_operador              AS usuario_operador_legajo,
    h.accion_realizada              AS accion_tipo, -- 'TOMA', 'APROBACION', 'RECHAZO', 'OBSERVACION'
    h.texto_observacion             AS observacion_rechazo_texto
FROM xxww_solicitudes_historial h;

GRANT SELECT ON VW_AUDITORIA_SOLICITUDES_HIST TO RO_AUDITORIA_TRAMITES_WEB;


-- 4. VISTA 3: PADRÓN Y AUDITORÍA DE CUENTAS DE USUARIOS
CREATE OR REPLACE VIEW VW_AUDITORIA_USUARIOS_WEB AS
SELECT 
    u.usu_id                        AS usuario_id,
    u.usu_nombre                    AS nombre,
    u.usu_apellido                  AS apellido,
    u.usu_tipo_doc                  AS tipo_documento,
    u.usu_documento                 AS numero_documento,
    u.usu_cuit                      AS cuit,
    u.usu_email                     AS correo_actual,
    u.usu_fecha_alta                AS fecha_creacion_cuenta,
    u.usu_estado                    AS estado_cuenta,
    u.usu_ultimo_login              AS fecha_ultimo_acceso,
    u.usu_ip_ultimo_login           AS ip_ultimo_acceso
FROM xxww_usuarios u;

GRANT SELECT ON VW_AUDITORIA_USUARIOS_WEB TO RO_AUDITORIA_TRAMITES_WEB;


-- 5. VISTA 4: HISTORIAL DE TELÉFONOS Y CORREOS (JOURNAL DE MODIFICACIONES)
CREATE OR REPLACE VIEW VW_AUDITORIA_CONTACTOS_HIST AS
SELECT 
    j.usu_id                        AS usuario_id,
    'TELEFONO'                      AS tipo_contacto,
    j.valor_anterior                AS contacto_anterior,
    j.valor_nuevo                   AS contacto_nuevo,
    j.fecha_modificacion            AS fecha_cambio,
    j.usuario_modificador           AS usuario_origen,
    j.canal_modificacion            AS canal_origen
FROM xxww_usuarios_telefonos_jn j
UNION ALL
SELECT 
    m.usu_id                        AS usuario_id,
    'EMAIL'                         AS tipo_contacto,
    m.email_anterior                AS contacto_anterior,
    m.email_nuevo                   AS contacto_nuevo,
    m.fecha_modificacion            AS fecha_cambio,
    m.usuario_modificador           AS usuario_origen,
    m.canal_modificacion            AS canal_origen
FROM xxww_usuarios_email_jn m;

GRANT SELECT ON VW_AUDITORIA_CONTACTOS_HIST TO RO_AUDITORIA_TRAMITES_WEB;


-- 6. VISTA 5: METADATOS DE ADJUNTOS CON HASH SHA-256 (SIN BINARIOS / SIN BLOBs)
-- Ejemplo de función de hash en servidor:
-- LOWER(RAWTOHEX(DBMS_CRYPTO.HASH(adj.archivo_blob, 3))) -- 3 = HASH_SH256 en DBMS_CRYPTO
CREATE OR REPLACE VIEW VW_AUDITORIA_ADJUNTOS_METADATA AS
SELECT 
    a.sol_id                        AS solicitud_id,
    a.adjunto_id                    AS adjunto_id,
    a.casillero_id                  AS casillero_codigo,
    c.descripcion                   AS casillero_descripcion,
    a.nombre_archivo                AS nombre_archivo_original,
    a.tamano_bytes                  AS tamano_archivo_bytes,
    a.fecha_carga                   AS fecha_upload,
    -- Huella SHA-256 pre-calculada en la tabla o generada por trigger en ingesta:
    a.sha256_hash                   AS huella_digital_sha256
FROM xxww_solicitudes_adjuntos a
LEFT JOIN xxww_casilleros_documentales c ON a.casillero_id = c.casillero_id;

GRANT SELECT ON VW_AUDITORIA_ADJUNTOS_METADATA TO RO_AUDITORIA_TRAMITES_WEB;


-- 7. VISTA 6: REPRESENTACIONES LEGALES Y APODERAMIENTOS
CREATE OR REPLACE VIEW VW_AUDITORIA_REPRESENTACIONES AS
SELECT 
    r.representacion_id             AS representacion_id,
    r.usu_id_titular                AS usuario_titular_id,
    r.usu_id_representante          AS usuario_representante_id,
    r.tipo_poder                    AS tipo_representacion, -- 'LEGAL', 'COMERCIAL', 'CONSORCIO'
    r.sol_id_tramite_origen         AS solicitud_tramite_origen,
    r.fecha_inicio                  AS vigencia_desde,
    r.fecha_fin                     AS vigencia_hasta,
    r.estado                        AS estado_vigencia
FROM xxww_representaciones r;

GRANT SELECT ON VW_AUDITORIA_REPRESENTACIONES TO RO_AUDITORIA_TRAMITES_WEB;
