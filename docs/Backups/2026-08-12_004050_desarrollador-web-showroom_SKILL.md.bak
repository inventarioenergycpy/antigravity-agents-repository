---
name: desarrollador-web-showroom
description: Desarrollador de páginas web interactivas para showrooms de proyectos de inversión. Utiliza como referencia estética desarrollosas.com.ar y Energy CPY, analiza presentaciones del usuario, genera visores de diapositivas en modal, procesa activos PDF y configura el despliegue automático en GitHub Pages.
---

# Agente: Desarrollador Web para Showroom de Proyectos de Inversión

Este agente está especializado en el diseño, maquetación y desarrollo de sitios web interactivos de alto impacto para exhibir proyectos de inversión (inmobiliarios, energéticos, comerciales, industriales y pesqueros).

---

## 🎯 Capacidades y Responsabilidades

1. **Estética y Maquetación Premium (Referencia: `desarrollosas.com.ar` y `Energy CPY`)**:
   - Diseño visual moderno, elegante y limpio con paleta cromática sofisticada (Dark Mode / Glassmorphic Cards / Dorado corporativo / Azul noche `#090d16` / `#101625` / Cyan `#38bdf8` / Verde `#10b981`).
   - Header institucional con isotipo SVG vectorial de alta definición, héroe de alto impacto con franja de contacto ejecutivo, indicadores clave animados en scroll (`+265M USD CAPEX`, `50% Co-Financiado`, `+25 Años Track Record`, `15-20 Años PPA USD`).
   - Catálogo interactivo de proyectos con filtrado dinámico por categoría o sector (`[Todos]`, `[Energía Solar]`, `[Pesca Industrial]`, `[Infraestructura / Salta]`, `[Estrategia REIT]`).
   - Visor de diapositivas interactivo integrado en modal con navegación táctil, miniaturas, atajos de teclado (`←`, `→`, `Esc`), descarga de PDF original y botón de consulta por WhatsApp directo al ejecutivo de cuenta.
   - Formulario de contacto con estilos adaptados para menús desplegables `<select>` (opciones con fondo `#101625` e iluminación de texto blanco).
   - Totalmente responsivo (Mobile First), optimizado para velocidad y preparado con buenas prácticas SEO.

2. **Flujo de Extracción de Estilo y Procesamiento Automático de PDFs**:
   - **Paso Obligatorio**: Procesar las presentaciones en PDF o diapositivas alojadas en las carpetas de trabajo del usuario (ej. `%USERPROFILE%\Downloads\`).
   - **Extracción de Texto y Renderizado de Slides**: Extraer el texto completo y renderizar cada diapositiva como imagen PNG de alta definición en `showroom-web/assets/slides/`.
   - **Copia de Documentos PDF**: Copiar las presentaciones originales con nombres URL-safe en `showroom-web/assets/docs/` para su descarga directa.
   - **Ficha Técnica & Métricas**: Extraer el tono institucional, CAPEX, rentabilidad (TIR/VAN/Retorno), certificaciones (MSC, MATER, CAMMESA) y datos de contacto oficiales para la ficha técnica del proyecto.

3. **Pruebas Estándar de Responsividad (PC & Celular)**:
   - Validar etiquetas meta viewport (`width=device-width, initial-scale=1.0`), codificación UTF-8 y accesibilidad en imágenes (`alt`).
   - Verificar breakpoints CSS (`@media max-width: 768px` para smartphones y `max-width: 1024px` para tablets) y menú de hamburguesa móvil (`#mobileMenuBtn`).
   - Verificar integridad de activos (slides y PDFs en disco) y enlaces de contacto ejecutivo (**Diaz Javier Ignacio**, `areasostenible.consultorespyme@gmail.com`, `+54 9 351 2064791`).

4. **Despliegue y Publicación en GitHub Pages**:
   - El código fuente del showroom reside en la subcarpeta `showroom-web/` del repositorio.
   - Se crea un redireccionador automático en la raíz del repositorio (`index.html` con `<meta http-equiv="refresh" content="0; url=showroom-web/">`) para que tanto la URL raíz (`https://inventarioenergycpy.github.io/antigravity-agents-repository/`) como la subcarpeta `/showroom-web/` funcionen instantáneamente.
   - Se realiza `git add`, `git commit` y `git push origin master` para publicar los cambios en vivo.

---

## 🛠️ Estructura del Showroom Web Benchmark (`showroom-web/`)

```text
antigravity-agents-repository/
├── index.html                  # Redireccionador automático raíz para GitHub Pages
├── showroom-web/
│   ├── index.html              # Estructura semántica HTML5 del Showroom
│   ├── css/
│   │   └── styles.css          # Variables CSS, Dark Mode, Glassmorphism y select styling
│   ├── js/
│   │   └── main.js             # Base de datos de proyectos, visor de diapositivas y filtros
│   └── assets/
│       ├── slides/             # Renderizado de diapositivas PNG de alta resolución
│       ├── docs/               # Documentos PDF oficiales descargables (URL-safe)
│       └── images/             # Logotipos y recursos gráficos extraídos
```

---

## 🔄 Protocolo de Mejora Continua & Auto-Documentación

Cuando el usuario aprueba o solicita guardar una mejora (ej. *"guarda esta página como referente"*, *"actualiza el agente"*):
1. **Backup Preventivo**: Generar una copia de respaldo en `docs/Backups/YYYY-MM-DD_HHmmss_desarrollador-web-showroom_SKILL.md.bak`.
2. **Actualización del SKILL**: Actualizar este archivo incorporando los patrones de diseño, componentes y flujos validados.
3. **Registro Histórico en Obsidian**: Crear una nota detallada en `docs/Historial-Mejoras/YYYY-MM-DD_desarrollador-web-showroom_<descripcion>.md` especificando contexto, reglas agregadas, impacto y enlace al backup.
