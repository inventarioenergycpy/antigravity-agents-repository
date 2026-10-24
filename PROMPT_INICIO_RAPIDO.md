# 📋 Prompt Maestro de Inicio Rápido Dinámico Multi-PC (Antigravity IDE)

> **Instrucciones**: Copie el bloque de texto dentro de la caja de código a continuación y péguelo en el chat de **Antigravity IDE** cada vez que inicie una nueva sesión de trabajo desde cero en cualquier computadora.

```text
Hola Antigravity. Deseo iniciar mi sesión de trabajo desde cero vinculándome a mi repositorio estructurado de agentes.

📌 DATOS DE MI CUENTA Y REPOSITORIO CENTRAL:
- Cuenta de GitHub Principal: inventarioenergycpy
- Organización de Proyectos EPEC: PROTELEM-EPEC (https://github.com/PROTELEM-EPEC) y repositorios satélites en protelemepec-coder
- Email de contacto / Google Drive: inventario.energycpy@gmail.com
- Repositorio GitHub Central: https://github.com/inventarioenergycpy/antigravity-agents-repository.git
- Workspace Local Objetivo: Detectar dinámicamente la ruta activa en el sistema. Puede ubicarse en 'D:\Proyectos\antigravity-agents-repository', en el scratchpad de Gemini ('%USERPROFILE%\.gemini\antigravity-ide\scratch\antigravity-agents-repository'), o enlazado mediante Junctions/Symlinks en cualquier otra partición o disco del sistema (ej. D:\, C:\).

⚙️ PASOS DE INICIALIZACIÓN Y CONFIGURACIÓN AUTOMÁTICA DINÁMICA:

1. Detección y Sincronización Git:
   - Identifica el espacio de trabajo actual o busca la carpeta local 'antigravity-agents-repository' (verificando tanto en 'D:\Proyectos\', en el workspace abierto en el IDE, como en las rutas de '.gemini' o scratchpads en los discos disponibles).
   - Si NO existe localmente en ninguna de las ubicaciones anteriores, clónalo con 'git clone https://github.com/inventarioenergycpy/antigravity-agents-repository.git' en la carpeta de proyectos activa (priorizando el disco D:\ o el workspace actual).
   - Si YA existe, navega a su directorio y ejecuta 'git pull origin master' para sincronizar la última versión de agentes, habilidades, backups y notas de Obsidian.

2. Escaneo Dinámico del Repositorio (Auto-Discovery de Agentes y Reglas):
   - Lee las directivas globales en '.agents/AGENTS.md'.
   - Realiza un escaneo completo de la carpeta '.agents/skills/' leyendo el 'SKILL.md' de cada habilidad instalada.
   - Revisa 'docs/Agentes/' y 'docs/00-Dashboard-MOC.md' para identificar todos los perfiles activos (12 agentes especialistas) y protocolos maestros.
   - Revisa el protocolo rector 'docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md' (Squad de 4 agentes con Triple QA).
   - Revisa 'docs/Proyectos/' y 'docs/PROTELEM/00-Indice-PROTELEM-EPEC.md' para reconocer los proyectos desarrollados en repositorios dedicados de 'inventarioenergycpy' y 'PROTELEM-EPEC'.

3. Política de Almacenamiento y Repositorios Dedicados:
   - Repositorio Central (antigravity-agents-repository): 100% exclusivo para documentación, habilidades (.agents/skills/), respaldos (.bak en docs/Backups/) y Bóveda Obsidian (docs/).
   - Flexibilidad de Almacenamiento Local: El entorno '.gemini', extensiones y scratchpads pueden estar reubicados o enlazados entre discos (ej. 'D:\Proyectos\', 'D:\Usuarios\...'). Respeta siempre la unidad y ruta física donde resida el workspace.
   - Google Workspace (Docs, Slides, Sheets): Almacenados en Google Drive de 'inventario.energycpy@gmail.com'.
   - Soluciones y Entregables Locales (Power BI .pbip, scripts Python, SQL): Carpeta de Descargas (%USERPROFILE%\Downloads) o directorio asignado del proyecto.
   - Proyectos Independientes (Web Showrooms, Pipelines de Datos, Apps Financieras, Soluciones EPEC):
     • Repositorios dedicados en GitHub bajo 'inventarioenergycpy/<nombre-proyecto>.git'.
     • Repositorios dedicados en GitHub bajo la organización 'PROTELEM-EPEC/<nombre-proyecto>.git' (ej. 'facturacion-reverse-engineering' y 'demo-dashboard') o en 'protelemepec-coder' (ej. 'adelat-cier-benchmarking', 'sigec-ruta-nueva-catastro-georef', 'asesoramiento-parque-solar-fotovoltaico').
     • Ficha técnica cruzada en 'docs/Proyectos/' o 'docs/PROTELEM/00-Indice-PROTELEM-EPEC.md'.

4. Metodología Obligatoria en 6 Etapas & Protocolo de Triple QA:
   - Toda tarea o desarrollo seguirá estrictamente:
     • Fase 1: Investigación en Fuentes Confiables y Verídicas.
     • Fase 2: Diseño Pre-Implementación & Análisis de Tesis.
     • Fase 3: Diagramación de Etapas & Pruebas Parciales.
     • Fase 4: Presentación de Prueba Piloto (Sujeta a Aprobación del Usuario).
     • Fase 5: Pruebas sobre el Modelo Final Implementado.
     • Fase 6: Auto-Documentación, Backup Preventivo (.bak en docs/Backups/) e Histórico en Obsidian (docs/Historial-Mejoras/).
   - Validación Obligatoria en 3 Instancias de QA (Multi-Perspective QA) antes de entregar cualquier resultado:
     • Instancia 1: QA Técnico & Algorítmico (cero errores runtime, tests deterministas, protocolo snapshot SMB).
     • Instancia 2: QA de Negocio, Dominio & Regulación (conformidad con SIGEC, tarifas EPEC, CCCN, CAMMESA).
     • Instancia 3: QA de Usabilidad, Replicabilidad & UX (diseño de tablas, enlaces funcionales, respaldo verificado).

5. Generación Dinámica del Menú de Trabajo:
   - Construye y preséntame el Menú de Selección interactivo estructurado de forma dinámica, listando:
     a) Squad Ágil Multi-Agente: Opción de activar el equipo de 4 (PM en Gemini 3.8 Flash High + 3 Operadores en Gemini 3.7 Flash High) configurados según el arquetipo del proyecto (A: GIS/Catastro, B: Facturación SIGEC, C: Finanzas/Showroom, D: Académico/MEM).
     b) Todos los Agentes Especialistas descubiertos en '.agents/skills/' (1 al 12: Analista Financiero, Ciencia de Datos & GIS, Desarrollador Web, Planificador AI, Asesor Legal, Arquitecto EPEC, Procesador YouTube, Transcriptor Audiovisual, Profesor MEM, Alumno Auditor, Copiloto Orquestador, Especialista Facturación EPEC).
     c) Las Acciones Operativas del Sistema:
        - [A] Agregar / Actualizar Nuevos Proyectos en Repositorios Dedicados (inventarioenergycpy o PROTELEM-EPEC)
        - [B] Registrar / Guardar Mejoras Confirmadas (Auto-Documentación + Backup Preventivo .bak)
        - [C] Ejecutar Rollback / Reversión a una Versión Anterior desde Backup
        - [D] Crear y Configurar un Nuevo Perfil de Agente Futuro
        - [E] Sincronizar Proyectos y Repositorios PROTELEM-EPEC (Red \\srvfs01 y upstream GitHub)
        - [F] Ver el menú de inicio rápido para actualizar las opciones a mostrar.

Dime cuando la inicialización y el escaneo estén completos y presenta el menú dinámico para que elija con qué agente o acción trabajar.
```
