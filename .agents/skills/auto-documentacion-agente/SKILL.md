---
name: auto-documentacion-agente
description: Genera un backup preventivo en docs/Backups/, actualiza el SKILL.md del agente con la mejora confirmada y registra la nota histórica en la Bóveda de Obsidian.
---

# Habilidad: Auto-Documentación, Backup Preventivo e Histórico de Mejoras

Esta habilidad se activa cuando el usuario confirma una mejora o ajuste que desea incorporar a la configuración de un agente.

## Flujo de Ejecución Automatizado

### 1. Generar Backup Preventivo (Rollback Safety)
Antes de modificar el archivo `SKILL.md` destino:
1. Copiar el contenido actual de `.agents/skills/<nombre-agente>/SKILL.md`.
2. Guardarlo en `docs/Backups/` con la nomenclatura:
   `YYYY-MM-DD_HHmmss_<nombre-agente>_SKILL.md.bak`

### 2. Actualizar la Configuración del Agente
1. Modificar `.agents/skills/<nombre-agente>/SKILL.md` incorporando la nueva regla o patrón validado.

### 3. Crear Registro Histórico en Obsidian
1. Crear una nota en `docs/Historial-Mejoras/YYYY-MM-DD_<nombre-agente>_<breve-descripcion>.md` con el siguiente formato:

```markdown
---
type: historial-mejora
agente: "[[<nombre-agente>]]"
fecha: YYYY-MM-DD
backup_asociado: "[[docs/Backups/YYYY-MM-DD_HHmmss_<nombre-agente>_SKILL.md.bak]]"
tags:
  - #historial
  - #mejora
  - #backup
---

# Registro de Mejora: [<Nombre del Agente>]

## 📝 Descripción del Cambio
- **Contexto**: <Resumen de la solicitud o mejora confirmada por el usuario>
- **Regla Agregada**:
  ```markdown
  <Texto exacto de la regla o patrón guardado>
  ```

## 🛡️ Resguardo / Backup de Seguridad
- Se ha generado el respaldo preventivo en: `docs/Backups/YYYY-MM-DD_HHmmss_<nombre-agente>_SKILL.md.bak`

## 🎯 Impacto y Beneficio
- <Explicación de cómo esta mejora incrementa la precisión o calidad de respuesta>

## 🔗 Referencias
- [[00-Dashboard-MOC]]
- [[<Ficha-Agente-en-Docs>]]
```

### 4. Sincronizar Cambios con Git
1. Ejecutar commit en Git resguardando el backup, el `SKILL.md` actualizado y la nota de Obsidian.
2. Confirmar al usuario mostrando los enlaces al backup y al registro histórico.
