---
tipo: indice
estado: en-progreso
sensibilidad: interna
tags:
  - sistema-epec-oracle
  - moc
  - epec
  - pliego
  - licitacion
aliases:
  - MOC Sistema EPEC Oracle
  - Nuevo sistema comercial EPEC
  - Pliego CIS
  - Pliegos CIS
---

# 🏛️ Sistema EPEC Oracle — Cerebro del proyecto

> [!abstract] Qué es esto
> MOC del proyecto que sigue la **licitación del nuevo sistema comercial y de facturación de EPEC** (CIS · MDM · WFM · CRM · CX · Portal). El material vive en una carpeta de red que es un vault propio y **de solo lectura**; acá se documenta de dónde sale, cómo está organizado y qué reglas rigen para leerlo.

## 🎯 Objetivo

Entender y seguir el pliego del nuevo sistema comercial: qué se pide (929 requerimientos en 35 grupos), qué quedó fuera de alcance, qué proponen los proveedores y qué defectos arrastra la documentación antes de que se emita el pliego definitivo.

No es un proyecto de desarrollo: es **seguimiento y análisis de un corpus documental** que evoluciona por versiones.

## 📥 De dónde sale la información

- [[Fuentes de información]] — la carpeta de red `\\srvfs01\ProyectoTelemedicion\42- Pliegos CIS`: qué contiene, cómo está organizada, la tabla de prioridad de fuentes y la **regla de solo lectura**.

> [!important] Un numeral no identifica un requerimiento
> La numeración del Anexo **no es estable entre versiones**: 489 de 701 requerimientos cambiaron de numeral entre marzo y agosto de 2026, y los grupos se renumeraron a partir del 25. El pliego cita la numeración vieja. Todo cruce se hace **por texto**. Detalle en `wiki/gobernanza/cambios-entre-versiones.md` de la fuente.

## 🧩 Dominio / temas

El wiki de la fuente organiza el corpus en doce temas. Se enlazan acá como mapa mental; el contenido vive allá, no se duplica:

| Tema | Grupos del Anexo | De qué va |
|---|---|---|
| Alcance y arquitectura | — | Ecosistema objetivo (CIS, MDM, WFM, CRM, CX, Portal, Motor IA), fuera de alcance, faltantes |
| Clientes y suministros | 2, 3, 4 | Clientes, servicios contratados, predios, constructoras |
| Medición y consumos | 6, 7, 8 | Medidores, lecturas, MDM, VEE, determinantes de facturación |
| Tarifas y facturación | 9–12, 24 | Motor tarifario, facturación al cliente / compleja / de terceros, gestión financiera |
| Cobranzas y morosidad | 13, 14, 34 | Pagos, cajas, mora, corte, pérdidas por ilícitos |
| Órdenes y trabajo de campo | 15, 30 | Órdenes, despacho, ruteo, movilidad, contratistas |
| CRM y ventas | 5, 16, 31, 32, 33 | Marketing, atención/BPM, CRM, grandes clientes, funciones de IA |
| Canales y portal | 29, 35 | Experiencia de cliente, portal de autogestión, omnicanalidad, e-commerce |
| Plataforma técnica | 1, 17–23, 25–28 | Extensibilidad, seguridad, auditoría, analítica, requisitos técnicos e integración |
| Proveedores y costos | — | Propuestas PRETECO/ESC y OPEN, escenarios, precios, plazos |
| Gobernanza | — | Responsables, criterios de aceptación, cambios entre versiones |
| Meta | — | Cómo funciona el propio wiki |

## 🔒 Seguridad

- [[Seguridad]] — clasificación de datos del proyecto. Es material de **licitación en curso**: precios de proveedores y análisis comparativos no se copian acá. Modelo global: [[Modelo de seguridad]].

## 🧾 Gestión

- Estado del corpus al 2026-08-04: 35 de 35 grupos documentados, 929 requerimientos transcriptos, 9 puntos de deuda técnica y 25 preguntas abiertas registrados en la fuente.

## ♻️ Conocimiento compartido que aplica

- [[Conocimiento compartido]] — infra y tooling transversal del entorno EPEC.
- Reglas del cerebro: [[Convenciones]] · [[Fuentes de verdad]].

## 🔖 Metadatos

| | |
|---|---|
| **Fuente de información** | `\\srvfs01\ProyectoTelemedicion\42- Pliegos CIS` — **solo lectura** |
| **Staging / trabajo propio** | `d:\Usuarios\pberecibar\Desktop\proyectos\my-brain\projects\sistema-epec-oracle` |
| **Tipo de proyecto** | Análisis documental / seguimiento de licitación |
| **Componentes en juego** | CIS · MDM · WFM · CRM · Plataforma de Experiencia de Cliente · Portal de autogestión · Motor IA |
| **Candidatos evaluados** | Oracle (C2M/CCS) · OPEN (SmartFlex) · PRETECO / ESC Partners |

---
- [[Home|← Inicio del cerebro]]
