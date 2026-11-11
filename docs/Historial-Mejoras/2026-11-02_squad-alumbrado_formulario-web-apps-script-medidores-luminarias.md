---
type: historial-mejora
agente: "[[11-Copiloto-Orquestador-de-Skills]]"
fecha: 2026-11-02
tags:
  - #historial
  - #mejora
  - #squad-agil
  - #google-apps-script
  - #alumbrado-publico
  - #triple-qa
---

# Registro de Mejora: Desarrollo de Formulario Dinámico y Web App para Relevamiento de Alumbrado Público y Medidores

## 📝 Descripción del Requerimiento y Solución
- **Objetivo**: Desarrollar un sistema de formulario dinámico para cuadrillas en calle con el fin de relevar el medidor instalado (fecha, número de medidor y lecturas multifunción E, EAR, EAP, EAV, ERT) y de forma secuencial y repetitiva el relevamiento por poste de luminarias conectado (cantidad de lámparas, hasta 3 fotos, coordenadas GPS y ubicación geocatastral).
- **Cuenta de Destino**: `relevamientocontrolgestion@gmail.com`.
- **Evolución Arquitectónica**:
  - En la **Compuerta de Clarificación e Inception**, se identificó que Google Forms nativo (`forms.google.com`) no cuenta con soporte para botones dinámicos de agregado de ítems en tiempo de ejecución, ni geolocalización satelital nativa automática, ni compresión de imágenes móvil.
  - Se acordó y desarrolló una **Google Apps Script Web App** mobile-first con frontend HTML5/CSS/JS y backend `Code.gs`, conectada automáticamente a Google Sheets (`Relevamiento_Alumbrado_Publico`) y Google Drive (`Fotos_Relevamiento_Alumbrado`).
  - Se estructuró un modelo de almacenamiento plano en 1 sola hoja de 23 columnas (Opción A2 seleccionada por el usuario).
  - Se implementó un algoritmo client-side en Canvas HTML5 para comprimir las fotos de cámara a ~250 KB (1.280px, 0.75 JPEG) antes de la subida, garantizando fluidez en redes 3G/4G y evitando exceder los límites de payload de Apps Script.

## 🛡️ Validación en 3 Instancias (Triple QA)
1. **Instancia 1 (QA Técnico & Algorítmico)**:
   - Verificación sintáctica y lógica sin errores.
   - Creación y ejecución de la suite de pruebas unitarias [`tests/test_payload_validation.py`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/tests/test_payload_validation.py) con 4 tests deterministas superados con exit code 0 (`OK`).
2. **Instancia 2 (QA de Negocio, Dominio & Regulación EPEC)**:
   - Correcta separación y unidades de magnitudes eléctricas para registradores de alumbrado público (E: Activa Total, EAR: Activa Resto, EAP: Activa Pico, EAV: Activa Valle, ERT: Reactiva Total).
   - Inclusión de tipologías de luminaria de alumbrado (LED, SAP, Vapor de Mercurio) y estados operativos.
   - Rango geográfico y geocatastral validado para la Provincia de Córdoba / Argentina.
3. **Instancia 3 (QA de Usabilidad, Replicabilidad & UX Mobile)**:
   - Interfaz con diseño mobile-first, inputs de altura táctil $\ge 48$px, botones ergonómicos `+` y `-`, y previsualización de miniaturas.
   - Generación de [`INSTRUCTIVO_DESPLIEGUE_GOOGLE.md`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/INSTRUCTIVO_DESPLIEGUE_GOOGLE.md) para despliegue guiado en menos de 5 minutos en la cuenta `relevamientocontrolgestion@gmail.com`.

## 🛠️ Diagnóstico y Resolución de Incidencias en Despliegue Apps Script

### 1. Incidencia de Codificación y Mojibake (Caracteres corruptos: `PÃºblico`, `âš¡`)
- **Causa**: Discrepancia en decodificación UTF-8 / ANSI en el portapapeles o editor web de Google Apps Script.
- **Solución**: Sustitución exhaustiva de emojis de 4 bytes por elementos `<svg>` vectoriales en línea y reemplazo de vocales con tilde por entidades HTML seguras (`&uacute;`, `&oacute;`, etc.).

### 2. Incidencia de Botones Inoperativos ("No funciona agregar poste ni guardar")
- **Diagnóstico Profundo (Remote Debugging CDP)**:
  - Inspección del iframe de producción `https://n-...-script.googleusercontent.com/userCodeAppPanel` reveló error `SyntaxError: Unexpected end of input` en el script evaluado y corte prematuro del código en la posición 6.968.
  - **Causa Raíz**: En la declaración de atributos de carga de cámara se utilizaba `accept="image/*"`. El preprocesador y sanitizador de Google Apps Script interpreta la secuencia `/*` dentro de una etiqueta `<script>` como el inicio de un bloque de comentarios multilinea de JavaScript (`/* ... */`). Al no encontrar un cierre `*/` en el resto del bloque, el sanitizador truncó silenciosamente todo el script hasta el cierre de la página, dejando funciones sin definir (`window.agregarPoste` = `undefined`).
- **Solución Aplicada**:
  - Reemplazo de todas las secuencias `image/*` por tipos MIME explícitos seguros: `accept="image/jpeg,image/png,image/webp,image/jpg"`.
  - Conversión del generador dinámico de tarjetas de poste de literales de plantilla (template literals backticks `` ` ``) a concatenación robusta mediante arreglos `.join("\n")`.
  - Inicialización activa de listeners tanto por atributo HTML como por asignación directa en `initApp()`.
  - Creación del archivo `index.html` en la raíz para permitir también despliegue sin autenticación en **GitHub Pages** con envío directo al backend `doPost()` de Apps Script.


### 3. Simplificación de Campos de Entrada Solicitada por el Usuario
- **Requerimiento**: Remover los campos de lecturas del medidor (E, EAR, EAP, EAV, ERT) y remover el campo de Nomenclatura Catastral en el módulo de postes.
- **Implementación**:
  - Eliminación de la sección de lecturas del medidor en Index.html y del selector de catastro en JavaScript.html.
  - Reducción del modelo plano de datos en Google Sheets de 23 a 16 columnas.
  - Compatibilidad regresiva automática en Code.gs (soporta escritura tanto en hojas de 23 columnas como de 16 columnas sin pérdida de datos).
  - Actualización de pruebas unitarias deterministas (	ests/test_payload_validation.py) con 4/4 tests exitosos.
  - Re-generación de Bundle_Standalone_AppsScript.html e index.html para GitHub Pages.

## 📂 Archivos Generados en el Repositorio Dedicado
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/README.md`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/README.md)
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/INSTRUCTIVO_DESPLIEGUE_GOOGLE.md`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/INSTRUCTIVO_DESPLIEGUE_GOOGLE.md)
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/docs/especificacion_funcional.md`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/docs/especificacion_funcional.md)
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Code.gs`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Code.gs)
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Index.html`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Index.html)
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Styles.html`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Styles.html)
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/JavaScript.html`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/JavaScript.html)
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Bundle_Standalone_AppsScript.html`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Bundle_Standalone_AppsScript.html)
- [`D:/Proyectos/relevamiento-alumbrado-publico-medidores/tests/test_payload_validation.py`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/tests/test_payload_validation.py)

## 🔗 Referencias en Bóveda Central
- [[00-Dashboard-MOC]]
- [[docs/Proyectos/2026-11-02_relevamiento-alumbrado-publico-medidores|Ficha Técnica del Proyecto]]
- [[docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores]]

