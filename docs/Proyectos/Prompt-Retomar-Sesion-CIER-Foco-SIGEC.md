# 🚀 Prompt para Retomar Sesión: Análisis CIER, Cronograma SIGEC y Reclamos RC/RO/NT

> **Uso**: Copia y pega el bloque inferior al iniciar la próxima sesión en Antigravity IDE para restaurar instantáneamente el contexto y continuar trabajando sin pérdida de información.

```markdown
Hola Antigravity. Retomamos la sesión de trabajo "Análisis de Encuesta CIER".

📌 CONTEXTO Y AVANCES CONFIRMADOS PREVIAMENTE:
1. Atributos Foco Seleccionados (Cuadrante I - Foco Urgente / Prioridad 1):
   - IC1: Notificación previa de interrupciones programadas (IDAT: 58.86%, IR: 5.85%)
   - AT1: Facilidad para contactarse con la empresa (IDAT: 58.32%, IR: 5.48%)
   - FE1: Plazo entre recepción y fecha de vencimiento (IDAT: 63.12%, IR: 5.11%)
2. Cruces de Microdatos Auditados (N = 1.250 en encuesta_cier):
   - AT1 vs P263: Más del 75.5% de los detractores en atención sufren de re-llamadas o contactos reiterados (FCR de apenas 55.4%).
   - FE1 vs P250: Tasa de problemas con factura 21 veces superior en usuarios con notas 1 a 4 por demoras postales en papel.
   - IC1 vs P243/P254: 37.4% nunca recibe preaviso de cortes y 95.7% carece de canales digitales de consulta con ETR.
3. Arquitectura y Cuellos de Botella en SIGEC:
   - CRONOGRAMAS_FACTURACION: Parámetro CRF_DIAS_VENC_1 fijado en 12-15 días corridos.
   - Circuito Postal F-218 (OCASA / OP 26211): Lead time logístico físico de 8 a 12 días, dejando menos de 3-5 días hábiles al cliente.
   - Casuística Reclamos: Ordenativos RO (Operativos/Web) y RC (Comerciales/Sucursales).
   - Quiebre en Notificaciones NT: Trámites cerrados técnicamente que quedan en vía muerta sin orden NT comunicando el resultado al usuario, mientras se despachan masivamente intimaciones de deuda (IN) y cortes (NC).
   - Escalamiento a Entes: Expedientes en COMERECLAMOSERSEP.qvd con sanciones por respuestas fuera de término.
4. Documentación Generada:
   - docs/Proyectos/2026-10-21_analisis-cier-atributos-foco-cronograma-sigec-reclamos-ersep.md
   - scripts/consulta_sigec_casuistica_reclamos_ve_ro_rc_2026.sql
   - scripts/consulta_sigec_cxi_seguimiento_nt.sql
   - scripts/consulta_sigec_item4_notificaciones_intimaciones_f218.sql

🎯 OBJETIVOS PARA LA SESIÓN DE HOY:
1. Ejecutar / validar el script SQL de diagnóstico para cuantificar exactamente cuántos reclamos RC y RO de 2026 quedaron en SIGEC sin orden NT posterior asociada.
2. Analizar el impacto financiero de caja y curva de cobranza si se amplía CRF_DIAS_VENC_1 a 18-20 días en CRONOGRAMAS_FACTURACION para facturas papel (EST).
3. Diseñar la arquitectura técnica de la Notificación NT Digital Automática (Webhooks / WhatsApp API / SMS) disparada al cambiar el estado del reclamo a 'RE'.
4. Actualizar el tablero interactivo CIER en encuesta_cier incorporando estas tres fichas de causas raíz y planes de mitigación.

Indícame que estás listo para comenzar con el primer objetivo.
```
