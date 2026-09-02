---
title: "Protocolo Operativo: Sincronización Dinámica y Copia Física de Archivos desde la Red PROTELEM"
tags:
  - #protocolo
  - #protelem
  - #sincronizacion
  - #copia-fisica
  - #backups
  - #obsidian
created: 2026-09-02
updated: 2026-09-02
---

# 🔄 Protocolo Operativo: Sincronización Dinámica y Copia Física Red PROTELEM (`\\srvfs01\...`)

Este protocolo establece la guía paso a paso para copiar físicamente la totalidad de los archivos y mantener sincronizada la Bóveda Central de Agentes **`antigravity-agents-repository`** con el corpus documental de la carpeta de red:
`\\srvfs01\ProyectoTelemedicion\Documentación\PROTELEM\PROJECTS`

---

## 📌 Principios Fundamentales

1. **Copia Física del 100% de los Archivos**: Ninguna actualización o reestructuración omitirá archivos. Todos los documentos `.md`, `.json` y configuraciones se copian físicamente a `docs/PROTELEM/PROJECTS/`.
2. **Preservación Total Sin Pérdida de Información**: El conocimiento documentado por el equipo se almacena réplica exacta dentro de la Bóveda Central.
3. **Seguridad y Backups Preventivos (`.bak`)**: Toda modificación de habilidades (`.agents/skills/`) requiere un respaldo previo en `docs/Backups/`.
4. **Clasificación Inteligente por Dominio**: Los contenidos se distribuyen entre los Agentes Especialistas (Analista Financiero, Ciencia de Datos, Desarrollador Web, Planificador, Asesor Legal, Arquitecto de Sistemas EPEC).
5. **Consulta Obligatoria ante Incompatibilidades**: Si se detecta un proyecto o tema que no encaja en los perfiles vigentes, se solicita autorización al usuario para crear un nuevo agente/repositorio o reasignarlo.

---

## 🛠️ Comandos y Pasos de Ejecución

### Paso 1: Copia Física Integral de Archivos
```powershell
$src = '\\srvfs01\ProyectoTelemedicion\Documentación\PROTELEM\PROJECTS'
$dest = 'D:\Proyectos\antigravity-agents-repository\docs\PROTELEM\PROJECTS'
if (!(Test-Path $dest)) { New-Item -ItemType Directory -Path $dest -Force }
Copy-Item -Path "$src\*" -Destination $dest -Recurse -Force
```

### Paso 2: Backup Preventivo de Habilidades
```powershell
$timestamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
Copy-Item ".agents/skills/<agente>/SKILL.md" "docs/Backups/$($timestamp)_<agente>_SKILL.md.bak"
```

### Paso 3: Auto-Documentación y Git Push
```powershell
git add .
git commit -m "docs(protelem): copia fisica e integracion dinamica de conocimiento red srvfs01"
git push origin master
```

---

## 🔗 Referencias
- [[00-Dashboard-MOC]]
- [[Proyectos/2026-09-02_protelem-conocimiento-integrado|Compendio Integrado de Conocimiento PROTELEM]]
