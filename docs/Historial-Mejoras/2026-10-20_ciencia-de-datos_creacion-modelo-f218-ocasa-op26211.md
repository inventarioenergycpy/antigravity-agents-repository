---
title: "Registro Histórico: Creación y Normalización del Archivo de Datos F-218 OCASA (O.P. 26211)"
fecha: 2026-10-20
agentes:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]]"
tipo: "etl-modelado-datos-f218"
tags:
  - #historial
  - #f218
  - #ocasa
  - #correo-interior
  - #op-26211
  - #power-bi
---

# 📦 Registro de Implementación: Modelo de Datos Normalizado F218 - OCASA (O.P. 26211)

## 1. Contexto y Requerimiento
A solicitud del usuario, se procesaron y estructuraron los datos de liquidación y certificación de correo postal correspondientes a la **O.P. 26211** (Adjudicatario: **ORGANIZACION COURIER ARGENTINA S.A. - OCASA**) a partir de la planilla fuente:
- **Origen**: `LIQUIDACION_CORREO_2025.xls` (Pestaña `O.P. 26211`), ubicada en la carpeta local de Descargas (`D:\Usuarios\jidiaz\Downloads`).
- **Destino Generado**: `F218 - OCASA.xlsx` depositado en la carpeta corporativa de red:
  - `\\srvfs01\ProyectoTelemedicion\38 - Informes Protelem\28-F218\F218 - OCASA.xlsx`
  - Copia de respaldo operativo en Descargas: `D:\Usuarios\jidiaz\Downloads\F218 - OCASA.xlsx`.

## 2. Arquitectura del Modelo de Datos Generado
El archivo implementa el estándar relacional de dos tablas para consumo directo desde **Power BI** (duplicando la especificación técnica de `F218 - EVOLTIS.xlsx`):

### A. Tabla Dimensión: `OP` (4 Líneas Contractuales)
- **Campos**: `OP Nro.` | `Adjudicatario` | `Linea` | `Uni` | `Cantidad` | `Descripcion` | `Precio Unitario` | `Precio Total` | `Fecha Inicio` | `Fecha limite` | `Plazo en meses` | `Sector`
- **Línea 1**: Impresión de Facturas y Notificaciones (19.680.869 unid. a $ 39,57 s/iva = $ 778.772.086,33).
- **Línea 2**: Braille (378 unid. a $ 18.090,41 s/iva = $ 6.838.174,98).
- **Línea 3**: Distribución de Facturas (16.401.126 unid. a $ 236,98 s/iva = $ 3.886.738.839,48).
- **Línea 4**: Distribución de Notificaciones (3.464.892 unid. a $ 377,01 s/iva = $ 1.306.298.938,92).
- **Sector**: `DEPARTAMENTO FACTURACION`. Plazo: 24 meses (01/09/2025 al 31/08/2027).

### B. Tabla de Hechos: `F218` (52 Registros Normalizados)
- **Campos**: `NRO OP` | `NRO F218` | `AÑOMES` | `LINEA` | `CANTIDAD` | `IMPORTE`
- **Granularidad**: 13 períodos liquidados (Septiembre 2025 a Septiembre 2026) x 4 líneas de servicio.
- **Formularios Certificados**: F-218 N° 25998, 26298, 26636, 26937, 27288, 27597, 27956, 28385, 28716, 29101, 29453, 29857 y 30136.

## 3. Matriz de Control y Validación de Totales
- **Cantidad Total de Piezas**: 22.588.442 piezas (Cuadre 100% exacto vs origen).
- **Importe Neto Acumulado s/IVA**: $ 3.478.151.192,02 (Diferencia: $ 0,00).
- **Integridad de Esquema**: Nombres de hojas, encabezados de columnas y tipos de datos idénticos a la plantilla de `F218 - EVOLTIS.xlsx`.
