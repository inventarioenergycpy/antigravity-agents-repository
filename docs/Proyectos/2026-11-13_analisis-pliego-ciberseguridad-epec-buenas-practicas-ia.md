---
title: "Análisis del Pliego LPE SIC Nº 21725 de EPEC y Buenas Prácticas para el Uso de IA en el Entorno Laboral"
tags:
  - #ciberseguridad
  - #epec
  - #fortinet
  - #nist-csf
  - #inteligencia-artificial
  - #buenas-practicas
  - #politica-ia
  - #licitacion-publica
created: 2026-11-13
autor: "Javier Ignacio Diaz - Asesor en Ciberseguridad & Gestión de Activos Críticos"
fuente_documento: "LPE SIC 21725 - Servicio de soporte y consultoria plataforma de seguridad - ciberseguridad.pdf"
---

# 🛡️ Análisis del Pliego LPE SIC Nº 21725 de EPEC y Buenas Prácticas para el Uso de IA en el Entorno Laboral

## 1. Contexto y Radiografía del Pliego LPE SIC Nº 21725
- **Entidad Convocante**: Empresa Provincial de Energía de Córdoba S.A.U. (EPEC) - Gerencia de Tecnología de la Información y Comunicaciones (GTIC).
- **Procedimiento**: Licitación Pública Electrónica (LPE) SIC Nº 21725.
- **Objeto**: *“Servicio de Soporte y Consultoría Plataforma de Seguridad - Ciberseguridad”*.
- **Volumen de Horas**: 4.800 horas profesionales ejecutables en 12 meses (esquema mixto presencial/remoto, 8x5 y guardia 24x7 para eventos críticos).
- **Marco Metodológico**: Framework de Ciberseguridad del NIST (*National Institute of Standards and Technology* - EE.UU.).
- **Plataforma Tecnológica**: Ecosistema **Fortinet** (FortiGate, FortiAnalyzer, FortiManager, FortiClient, FortiMail, FortiSIEM/EDR).

---

## 2. Cláusulas Contractuales Críticas frente al uso de Tecnologías y Datos

### Artículo 8 del PET (Confidencialidad Taxativa):
> *"Toda la información técnica, económica, comercial, financiera, etc. de titularidad y/o manejada por EPEC... tendrá el carácter de **CONFIDENCIAL**, no pudiendo el Contratista ni ningún miembro de su empresa, difundirla, total ni parcialmente... De igual manera, **no podrá el Contratista, ni sus integrantes; replicar, extraer, difundir, ni de ninguna manera filtrar, ni revelar datos y/o información existente en hardware, software, aplicaciones y bases de datos de EPEC... ni utilizarla en beneficio propio ni extraer copias en ningún soporte.**"*

### Artículo VII del PET (Herramientas Corporativas):
> *"Disponer de herramientas de acceso remoto para la asistencia o ejecución de tareas remotas cuando así se lo requiera. **Las mismas deberán ser corporativas provistas por la EPEC o en coordinación con ésta.**"*

---

## 3. Matriz de Riesgos del Uso de IA en el Entorno Laboral de EPEC

1. **Fuga de Topología de Red y Configuración**: Pegar en una IA pública scripts o configuraciones de FortiGate (`show full-configuration`), exponiendo el perímetro de defensa de una infraestructura crítica de energía eléctrica.
2. **Filtración de Datos Personales / Comerciales**: Cargar bases de datos de clientes, deudas o subsidios de Tarifa Social (violación de la Ley Nacional 25.326 y Art. 8 PET).
3. **Exposición de Secretos y Credenciales**: Enviar logs que contienen API Keys, tokens de sesión o contraseñas.
4. **Shadow AI en Endpoints**: Empleo de extensiones de navegador con IA o software no homologado en notebooks conectadas vía VPN.
5. **Código Inseguro o Alucinado**: Generación de scripts automáticos con dependencias inexistentes o vulnerabilidades (Package Hallucination / Typosquatting) sin pasar por análisis estático de código (SAST).

---

## 4. Guía de Buenas Prácticas para el Uso de IA en el Entorno Laboral (Alineada al NIST CSF 2.0 y NIST AI RMF 1.0)

### A. GOBERNAR (Govern)
- **Emitir una Política Corporativa de Uso Aceptable de IA (IA-AUP)** aprobada por la GTIC.
- **Prohibición estricta de Shadow AI** y cuentas públicas gratuitas que se reentrenen con datos del usuario.
- **Catálogo Oficial de Herramientas Homologadas** con acuerdos contractuales de privacidad empresarial (*Zero Data Retention* y *No Model Training*).
- **Declaración Jurada para Consultores**: Los adjudicatarios del pliego deben declarar formalmente qué asistentes de IA utilizan en la ejecución de las 4.800 horas.

### B. IDENTIFICAR (Identify) — Semáforo de Prompts
- 🟢 **VERDE (Permitido)**: Consultas conceptuales de normas públicas, estructura genérica de documentos o sintaxis estándar de código (Python, SQL genérico).
- 🟡 **AMARILLO (Requiere Sanitización Previa)**: Fragmentos de código donde se hayan sustituido IPs, servidores y variables por marcadores ficticios; logs anonimizados con rangos RFC 5737.
- 🔴 **ROJO (PROHIBIDO)**: Configuraciones de Fortinet, IPs internas, credenciales, datos de usuarios de EPEC, esquemas unifilares de Subestaciones (SET) y contratos confidenciales.

### C. PROTEGER (Protect)
- **DLP en FortiGate**: Configurar reglas de Data Loss Prevention para bloquear la salida de patrones de CUIL/CUIT, tarjetas de crédito y comandos como `show full-configuration` o `private_key` hacia servicios de IA generativa.
- **Filtrado Web / CASB en FortiClient**: Bloquear herramientas de IA no homologadas en terminales corporativas y túneles VPN.
- **Inspección SAST/DAST**: Todo código o script asistido por IA debe ser auditado con escáneres estáticos y revisión por pares antes de ejecutarse en producción.

### D. DETECTAR (Detect)
- **Monitoreo en FortiAnalyzer y FortiSIEM**: Detectar transferencias de datos anormalmente altas o continuas hacia endpoints de IA generativa.
- **Detección de Extensiones Maliciosas**: Auditar complementos de navegador en endpoints mediante FortiClient / EDR.
- **Filtrado de Spear Phishing asistido por IA**: Reforzar los motores heurísticos de FortiMail contra ataques de ingeniería social generados por IA.

### E. RESPONDER Y RECUPERAR (Respond & Recover)
- **Playbook de Incidentes por Fuga en IA**: Protocolo inmediato de aislamiento del endpoint, revocación y rotación urgente de credenciales expuestas y solicitud de purga de logs al proveedor de IA.
- **Capacitación Continua**: Incluir módulos prácticos de concientización sobre uso seguro de IA en el plan de formación anual de la GTIC.
