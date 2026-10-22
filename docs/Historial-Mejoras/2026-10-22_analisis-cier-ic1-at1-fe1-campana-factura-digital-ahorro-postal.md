---
title: "Registro Histórico: Diagnóstico Atributos CIER Cuadrante I (IC1, AT1, FE1), Modelo de Ahorro Correo F-218 y Campaña de Captación de Factura Digital"
fecha: 2026-10-22
agentes:
  - "[[docs/Agentes/01-Analista-Financiero|Agente 01 - Analista Financiero]]"
  - "[[docs/Agentes/02-Ciencia-de-Datos|Agente 02 - Ciencia de Datos]]"
  - "[[docs/Agentes/03-Desarrollador-Web-Showroom|Agente 03 - Desarrollador Web Showroom]]"
  - "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Agente 06 - Arquitecto de Sistemas EPEC]]"
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Agente 11 - Copiloto Orquestador]]"
proyecto: "encuesta-cier-epec"
tags:
  - #historial-mejora
  - #cier
  - #ic1
  - #at1
  - #fe1
  - #factura-digital
  - #op-26211
  - #f218
  - #campaña-comercial
  - #ahorro-correo
---

# 📜 Registro Histórico: Diagnóstico Atributos CIER Cuadrante I (IC1, AT1, FE1), Modelo de Ahorro Correo F-218 y Campaña de Captación de Factura Digital

## 1. Contexto y Objetivos de la Sesión
A solicitud del usuario, se profundizó en la resolución de los tres atributos más críticos de la **Encuesta CIER EPEC (Cuadrante I - Foco Urgente)**:
1. **`IC1` (Aviso cortes programados)** y **`AT1` (Canales de contacto)**: Auditoría de canales masivos (Instagram, Twitter/X, Facebook, Web) para diagnosticar por qué el usuario no logra saber si su suministro está afectado y el consecuente colapso de las líneas telefónicas (0800).
2. **`FE1` (Plazo entre recepción y vencimiento)**: Análisis de ordenativos en SIGEC (`RN`, `RO`, `RC`) para entender los reclamos generados por la factura papel de OCASA (O.P. 26211 / F-218).
3. **Modelado Financiero de Ahorro por Factura Digital (`SIM`)**: Cálculo del costo postal por suministro y simulación de escenarios de ahorro anual eliminando el franqueo físico.
4. **Análisis de Sensibilidad de Costos de Mensajería**: Evaluación del costo unitario de WhatsApp a **$ 5.000 ARS**, demostrando su inviabilidad como canal saliente masivo (+1.394% más caro que el correo papel).
5. **Diseño de Campaña de Captación sobre la Base de 922.958 Titulares**: Segmentación y cálculo de ROI activando el 40% de titulares con celular mediante SMS 1-clic y Ciudadano Digital (CiDi).

---

## 2. Documentos y Entregables Técnicos Generados

Se elaboraron y estructuraron tres informes maestros en la Bóveda de Obsidian (`docs/Proyectos/`):

1. **[`docs/Proyectos/2026-10-22_analisis-critico-cier-ic1-at1-fe1-sigec-redes.md`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Proyectos/2026-10-22_analisis-critico-cier-ic1-at1-fe1-sigec-redes.md)**:
   - Anatomía de las publicaciones de EPEC en redes sociales ("Trabajos por Mejoras").
   - Diagnóstico de la desconexión eléctrica (SET / Alimentador) vs. geográfica (barrial/catastral) y la ausencia de búsqueda por NIS/Contrato.
   - Vínculo causal con el colapso de `AT1` (re-llamadas masivas al 0800 y apertura de órdenes `RO` por cortes programados no advertidos).
   - Casuística de los ordenativos `RN` (no recepción), `RC` (sucursal) y `RO` (web) frente a la factura física.
   - Plan de 5 palancas para la migración a Factura Digital (`SIM`).

2. **[`docs/Proyectos/2026-10-22_estimacion-ahorro-financiero-factura-digital-epec.md`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Proyectos/2026-10-22_estimacion-ahorro-financiero-factura-digital-epec.md)**:
   - Parámetros contractuales auditados de la O.P. 26211: Impresión ($ 39,57 s/IVA) + Distribución ($ 236,98 s/IVA) = **$ 276,55 s/IVA** (**$ 334,63 c/IVA**) por factura papel.
   - **Costo Anual de Correo por Suministro**: **$ 4.015,51 c/IVA al año** (12 facturas).
   - Gasto Anual Actual de Correo Facturas: **$ 2.672,28 Millones de Pesos c/IVA** (7.985.884 piezas).
   - Sensibilidad WhatsApp a $ 5.000: Demostración del sobrecosto de +$ 37.257 Millones si se utilizara como push masivo (14,94 veces más caro que el correo de OCASA).
   - Solución multicanal de costo marginal cero: Email + Notificaciones Push en App Móvil EPEC + Web.
   - Ahorro Neto Anual para EPEC: **$ 1.603 Millones de Pesos** (con 60% de digitalización) y **$ 2.271 Millones** (régimen 85% papel por excepción).

3. **[`docs/Proyectos/2026-10-22_estrategia-campana-captacion-factura-digital.md`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Proyectos/2026-10-22_estrategia-campana-captacion-factura-digital.md)**:
   - Radiografía del padrón de 922.958 titulares:
     - 40,0% con celular (369.080): 270.710 solo celular + 98.370 celular y fijo.
     - 36,1% solo fijo (332.991).
     - 23,9% sin teléfono (220.887).
   - Campaña SMS 1-clic tokenizada ($ 12/envío) + CiDi Push (Costo $0): Inversión de $ 4,43 M para convertir 92.270 suministros y ahorrar **$ 370,51 Millones al año** (Payback: 4,4 días).
   - Captura en segmentos 2 y 3: Cruce gratuito con padrón CiDi (Gobierno de Córdoba), IVR saliente y QR dinámico con token de contrato en la propia factura papel de OCASA.
   - Balance global Fase 1: Inversión de **$ 9,73 M**, conversión de **154.318 suministros (16,7%)** y ahorro anual generado de **$ 619,67 Millones de Pesos** (Payback total: 5,7 días).

---

## 3. Impacto en la Bóveda y Metodología en 6 Etapas
- **Fase 1 (Investigación)**: Datos contractuales de la OP 26211 y publicaciones reales de EPEC en redes auditadas.
- **Fase 2 (Diseño)**: Fórmulas de unit economics por suministro y funnel de conversión por canal.
- **Fase 3 (Pruebas Parciales)**: Modelado de escenarios de sensibilidad a diferentes costos de mensajería (SMS $12 vs WA $5.000).
- **Fase 4 (Prueba Piloto)**: Presentación al usuario con aprobación explícita (*"está muy bueno, documentar todo y cargar"*).
- **Fase 5 (Pruebas Finales)**: Validación de balances y cuadres contra F-218 y tabla de contratos.
- **Fase 6 (Auto-Documentación y Carga)**: Asentamiento del presente registro, actualización del MOC y commit/push al repositorio remoto.
