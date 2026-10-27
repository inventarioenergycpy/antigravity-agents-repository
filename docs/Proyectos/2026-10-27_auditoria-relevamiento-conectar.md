---
type: proyecto
proyecto: "Auditoría de Relevamientos CONECTAR: Reglas de Negocio y Resolución SIGEC"
organizacion: "PROTELEM-EPEC"
repositorio_remoto: "https://github.com/PROTELEM-EPEC/auditoria-relevamiento-conectar"
ruta_local: "D:\Proyectos\auditoria-relevamiento-conectar"
rama_activa: "main"
agente_responsable: "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|11 - Copiloto Orquestador]] & [[docs/Agentes/02-Ciencia-de-Datos|02 - Ciencia de Datos]]"
fecha_creacion: 2026-10-27
tags:
  - #proyecto
  - #protelem
  - #epec
  - #conectar
  - #auditoria
  - #medidores
  - #sigec
  - #reglas-de-negocio
---

# ⚡ Proyecto: Auditoría de Relevamientos CONECTAR (PROTELEM-EPEC)

- **Repositorio Remoto**: [https://github.com/PROTELEM-EPEC/auditoria-relevamiento-conectar](https://github.com/PROTELEM-EPEC/auditoria-relevamiento-conectar)
- **Ruta Local**: `D:\Proyectos\auditoria-relevamiento-conectar`
- **Archivo de Campo Fuente**: `D:\Usuarios\jidiaz\Downloads\Casos con error por relevamiento CONECTAR.xlsx` (Hoja: `'Matias - Casos de hoy'`)
- **Informe de Salida Enriquecido**: `C:\Users\jidiaz\Downloads\Auditoria_Casos_Error_CONECTAR_SIGEC_2026.xlsx`

---

## 🎯 Resumen Ejecutivo

Sistema integral de auditoría, catalogación de reglas de negocio y diagnóstico algorítmico sobre una muestra de **1.348 medidores observados con error** en el relevamiento de campo realizado por la contratista **CONECTAR** para EPEC.

El proyecto formaliza por qué se producen las discrepancias en terreno (errores humanos de tipeo, reemplazos de medidores por guardias sin registrar, desfases toponímicos y retrasos operativos), articula los cruces masivos contra **Oracle 19c SIGEC** (`XXSIGEC.SERVICIOS`, `GEOREF.VW_SUMINISTROS`, `XXSIGEC.EQUIPOS`, `XXSIGEC.STOCK_EQUIPOS`) y los **Geoservicios WFS**, e implementa un motor de decisión determinista en Python (`audit_conectar_cases.py`) para clasificar el estado de cada suministro.

---

## 📊 Matriz de 19 Tipologías de Error Analizadas (1.348 Casos)

1. **MEDIDOR INEXISTENTE (453 casos - 33.6%)**: Series de medidor que no existen en `STOCK_EQUIPOS` (frecuentes errores de digitación de cuadrilla).
2. **LOCALIDAD INVALIDA (298 casos - 22.1%)**: Discrepancia entre la localidad declarada en campo y el nomenclador `AGF_CODIGO` de EPEC.
3. **MEDIDOR NO COINCIDE (176 casos - 13.1%)**: El medidor montado físicamente no coincide con el contrato activo en `EQUIPOS` (acometidas contiguas cruzadas en nichos dobles).
4. **GRUPO INVALIDO POR CANTIDAD (145 casos - 10.8%)**: Lote que excedió la cuota de carga asignada.
5. **MEDIDOR RETIRADO (84 casos - 6.2%)**: Medidores con baja administrativa en SIGEC pero que siguen presentes en campo.
6. **BARRIO INVALIDO (84 casos - 6.2%)**: Discrepancias con la codificación `BAR_CODIGO` de EPEC.
7. **SUBESTACION INEXISTENTE (33 casos - 2.4%)**: SET declarada difiere de `srv_subestacion_tec`.
8. **OTROS (75 casos - 5.6%)**: Localidad/Barrio inválido (14), Altura nula (13), Casos vuelta atrás (10), Duplicados (15), Zona, DC, DPP, Ilegible, Sin SET (6).

---

## 📚 Documentación Técnica en el Repositorio Dedicado

- [`docs/01_contexto_y_problematica_relevamiento.md`](file:///D:/Proyectos/auditoria-relevamiento-conectar/docs/01_contexto_y_problematica_relevamiento.md): Qué es el relevamiento y por qué se producen discrepancias.
- [`docs/02_arquitectura_datos_y_origenes.md`](file:///D:/Proyectos/auditoria-relevamiento-conectar/docs/02_arquitectura_datos_y_origenes.md): Tablas Oracle 19c, diccionario de campos y WFS.
- [`docs/03_catalogo_reglas_de_negocio.md`](file:///D:/Proyectos/auditoria-relevamiento-conectar/docs/03_catalogo_reglas_de_negocio.md): Árboles de decisión, heurísticas de tipeo y matriz de resolución.
- [`docs/04_algoritmo_de_cruce_y_diagnostico_sigec.md`](file:///D:/Proyectos/auditoria-relevamiento-conectar/docs/04_algoritmo_de_cruce_y_diagnostico_sigec.md): Estrategia de chunking <= 900 y optimización en memoria.
- [`docs/05_guia_operativa_agentes_ia_y_mejora_continua.md`](file:///D:/Proyectos/auditoria-relevamiento-conectar/docs/05_guia_operativa_agentes_ia_y_mejora_continua.md): Manual para Agentes IA (Zero Vibes QA, Blackboard, Hand-offs).
