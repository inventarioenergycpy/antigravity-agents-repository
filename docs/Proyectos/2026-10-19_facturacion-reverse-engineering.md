---
title: "Ficha Técnica: Facturación EPEC - Simulador y Reverse Engineering"
proyecto: "facturacion-reverse-engineering"
fecha: 2026-10-19
agente: "[[docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering|Agente 12 - Facturación Reverse Engineering]] & [[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto EPEC]]"
repositorio_remoto: "https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering"
tags:
  - #proyecto
  - #facturacion
  - #reverse-engineering
  - #sigec
  - #tarifas
  - #simulador
  - #epec
---

# ⚡ Proyecto Dedicado: Facturación EPEC · Reverse Engineering y Simulador Interactivo

- **Repositorio Remoto Oficial**: [`https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering`](https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering)
- **Directorio Local de Trabajo**: [`D:\Proyectos\facturacion-reverse-engineering`](file:///D:/Proyectos/facturacion-reverse-engineering) / [`C:\Users\jidiaz\.gemini\antigravity-ide\scratch\facturacion-reverse-engineering`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/facturacion-reverse-engineering)
- **Agente Responsable**: [[docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering|Agente 12: Ingeniero Especialista en Facturación Reverse Engineering]]

---

## 🎯 1. Resumen Ejecutivo y Alcance
Este proyecto reconstruye por ingeniería inversa el comportamiento exacto del motor de cálculo de facturación comercial SIGEC de EPEC.  
Dispone de:
1. **Simulador Offline Interactivo (`web/factura_simulada.html`)**: Permite simular libremente o cotejar facturas reales emitidas, visualizando el encendido de reglas, tablas de SIGEC y prorrateos por vigencias tarifarias.
2. **Motor de Cálculo Puro en JavaScript (`web/motor.js`)**: Sin dependencias de DOM ni navegador, operable en Node.js o embebido.
3. **Mapeo de 31 Tablas de SIGEC (`docs/glosario_tablas.md`)**: Claves primarias, foráneas y relaciones para reconstruir cualquier documento emitido.
4. **Suite de Consultas SQL Documentadas (`docs/modelo_factura_documentado.sql`)**: 13 consultas maestras (A a M) optimizadas para Oracle 19c (`PRODEBS_SEE`).
5. **Auditoría Tributaria Exhaustiva**: Base imponible, alícuotas y ordenanzas de los 124 municipios cordobeses, fondos FODEP y ERSeP.

---

## 🔒 2. Protocolo de Sincronización Upstream Permanente
El Agente 12 dispone de un script de control automatizado en:
[`.agents/skills/facturacion-reverse-engineering/scripts/sync_upstream.py`](file:///D:/Proyectos/antigravity-agents-repository/.agents/skills/facturacion-reverse-engineering/scripts/sync_upstream.py)

Antes de iniciar cualquier sesión de análisis o modelado sobre facturas de EPEC, se ejecuta:
```bash
python .agents/skills/facturacion-reverse-engineering/scripts/sync_upstream.py --pull
```
Lo cual verifica `origin/main` y previene inconsistencias por cambios en resoluciones del ERSeP o cuadros tarifarios.

---

## 🔗 3. Enlaces Relacionales
* [[00-Dashboard-MOC|Dashboard Central MOC]]
* [[docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering|Perfil de Agente 12]]
* [[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Agente 06: Arquitecto de Sistemas EPEC]]
