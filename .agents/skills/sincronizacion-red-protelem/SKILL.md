---
name: sincronizacion-red-protelem
description: Protocolo automatizado para escanear, analizar e integrar dinámicamente nuevas actualizaciones o proyectos guardados en la carpeta de red \\srvfs01\ProyectoTelemedicion\Documentación\PROTELEM\PROJECTS dentro de antigravity-agents-repository, generando backups preventivos .bak y enriqueciendo las habilidades de los agentes sin perder información.
---

# Habilidad: Protocolo de Sincronización Dinámica Red PROTELEM (`sincronizacion-red-protelem`)

Esta habilidad define el **protocolo operativo estandarizado** para actualizar el conocimiento y las habilidades del ecosistema de agentes cada vez que se agreguen o modifiquen proyectos en la carpeta de red:
`\\srvfs01\ProyectoTelemedicion\Documentación\PROTELEM\PROJECTS`

---

## 🔄 Flujo de Ejecución del Protocolo

```mermaid
graph TD
    Trigger["Solicitud de Sincronización / Actualización Red PROTELEM"] --> Step1["1. Escaneo de Red (\\srvfs01\...\PROJECTS)"]
    Step1 --> Step2["2. Análisis de Novedades y Clasificación de Dominio"]
    
    Step2 --> CheckCompat{"¿Es compatible con los Agentes 1 a 6?"}
    
    CheckCompat -- Sí --> Step3["3. Backup Preventivo (.bak en docs/Backups/)"]
    CheckCompat -- No --> Consult["❓ Consultar al Usuario:\nOpción A: Crear Nuevo Agente / Repo\nOpción B: Reasignar a Agente Existente"]
    Consult --> Step3

    Step3 --> Step4["4. Actualización Incremental de SKILL.md"]
    Step4 --> Step5["5. Auto-Documentación en Bóveda Obsidian"]
    Step5 --> Step6["6. Commit y Push a GitHub (antigravity-agents-repository)"]
```

---

## 📋 Pasos Detallados del Protocolo

### 1. Escaneo de Red e Identificación de Novedades
- Ejecutar lectura recursiva sobre `\\srvfs01\ProyectoTelemedicion\Documentación\PROTELEM\PROJECTS`.
- Comparar los archivos, timestamps y proyectos detectados contra la ficha compendio `docs/Proyectos/2026-09-02_protelem-conocimiento-integrado.md` e índices previos.
- Identificar carpetas o notas creadas, modificadas o ampliadas por el equipo.

### 2. Clasificación de Dominio por Agente Especialista
Mapear cada novedad identificada según el perfil del agente correspondiente:
- **`ciencia-de-datos`**: Tablas Oracle `XXSIGEC`, reglas de negocio para reportes BI (`normativa-epec`), archivos QVD Qlik Sense, motores Text-to-SQL, ETLs y pipelines de datos.
- **`asesor-legal-financiero`**: Modificaciones al Reglamento de Comercialización EPEC, régimen legal de ilícitos, recupero de energía, contratos de servicios públicos y servidumbres.
- **`desarrollador-web-showroom`**: Nuevas convenciones de publicación de reportes técnicos HTML estáticos, visualización web de informes o tableros estáticos.
- **`arquitecto-sistemas-epec`**: Nuevos pliegos, anexos, 929 requerimientos CIS/MDM/WFM/CRM, evaluación de proveedores (Oracle C2M/CCS, OPEN, PRETECO/ESC) o arquitectura empresarial.
- **`analista-financiero`**: Evaluaciones económico-financieras de tarifas, modelos de costos o flujo de fondos de proyectos EPEC.

> [!CAUTION]
> **Regla de Compatibilidad y Consulta**:
> Si se descubre un nuevo proyecto o cuerpo documental en la red que **NO sea compatible** con los agentes 1 a 6 creados, **DETENER** la actualización e interrogar al usuario para elegir entre:
> - *Opción A*: Crear un nuevo perfil de agente (`.agents/skills/<nuevo-agente>/SKILL.md`) y/o repositorio dedicado.
> - *Opción B*: Autorizar la asignación del nuevo tema a un agente existente.

### 3. Generación de Backups Preventivos (`docs/Backups/`)
- **REGLA OBLIGATORIA**: Antes de aplicar cualquier cambio en un archivo `.agents/skills/<agente>/SKILL.md`, crear una copia de respaldo en:
  `docs/Backups/YYYY-MM-DD_HHmmss_<nombre-agente>_SKILL.md.bak`

### 4. Enriquecimiento Incremental de Habilidades
- Editar `.agents/skills/<agente>/SKILL.md` incorporando los nuevos conocimientos, patrones o reglas descubiertos.
- Garantizar que la modificación sea **incremental y aditiva**, preservando el 100% del conocimiento documentado previamente.
- Mantener intacta la estructura obligatoria de **Metodología en 6 Etapas**.

### 5. Auto-Documentación en Bóveda Obsidian
- Actualizar o crear la nota correspondiente en `docs/Proyectos/`.
- Registrar la entrada histórica en `docs/Historial-Mejoras/YYYY-MM-DD_protelem_sincronizacion_<tema>.md`.
- Actualizar los diagramas relacionales y enlaces en `docs/00-Dashboard-MOC.md`.

### 6. Sincronización Remota en GitHub
- Ejecutar en `D:\Proyectos\antigravity-agents-repository`:
  `git add .`
  `git commit -m "docs(protelem): sincronizacion automatica de conocimiento red srvfs01 - <descripcion>"`
  `git push origin master`
