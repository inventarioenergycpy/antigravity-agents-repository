# Mejora Continua: Control de Relevamiento Catastral, Geoservicio WFS y Prioridad Normativa (Ley 5.057)

- **Fecha**: 2026-09-23
- **Agente**: `ciencia-de-datos`
- **Área**: GIS, Auditoría Catastral, OGC WFS y Visualizadores Web Interactivos

## Resumen de la Mejora
Se incorporó al agente de Ciencia de Datos la capacidad especializada de:
1. **Auditoría y Cruce Catastral Evolutivo en 3 Etapas**: Control de relevamiento en crudo, aplicación de correcciones tabulares y validación espacial definitiva.
2. **Conexión a Geoservicios WFS OGC**: Extracción programática de capas vectoriales (`EPEC:vm_vt_parcelas_subestacion`, `EPEC:vt_parcelas_union`) mediante `DescribeFeatureType`, filtros CQL (`cql_filter`) y manejo de proyecciones cartográficas (`EPSG:4326` a `EPSG:22174`).
3. **Descomposición Normativa de Nomenclatura Catastral (Córdoba)**:
   - Estructura unificada de 16 dígitos: `DD-PP-LL-CC-SS-MMM-PPP` (Ley N° 5.057 y Resoluciones Normativas de Catastro y Rentas).
   - **Regla de Prioridad Funcional**: Prevalencia de la Manzana y Lote explícitos en la dirección del relevamiento y SIGEC para resolver desajustes de precisión GPS.
4. **Cruce Espacial Point-in-Polygon (Shapely)**: Verificación geométrica de contención y distancias hacia polígonos parcelarios oficiales.
5. **Visualizadores GIS Interactivos (HTML/CSS/JS standalone)**: Dashboards ejecutivos con Leaflet, cambio dinámico de etapas en tiempo real, inspector lateral de medidor y tabla comparativa vinculada al mapa.
6. **Gestión Segura de Credenciales WFS**: Registro centralizado de accesos a geoservicios provinciales.

## Proyectos Vinculados
- Repositorio Dedicado: [`control-catastral-georeferencia`](https://github.com/inventarioenergycpy/control-catastral-georeferencia)
- Documentación de Proyecto: `docs/Proyectos/2026-09-23_control-catastral-georeferencia.md`
