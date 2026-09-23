---
title: "Registro de Mejora: Integración de Protocolo de Conexión Oracle (oracledb Modo Thick 64-bit)"
tags:
  - #historial-mejoras
  - #ciencia-de-datos
  - #oracle
  - #oracledb
  - #seguridad
fecha: 2026-09-11
agente_responsable: ciencia-de-datos
backup_referencia: "[[docs/Backups/2026-09-11_153100_ciencia-de-datos_SKILL.md.bak]]"
---

# Registro de Mejora: Integración de Protocolo de Conexión Oracle (oracledb Modo Thick 64-bit)

- **Fecha**: 2026-09-11
- **Agente Afectado**: `ciencia-de-datos`
- **Archivo de Backup Preventivo**: `docs/Backups/2026-09-11_153100_ciencia-de-datos_SKILL.md.bak`

---

## 1. Contexto y Justificación
Se requería estandarizar la conexión directa a la base de datos Oracle empresarial (`PRODEBS_SEE` / `epec2-scan2.epec.net`) utilizando la información validada en `conexion_oracle_referencia.md`. Durante la fase de investigación y pruebas piloto sobre el entorno local, se constató que:
1. El modo Thin de `python-oracledb` falla con `DPY-3015` debido al tipo de verifier de contraseñas (`0x939`) de la base de datos.
2. Es obligatorio utilizar el **Modo Thick** inicializando el cliente Oracle 19c local de 64 bits (`C:\app\client\product\19.0.0\client_2\bin`).
3. Para prevenir bloqueos o modificaciones accidentales en bases de producción, se requiere implementar un Context Manager de solo lectura (`OracleReadOnly`) con `SET TRANSACTION READ ONLY`.

---

## 2. Cambios Implementados

1. **Incorporación del Protocolo en `SKILL.md`**:
   - Se añadió la capacidad de conexión y consulta a bases de datos Oracle con `oracledb`.
   - Se documentó el esquema requerido en `.env` y el parámetro `OR_INSTANT_CLIENT`.
   - Se estableció la regla de uso del Context Manager `OracleReadOnly`.

2. **Copia de Documentación de Referencia**:
   - Se integró la guía completa en [`docs/PROTELEM/PROJECTS/sigec-explorer/Conexion-Oracle-Referencia.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/PROTELEM/PROJECTS/sigec-explorer/Conexion-Oracle-Referencia.md).

3. **Actualización de la Ficha Técnica**:
   - Se actualizó `docs/Agentes/02-Ciencia-de-Datos.md` con las nuevas tecnologías y referencias.

---

## 3. Pruebas y Validación Realizadas
- **Prueba Piloto Ejecutada**: Consulta `SELECT * FROM DUAL` ejecutada mediante Python 3.12 y `oracledb` en modo Thick apuntando a `C:\app\client\product\19.0.0\client_2\bin`.
- **Resultado Obtenido**:
  ```text
    DUMMY
  0     X
  ```
- **Validación de Solo Lectura**: Transacciones DML restringidas a nivel de sesión.

---

## 4. Referencias Cruzadas
- [[00-Dashboard-MOC]]
- [[docs/Agentes/02-Ciencia-de-Datos|Ficha Técnica: Ciencia de Datos]]
- [[docs/PROTELEM/PROJECTS/sigec-explorer/Conexion-Oracle-Referencia|Guía de Conexión Oracle]]
