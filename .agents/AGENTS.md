# Directivas y Reglas Globales de Agentes - Antigravity IDE

## 1. Identificación y Credenciales del Entorno
- **Cuenta de GitHub**: `inventarioenergycpy`
- **Correo de Contacto / Google Drive**: `inventario.energycpy@gmail.com`
- **Forma de Autenticación**: Registro directo asociado a la cuenta de Gmail.

---

## 2. Política Estricta de Almacenamiento y Entregables

### A. Informes y Documentos de Google Workspace
- **Regla**: Todos los informes, análisis financieros, presentaciones ejecutivas y tablas de cálculo creadas mediante herramientas de Google (Google Docs, Google Slides, Google Sheets, etc.) deben crearse y organizarse en la unidad de **Google Drive** de la cuenta `inventario.energycpy@gmail.com`.
- No deben guardarse en la raíz del repositorio local de Git a menos que sean exportaciones explícitas solicitadas en formato `.md`.

### B. Soluciones Locales, Proyectos y Scripts
- **Regla**: Todo archivo ejecutable, código fuente generado (scripts de Python, notebooks PySpark, consultas SQL) y archivos de proyectos **Power BI Project (`.pbip` / `.pbit`)** **NO** se subirán al repositorio público/privado de GitHub a menos que el usuario lo indique expresamente.
- **Ubicación de Salida Obligatoria**: Deben depositarse y estructurarse directamente en la carpeta local de **Descargas del Sistema**:
  - En Windows: `%USERPROFILE%\Downloads` (ej. `C:\Users\<Usuario>\Downloads\`).

---

## 3. Protocolo Obligatorio de Auto-Documentación y Mejora Continua

Cuando el usuario exprese confirmación para guardar una mejora o corrección (ejemplos: *"guarda esta mejora"*, *"registra este ajuste"*, *"actualiza la configuración del agente"*, *"me gusta este formato, consérvalo"*), el agente **DEBE**:

1. Invocar la habilidad `.agents/skills/auto-documentacion-agente/SKILL.md`.
2. Actualizar el archivo `SKILL.md` del agente correspondiente en `.agents/skills/<nombre-agente>/SKILL.md` incorporando las nuevas pautas o patrones validados.
3. Redactar una nota de historial en la Bóveda de Obsidian dentro de `docs/Historial-Mejoras/YYYY-MM-DD_<descripcion>.md` especificando:
   - **Fecha**: Fecha actual.
   - **Agente Afectado**: Nombre del agente.
   - **Mejora Aplicada**: Resumen de la corrección o regla añadida.
   - **Impacto**: Por qué mejora la calidad de respuesta.

---

## 4. Integración con la Bóveda de Obsidian

- La raíz del repositorio actúa como Bóveda de Obsidian (Opción A).
- Toda documentación creada o modificada debe incluir:
  - **YAML Frontmatter** con `title`, `tags`, `updated` y `type`.
  - Enlaces Wiki relacionales (ej. `[[00-Dashboard-MOC]]`, `[[01-Analista-Financiero]]`).
  - Formato Markdown compatible con resaltado de Obsidian.
