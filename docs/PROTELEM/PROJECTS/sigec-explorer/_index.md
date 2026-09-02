---
tipo: indice
estado: vigente
sensibilidad: interna
tags:
  - sigec-explorer
  - moc
  - oracle
  - epec
aliases:
  - MOC SIGEC Explorer
  - Home SIGEC Explorer
---

# 🗄️ SIGEC Explorer — Cerebro del proyecto

> [!abstract] Qué es esto
> Map of Content (MOC) del proyecto. Punto de entrada al segundo cerebro en Obsidian: esquema Oracle, arquitectura, catálogo de tablas, chat texto-a-SQL y decisiones, todo interconectado con wikilinks.

## 🎯 Objetivo

Herramienta interna para EPEC con doble función:
1. **Explorador de esquema** — cualquier compañero entiende `XXSIGEC` sin tocar la base.
2. **Chat texto-a-SQL** — preguntas en lenguaje natural → SELECT listo para ejecutar.

## 🏗️ Arquitectura del sistema

- [[Arquitectura]] — diseño en dos fases (catálogo + chat), stack, árbol de archivos
- [[Chat Texto-a-SQL]] — flujo completo: sinónimos → retriever → LLM → validación → respuesta
- [[Seguridad]] — modelo de seguridad en 4 capas (privilegios Oracle, transacción, validación estructural, blacklist)

## ⚖️ Dominios y fronteras

- [[Modelo de Facturación]] — cómo se lee **una factura**: importe (`DOC_IMPORTE` = neto + impuestos), kWh (`DOC_CONSUMO`) y días del período (`DOC_FECHA_DESDE/HASTA`), todo en una fila de `DOCUMENTOS`. Incluye la trampa del período-etiqueta (≠ mes consumido)
- [[Fronteras - Legales e Ilícitos]] — mapa de las fronteras con **Fraude e Ilícitos** (módulo interno vivo) y **Legales** (`FECHA_PASE_GJ` + oficios judiciales hacia `XXLG`), qué está vivo y qué es arqueología

## 🗃️ Esquema Oracle

- [[Esquema XXSIGEC]] — hallazgos Fase 0: 1 036 tablas, FK híbridas, prefijos, tablas hub
- [[Catálogo]] — estructura de `catalog.json` v2, FK declaradas + inferidas dirigidas, resultados de validación
- [[Sinónimos]] — `synonyms.json`: mapeo vocabulario usuario → esquema XXSIGEC, cómo mantenerlo

## 🧾 Gestión del proyecto

- [[Decisiones]] — decisiones técnicas y trade-offs
- [[Sprints]] — estado actual, roadmap y criterios de done por fase

## 🔖 Metadatos

| | |
|---|---|
| **Repo** | `d:\Usuarios\pberecibar\Desktop\proyectos\mapeo-bd-sigec-oracle` |
| **Stack** | Python 3.12 · FastAPI · python-oracledb (Thick) · HTML + Vanilla JS · Claude API |
| **Base de datos** | Oracle `PRODEBS_SEE` · schema `XXSIGEC` · usuario `smunge` (solo lectura) |
| **Conexión** | `epec2-scan2:1521` · Instant Client `C:\Oracle\instantclient_23_6` |
| **Conexión (compartida)** | [[Oracle EPEC - Conexión y convenciones\|kernel de conexión + convenciones SIGEC]] (Shared) |
| **Proyecto relacionado** | [[plataforma-clientes/_index\|Plataforma de Clientes]] (mismo Oracle, distinto schema) |
