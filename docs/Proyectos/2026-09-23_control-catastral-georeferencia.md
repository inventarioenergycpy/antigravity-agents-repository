# Proyecto: Control de Relevamiento Catastral & Auditoría Espacial WFS (EPEC)

**Fecha**: 2026-09-23  
**Agente Líder**: `ciencia-de-datos`  
**Repositorio Dedicado**: [`https://github.com/inventarioenergycpy/control-catastral-georeferencia`](https://github.com/inventarioenergycpy/control-catastral-georeferencia)  
**Estado**: Activo / En Producción  

---

## 🎯 Objetivo y Alcance

Auditoría integral, corrección evolutiva y validación espacial de medidores eléctricos relevados en campo por contratistas de EPEC, cruzándolos contra las capas oficiales del geoservicio WFS provincial (`EPEC:vm_vt_parcelas_subestacion`, `EPEC:t_subestaciones_poly_union_ok` y `EPEC:vt_parcelas_union`).

El proyecto abarca el relevamiento de 3 subestaciones críticas:
1. **SET 1000-0249** (Detalle #4314): 321 registros (Circunscripción 15, Secciones 05 y 07).
2. **SET 1000-4223** (Detalle #4268): 150 registros (Circunscripción 16, Sección 32).
3. **SET 1000-4225** (Detalle #4271): 81 registros (Circunscripción 16, Sección 32 - Barrio Manzana 139).

---

## 📊 Métricas de Validación Espacial (552 Registros)

| Subestación | Total Registros | Georreferenciados | Coincide Original | Corregido 1ra Etapa | Ajustado WFS | Asociación SET WFS |
|---|---|---|---|---|---|---|
| **SET 1000-0249** | 321 | 297 (92.5%) | 200 | 0 | 97 | 294 dentro / 3 a <8m |
| **SET 1000-4223** | 150 | 150 (100%) | 122 | 19 | 9 | 100% dentro del polígono |
| **SET 1000-4225** | 81 | 81 (100%) | 49 | 1 | 31 (Mza 139) | 100% dentro del polígono |
| **TOTAL UNIFICADO** | **552** | **528 (95.7%)** | **371 (67.2%)** | **20 (3.6%)** | **137 (24.8%)** | **Validación Espacial 100%** |

---

## 🗺️ Componentes Principales

1. **Dashboard GIS Interactivo (`index.html`)**:
   - Selector de subestaciones (`Todas`, `0249`, `4223`, `4225`).
   - Visualización de contornos de subestación (`EPEC:t_subestaciones_poly_union_ok`).
   - Visualización de 965 parcelas vectoriales oficiales (`EPEC:vm_vt_parcelas_subestacion`).
   - Selector temporal de 3 etapas (*1. Original*, *2. 1ra Corrección*, *3. Validación WFS*).
   - Tabla de datos sincronizada con búsqueda en tiempo real y zoom bidireccional.
2. **Entregables de Planillas Excel**:
   - `ConectarRelevados_Detalle_de_Subestacion_#4314_-_1000-0249_CORREGIDO_WFS.xlsx` (97 modificaciones resaltadas).
   - `ConectarRelevados_Detalle_de_Subestacion_#4268_-_1000-4223_CORREGIDO_WFS.xlsx`
   - `ConectarRelevados_Detalle_de_Subestacion_#4271_-_1000-4225_CORREGIDO_WFS.xlsx`
   - `Cruce_Espacial_Geoservicio_WFS_SET_4223_4225_0249.xlsx` (Matriz maestra de auditoría multietapa).

---

## 🔑 Credenciales del Geoservicio WFS

- **URL**: `https://maaysp-ws.cba.gov.ar/EPEC/wfs`
- **Usuario**: `EPEC_comercial`
- **Contraseña**: `Bratis-c0m3rc14l`
- **Capas Activas**: `EPEC:t_subestaciones_poly_union_ok`, `EPEC:vm_vt_parcelas_subestacion`, `EPEC:vt_parcelas_union`
