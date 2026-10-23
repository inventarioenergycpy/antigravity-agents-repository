---
title: "Ciencia de Datos - Reasignación de Rutas de Lectura Conexas, Maximización de Calles Compartidas y Escalamiento Distrito 1"
fecha: 2026-10-23
agente: "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos y BI EPEC]]"
tipo: "mejora_algoritmo"
tags:
  - #historial-mejoras
  - #ciencia-de-datos
  - #ruteo-conexo
  - #calles-compartidas
  - #catastro
  - #sigec
  - #wfs
  - #distrito-1
backup: "[[docs/Backups/2026-10-23_085000_ciencia-de-datos_SKILL.md.bak]]"
---

# Registro de Mejora: Reasignación de Rutas de Lectura Conexas con Maximización de Calles Internas Compartidas (Distrito 1 EPEC)

## 📝 1. Contexto y Diagnóstico del Problema

Al analizar geoespacialmente los resultados del modelo de ruteo previo (basado en un barrido espacial 1D ordenado por circunscripción, sección y coordenadas), se detectó que las manzanas agrupadas por ruta nueva no estaban contiguas unas de otras. En zonas limítrofes entre secciones o con trazados irregulares, el ordenamiento generaba saltos espaciales arbitrarios, forzando al tomador de estado a desplazarse entre bloques desconectados.

El usuario solicitó:
1. Rehacer la asignación de rutas de lectura nuevas asegurando **estricta contigüidad geográfica** entre manzanas.
2. Enriquecer el **Código de Trazabilidad Catastral** incorporando la geoposición de la manzana y las calles que la rodean.
3. Diseñar la agrupación de forma tal que las manzanas dentro de una misma ruta **compartan la mayor cantidad posible de calles internas perimetrales**, optimizando el recorrido peatonal en ambas aceras.

---

## 🛠️ 2. Arquitectura de Solución Implementada (Metodología en 6 Etapas)

### A. Capa de Datos e Índice Invertido Vial
* Se integró la capa WFS provincial oficial `EPEC:vm_manzanas_calles_new` (30.230 manzanas con ~4 calles perimetrales cada una).
* Se complementó el universo no digitalizado mediante las calles registradas en las direcciones postales de los suministros en `georef.vw_suministros`, logrando una **cobertura del 100% de manzanas con sus calles asociadas** (promedio: 10,0 nombres de calle por manzana en la trama urbana).

### B. Algoritmo de Agrupamiento Conexo Ponderado (Seed & Expand con Grafo de Calles)
* **Función de Afinidad Topológica:**
  $$\text{Score}(C, R) = 50.000 + (|S(C) \cap S(R)| \times 10.000) - \text{Distancia\_Metros}$$
  donde $S(C)$ son las calles del candidato y $S(R)$ son las calles acumuladas de la ruta actual.
* **Prioridad Vial Absoluta:** Se priorizan drásticamente candidatos adyacentes que compartan 1, 2 o más calles perimetrales antes de considerar distancia euclidiana pura.
* **Cierre de Ruta y Restricción de Capacidad:**
  - Capacidad objetivo: **180 suministros/ruta** (Tolerancia: [160, 200]).
  - Tratamiento de Macro-manzanas individuales (> 200 suministros) con particionamiento equitativo interno.

### C. Código de Trazabilidad Catastral Enriquecido (`CTC-GEO`)
Se estructuró el identificador canónico jerárquico:
```text
1-{GRUPO}-{DPPO}-{PED}-{PUEB}-{CIRC}-{SECC}-{MZA}-{PARC}-{GEO_QUAD}
Ejemplo: 1-16-11-01-01-31-04-003-018-Q31416418
```
Junto con los atributos explícitos en el padrón:
* `geo_centroide_lat` / `geo_centroide_lon`: Baricentro de coordenadas de la manzana.
* `geo_quad`: Celda territorial de 500m × 500m.
* `cant_calles_perimetro` y `calles_perimetrales_mza`: Catálogo de calles que delimitan la manzana.
* `cant_calles_compartidas` y `calles_compartidas_en_ruta`: Listado de calles internas compartidas entre las manzanas de la ruta.
* `tipo_contiguidad`: `CONEXA` | `INDIVIDUAL` | `MACRO_MANZANA`.
* `orden_lectura_sugerido`: Secuencia optimizada de toma de estado.

---

## 📊 3. Resultados Globales del Escalamiento (Distrito 1 Completo)

El motor batch procesó los **20 grupos cíclicos regulares** en **3,62 minutos**, logrando:

| Métrica Consolidada | Modelo Anterior (1D Sweep) | **Nuevo Modelo Conexo (Calles Compartidas)** | Impacto Operativo |
| :--- | :---: | :---: | :--- |
| **Suministros Totales Procesados** | 585.472 | **585.727** | **100% Cobertura (0 huérfanos)**. |
| **Total de Rutas Nuevas** | 3.669 rutas | **3.300 rutas** | Consolidación más compacta (-369 rutas). |
| **Media Global Suministros/Ruta** | 159,6 sum/ruta | **177,4 sum/ruta** | **Alineado al target ideal de 180**. |
| **Contigüidad Espacial** | ❌ Saltos de sección | **✅ 100% Contigua** | Clusters geográficos compactos. |
| **Calles Compartidas (Multi-Mza)** | *No medido / Disperso* | **10,16 calles/ruta** | **Recorrido peatonal en ambas aceras**. |
| **Tiempo Total de Cómputo** | 4,2 min | **3,62 minutos** | Alta eficiencia algorítmica. |

---

## 📦 4. Entregables Generados

1. **Padrón Maestro Completo en Descargas:**
   - `C:\Users\jidiaz\Downloads\padron_nuevas_rutas_distrito1_completo.csv` (105,4 MB, 585.727 filas).
2. **Copia de Alto Rendimiento en Parquet:**
   - `D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\padron_nuevas_rutas_distrito1_completo.parquet` (32,8 MB).
3. **Resúmenes Ejecutivos:**
   - `D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\resumen_todas_rutas_nuevas_distrito1.csv` (3.300 rutas con detalle de calles compartidas).
   - `D:\Proyectos\sigec-ruta-nueva-catastro-georef\data\summary\resumen_comparativo_grupos_distrito1.csv` (indicadores comparativos por grupo).
4. **Scripts Versionados:**
   - `D:\Proyectos\sigec-ruta-nueva-catastro-georef\scripts\escalar_nuevas_rutas_distrito1.py`.
   - `D:\Proyectos\sigec-ruta-nueva-catastro-georef\scripts\test_ruteo_conexo_g16.py`.

---

## 🛡️ 5. Resguardo Preventivo y Rollback

* **Copia de Seguridad Preventiva:** `docs/Backups/2026-10-23_085000_ciencia-de-datos_SKILL.md.bak`.
* **Habilidades Actualizadas:** `.agents/skills/ciencia-de-datos/SKILL.md` y `docs/Agentes/02-Ciencia-de-Datos.md`.
