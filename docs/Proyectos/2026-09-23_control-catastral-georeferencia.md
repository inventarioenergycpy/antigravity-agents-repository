# Proyecto: Control de Relevamiento Catastral y Georreferenciación (Subestaciones 4223 y 4225)

- **Repositorio en GitHub**: [`inventarioenergycpy/control-catastral-georeferencia`](https://github.com/inventarioenergycpy/control-catastral-georeferencia)
- **Fecha de Creación**: 2026-09-23
- **Agente Responsable**: `ciencia-de-datos`
- **Organización / Entorno**: EPEC / Dirección General de Catastro de Córdoba

---

## 🎯 Objetivo del Proyecto
Auditar, corregir y validar de forma integral el relevamiento catastral de 231 suministros eléctricos correspondientes a las Subestaciones **4223** (150 suministros) y **4225** (81 suministros), superponiendo las coordenadas geográficas (`lat`, `lon`) contra el geoservicio WFS oficial de EPEC y aplicando la estructura normativa unificada de nomenclatura catastral (Ley N° 5.057).

---

## 🔐 Parámetros y Credenciales del Geoservicio WFS

- **URL del Servicio**: `https://maaysp-ws.cba.gov.ar/EPEC/wfs`
- **Versión OGC**: WFS 1.1.0 / 2.0.0
- **Usuario**: `EPEC_comercial`
- **Contraseña**: `Bratis-c0m3rc14l`
- **Capas Principales**:
  - `EPEC:vm_vt_parcelas_subestacion` (Materialized view con polígonos parcelarios vinculados a subestaciones `ctmtbt`).
  - `EPEC:vt_parcelas_union` (Capa parcelaria general provincial).
  - `EPEC:t_subestaciones_poly_union_ok` (Polígonos de cobertura de subestaciones).

---

## 📐 Marco Normativo Catastral (Ley N° 5.057)

Estructura secuencial jerárquica de 16 dígitos:
$$\text{11 (Dpto)} - \text{01 (Ped)} - \text{01 (Pue)} - \text{16 (Circ)} - \text{32 (Secc)} - \mathbf{\text{MMM (Manzana)}} - \mathbf{\text{PPP (Parcela/Lote)}}$$

### Regla de Prioridad Funcional:
Cuando en la dirección de relevamiento o en el registro SIGEC conste de forma explícita la **Manzana y Lote** (ej. `MANZANA 139 LOTE 1` al `30`), este dato tiene **prioridad rectora** para definir la nomenclatura catastral unívoca, resolviendo cualquier imprecisión métrica del GPS.

---

## 📦 Entregables Generados en el Repositorio

1. **Dashboard GIS Interactivo (`index.html` / `dashboard_relevamiento_catastral.html`)**:
   - Visualizador web con mapa Leaflet, polígonos de parcelas WFS, selector de 3 etapas en tiempo real, inspector lateral de medidor y tabla comparativa vinculada.
2. **Archivos Excel con Validación Normativa y Espacial (`data/`)**:
   - `ConectarRelevados_Detalle_de_Subestacion_#4268_-_1000-4223_CORREGIDO_WFS.xlsx` (150 registros).
   - `ConectarRelevados_Detalle_de_Subestacion_#4271_-_1000-4225_CORREGIDO_WFS.xlsx` (81 registros).
   - `Cruce_Espacial_Geoservicio_WFS_SET_4223_4225.xlsx` (Matriz de auditoría punto a punto).
3. **Pipeline de Procesamiento en Python (`src/`)**:
   - `wfs_client.py`: Cliente de consulta y descarga de polígonos WFS.
   - `spatial_join.py`: Motor de superposición geométrica point-in-polygon con Shapely.
   - `normative_processor.py`: Motor de asignación de nomenclaturas según Ley 5.057.
   - `generate_reports.py`: Generador de reportes Excel y datasets JSON.
