---
title: "Memorándum: Solicitud de Accesos a Datos de Oficina Virtual y SIGEC para Resolución de Trámites Comerciales"
tags:
  - #epec
  - #gtic
  - #memo
  - #tramites-comerciales
  - #sigec
  - #oficina-virtual
fecha: 2026-10-20
emisor: "Área de Análisis y Control de Trámites Comerciales"
destinatario: "Gerencia de Tecnologías de la Información y Comunicaciones (GTIC)"
estado: Definitivo_Formal
---

# MEMORÁNDUM

**DE:** Área de Análisis y Control de Trámites Comerciales  
**A:** Gerencia de Tecnologías de la Información y Comunicaciones (GTIC)  
**FECHA:** 20 de Octubre de 2026  
**ASUNTO:** Solicitud de accesos de sólo lectura a datos de Oficina Virtual y SIGEC para optimización en la resolución de trámites comerciales  

---

Por medio del presente, se solicita la habilitación de accesos de **sólo lectura (`SELECT`)** a tablas, vistas o réplicas de datos asociadas a la plataforma de **Oficina Virtual (canal web)** y su articulación con **SIGEC**, con el propósito de optimizar la gestión, trazabilidad y resolución de trámites comerciales.

A tal efecto, se detallan a continuación los 8 bloques de información requeridos:

1. **Solicitudes (`xxww_solicitudes_new` o vista equivalente):**  
   Número de solicitud, fecha de alta, tipo de trámite, estado actual, cuenta de usuario que la cargó, suministro y contrato asociados, oficina comercial asignada; junto con el historial de cambios de estado (fecha, usuario que tomó el trámite, usuario que aprobó o rechazó, y texto de la observación o motivo de rechazo).

2. **Cuentas de Usuario (`xxww_usuarios`):**  
   Identificador de cuenta, nombre, apellido, DNI, correo electrónico, fecha de creación, estado y fecha de último acceso (a fin de vincular y analizar relaciones entre cuentas).

3. **Historial de Teléfonos (`xxww_usuarios_telefonos` y tabla de journal/auditoría):**  
   Número, tipo de línea, fecha de alta y registro histórico de modificaciones (número anterior, número nuevo, fecha del cambio y canal/origen desde donde se realizó).

4. **Historial de Correos Electrónicos:**  
   Auditoría de modificaciones de email con dirección anterior, dirección nueva, fecha del cambio y canal/origen.

5. **Adjuntos (exclusivamente metadatos):**  
   Por cada solicitud: nombre de archivo, casillero (tipo de documento), tamaño en bytes, fecha de carga y, de ser factible su cálculo en el servidor, la huella criptográfica **SHA-256**. *(Nota: No se requiere la transferencia de archivos físicos ni binarios; el hash permite detectar documentos duplicados o reutilizados entre distintas cuentas manteniéndose los archivos en el servidor).*

6. **Representaciones y Apoderamientos:**  
   Identificación de titulares y representantes/apoderados vinculados a cada cuenta o suministro, tipo de representación legal y datos registrados en la Oficina Virtual.

7. **Vínculo Unívoco con SIGEC:**  
   Número de ordenativo comercial (reclamo o conexión) originado por cada solicitud o verificación de conexión, atando sin ambigüedad la gestión web al circuito operativo de SIGEC.

8. **Catálogos Maestros:**  
   Tablas de referencia de tipos de solicitud, estados y casilleros de documentación, requeridas para la correcta decodificación de códigos operacionales.

---

**Condiciones del Acceso:**
* **Perfil:** Estricto permiso de consulta (`SELECT`).
* **Usuario solicitante:** `JIDIAZ` (o cuenta técnica que GTIC determine).
* **Modalidad:** Vistas directas, rol dedicado o esquema de consulta sin afectación al entorno transaccional.

Sin otro particular, agradecemos desde ya su colaboración y quedamos a disposición ante cualquier consulta técnica.

---
**Firma:** _______________________________________  
*Área de Análisis y Control de Trámites Comerciales*
