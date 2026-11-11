---
type: historial-mejora
agente: "[[11-Copiloto-Orquestador-de-Skills]]"
fecha: 2026-11-03
tags:
  - #historial
  - #mejora
  - #squad-agil
  - #alumbrado-publico
  - #localstorage
  - #persistencia
  - #potencia-luminaria
  - #triple-qa
---

# Registro de Mejora: Persistencia de Borrador en LocalStorage Anti-Recarga y Menú Opcional de Potencia en Watts

## 📝 Descripción del Requerimiento y Solución

### 1. Defecto Corregido: Pérdida de Datos ante Recarga Accidental de la Página
- **Diagnóstico**: En dispositivos móviles, un gesto involuntario de deslizamiento hacia abajo (*pull-to-refresh*) o el cambio temporal hacia otra aplicación (ej. Maps, WhatsApp) provocaba que el navegador recargara la pestaña, borrando por completo los postes relevados, las fotos capturadas y las coordenadas GPS en curso.
- **Solución Implementada**:
  - Se incorporó un subsistema reactivo de persistencia client-side basado en `localStorage` bajo la clave `relevamiento_alumbrado_borrador_v1`.
  - **Auto-Guardado en Tiempo Real**: Toda modificación de datos (tipeo de medidor, fecha, ajuste de contadores, cambios en desplegables, captura de GPS y compresión de fotos) se guarda automáticamente en el almacenamiento local del teléfono con técnica de *debouncing* (300 ms).
  - **Recuperación Automática de Sesión**: Al cargar o recargar la aplicación (`initApp()`), el sistema detecta si existe un relevamiento en curso y restaura íntegramente: número de medidor, fecha, cantidad y secuencia de postes, tecnologías, potencias, estados, coordenadas GPS en vivo y previsualizaciones fotográficas con botones de borrado.
  - **Banner Interactivo de Confirmación**: Se despliega un aviso visual (`#aviso-borrador`) notificando la restauración de la sesión con opción de descartar el borrador para iniciar una nueva carga limpia.
  - **Protección `beforeunload`**: Se añadió un listener nativo de advertencia ante cierre o navegación no deseada.
  - **Purga Segura**: El borrador se elimina de `localStorage` al confirmarse el envío exitoso al servidor o al presionar expresamente "Iniciar Nuevo Relevamiento" o "Descartar Borrador".

### 2. Nuevo Menú Desplegable Opcional: Potencia de Luminaria
- **Requerimiento**: Luego de aclarar el tipo de tecnología de la luminaria, incorporar un menú opcional desplegable que indique la potencia de cada artefacto con los valores solicitados.
- **Implementación**:
  - En cada tarjeta de poste (`agregarPoste()`) se añadió el selector `#poleId-potencia`:
    - `No especificada` (valor por defecto / opcional)
    - `50W`
    - `100W`
    - `150W`
    - `200W`
    - `250W`
  - Se mapea en el payload JSON como `potenciaLuminaria`.

### 3. Evolución del Modelo Plano de Google Sheets a 17 Columnas
- En [`src/Code.gs`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/src/Code.gs), se insertó `Potencia_Luminaria` como columna 8 (entre `Tipo_Luminaria` y `Estado_Luminaria`).
- **Migración Transparente y Retrocompatible**: Si la hoja de cálculo ya existía con 16 columnas, la función `obtenerOCrearHojaCalculo()` detecta automáticamente la columna y ejecuta `sheet.insertColumnAfter(7)` con su encabezado azul oscuro estilizado, sin alterar los datos históricos existentes.

---

## 🛡️ Validación en 3 Instancias (Triple QA)

1. **Instancia 1 (QA Técnico & Algorítmico)**:
   - Verificación sintáctica y ejecución de la suite de pruebas unitarias en Python [`tests/test_payload_validation.py`](file:///D:/Proyectos/relevamiento-alumbrado-publico-medidores/tests/test_payload_validation.py): **5/5 tests pasados exitosamente (`OK`)** en 0.015s.
   - Verificación de renderizado y persistencia en navegador Edge Headless (`--dump-dom`) confirmando restauración de postes con `150W` y `250W` y visibilidad de `.draft-alert`.
2. **Instancia 2 (QA de Negocio, Dominio & Regulación EPEC)**:
   - Exactitud de las potencias estándar utilizadas en el parque de alumbrado público de la provincia (50W, 100W, 150W, 200W, 250W para tecnologías LED y descarga SAP).
   - Preservación íntegra de la base de datos en Google Sheets y carpetas de Google Drive.
3. **Instancia 3 (QA de Usabilidad, Replicabilidad & UX Mobile)**:
   - Cero fricción en calle: la cuadrilla no pierde su trabajo si el teléfono se apaga o se refresca la pantalla.
   - Menú de potencia ergonómico y con opción neutral "No especificada" para no trabar el relevamiento si la potencia de placa no es visible.

---

## 🔒 Respaldos Preventivos (.bak) Creados
- `docs/Backups/2026-11-03_153000_00-Dashboard-MOC.md.bak`
- `docs/Backups/2026-11-03_153000_relevamiento-alumbrado-publico-medidores.md.bak`

