---
title: "Registro Histórico: Diagnóstico de Atributos Foco CIER (IC1, AT1, FE1), Cronograma SIGEC y Casuística RO/RC/NT/ERSeP"
fecha: 2026-10-21
agentes:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
  - "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto de Sistemas EPEC]]"
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]]"
tipo: "analisis-estadistico-y-sigec"
tags:
  - #historial
  - #cier
  - #sigec
  - #cronograma-facturacion
  - #reclamos-ro-rc
  - #notificaciones-nt
  - #ersep
---

# 📦 Registro de Implementación: Diagnóstico Atributos Foco CIER, Cronograma SIGEC y Circuito RO/RC/NT

## 1. Contexto y Objetivos
A solicitud del usuario, en la sesión *"Análisis de Encuesta CIER"*, se realizó un diagnóstico profundo sobre los **tres atributos prioritarios del Cuadrante I (Foco Urgente)** de la Matriz CIER:
1. `IC1`: Notificación previa de interrupciones programadas (IDAT: 58.86%, IR: 5.85%).
2. `AT1`: Facilidad para contactarse con la empresa (IDAT: 58.32%, IR: 5.48%).
3. `FE1`: Plazo entre recepción y fecha de vencimiento (IDAT: 63.12%, IR: 5.11%).

## 2. Hallazgos Principales

### A. Cruces de Microdatos de Encuestas ($N = 1.250$):
- **`AT1` vs. `P263` (FCR)**: El 71.1% de los satisfechos resolvió en el 1º contacto, mientras que el **75.5% de los insatisfechos (notas 1 a 4) sufrió reiteración de contactos ($\ge 2$ veces)**.
- **`FE1` vs. `P250` (Problemas Factura)**: Tasa de problemas con factura **21 veces más alta** en clientes con notas 1-4 (35.6% vs. 1.7%), vinculada a la entrega tardía o vencida de la factura física.
- **`IC1` vs. `P254`**: El 37.4% nunca recibe preaviso de cortes y el 95.7% de los detractores carece de canales digitales de consulta con Horario Estimado de Restitución (ETR).

### B. Cronograma SIGEC y Embudo Postal:
- Parámetro `CRF_DIAS_VENC_1` en `CRONOGRAMAS_FACTURACION` configurado en 12-15 días corridos.
- La logística postal física (OCASA / OP 26211 / F-218) insume entre 8 y 12 días corridos de lead time, comprimiendo el margen del cliente a menos de 5 días hábiles.

### C. Casuística RO vs. RC y Quiebre de Notificaciones NT:
- Convivencia de Reclamos Operativos (`RO` / Web) y Reclamos Comerciales (`RC` / Sucursal).
- Detección de la **"Vía Muerta Comunicacional"**: trámites cerrados internamente que nunca despachan la orden `NT` (Notificación de resultado) al cliente, mientras el sistema envía masivamente por correo intimaciones de deuda (`IN`) y corte (`NC`) en el Ítem 4 de la F-218.
- Escalamiento directo de usuarios desatendidos ante el **ERSeP** (`COMERECLAMOSERSEP.qvd`).

## 3. Entregables y Documentos Generados
- Ficha técnica completa: [`docs/Proyectos/2026-10-21_analisis-cier-atributos-foco-cronograma-sigec-reclamos-ersep.md`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Proyectos/2026-10-21_analisis-cier-atributos-foco-cronograma-sigec-reclamos-ersep.md).
- Prompt de reanudación: [`docs/Proyectos/Prompt-Retomar-Sesion-CIER-Foco-SIGEC.md`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Proyectos/Prompt-Retomar-Sesion-CIER-Foco-SIGEC.md).
- Scripts SQL de soporte:
  - `scripts/consulta_sigec_casuistica_reclamos_ve_ro_rc_2026.sql`
  - `scripts/consulta_sigec_cxi_seguimiento_nt.sql`
  - `scripts/consulta_sigec_item4_notificaciones_intimaciones_f218.sql`
