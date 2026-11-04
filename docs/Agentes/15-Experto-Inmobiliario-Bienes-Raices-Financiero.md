---
title: "Agente 15: Experto en Bienes Raíces, Inversiones Inmobiliarias & Modelado Financiero"
role: "Especialista en Real Estate Financial Modeling, Búsqueda Web de Inmuebles, Análisis Comparativo de Ofertas (CMA) y Escalamiento Patrimonial Inmobiliario"
skill: ".agents/skills/experto-inmobiliario-bienes-raices-financiero/SKILL.md"
repo_dedicado: "https://github.com/inventarioenergycpy/real-estate-investment-intelligence.git"
created: 2026-11-04
tags:
  - #agente
  - #real-estate
  - #inmobiliario
  - #bienes-raices
  - #cordoba
  - #cma-valuation
  - #trade-up-ladder
  - #dcf-real-estate
  - #fideicomisos
  - #cpi-cordoba
---

# 🧭 Agente 15: Experto en Bienes Raíces, Inversiones Inmobiliarias & Modelado Financiero

## 📋 Resumen del Perfil
El **Agente 15** es el especialista del ecosistema **Antigravity IDE** dedicado a la inteligencia estratégica del mercado inmobiliario, el modelado financiero cuantitativo de inversiones en bienes raíces y el diseño de planes de **Escalamiento Patrimonial Inmobiliario (Trade-Up Ladder / Property Stepping Stone)** con foco prioritario en **Córdoba Capital e Interior** (Sierras Chicas, Punilla y Calamuchita) y principales centros urbanos de Argentina y la región.

El agente combina la prospección y rastreo de ofertas en portales inmobiliarios (Zonaprop, Clasificados La Voz, Argenprop, MercadoLibre Inmuebles) con el rigor tributario y arancelario de la plaza cordobesa (Colegio Profesional Inmobiliario CPI Ley Provincial 9445, Dirección General de Rentas Córdoba DGR y Colegio de Escribanos), permitiendo a inversores evaluar propiedades iniciales, descontar costos de cierre y reinvertir el capital de forma secuencial en activos de mayor jerarquía, mayor plusvalía y superior flujo de fondos.

---

## ⚙️ Módulos de la Suite de Software Dedicada

El agente opera sobre el repositorio dedicado [`real-estate-investment-intelligence`](https://github.com/inventarioenergycpy/real-estate-investment-intelligence.git) ubicado en `D:\Proyectos\real-estate-investment-intelligence`:

1. **`MarketSearcher` (`core/market_searcher.py`)**:
   - Motor de búsqueda y filtrado de avisos por zona, precio en USD, metraje cubierto/total, dormitorios y portales.
   - Catálogo representativo de propiedades testigo en barrios consolidados (Nueva Córdoba, General Paz, Cofico, Alberdi, Centro, Cerro de las Rosas, Manantiales, Villa Allende, Carlos Paz).
2. **`PropertyEvaluator` (`core/property_evaluator.py`)**:
   - Análisis Comparativo de Mercado (CMA) determinista.
   - Cálculo de superficie efectiva ponderada ($100\%\text{ cubierta} + 50\%\text{ descubierta}$).
   - Medición de desvío porcentual respecto al benchmark de la zona y cálculo de **Opportunity Score (0 a 100)** para detectar inmuebles subvaluados.
3. **`InvestmentLadderSimulator` (`core/investment_ladder.py`)**:
   - Simulador de Escalamiento Patrimonial Inmobiliario (Trade-Up).
   - Cálculo de desglose de liquidación de la propiedad inicial: deducción de honorarios CPI (3%), Sellos DGR (1.5% al 50%), gastos notariales y certificados.
   - Determinación del poder de compra y evaluación simultánea de opciones de reemplazo con cálculo de **Gap Financiero**, **salto de metros cuadrados**, **ganancia neta de renta** y **período de amortización de fricciones**.
4. **`RealEstateFinancialModeler` (`core/financial_modeler.py`)**:
   - Modelado financiero completo: Ingreso Operativo Neto (**NOI**), CAP Rate bruto y neto, Cash-on-Cash Return.
   - Flujo de Fondos Descontado (**DCF a 5 y 10 años**) con valor de reventa terminal y cálculo de **TIR (IRR)** y **VAN (NPV)** en USD.
   - Matriz de sensibilidad: Renta Tradicional vs. Renta Temporaria (Airbnb/Booking).
5. **`RealEstateSheetsExporter` (`core/sheets_exporter.py`)**:
   - Exportación de libros Excel (`.xlsx` multi-hoja) y CSV optimizados para su carga en Google Drive (`inventario.energycpy@gmail.com`) o apertura en Google Sheets / Excel.
6. **`Suite de Tests` (`tests/test_real_estate_suite.py`)**:
   - 5 pruebas unitarias deterministas que validan aserciones numéricas, cálculo de fricciones y convergencia matemática con exit code 0.

---

## 🎯 Articulación con los demás Agentes del Ecosistema

- **Agente 01 (Analista Financiero)**: Asiste en la modelización macroeconómica, costo de capital (WACC), evaluación de inflación en USD y optimización de flujos de caja.
- **Agente 02 (Ciencia de Datos & GIS)**: Provee georreferenciación parcelaria, análisis espacial con capas WFS IDECOR / Catastro de Córdoba y mapas de calor de precios por m².
- **Agente 03 (Desarrollador Web Showroom)**: Genera visualizadores web interactivos de inmuebles, fichas comerciales con Google Stitch y diseño Glassmorphism bajo `DESIGN.md`.
- **Agente 05 (Asesor Legal-Financiero)**: Audita contratos de compraventa, boletos ad-referendum, reservas, garantías de alquiler (DNU 70/2023) y fideicomisos inmobiliarios al costo (arts. 1666 y ss. CCCN).
- **Agente 11 (Copiloto Orquestador)**: Conduce el Squad Ágil Adaptativo cuando se requiere un análisis integral de inversión inmobiliaria a gran escala.
- **Agente 13 (Desarrollador Parques Solares)**: Asesora en evaluación de tierra rural/periurbana para proyectos solares y servidumbres de paso.

---

## 🔗 Enlaces Relacionales
- **Habilidad Central**: [`.agents/skills/experto-inmobiliario-bienes-raices-financiero/SKILL.md`](file:///D:/Proyectos/antigravity-agents-repository/.agents/skills/experto-inmobiliario-bienes-raices-financiero/SKILL.md)
- **Repositorio Dedicado en Disco**: [`D:\Proyectos\real-estate-investment-intelligence`](file:///D:/Proyectos/real-estate-investment-intelligence)
- **Ficha del Proyecto**: `[[docs/Proyectos/2026-11-04_real-estate-investment-intelligence|Proyecto: Real Estate Investment Intelligence]]`
- **Tablero MOC Principal**: `[[00-Dashboard-MOC]]`

