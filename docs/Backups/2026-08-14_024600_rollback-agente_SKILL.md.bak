---
name: rollback-agente
description: Restaura la configuración de un agente desde un backup preventivo almacenado en docs/Backups/ cuando el usuario solicita una reversión o rollback.
---

# Habilidad: Rollback y Reversión de Agentes

Esta habilidad se activa cuando el usuario solicita revertir la configuración de un agente a un estado anterior (ejemplos: *"haz un rollback al analista financiero"*, *"restaura la versión anterior de este agente"*, *"deshaz la última mejora"*).

## Flujo de Reversión

1. **Listar los Backups Disponibles**:
   - Inspeccionar la carpeta `docs/Backups/` y mostrar los archivos `.bak` filtrados por el agente solicitado.

2. **Confirmar la Versión a Restaurar**:
   - Presentar al usuario la lista de respaldos con fecha y hora de creación para que elija o confirme la versión de restauración.

3. **Ejecutar el Rollback**:
   - Copiar el contenido del archivo `.bak` seleccionado desde `docs/Backups/` sobre `.agents/skills/<nombre-agente>/SKILL.md`.

4. **Registrar la Reversión en Obsidian**:
   - Crear una entrada en `docs/Historial-Mejoras/YYYY-MM-DD_<nombre-agente>_ROLLBACK.md` documentando que se ha restaurado la versión anterior.

5. **Confirmar al Usuario**:
   - Notificar que el agente ha sido restaurado exitosamente a su configuración anterior.
