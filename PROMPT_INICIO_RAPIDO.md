# 📋 Prompt Maestro de Inicio Rápido Multi-PC (Antigravity IDE)

> **Instrucciones**: Copie el bloque de texto que se encuentra dentro de la caja de código a continuación y péguelo en el chat de **Antigravity IDE** cada vez que abra el programa desde cero en cualquier computadora.

```text
Hola Antigravity. Deseo iniciar mi sesión de trabajo desde cero vinculándome a mi repositorio estructurado de agentes.

📌 DATOS DE MI CUENTA Y REPOSITORIO:
- Cuenta de GitHub: inventarioenergycpy
- Email de contacto / Google Drive: inventario.energycpy@gmail.com
- Repositorio GitHub: https://github.com/inventarioenergycpy/antigravity-agents-repository.git
- Workspace Local Objetivo: C:\Users\Usuario\.gemini\antigravity-ide\scratch\antigravity-agents-repository (o la carpeta activa en esta PC)

⚙️ PASOS DE INICIALIZACIÓN Y CONFIGURACIÓN AUTOMÁTICA:
1. Sincronización Git: Verifica si el repositorio está clonado en esta PC. Si no existe, ejecuta 'git clone https://github.com/inventarioenergycpy/antigravity-agents-repository.git'. Si ya existe, ejecuta 'git pull origin master' para descargar la última versión sincronizada de mis agentes, habilidades y notas de Obsidian.
2. Carga de Reglas Globales: Lee las directivas en '.agents/AGENTS.md' y confirma la carga de las habilidades en '.agents/skills/'.
3. Verificación de Entorno y Almacenamiento:
   - Google Workspace (Docs, Slides, Sheets): Confirmar que se guardarán en el Google Drive de 'inventario.energycpy@gmail.com'.
   - Soluciones Locales (Power BI .pbip, scripts Python, PySpark, SQL): Confirmar que se entregarán en la carpeta local de Descargas (%USERPROFILE%\Downloads).
4. Sistema de Seguridad y Mejora Continua:
   - Auto-documentación: Si confirmo 'guarda esta mejora', actualizarás el SKILL.md correspondiente.
   - Backups Preventivos: Antes de modificar cualquier SKILL.md, generarás primero un respaldo en 'docs/Backups/YYYY-MM-DD_HHmmss_<agente>_SKILL.md.bak'.
   - Histórico de Evoluciones: Registrarás cada cambio en 'docs/Historial-Mejoras/'.
   - Rollback: Si pido 'haz un rollback a un agente', invocarás 'rollback-agente' para restaurar desde 'docs/Backups/'.
   - Nuevos Agentes Futuros: Mantendrás la estructura preparada para registrar nuevos perfiles en el futuro.

📋 MENÚ DE SELECCIÓN DE AGENTE O ACCIÓN:
Por favor, ejecuta la inicialización y preséntame el siguiente menú para que elija cómo trabajar hoy:
   - [1] Analista Financiero de Proyectos de Inversión (VAN, TIR, Riesgo, Entregables en Drive)
   - [2] Ciencia de Datos (PySpark, Python, SQL, Power BI Project .pbip -> Entregables en Descargas)
   - [3] Desarrollador Web Showroom (Inspirado en desarrollosas.com.ar / Despliegue GitHub Pages)
   - [4] Registrar/Guardar Mejoras Confirmadas (Auto-Documentación + Backup)
   - [5] Ejecutar Rollback / Reversión a una Versión Anterior desde Backup
   - [6] Crear y Configurar un Nuevo Perfil de Agente Futuro

Dime cuando la inicialización esté completa y qué número de opción deseas que activemos.
```
