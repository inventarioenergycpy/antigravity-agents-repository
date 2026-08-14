# Directivas y Reglas Globales de Agentes - Antigravity IDE

## 1. Identificación y Credenciales del Entorno
- **Cuenta de GitHub**: `inventarioenergycpy`
- **Correo de Contacto / Google Drive**: `inventario.energycpy@gmail.com`
- **Forma de Autenticación**: Registro directo asociado a la cuenta de Gmail.

---

## 2. Propósito del Repositorio y Política de Almacenamiento

### A. Repositorio Central de Agentes (`antigravity-agents-repository`)
- **Regla Estricta**: Este repositorio está destinado **100% exclusivamente a la documentación de agentes, habilidades (`.agents/skills/`), reglas globales (`.agents/AGENTS.md`), respaldos (`docs/Backups/`) y la Bóveda de Obsidian (`docs/`)**.
- No debe contener código fuente final ni prototipos pesados de proyectos individuales.

### B. Informes y Documentos de Google Workspace
- **Regla**: Todos los informes, análisis financieros, presentaciones ejecutivas y planillas creadas en Google Workspace (Docs, Slides, Sheets) se almacenan en el **Google Drive** de `inventario.energycpy@gmail.com`.

### C. Entregables Locales de Trabajo Directo
- **Regla**: Entregables temporales, scripts de un solo uso o borradores de Power BI Project (`.pbip`) se depositan en la carpeta local de **Descargas del Sistema** (`%USERPROFILE%\Downloads`).

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
- Toda documentación creada o modificada debe incluir metadatos YAML frontmatter y enlaces relacionales (`[[00-Dashboard-MOC]]`, `[[docs/Backups/]]`, `[[docs/Proyectos/]]`, etc.).

---

## 6. Protocolo Multi-Repositorio: Creación de Repositorios Dedicados por Proyecto

Cada vez que un agente desarrolle un nuevo proyecto (página web showroom, aplicación de análisis de datos, modelo financiero dinámico u otro sistema) cuya naturaleza sea distinta a los anteriores:

1. **Parametrización del Nuevo Repositorio**:
   - Inicializar una nueva carpeta local independiente (ej. `C:\Users\Usuario\.gemini\antigravity-ide\scratch\<nombre-proyecto>`).
   - Crear y vincular un nuevo repositorio remoto en GitHub bajo la cuenta del usuario:
     `https://github.com/inventarioenergycpy/<nombre-proyecto-kebab-case>.git`

2. **Estructura Interna del Repositorio de Proyecto**:
   - `README.md`: Descripción ejecutiva del proyecto, objetivos y enlace a su despliegue (ej. GitHub Pages).
   - `docs/`: Documentación técnica puntual del proyecto y notas de arquitectura.
   - `src/` o raíz del proyecto: Código fuente ejecutable, componentes e interfaz.
   - `assets/`: Recursos gráficos e imágenes URL-safe.

3. **Registro Cruzado en la Bóveda Central (`antigravity-agents-repository`)**:
   - Crear una nota de registro en `docs/Proyectos/YYYY-MM-DD_<nombre-proyecto>.md` especificando:
     - Nombre del proyecto y objetivo.
     - Agente responsable del desarrollo.
     - Enlace al repositorio de GitHub creado (`https://github.com/inventarioenergycpy/<nombre-proyecto>`).
     - Enlace al despliegue o demo activa.
   - Actualizar el índice general en `docs/00-Dashboard-MOC.md` en la sección `[[Proyectos/|Proyectos Desarrollados]]`.

