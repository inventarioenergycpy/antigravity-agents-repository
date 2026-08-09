# 🛡️ Espacio de Resguardos y Backups (Rollback Safety)

Esta carpeta almacena las copias de seguridad de las configuraciones de los agentes antes de aplicar cualquier mejora o actualización a sus archivos `SKILL.md`.

## Nomenclatura de Archivos de Backup
`YYYY-MM-DD_HHmmss_<nombre-agente>_SKILL.md.bak`

## Proceso de Restauración / Rollback
Si requiere revertir la configuración de un agente a un estado anterior:
1. Indique al agente: *"Restaura el agente <nombre-agente> desde el backup de la fecha YYYY-MM-DD"*.
2. El agente invocará la habilidad `rollback-agente` para sobrescribir el `SKILL.md` actual con la versión `.bak` seleccionada.
