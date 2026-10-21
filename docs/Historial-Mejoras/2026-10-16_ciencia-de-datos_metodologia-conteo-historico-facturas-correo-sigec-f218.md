---
title: "Registro Histórico: Metodología y Suite SQL para Conteo Histórico de Facturas Enviadas al Correo (SIGEC / F-218 / OP)"
fecha: 2026-10-16
agentes:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos & BI]]"
  - "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto de Sistemas EPEC]]"
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]]"
tipo: "desarrollo-sql-metodologia"
tags:
  - #historial
  - #sigec
  - #facturacion
  - #correo
  - #f218
  - #liquidacion-op
---

# 📝 Registro de Mejora: Metodología de Conteo Histórico de Facturas Impresas Enviadas al Correo en SIGEC (Conciliación F-218 y Liquidación OP)

## 1. Contexto y Problemática
El conteo de contratos con `CNT_TIPO_IMPRESION = 'EST'` en la tabla maestra `XXSIGEC.CONTRATOS` refleja únicamente el estado actual y no el momento en que se facturó. Esto subestima o distorsiona las cantidades devengadas en las rendiciones mensuales del Formulario F-218 frente a las Órdenes de Provisión (OP 23100, OP 25238, OP 26211).

## 2. Acciones Realizadas
1. **Inspección de las Planillas de Control de Gestión en Red**:
   - `\\srvfs01\Control_de_Gestion\DEPARTAMENTO FACTURACION\CORREO DEL INTERIOR\LIQUIDACION_CORREO_2025.xls`
   - `Resumen_Detalle_F218.xlsx`
   - `Detalle y Evol Fact y Notif 2023 al 2026.xlsx`
   - Identificación de los precios unitarios y volúmenes por ítem (Ítem 1 Impresión, Ítem 3 Distribución).
2. **Diseño de Solución Técnica Dual en Oracle SIGEC**:
   - **Enfoque Transaccional (`XXSIGEC.DOCUMENTOS`)**: Basado en `DOC_ENVIADO_CORREO IS NOT NULL`, `CODIGO_MODELO_IMPRESION_XML` y `DOC_FECHA_EMISION`.
   - **Enfoque Point-in-Time (`XXSIGEC.CONTRATOS_JN`)**: Cruce temporal analítico con el Journal histórico de contratos para reconstruir el `CNT_TIPO_IMPRESION` a la fecha exacta de emisión.
3. **Generación de Entregables**:
   - Script SQL maestro: [`scripts/consulta_sigec_historico_facturas_correo_f218.sql`](file:///D:/Proyectos/antigravity-agents-repository/scripts/consulta_sigec_historico_facturas_correo_f218.sql).
   - Documento técnico: [`docs/Proyectos/2026-10-16_sigec_metodologia-conteo-historico-facturas-correo-f218.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/Proyectos/2026-10-16_sigec_metodologia-conteo-historico-facturas-correo-f218.md).


### Actualización Ítem 4 (Notificaciones e Intimaciones):
- Integración de la tabla `XXSIGEC.SEGUIMIENTO_IMP_VARIOS` para el conteo y auditoría del Ítem 4 en la F-218.
- Clasificación de tipologías `IN`, `IA`, `IG`, `NE`, `ND`, `NO`, `NC`.
- Creación de la suite SQL dedicada: `scripts/consulta_sigec_item4_notificaciones_intimaciones_f218.sql`.

### Estado de Cierre de Sesión (2026-10-16):
- **Dictamen del Usuario**: El análisis no es concluyente y debe continuar a futuro.
- **Acción**: Se preservan las consultas y evidencias elaboradas (`scripts/consulta_sigec_historico_facturas_correo_f218.sql`, `scripts/consulta_sigec_item4_notificaciones_intimaciones_f218.sql`, `scripts/consulta_sigec_control_2026_item3_facturas_f218.sql`), catalogando el proyecto con estado abierto y registrando la hoja de ruta de validaciones pendientes.