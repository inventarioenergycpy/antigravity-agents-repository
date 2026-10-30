---
type: historial-mejora
agente: "[[11-Copiloto-Orquestador-de-Skills]]"
fecha: 2026-10-30
backups_asociados:
  - "[[docs/Backups/2026-10-30_134500_AGENTS.md.bak]]"
  - "[[docs/Backups/2026-10-30_134500_copiloto-orquestador-skills_SKILL.md.bak]]"
  - "[[docs/Backups/2026-10-30_134500_ciencia-de-datos_SKILL.md.bak]]"
  - "[[docs/Backups/2026-10-30_134500_facturacion-reverse-engineering_SKILL.md.bak]]"
  - "[[docs/Backups/2026-10-30_134500_arquitecto-sistemas-epec_SKILL.md.bak]]"
  - "[[docs/Backups/2026-10-30_134500_Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md.bak]]"
tags:
  - #historial
  - #mejora
  - #backup
  - #oracle
  - #base-de-datos
  - #pacing
  - #throttling
  - #copiloto-orquestador
  - #multi-agente
---

# Registro de Mejora: Protocolo Transversal de Consultas Seguras a Bases de Datos (Oracle y Motores SQL): Pacing, Retardos Obligatorios (Throttling) y Protección contra Sobrecarga

## 📝 Descripción del Cambio
- **Contexto**: A solicitud del usuario, para proteger los clusters transaccionales de producción y analítica (como el entorno Oracle RAC `epec2-scan2.epec.net / PRODEBS_SEE` y los esquemas `XXSIGEC`, `GEOREF`, así como bases de datos corporativas SQL y Microsoft Fabric), se estableció la directiva mandatoria de intercalar retardos (*pacing / throttling*) entre consultas sucesivas o por lotes, impidiendo ráfagas inmediatas continuas que saturen los buffers y procesadores del servidor.
- **Regla Incorporada Transversalmente**:
  ```markdown
  ### Protocolo de Consultas Seguras a Bases de Datos (Pacing y Throttling Obligatorio)
  1. Principio de No-Saturación: Prohibido disparar ráfagas continuas de queries en bucles cerrados (hammering / loop flooding) o barridos no particionados sin pausa.
  2. Retardo Preventivo Inter-Consulta Obligatorio (Pacing):
     - Consultas iterativas o por lotes: pausa obligatoria de 300 ms a 1.000 ms (0,3 s a 1,0 s) mediante `time.sleep(0.5)` entre llamadas consecutivas.
     - Consultas masivas o joins pesados (ej. DOCUMENTOS, ITEMS, AUDITORIA_CAMMESA): retardo de 1.000 ms a 2.000 ms (1 s a 2 s) entre chunks para desocupar buffers y CPU.
  3. Loteado Controlado (Chunking <= 500 a 900 elementos): Particionar cláusulas IN (...) en bloques de hasta 500 a 900 elementos para evitar ORA-01795 y reducir el número total de llamadas a la base de datos, aplicando la pausa al finalizar cada bloque.
  4. Modo Solo Lectura y Aislamiento: Iniciar sesión inmediatamente con `SET TRANSACTION READ ONLY` y utilizar context managers para garantizar el cierre automático de cursores y conexiones.
  5. Backoff Exponencial: Si se detecta lentitud inusual (latencia >= 2.000 ms) o advertencias de contención (ORA-01013), duplicar progresivamente el tiempo de espera (0,5s -> 1s -> 2s -> 4s).
  ```

---

## 📂 Archivos y Habilidades Actualizados

1. [`.agents/AGENTS.md`](file:///D:/Proyectos/antigravity-agents-repository/.agents/AGENTS.md):
   - Incorporación de la **Sección 8: Protocolo de Consultas Seguras a Bases de Datos (Oracle y Motores Relacionales/NoSQL): Pacing, Retardos Obligatorios (Throttling) y Protección contra Sobrecarga** como directiva global del repositorio.
2. [`.agents/skills/copiloto-orquestador-skills/SKILL.md`](file:///D:/Proyectos/antigravity-agents-repository/.agents/skills/copiloto-orquestador-skills/SKILL.md):
   - Exigencia de inclusión de restricciones de Pacing y Throttling en los contratos WBS de tareas que involucren bases de datos.
   - Supervisión activa en el Despacho Secuencial (Punto 4 de Protección de BD) y verificación obligatoria en la Instancia 1 de QA Técnico.
3. [`docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md):
   - Criterio de evaluación en Instancia 1 de QA Técnico.
   - Parámetros tipados en el contrato WBS Hand-off Schema (`DB Pacing >= 300 ms`, `DB Chunking <= 500`, `SET TRANSACTION READ ONLY`).
   - Nueva sección normativa **6.7. Protocolo de Consultas Seguras a Bases de Datos (Oracle y Motores Relacionales): Pacing y Retardo Obligatorio (Throttling)** en el Apéndice Técnico.
4. [`.agents/skills/ciencia-de-datos/SKILL.md`](file:///D:/Proyectos/antigravity-agents-repository/.agents/skills/ciencia-de-datos/SKILL.md) & [`docs/Agentes/02-Ciencia-de-Datos.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/Agentes/02-Ciencia-de-Datos.md):
   - Actualización del punto 2 de capacidades (SQL, Oracle & Fabric) con retardo de 300 ms a 1.000 ms y chunking $\le 500-900$.
   - Incorporación de la regla obligatoria 9 de Pacing y Throttling para todas las extracciones de datos.
5. [`.agents/skills/facturacion-reverse-engineering/SKILL.md`](file:///D:/Proyectos/antigravity-agents-repository/.agents/skills/facturacion-reverse-engineering/SKILL.md) & [`docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering.md):
   - Adición de la Regla No Negociable 5: Pacing y retardos obligatorios en consultas a Oracle 19c (`DOCUMENTOS`, `ITEMS`, `casos_documento.py`, `en_lotes`).
6. [`.agents/skills/arquitecto-sistemas-epec/SKILL.md`](file:///D:/Proyectos/antigravity-agents-repository/.agents/skills/arquitecto-sistemas-epec/SKILL.md) & [`docs/Agentes/06-Arquitecto-Sistemas-EPEC.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/Agentes/06-Arquitecto-Sistemas-EPEC.md):
   - Actualización de la Sección 5 de Política de Seguridad y Consultas a Base de Datos (Pacing y Throttling) para exploraciones de esquemas y diccionarios de datos Oracle.
7. [`docs/Agentes/11-Copiloto-Orquestador-de-Skills.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/Agentes/11-Copiloto-Orquestador-de-Skills.md):
   - Ficha técnica actualizada con el rol de auditor de pacing en el WBS jerárquico.
8. [`docs/00-Dashboard-MOC.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/00-Dashboard-MOC.md):
   - Registro en la lista relacional de Historial de Mejoras Continuas y entrada cronológica reciente.

---

## 🛡️ Resguardo / Backups Preventivos Generados
- `docs/Backups/2026-10-30_134500_AGENTS.md.bak`
- `docs/Backups/2026-10-30_134500_copiloto-orquestador-skills_SKILL.md.bak`
- `docs/Backups/2026-10-30_134500_ciencia-de-datos_SKILL.md.bak`
- `docs/Backups/2026-10-30_134500_facturacion-reverse-engineering_SKILL.md.bak`
- `docs/Backups/2026-10-30_134500_arquitecto-sistemas-epec_SKILL.md.bak`
- `docs/Backups/2026-10-30_134500_Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md.bak`

---

## 🎯 Impacto y Beneficio Operativo
- **Cero Saturación del Servidor Oracle RAC**: Se erradica el riesgo de degradación del rendimiento en los nodos transaccionales de EPEC durante extracciones masivas de facturación o catastros.
- **Convivencia Armónica con la Operación Comercial**: Las pausas controladas (300 ms a 1.000 ms) permiten al motor de base de datos desocupar *buffer cache*, memoria PGA y locks de lectura sin afectar a usuarios de ventanilla o cuadrillas.
- **Estandarización Transversal e Integración WBS**: Todo nuevo script o tarea despachada por el Copiloto Orquestador incorpora de forma predeterminada el pacing y el chunking dentro de sus restricciones operativas y criterios de QA Técnico.
