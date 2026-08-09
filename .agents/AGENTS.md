# Directivas y Reglas Globales de Agentes - Antigravity IDE

## 1. Identificación y Credenciales del Entorno
- **Cuenta de GitHub**: `inventarioenergycpy`
- **Correo de Contacto / Google Drive**: `inventario.energycpy@gmail.com`
- **Forma de Autenticación**: Registro directo asociado a la cuenta de Gmail.

---

## 2. Política Estricta de Almacenamiento y Entregables

### A. Informes y Documentos de Google Workspace
- **Regla**: Todos los informes, análisis financieros, presentaciones ejecutivas y tablas de cálculo creadas mediante herramientas de Google (Google Docs, Google Slides, Google Sheets) se almacenan en el **Google Drive** de `inventario.energycpy@gmail.com`.

### B. Soluciones Locales, Proyectos y Scripts
- **Regla**: Todo código ejecutable (Python, PySpark, SQL) y proyectos **Power BI Project (`.pbip` / `.pbit`)** se depositan en la carpeta local de **Descargas del Sistema**:
  - Windows: `%USERPROFILE%\Downloads` (ej. `C:\Users\<Usuario>\Downloads\`).

---

## 3. Creación de Nuevos Perfiles de Agentes Futuros

Para incorporar un nuevo perfil de agente al repositorio:
1. Crear el directorio de la habilidad en `.agents/skills/<nombre-nuevo-agente>/SKILL.md` con su YAML frontmatter y pautas operativas.
2. Crear la ficha técnica legible en Obsidian dentro de `docs/Agentes/<Nombre-Nuevo-Agente>.md`.
3. Actualizar el tablero principal `docs/00-Dashboard-MOC.md` agregando el nuevo agente al diagrama Mermaid y a la lista relacional.

---

## 4. Protocolo Obligatorio de Backup, Histórico y Rollback

Cuando el usuario apruebe o solicite guardar una mejora (ej. *"guarda esta mejora"*, *"actualiza este agente"*), se activará el siguiente protocolo estricto:

### Paso 1: Backup Preventivo (Rollback Protection)
- **ANTES** de aplicar cualquier cambio en `SKILL.md`, crear una copia exacta de respaldo de la versión actual en la carpeta:
  - `docs/Backups/YYYY-MM-DD_HHmmss_<nombre-agente>_SKILL.md.bak`

### Paso 2: Aplicación del Cambio
- Actualizar `.agents/skills/<nombre-agente>/SKILL.md` incorporando la nueva pauta o corrección.

### Paso 3: Registro Histórico en Obsidian
- Crear una entrada detallada de la mejora en `docs/Historial-Mejoras/YYYY-MM-DD_<nombre-agente>_<descripcion>.md` especificando contexto, regla agregada, impacto y enlace al archivo de backup creado.

### Paso 4: Reversión / Rollback (En caso de requerirse)
- Si el usuario solicita revertir un cambio (ej. *"haz un rollback al agente"*, *"restaura la versión anterior de este agente"*), invocar la habilidad `.agents/skills/rollback-agente/SKILL.md` para restaurar desde `docs/Backups/` el archivo `.bak` seleccionado.

---

## 5. Integración con la Bóveda de Obsidian

- La raíz del repositorio actúa como Bóveda de Obsidian (Opción A).
- Toda documentación creada o modificada debe incluir metadatos YAML frontmatter y enlaces relacionales (`[[00-Dashboard-MOC]]`, `[[docs/Backups/]]`, etc.).
