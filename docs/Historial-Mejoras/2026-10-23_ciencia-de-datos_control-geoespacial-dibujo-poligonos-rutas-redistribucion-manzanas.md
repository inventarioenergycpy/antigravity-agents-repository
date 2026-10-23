# Control Geoespacial de Rutas, Dibujo de Polígonos de Manzanas y Redistribución Disjunta - Distrito 1 (EPEC)

- **Fecha:** 2026-10-23
- **Agente:** Agente 02 - Ciencia de Datos (Supervisado por Agente 11 - Copiloto Orquestador)
- **Repositorio:** `PROTELEM-EPEC/sigec-ruta-nueva-catastro-georef`
- **Distrito:** 1 (Córdoba Capital y Gran Córdoba)
- **Universo:** 585.727 suministros / 18.771 manzanas catastrales / 3.299 rutas homogéneas

---

## 1. Contexto y Nuevos Requerimientos

A fin de garantizar que las nuevas rutas de lectura no solo cumplan con la capacidad de carga ($180 \pm 20$ suministros) y la contigüidad de calles internas compartidas, se incorporó un paso adicional de **Control Geoespacial Vectorial**:
1. **Dibujo de Coberturas de Rutas por Manzanas Agrupadas**: Generación de los polígonos unificados (`unary_union`) de cada ruta a partir de las geometrías oficiales de manzanas catastrales (IDECOR).
2. **Control de Parámetros Establecidos**: Verificación de capacidad operativa ($180 \pm 20$), área territorial en hectáreas, perímetro e índice isoperimétrico de compacidad ($4 \pi \cdot \text{Área} / \text{Perímetro}^2$).
3. **Detección de Superposición de Polígonos**: Evaluación mediante índice espacial 2D (`STRtree`) de solapamientos entre rutas adyacentes del mismo grupo cíclico.
4. **Redistribución Geoespacial de Manzanas**: Detección de manzanas atípicas/desplazadas (>2 km de la mediana de su ruta) y reasignación automática a la ruta local más cercana con capacidad disponible, eliminando intersecciones geométricas.

---

## 2. Diagnóstico y Solución Geoespacial

### A. Diagnóstico de Causas de Solapamiento
1. **Suministros Atípicos de Rutas Históricas**: Existían suministros con códigos de ruta histórica que distaban más de 3 km del núcleo de su ruta nueva (arrastrados por inercia de lectura histórica), expandiendo artificialmente el polígono de la ruta a través de la ciudad.
2. **Macro-Manzanas (>200 suministros)**: Conjuntos residenciales y countries (como Docta, Siete Soles o macro-parcelas con más de 1.000 suministros) que abarcan múltiples rutas requerían partición espacial disjunta para evitar que todas las sub-rutas compartieran el macro-polígono exterior completo.
3. **Manzanas Genéricas (000)**: Suministros con nomenclatura catastral incompleta (`11-01-01-01-01-000`) se representaban con un buffer métrico puntual (25 m) en lugar de proyectar el polígono global del ejido.

### B. Algoritmo de Redistribución Geoespacial
- Indexación de centroides de ruta mediante árbol espacial `cKDTree`.
- Detección de **366 manzanas desplazadas** (>2 km de su mediana).
- Reasignación de **1.886 suministros** a su ruta local contigua más cercana respetando el umbral de capacidad ($180 \pm 20$).

### C. Generación Vectorial de Polígonos de Rutas
- Consolidación y disolución de geometrías con `make_valid` y `buffer(0)`.
- Cobertura espacial exportada para **3.299 rutas** de lectura en formato GeoJSON y Parquet.

---

## 3. Artefactos Generados y Sincronizados

1. **Capa Vectorial de Rutas (GeoJSON y Parquet)**:
   - `data/summary/rutas_nuevas_poligonos_distrito1.geojson` (28,6 MB)
   - `data/summary/rutas_nuevas_poligonos_distrito1.parquet`
   - Copia directa en `D:\Usuarios\jidiaz\Downloads\rutas_nuevas_poligonos_distrito1.geojson`
2. **Padrón Maestro Actualizado (585.727 filas, 34 columnas)**:
   - Nuevos campos: `control_superposicion`, `distancia_centroide_ruta_km`, `obs_control_topologico`.
   - Exportado en `C:\Users\jidiaz\Downloads\padron_nuevas_rutas_distrito1_completo.csv` y `D:\Usuarios\jidiaz\Downloads\`.
3. **Script de Producción Automatizado**:
   - `scripts/control_geoespacial_rutas_poligonos_distrito1.py` (Commit `0b9db7e` en GitHub).
