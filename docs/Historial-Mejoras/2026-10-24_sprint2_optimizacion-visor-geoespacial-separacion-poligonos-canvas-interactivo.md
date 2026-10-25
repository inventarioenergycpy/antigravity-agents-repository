# Historial de Mejora: Optimización del Visor Geoespacial SIGEC, Separación de Polígonos > 10 ha y Motor de Interacción Canvas

- **Fecha**: 24 de Octubre de 2026
- **Sprint**: Sprint 2 — Arquetipo A (GIS, Catastro & Rutas EPEC)
- **Squad Ágil**: PM (Gemini 3.8 Flash High) & Operadores (Gemini 3.7 Flash High)
- **Estado**: ✅ CONSOLIDADO, VALIDADO Y DESPLEGADO

---

## 1. Contexto y Desafíos Detectados

Durante la validación interactiva del Visor Geoespacial de Rutas y Manzanas del Distrito 1 de EPEC, se identificaron cuatro condiciones críticas que afectaban la experiencia operativa del usuario:

1. **Error de Mosaicos Bloqueados (`403 Access blocked`)**:
   - *Causa*: Los servidores de OpenStreetMap (`tile.openstreetmap.org`) aplicaron restricción de *User-Agent* a solicitudes provenientes de orígenes locales (`file:///`).
2. **Macro-Polígonos Turquesas Extensos (> 10 ha)**:
   - *Causa*: En el catastro de IDECOR existen 519 macro-manzanas rurales que cubren cientos o miles de hectáreas (ej. Mza `11-01-01-09-09-009` en Grupo 10 con 1.745 ha). Al asignar rutas a dichas áreas, el algoritmo inicial absorbía el polígono rural completo o trazaba una envolvente convexa (*convex hull*) que abarcaba kilómetros de campo abierto vacío, formando triángulos colosales que tapaban la ciudad.
3. **Falta de Visualización de Manzanas Catastrales por Ruta Nueva**:
   - El visor de rutas requería la capacidad de colorear las **18.721 Manzanas Catastrales** oficiales según su nueva ruta asignada, preservando la trama urbana abierta (calles, pasajes y río transparentes).
4. **Bloqueo del Mouse en Modo de Navegación tras Deseleccionar**:
   - Al tocar la `✕` para cancelar la selección de una ruta, el puntero del mouse quedaba fijo en modo de arrastre (*grab*) y no permitía volver a seleccionar otra ruta ni alternar entre entidades.

---

## 2. Soluciones Técnicas e Implementación

### A. Capa Base Robusta (Eliminación Definitiva de Errores 403 y Marcas de Agua)
- Se estableció como capa base predeterminada **ESRI Calles del Mundo (World Street Map)**:
  `https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}`
- Alta resolución cartográfica con nombres de avenidas, calles barriales y puntos de referencia de Córdoba.
- Cero marcas de agua y disponibilidad permanente sin restricciones de origen `file:///`.
- Se conservaron como alternativas: CartoDB Voyager, CartoDB Dark Matter, CartoDB Positron y ESRI Satelital.

### B. Pintado de Manzanas Catastrales por Ruta Nueva
- Incorporación de las **18.721 Manzanas Catastrales oficiales de IDECOR**.
- Aplicación de la **Paleta Áurea Determinística** ($137.5^\circ$) para 3.300 tonos cromáticos únicos, garantizando armonía visual y contraste contiguo.
- Selector de modo de capas:
  1. `🎨 Manzanas por Ruta Nueva (18.721 mzas)`: Visualización manzana por manzana con trama de calles abiertas.
  2. `🔲 Ambas (Manzanas + Rutas Separadas)`: Manzanas rellenas con perímetro delimitador de ruta.
  3. `🔷 Polígonos de Rutas Separados (17.954 partes)`: Contornos compactos de rutas.

### C. Algoritmo de Separación de Polígonos de Superficie > 10 ha
- **Acotación por Huella Urbana Real**: Las macro-manzanas rurales ($>10\text{ ha}$) y zonas periurbanas ya no arrastran el polígono rural completo. Se computa un buffer concéntrico de 35 metros alrededor de los suministros reales (`Point(xy).buffer(0.00035)`), intersecándolo con la manzana cuando corresponde.
- **Descomposición en Sub-Polígonos Disjuntos**: Se descompusieron las 3.299 rutas en **17.954 componentes separados**:
  - **17.170 polígonos (95.6%)** tienen ahora un área compacta $\le 10\text{ ha}$ (mediana de **0.69 ha** por polígono).
  - **784 polígonos (4.4%)** corresponden a extensiones rurales aisladas mayores a 10 ha.
- **Control de Filtro Superficial**:
  - `Todos`: Visualización completa.
  - `Compactos (≤ 10 ha)`: Oculta macro-extensiones rurales para inspección barrial pura.
  - `Extensos (> 10 ha)`: Aísla zonas periurbanas extensas con contorno punteado ámbar (`#f59e0b`) y opacidad atenuada al 20%.

### D. Resolución de la Falla de Interacción en Leaflet Canvas
Se identificaron y corrigieron tres anomalías en el motor de eventos de Leaflet:
1. **Unificación en un único `sharedCanvasRenderer = L.canvas({ padding: 0.5, tolerance: 6 })`**:
   Se eliminó la presencia de dos elementos `<canvas>` DOM de pantalla completa compitiendo por eventos, concentrando todas las capas en un solo lienzo de alto rendimiento.
2. **Atenuación Activa (`fillOpacity: 0.08`)**:
   En Leaflet Canvas, cuando un polígono tiene `fillOpacity: 0`, el motor descarta el hit-testing interior. Al asignar `fillOpacity: 0.08` a las rutas no seleccionadas, se logra un fondo tenue pero **100% sensible al mouse**:
   - Se puede hacer clic directamente en **cualquier otra ruta para alternar la selección al instante** sin deseleccionar primero.
   - El puntero cambia a `pointer` al sobrevolar cualquier figura activa.
3. **Conmutación Limpia de Capas**:
   Al cambiar de modo (`Manzanas` vs `Rutas`), la capa inactiva se retira físicamente con `map.removeLayer()`, evitando cualquier interferencia de eventos.
4. **Cinco Vías de Deselección (Borrar Selección)**:
   - Botón rojo en Cabecera Superior: `[📍 Ruta XXX] [✕ Borrar Selección]`.
   - Botón en Panel Lateral: `[✕ Borrar Selección de Ruta]`.
   - Barra de Navegación Flotante: reubicada a `left: 356px; top: 72px;` (no queda tapada por el panel lateral).
   - Clic en área vacía del mapa.
   - Atajo de teclado `Escape` (`Esc`).

---

## 3. Matriz de Validación Triple QA Gate

| Instancia | Evaluación Realizada | Resultado | Dictamen |
| :--- | :--- | :--- | :---: |
| **QA 1: Técnico & Performance** | Unificación en single Canvas Renderer, carga de 18.721 manzanas + 17.954 polígonos separados a 60 FPS, eliminación de llamadas 403 y resolución de pointer-events. | 0 errores en consola; respuesta inmediata en drag, zoom y clicks. | **APROBADO** |
| **QA 2: Negocio EPEC & Cartografía** | Cobertura total de 585.727 suministros, 3.299 rutas, 20 ciclos de facturación, semaforización de capacidad (160–200) y segmentación rigurosa de polígonos $\le 10\text{ ha}$. | 100% de los datos mapeados; trazado de calles nítido y legible. | **APROBADO** |
| **QA 3: Usabilidad & UX** | Verificación de las 5 opciones de deselección, alternancia fluida de selección directa entre rutas, atajos `Ctrl+Scroll`, `Esc`, `+`, `−`, y responsive glassmorphic. | Flujo de inspección continuo sin interrupciones de puntero. | **APROBADO** |

---

## 4. Archivos y Rutas de Despliegue

- **Visor de Control Directo**:
  - `D:\Usuarios\jidiaz\Downloads\visor_rutas_poligonos_distrito1.html`
  - `C:\Users\jidiaz\Downloads\visor_rutas_poligonos_distrito1.html`
- **Visor Integral SIGEC**:
  - `D:\Usuarios\jidiaz\Downloads\visor_manzanas_rutas\index.html`
  - `C:\Users\jidiaz\Downloads\visor_manzanas_rutas\index.html`
- **Datasets Procesados**:
  - `data/rutas_poligonos_data.js` (17.954 polígonos separados)
  - `data/manzanas_rutas_data.js` (18.721 manzanas catastrales oficiales)
- **Scripts de Generación en Repositorio**:
  - `scripts/procesar_rutas_poligonos_separados.py`
  - `scripts/generar_visor_rutas_poligonos_distrito1.py`
  - `scripts/actualizar_visor_manzanas_rutas.py`
