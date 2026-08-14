# 🚀 Bóveda Central de Agentes de Antigravity IDE & Obsidian (`antigravity-agents-repository`)

Este repositorio es el **Hub Bóveda Central 100% dedicado** al almacenamiento de perfiles de agentes AI, habilidades (*skills*), directivas globales, respaldos preventivos y documentación interactiva en **Obsidian** para la cuenta **`inventarioenergycpy`** (`inventario.energycpy@gmail.com`).

---

## 📌 Principios de Arquitectura & Gobernanza

1. **Hub Bóveda Central de Agentes (100% Documentación & Skills)**:
   - Este repositorio no almacena código fuente final ni prototipos de proyectos particulares.
   - Contiene el núcleo de habilidades (`.agents/skills/`), directivas globales (`.agents/AGENTS.md`), respaldos (`docs/Backups/`) y la Bóveda de Obsidian (`docs/`).

2. **Estrategia Multi-Repositorio por Proyecto**:
   - Cada proyecto nuevo e independiente (sitio web showroom, pipeline de datos, modelo financiero) se desarrolla en su **propio repositorio de GitHub dedicado** bajo la cuenta `inventarioenergycpy` (ej. `https://github.com/inventarioenergycpy/showroom-energycpy`).
   - Cada proyecto cuenta con su propio despliegue autónomo (ej. GitHub Pages), `README.md` y documentación puntual, registrándose en la bóveda central en `docs/Proyectos/`.

3. **Metodología Estandarizada en 6 Etapas**:
   - **Etapa 1**: Investigación en fuentes verídicas y confiables.
   - **Etapa 2**: Diseño Pre-Implementación & Análisis de Tesis.
   - **Etapa 3**: Diagramación de Etapas & Pruebas Parciales.
   - **Etapa 4**: Prueba Piloto sujeta a Aprobación del Usuario.
   - **Etapa 5**: Pruebas Integrales sobre el Modelo Final.
   - **Etapa 6**: Auto-Documentación, Resguardos `.bak` y Persistencia en Obsidian.

---

## 🤖 Agentes Especialistas Disponibles

| # | Agente | Enfoque | Entregables Principales |
| :-: | :--- | :--- | :--- |
| **1** | **Analista Financiero** | Evaluación cuantitativa/cualitativa de proyectos de inversión (VAN, TIR, EBITDA, WACC), investigación de mercado y riesgo. | Google Docs, Google Slides, Google Sheets en Google Drive. |
| **2** | **Ciencia de Datos** | Procesamiento distribuido masivo de datos (PySpark, Python, SQL) y tableros Power BI Project (`.pbip`). | Entregables locales en `%USERPROFILE%\Downloads\` o repositorios de datos dedicados. |
| **3** | **Desarrollador Web Showroom** | Diseño y desarrollo de plataformas web interactivas Dark Mode / Glassmorphic para proyectos de inversión. | Repositorios web dedicados en GitHub (`inventarioenergycpy/<nombre-web>`) con GitHub Pages independiente. |
| **4** | **Planificador y Diseñador de Agentes** | Investigación verídica, diseño pre-implementación, tesis, pruebas piloto y auto-documentación para nuevos agentes futuros. | Fichas técnicas, `SKILL.md` estructurado y mapa MOC en Obsidian. |

---

## 🛡️ Sistema de Seguridad, Backups y Rollback

- **Auto-Documentación**: Al decir *"guarda esta mejora"*, el agente ejecuta `auto-documentacion-agente`.
- **Backups Preventivos**: Generación de respaldos `.bak` en `docs/Backups/` antes de cada modificación.
- **Rollback**: Invocación de `rollback-agente` para restaurar versiones anteriores.
- **Registro Histórico**: Trazabilidad completa en `docs/Historial-Mejoras/`.

---

## 📁 Estructura de la Bóveda Central

```text
antigravity-agents-repository/
├── .agents/                                # Habilidades y reglas para Antigravity IDE
│   ├── AGENTS.md                           # Directivas globales y protocolo multi-repositorio
│   └── skills/                             # Habilidades especializadas
│       ├── analista-financiero/
│       ├── ciencia-de-datos/
│       ├── desarrollador-web-showroom/
│       ├── planificador-agentes/
│       ├── auto-documentacion-agente/
│       └── rollback-agente/
├── docs/                                   # Bóveda de Obsidian (Obsidian Vault Layer)
│   ├── 00-Dashboard-MOC.md                 # Dashboard principal en Obsidian
│   ├── Agentes/                            # Fichas técnicas de los agentes
│   ├── Proyectos/                          # Registro e índice de repositorios dedicados
│   ├── Backups/                            # Copias de resguardo .bak
│   └── Historial-Mejoras/                  # Registro histórico de evoluciones
└── README.md
```

