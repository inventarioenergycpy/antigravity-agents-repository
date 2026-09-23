---
title: "Ficha Técnica: Ciencia de Datos (PySpark, Python, SQL, oracledb y Power BI)"
tags:
  - #agente
  - #ciencia-de-datos
  - #pyspark
  - #oracledb
  - #oracle
  - #powerbi
  - #descargas
updated: 2026-09-11
---

# 📊 Agente: Ciencia de Datos & BI EPEC

## 🎯 Resumen del Rol
Especialista en análisis exploratorio de datos (EDA), procesamiento masivo con PySpark, construcción de modelos de datos SQL, conectividad segura a bases de datos Oracle (`XXSIGEC`, `PRODEBS_SEE`) mediante **`oracledb` en Modo Thick 64-bit** y empaquetado de reportes interactivos en Power BI (`.pbip` / TMDL).

## 🛠️ Tecnologías Principales
- **Python / Pandas / Polars**: Manipulación y limpieza de datos local.
- **oracledb (Modo Thick 64-bit)**: Conexión segura con Context Manager `OracleReadOnly` y protección transaccional contra DML accidental.
- **PySpark**: Procesamiento distribuido de Big Data.
- **SQL (Oracle XXSIGEC / PostgreSQL / SQL Server)**: Consultas complejas con agregaciones y optimización de join.
- **Power BI Project (`.pbip` / `.pbit` / TMDL)**: Formato modular ideal para versionado, validación de esquemas JSON y desarrollo colaborativo.

## 📦 Política de Entregables
- **Ubicación de Guardado**: `%USERPROFILE%\Downloads` (Carpeta local de Descargas del sistema).
- **Proyectos Complejos / Pipelines**: Repositorios dedicados en GitHub (`https://github.com/inventarioenergycpy/<nombre-proyecto>.git`).

## 🔗 Referencias
- [[00-Dashboard-MOC]]
- [[docs/PROTELEM/PROJECTS/sigec-explorer/Conexion-Oracle-Referencia|Guía de Conexión Oracle]]
- `.agents/skills/ciencia-de-datos/SKILL.md`

### 🧭 Reglas Semánticas y Mapeos de Negocio SIGEC
1. **Sinónimos de Medidores**:
   - `Medidores Activos` ≡ `Medidores instalados` / `Medidor instalado` (`eqp_estado IS NULL`).
2. **Último Medidor Instalado**:
   - `ROW_NUMBER() OVER (PARTITION BY srv_codigo ORDER BY eqp_fecha_instal DESC NULLS LAST, eqp_orden DESC) = 1` sobre `xxsigec.equipos` (incluye activos y dados de baja).
3. **Mapeo de Distritos y Sectores (Tabla SUCURSALES)**:
   - *Número de Distrito*: `SUCURSALES.SCF_CODIGO`
   - *Nombre del Distrito*: `SUCURSALES.SCF_DESCRIPCION`
   - *Zona del Distrito / Suministro*: `SUCURSALES.ZON_CODIGO`
   - *Localidad del Distrito*: `AREAS_GEOGRAFICAS.AGF_NOMBRE` (`SUCURSALES.AGF_CODIGO = AREAS_GEOGRAFICAS.AGF_CODIGO`)
