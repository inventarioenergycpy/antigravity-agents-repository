---
title: "Ficha Técnica: Arquitecto de Sistemas EPEC"
type: agente
agente: "arquitecto-sistemas-epec"
tags:
  - #agente
  - #arquitectura
  - #sistemas-epec
  - #cis
  - #mdm
  - #pliegos
  - #licitaciones
created: 2026-09-02
---

# 🏗️ Agente 6: Arquitecto de Sistemas EPEC

- **Identificador de Skill**: `arquitecto-sistemas-epec`
- **Ubicación de Habilidad**: `.agents/skills/arquitecto-sistemas-epec/SKILL.md`
- **Rol Principal**: Evaluación de arquitectura empresarial de sistemas comerciales (CIS / MDM / WFM / CRM / CX / Portal), seguimiento del pliego licitatorio (929 requerimientos en 35 grupos) y benchmarking de soluciones de mercado (Oracle C2M/CCS, OPEN SmartFlex, PRETECO/ESC).

---

## 🎯 Capacidades Clave

1. **Gobernanza de Pliegos y Requerimientos**:
   - Seguimiento de los 929 requerimientos funcionales y técnicos clasificados en 35 grupos.
   - Trazabilidad de cambios entre versiones de pliegos y matriz de inconsistencias.
2. **Arquitectura Empresarial Objetivo**:
   - Mapeo de módulos core: CIS, MDM, WFM, CRM, Portal de Autogestión y Motor IA.
   - Definición de integraciones con la infraestructura legacy `XXSIGEC` y bases Oracle EPEC, aplicando obligatoriamente el protocolo de consultas seguras con `SET TRANSACTION READ ONLY` y pausas de pacing (300 ms a 1.000 ms) entre consultas para evitar la sobrecarga del entorno transaccional.
3. **Benchmarking de Proveedores**:
   - Análisis técnico-económico comparativo entre Oracle C2M/CCS, OPEN SmartFlex y propuestas integradoras.
4. **Metodología en 6 Etapas**:
   - Aplicación estricta del flujo secuencial con auto-documentación y resguardo en Obsidian.

---

## 🔗 Referencias
- [[00-Dashboard-MOC]]
- [[Proyectos/2026-09-02_protelem-conocimiento-integrado|Conocimiento Integrado PROTELEM]]

---

## ⚡ Enriquecimiento Académico (70 Clases Diplomaturas + Smart Grids / AMI / FLISR)
- **Infraestructura AMI en 4 Cuadrantes y MDM (VEE)**: Integración de medidores bidireccionales 15-minutales ($+P, -P, Q_1..Q_4$) mediante protocolos **DLMS/COSEM (IEC 62056), Modbus, MQTT, 4G/NB-IoT y RF Mesh** con concentradores DCU, HES y motor de Validación, Estimación y Edición (VEE).
- **Telecontrol FLISR, Protecciones y Calidad SAIDI/SAIFI**: Coordinación de reconectadores (*reclosers* 1R+2L) y seccionalizadores bajo lógica **FLISR** para reducir el **SAIDI** de horas a segundos; protecciones **ANSI 87T, 50/51 y 21** (IEC 61850); monitoreo de calidad de onda ($\text{THD}_V \le 5\%$ según IEEE 519 / IEC 61000) y Contabilidad Regulatoria en el CIS para bonificaciones automáticas y RTI del VAD.
- **Vínculos de Cátedra**: [[docs/Cursos/Diplomatura-Energia-Electrica/Monografia-Integral-Diplomatura-Energia-Electrica|Monografía Diplomatura Energía Eléctrica]] | [[docs/Cursos/Diplomatura-Transicion-Energetica/Monografia-Integral-Diplomatura-Transicion-Energetica|Monografía Diplomatura Transición Energética]].
