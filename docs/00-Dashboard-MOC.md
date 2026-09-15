---
title: "Dashboard MOC - Repositorio de Agentes Antigravity IDE"
tags:
  - #moc
  - #dashboard
  - #antigravity
  - #obsidian
  - #backups
  - #rollback
created: 2026-08-09
updated: 2026-09-03
---

# ðŸ§­ BÃ³veda de Agentes Antigravity IDE - Map of Content (MOC)

Bienvenido a la BÃ³veda de Obsidian para la gestiÃ³n estructurada de agentes con habilidades avanzadas, **soporte para nuevos perfiles futuros**, **historial de evoluciones** y **sistema de resguardo/rollback preventivo**.

---

## ðŸ“Œ Datos del Entorno
- **Cuenta GitHub**: `inventarioenergycpy`
- **Correo ElectrÃ³nico**: `inventario.energycpy@gmail.com`
- **Modo de AutenticaciÃ³n**: Inicio directo con Google OAuth.
- **Protocolo de Desarrollo**: **MetodologÃ­a Estandarizada en 6 Etapas** aplicada al 100% de las habilidades (`InvestigaciÃ³n en Fuentes Confiables -> DiseÃ±o & Tesis -> Pruebas Parciales -> Prueba Piloto con AprobaciÃ³n -> Pruebas Finales -> Auto-DocumentaciÃ³n & BÃ³veda Obsidian`).

---

## ðŸ—ï¸ Arquitectura del Sistema de Agentes y Repositorios Dedicados

```mermaid
graph TD
    Hub["antigravity-agents-repository (Hub BÃ³veda Central)"] --> MOC["00-Dashboard-MOC"]
    
    MOC --> AF["01-Analista-Financiero"]
    MOC --> CD["02-Ciencia-de-Datos"]
    MOC --> DW["03-Desarrollador-Web-Showroom"]
    MOC --> PA["04-Planificador-de-Agentes"]
    MOC --> LF["05-Asesor-Legal-Financiero"]
    MOC --> ASE["06-Arquitecto-Sistemas-EPEC"]
    MOC --> NA["Nuevos Agentes Futuros"]
    
    MOC --> AutoDoc["Auto-DocumentaciÃ³n"]
    AutoDoc --> Backup["BÃ³veda de Backups (docs/Backups/)"]
    AutoDoc --> Historial["HistÃ³rico de Mejoras (docs/Historial-Mejoras/)"]
    
    MOC --> ProyectosHub["Proyectos Independientes (docs/Proyectos/)"]
    ProyectosHub --> RepoWeb["Repo Web: inventarioenergycpy/showroom-energycpy"]
    ProyectosHub --> RepoData["Repo Data: inventarioenergycpy/protelem-..."]
    ProyectosHub --> RepoDash["Repo Finanzas: inventarioenergycpy/dashboard-..."]
    ProyectosHub --> RepoForwarded["Repo VPU: inventarioenergycpy/forwarded-message"]
    ProyectosHub --> RepoCIER["Repo CIER: inventarioenergycpy/encuesta-cier-epec"]
    
    MOC --> SyncProtelem["Protocolo SincronizaciÃ³n Red PROTELEM (\\srvfs01\...)"]
    
    Backup --> Rollback["Habilidad Rollback-Agente"]
```

---

## ðŸ“‚ Ãreas de la BÃ³veda Obsidian

### 1. [[Agentes/01-Analista-Financiero|Analista Financiero & Modelador EconÃ³mico]]
- **Entregables**: Google Drive (`inventario.energycpy@gmail.com`) / Repositorios Financieros Dedicados / Memorias de CÃ¡lculo & Doble Estructura Documental.

### 2. [[Agentes/02-Ciencia-de-Datos|Ciencia de Datos (PySpark, Python, SQL, Power BI TMDL & Reglas BI EPEC)]]
- **Entregables**: Descargas / Repositorios de Datos / Motor Text-to-SQL / Diccionario 505 QVDs Qlik Sense / Reglas BI Normativa EPEC.

### 3. [[Agentes/03-Desarrollador-Web-Showroom|Desarrollador Web Showroom e Informes TÃ©cnicos]]
- **Entregables**: Repositorios Web Dedicados en GitHub (`inventarioenergycpy/<proyecto-web>`) / Sitios EstÃ¡ticos de Reportes HTML.

### 4. [[Agentes/04-Planificador-Disenador-de-Agentes|Planificador y DiseÃ±ador de Agentes AI]]
- **Entregables**: InvestigaciÃ³n verÃ­dica, diseÃ±o pre-implementaciÃ³n, roadmap de pruebas parciales, pruebas piloto y auto-documentaciÃ³n de nuevos agentes.

### 5. [[Agentes/05-Asesor-Legal-Financiero|Asesor Legal en IntermediaciÃ³n Financiera y RegulaciÃ³n EnergÃ©tica]]
- **Entregables**: Estrategia documental en 3 capas, NCNDA, corretaje con overprice, mandatos, fee sharing, Reglamento EPEC en Google Drive (`inventario.energycpy@gmail.com`).

### 6. [[Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto de Sistemas EPEC (CIS / MDM / Licitaciones)]]
- **Entregables**: Arquitectura de Sistemas Comerciales, seguimiento de pliegos licitatorios (929 requerimientos en 35 grupos), benchmarking de proveedores (Oracle C2M/CCS, OPEN, PRETECO/ESC) en BÃ³veda Central y repositorios dedicados.

### 7. [[Protocolo-Sincronizacion-Red-PROTELEM|Protocolo Operativo de SincronizaciÃ³n Red PROTELEM (\\srvfs01\...)]]
- **Habilidad**: `.agents/skills/sincronizacion-red-protelem/SKILL.md`
- **PropÃ³sito**: Sincronizar automÃ¡ticamente cualquier nueva documentaciÃ³n o proyecto guardado en la red `\\srvfs01\ProyectoTelemedicion\DocumentaciÃ³n\PROTELEM\PROJECTS` hacia la BÃ³veda Central con backups preventivos `.bak` y sin pÃ©rdida de informaciÃ³n.

### 8. [[Proyectos/README|Ãndice de Proyectos e Repositorios Dedicados]]
- Fichas tÃ©cnicas, enlaces a repositorios remotos y URLs live de cada proyecto desarrollado por los agentes.

---

## ðŸ›¡ï¸ Sistema de Seguridad, HistÃ³rico y Rollback

1. **CreaciÃ³n de Nuevos Agentes Futuros**:
   - Para agregar un agente en el futuro, crear `.agents/skills/<nuevo-agente>/SKILL.md` y su ficha en `docs/Agentes/`.
2. **Backups Preventivos**:
   - Cada mejora genera automÃ¡ticamente una copia de respaldo en `[[docs/Backups/README|docs/Backups/]]`.
3. **Registro HistÃ³rico**:
   - Cada cambio queda registrado cronolÃ³gicamente en `docs/Historial-Mejoras/`.
4. **Capacidad de Rollback / ReversiÃ³n**:
   - Si un cambio no resulta satisfactorio, la habilidad `rollback-agente` restaura cualquier versiÃ³n anterior almacenada en `docs/Backups/`.

---

## ðŸ“œ Historial de Mejoras Continuas
- [[Historial-Mejoras/00-Registro-Inicial|00-Registro Inicial de Arquitectura]]
- [[Historial-Mejoras/2026-08-12_desarrollador-web-showroom_maquetacion-energy-cpy|2026-08-12 Desarrollador Web Showroom - MaquetaciÃ³n Benchmark Energy CPY]]
- [[Historial-Mejoras/2026-08-12_desarrollador-web-showroom_buenas-practicas-github|2026-08-12 Desarrollador Web Showroom - IntegraciÃ³n de Buenas PrÃ¡cticas Oficiales de GitHub]]
- [[Historial-Mejoras/2026-08-14_protocolo-multi-repositorio-proyectos|2026-08-14 RedefiniciÃ³n BÃ³veda Central de Agentes 100% y Protocolo Multi-Repositorio por Proyecto]]
- [[Historial-Mejoras/2026-08-14_registro-agente-planificador|2026-08-14 CreaciÃ³n e IntegraciÃ³n del Agente Planificador y DiseÃ±ador de Agentes AI]]
- [[Historial-Mejoras/2026-08-14_estandarizacion-estricta-protocolo-6-etapas|2026-08-14 EstandarizaciÃ³n Secuencial del Protocolo de 6 Etapas en todas las Skills]]
- [[Historial-Mejoras/2026-08-20_ciencia-de-datos_ingenieria-inversa-pbip-tmdl|2026-08-20 Ciencia de Datos - IntegraciÃ³n de Estrategias de IngenierÃ­a Inversa y DocumentaciÃ³n TMDL / PBIP]]
- [[Historial-Mejoras/2026-08-21_registro-agente-legal-financiero|2026-08-21 Asesor Legal en IntermediaciÃ³n Financiera - IntegraciÃ³n de Estrategia Documental en 3 Capas y Marco CCCN/ICC]]
- [[Historial-Mejoras/2026-08-23_desarrollo-dashboard-gestion-intermediacion|2026-08-23 Desarrollo y Despliegue del Dashboard de GestiÃ³n e IntermediaciÃ³n Financiera con Matriz Legal en 3 Capas]]
- [[Historial-Mejoras/2026-08-27_dashboard_importador-excel-dinamico-diff-rollback|2026-08-27 Plantillas Excel DinÃ¡micas Adaptables, Motor de Diff Visual, Cargas Parciales y Rollback]]
- [[Historial-Mejoras/2026-08-28_desarrollador-web-showroom_mejoras-estrategicas-showroom|2026-08-28 Desarrollador Web Showroom - Selector BilingÃ¼e, Filtros Desde-Hasta, Ruteo Silencioso y GestiÃ³n de Estados]]
- [[Historial-Mejoras/2026-09-02_protelem_integracion-conocimiento-y-nuevo-agente-arquitecto|2026-09-02 IntegraciÃ³n de Conocimiento Red PROTELEM y CreaciÃ³n del Agente 6: Arquitecto de Sistemas EPEC]]
- [[Historial-Mejoras/2026-09-03_forwarded-message_integracion-escritura-83-y-vpu-fideicomiso|2026-09-03 Proyecto Forwarded Message - IntegraciÃ³n Notarial Escritura NÂº 83 y VPU Fideicomiso]]
- [[Historial-Mejoras/2026-09-08_forwarded-message_presentacion-google-slides|2026-09-08 Proyecto Forwarded Message - GeneraciÃ³n de PresentaciÃ³n Ejecutiva Google Slides para Google Drive]]
- [[Historial-Mejoras/2026-09-03_analista-financiero_regla-replicabilidad-doble-estructura-fehaciente|2026-09-03 Analista Financiero - Regla Elemental de Replicabilidad, Doble Estructura Documental y Memorias de CÃ¡lculo]]
- [[Configuracion-Credenciales-GitHub|ConfiguraciÃ³n y Resguardo de Credenciales GitHub PAT]]

---

## ðŸš€ Proyectos y Soluciones en Repositorios Dedicados
- [[Proyectos/2026-08-14_showroom-energycpy|2026-08-14 Showroom Energy CPY (Web Showroom Benchmark)]]
- [[Proyectos/2026-08-20_protelem-indicadores-gerencia-comercial|2026-08-20 PROTELEM - Indicadores Gerencia Comercial (DocumentaciÃ³n & Arquitectura SemÃ¡ntica)]]
- [[Proyectos/2026-08-23_dashboard-gestion-intermediacion|2026-08-23 Dashboard de GestiÃ³n e IntermediaciÃ³n Financiera con Matriz Legal en 3 Capas]]
- [[Proyectos/2026-09-02_forwarded-message|2026-09-02 Proyecto Forwarded Message (Green Hydrogen, Solar Hub & Granja MarÃ­tima Abisal - VPU Fideicomiso)]]
- [[Proyectos/2026-09-02_protelem-conocimiento-integrado|2026-09-02 Compendio Integrado de Conocimiento Red PROTELEM (5 Proyectos EPEC)]]
- 2026-09-04 | [[docs/Historial-Mejoras/2026-09-04_ciencia-de-datos_historial-fallas-y-soluciones-tmdl-pbip|Ciencia de Datos - Historial de Fallas y Soluciones TMDL / PBIP]]
- 2026-09-06 | [[docs/Historial-Mejoras/2026-09-06_ciencia-de-datos_resolucion-fallas-pbip-json-schema-y-artefactos|Ciencia de Datos - ResoluciÃ³n de Fallas PBIP JSON Schema y Artefactos (Power BI Release 2026)]]
- [[Historial-Mejoras/2026-09-11_ciencia-de-datos_integracion-conexion-oracle-oracledb-thick|2026-09-11 Ciencia de Datos - Integración de Protocolo de Conexión Oracle (oracledb Modo Thick 64-bit)]]
- [[Historial-Mejoras/2026-09-13_analista-financiero_reorganizacion-partes-y-comision-contrato-besana|2026-09-13 Analista Financiero - Reorganización de Partes y Comisión 50/50 en Contrato de Corretaje BESANA - ERV]]


