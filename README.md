# 🚀 Repositorio Estructurado de Agentes de Antigravity IDE & Bóveda Obsidian

Este repositorio contiene la arquitectura central de agentes, habilidades (*skills*), reglas y documentación interactiva legible en **Obsidian** para la cuenta **`inventarioenergycpy`** (`inventario.energycpy@gmail.com`).

---

## 📌 Características Principales

1. **Bóveda Integrada de Obsidian (Opción A)**:
   - La raíz del repositorio funciona como Bóveda (*Vault*) de Obsidian.
   - Incluye un **Dashboard / Map of Content (`docs/00-Dashboard-MOC.md`)** interactivo con notas relacionales, etiquetas `#agente` y grafos de conocimiento.
2. **Sincronización Multi-PC con Menú de Inicio Interactivo**:
   - Script de consola `scripts/start.ps1` ejecutable en cualquier PC para validar la conexión a GitHub, sincronizar el repositorio y preparar el entorno de trabajo en Antigravity IDE.
3. **Política de Almacenamiento de Salidas**:
   - **Herramientas de Google Workspace**: Los informes, diapositivas y planillas creados por los agentes se almacenan en el **Google Drive** de `inventario.energycpy@gmail.com` (Google Docs, Google Slides, Google Sheets).
   - **Soluciones y Archivos Locales**: Los proyectos de Power BI (`.pbip`), scripts Python/PySpark y consultas SQL se guardan localmente en la carpeta de **Descargas del sistema** (`%USERPROFILE%\Downloads`).
4. **Mecanismo de Auto-Documentación**:
   - Instrucción en `.agents/AGENTS.md` para que los agentes registren e incorporen automáticamente mejoras o correcciones confirmadas por el usuario.

---

## 🤖 Agentes Disponibles

| Agente | Enfoque | Entregables Principales |
| :--- | :--- | :--- |
| **Analista Financiero** | Evaluación de proyectos de inversión, tendencias de mercado y riesgo. | Google Docs, Google Slides, Google Sheets en Google Drive. |
| **Ciencia de Datos** | Análisis de grandes volúmenes de datos con Python, PySpark, SQL y Power BI. | Archivos Power BI Project (`.pbip`) y scripts en `%USERPROFILE%\Downloads`. |
| **Desarrollador Web Showroom** | Creación de showrooms web interactivos para proyectos de inversión. | Código HTML/CSS/JS maquetado (estilo `desarrollosas.com.ar`) en `showroom-web/` listo para GitHub Pages. |

---

## 💻 Guía de Inicio Rápido en un Nuevo PC

Al iniciar sesión en una nueva computadora con la cuenta de Gmail/GitHub:

1. Abrir PowerShell en la raíz del proyecto.
2. Ejecutar el menú de inicio interactivo:
   ```powershell
   .\scripts\start.ps1
   ```
3. Seleccionar las opciones para:
   - Verificar credenciales Git (`inventarioenergycpy`).
   - Sincronizar habilidades mediante `git pull` / `git push`.
   - Verificar carpeta local de Descargas.

---

## 📁 Estructura del Repositorio

```text
.
├── .agents/                                # Habilidades y reglas para Antigravity IDE
│   ├── AGENTS.md                           # Reglas globales y auto-documentación
│   └── skills/                             # Habilidades especializadas
│       ├── analista-financiero/
│       ├── ciencia-de-datos/
│       ├── desarrollador-web-showroom/
│       └── auto-documentacion-agente/
├── docs/                                   # Bóveda de Obsidian (Obsidian Vault Layer)
│   ├── 00-Dashboard-MOC.md                 # Nota principal / Dashboard en Obsidian
│   ├── Agentes/                            # Fichas técnicas de los agentes
│   ├── Habilidades/                        # Catálogo de skills
│   └── Historial-Mejoras/                  # Registro de cambios confirmados por el usuario
├── scripts/
│   ├── start.ps1                           # Menú de inicio CLI interactivo Multi-PC
│   ├── setup_environment.ps1               # Inicialización del entorno local
│   └── sync_repository.ps1                 # Sincronización Git automática
├── showroom-web/                           # Showroom web listo para GitHub Pages
│   ├── index.html
│   ├── css/styles.css
│   └── js/main.js
└── README.md
```
