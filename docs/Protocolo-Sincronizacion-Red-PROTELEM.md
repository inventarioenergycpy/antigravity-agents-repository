---
title: "Protocolo Operativo: Sincronización Dinámica de Conocimiento desde la Red PROTELEM"
tags:
  - #protocolo
  - #protelem
  - #sincronizacion
  - #backups
  - #obsidian
created: 2026-09-02
updated: 2026-09-02
---

# 🔄 Protocolo Operativo: Sincronización Dinámica Red PROTELEM (`\\srvfs01\...`)

Este protocolo establece la guía paso a paso para que cualquier agente o usuario mantenga sincronizada la Bóveda Central de Agentes **`antigravity-agents-repository`** con el corpus documental de la carpeta de red:
`\\srvfs01\ProyectoTelemedicion\Documentación\PROTELEM\PROJECTS`

---

## 📌 Principios Fundamentales

1. **Preservación 100% Sin Pérdida de Información**: Ninguna actualización o reestructuración eliminará conocimiento documentado previamente por el equipo.
2. **Seguridad y Backups Preventivos (`.bak`)**: Toda modificación de habilidades (`.agents/skills/`) requiere un respaldo previo en `docs/Backups/`.
3. **Clasificación Inteligente por Dominio**: Los nuevos contenidos se distribuyen entre los Agentes Especialistas (Analista Financiero, Ciencia de Datos, Desarrollador Web, Planificador, Asesor Legal, Arquitecto de Sistemas EPEC).
4. **Consulta Obligatoria ante Incompatibilidades**: Si se detecta un proyecto o tema que no encaja en los perfiles vigentes, se solicita autorización al usuario para crear un nuevo agente/repositorio o reasignarlo.

---

## 🛠️ Comandos y Pasos de Ejecución

### Paso 1: Escaneo de Red
```powershell
Get-ChildItem -Path '\\srvfs01\ProyectoTelemedicion\Documentación\PROTELEM\PROJECTS' -Recurse -File | Select-Object FullName, Length, LastWriteTime
```

### Paso 2: Backup Preventivo
```powershell
$timestamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
Copy-Item ".agents/skills/<agente>/SKILL.md" "docs/Backups/$($timestamp)_<agente>_SKILL.md.bak"
```

### Paso 3: Auto-Documentación y Git Push
```powershell
git add .
git commit -m "docs(protelem): sincronizacion automatica de conocimiento red srvfs01"
git push origin master
```

---

## 🔗 Referencias
- [[00-Dashboard-MOC]]
- [[Proyectos/2026-09-02_protelem-conocimiento-integrado|Compendio Integrado de Conocimiento PROTELEM]]
