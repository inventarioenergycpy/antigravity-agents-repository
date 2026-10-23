# Control Topológico, Enriquecimiento de Manzanas con Alturas y Auditoría Geográfica Distrito 1 (EPEC)

- **Fecha:** 2026-10-23
- **Agente:** Agente 02 - Ciencia de Datos (Supervisado por Agente 11 - Copiloto Orquestador)
- **Repositorio:** `PROTELEM-EPEC/sigec-ruta-nueva-catastro-georef`
- **Distrito:** 1 (Córdoba Capital y Gran Córdoba)
- **Universo:** 585.727 suministros / 18.771 manzanas catastrales / 3.300 rutas homogéneas

---

## 1. Contexto y Objetivos

A partir del requerimiento operativo de optimización de rutas de lectura y saneamiento de información cadastral/geográfica:
1. **Control Topológico de Manzanas en Rutas**: Evitar que una ruta contenga manzanas periféricas o peninsulares con 3 o más calles perimetrales exteriores (obligando a una fuerte integración interna con al menos 2 calles compartidas).
2. **Control de Coincidencia de Calles y Triangulación con 2 Vecinos**: Identificar suministros cuya calle declarada en SIGEC no coincida con las calles perimetrales de su manzana catastral, aplicando triangulación secuencial en el orden de lectura con **al menos 2 vecinos** para consolidar su ubicación verdadera y reasignar la manzana/ruta según corresponda.
3. **Auditoría de Georreferencia (+-70 metros)**: Validar la distancia métrica entre las coordenadas registradas del suministro y la posición estimada de la dirección (cruzando los tramos de ejes municipales oficiales `EPEC:tramodecalle_muni` con alturas iniciales/finales y centroides de manzana).
4. **Propiedades Extendidas de Manzanas (Calles y Alturas)**: Construir un catálogo maestro dimensional de manzanas (`maestro_manzanas_calles_alturas`) con las calles perimetrales y sus rangos de numeración `[altura_min - altura_max]`, embebiendo además este atributo en el padrón maestro de suministros.

---

## 2. Implementación Metodológica

### A. Extracción y Normalización de Ejes Municipales
- Descarga y almacenamiento en caché WGS84 de la capa oficial de GeoServer EPEC: `EPEC:tramodecalle_muni` (54.232 tramos) en `data/tramodecalle_muni_4326.parquet`.
- Atributos indexados: nombre normalizado sin prefijos (`norm_street`), altura inicial/final impar y par, y punto medio métrico.

### B. Catálogo Maestro de Manzanas (`maestro_manzanas_calles_alturas`)
- Consolidación de **18.771 manzanas catastrales únicas**.
- Atributos por manzana:
  - `mza_wfs`: Nomenclatura catastral oficial de 16 caracteres (`11-01-01-XX-YY-ZZZ`).
  - `cant_suministros`: Total de servicios conectados.
  - `centroide_lat`, `centroide_lon`: Coordenadas medias del polígono.
  - `cant_calles_perimetro`: Cantidad de calles que circundan la manzana.
  - `calles_perimetrales`: Lista de nombres de calles.
  - `mza_calles_con_alturas`: Rango estructurado de numeración por calle (ej. `ONOFRE MARIMON [7200-7299]`).

### C. Triangulación de Consenso con 2 Vecinos
- Búsqueda binaria (`bisect`) en la secuencia ordenada por `orden_actual` de la misma `ruta_actual`:
  - Se examina la ventana inmediata de +/- 5 vecinos de lectura.
  - Si 2 vecinos leen la misma calle y su manzana catastral sí contiene esa calle en WFS, se consolida la reasignación de la manzana y se documenta en `obs_reasignacion_calle` y `motivo_asignacion_analisis`.

### D. Auditoría de Georreferencia (+-70 metros)
- Cálculo métrico euclidiano de dispersión:
  - Distancia punto a eje municipal con rango de altura coincidente.
  - Distancia punto a centroide de manzana asignada.
  - `distancia_desfase_m`: Mejor distancia de aproximación.
  - `alerta_georef`: `OK (<=70m)` (78,0%), `DESFASADA (>70m)` (21,7%), `SIN_COORDENADAS` (0,3%).

---

## 3. Artefactos Generados y Sincronizados

1. `sigec-ruta-nueva-catastro-georef/data/summary/padron_nuevas_rutas_distrito1_completo.parquet` (585.727 filas, 31 columnas).
2. `sigec-ruta-nueva-catastro-georef/data/summary/maestro_manzanas_calles_alturas.parquet` y `.csv` (18.771 manzanas).
3. `C:\Users\jidiaz\Downloads\padron_nuevas_rutas_distrito1_completo.csv`.
4. `D:\Usuarios\jidiaz\Downloads\padron_nuevas_rutas_distrito1_completo.csv`.
5. `D:\Usuarios\jidiaz\Downloads\maestro_manzanas_calles_alturas.csv`.
6. Script de producción: `scripts/escalar_rutas_control_completo_distrito1.py`.
