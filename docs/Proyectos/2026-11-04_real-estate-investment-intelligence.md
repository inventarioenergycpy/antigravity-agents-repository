---
title: "Real Estate Investment Intelligence: Inteligencia Inmobiliaria, Valuación CMA y Escalamiento Patrimonial en Córdoba"
date: 2026-11-04
agente: "[[15-Experto-Inmobiliario-Bienes-Raices-Financiero]]"
repo_github: "https://github.com/inventarioenergycpy/real-estate-investment-intelligence.git"
local_path: "D:\\Proyectos\\real-estate-investment-intelligence"
tags:
  - #proyecto
  - #real-estate
  - #inmobiliario
  - #cordoba
  - #cma-valuation
  - #trade-up-ladder
  - #dcf-real-estate
---

# 🏢 Real Estate Investment Intelligence: Suite de Inteligencia Inmobiliaria, Valuación CMA y Escalamiento Patrimonial (Córdoba Capital e Interior)

## 📌 1. Resumen Ejecutivo
Desarrollo e inicialización de la suite integral en Python **`real-estate-investment-intelligence`**, orientada a la prospección de mercado, tasación comparativa (**CMA**), modelado financiero cuantitativo (**NOI, CAP Rate, DCF, TIR y VAN**) y diseño de planes de **Escalamiento Patrimonial Inmobiliario (Trade-Up Ladder)** en la Provincia de Córdoba, abarcando tanto barrios consolidados y pericentrales de **Córdoba Capital** como urbanizaciones de **Sierras Chicas**, **Valle de Punilla** y **Calamuchita**.

El sistema incorpora de manera determinista la normativa impositiva y arancelaria de Córdoba:
- **Colegio Profesional Inmobiliario de Córdoba (CPI - Ley 9445)**: Honorarios de intermediación en compraventa del 3% al vendedor y 3% al comprador.
- **Dirección General de Rentas de Córdoba (DGR)**: Alícuota del Impuesto de Sellos sobre actos onerosos y boletos (1.5% distribuido equitativamente 50/50).
- **Aranceles Notariales**: Estimación del 2.2% para honorarios y aportes de escrituración notarial, más certificados de dominio e inhibición.

---

## ⚙️ 2. Arquitectura de Módulos Desarrollada

El proyecto reside en el repositorio dedicado `https://github.com/inventarioenergycpy/real-estate-investment-intelligence.git` (`D:\Proyectos\real-estate-investment-intelligence`):

| Módulo | Archivo | Responsabilidad Principal |
| :--- | :--- | :--- |
| **Benchmarks Zonales** | `core/cordoba_market_data.py` | Catálogo de precios de referencia USD/m², rentabilidades por alquiler tradicional y temporario, liquidez y aranceles CPI/DGR. |
| **Buscador de Mercado** | `core/market_searcher.py` | Motor de búsqueda y filtrado de ofertas con catálogo representativo de avisos reales de Zonaprop, Clasificados La Voz, Argenprop y MercadoLibre. |
| **Evaluador CMA** | `core/property_evaluator.py` | Cálculo de m² efectivos ponderados, valor de mercado, desvíos porcentuales y **Opportunity Score (0 a 100)**. |
| **Simulador de Escalamiento** | `core/investment_ladder.py` | Circuito de venta de propiedad inicial, deducción de costos de cierre, cálculo de poder de compra y ranking de candidatos viables de salto. |
| **Modelador Financiero** | `core/financial_modeler.py` | Modelado de NOI, CAP Rate neto, Cash-on-Cash, DCF a 5 años, cálculo de TIR (IRR) y VAN (NPV), y contraste Tradicional vs. Airbnb. |
| **Exportador Tabular** | `core/sheets_exporter.py` | Generación de libros Excel multi-hoja (`.xlsx`) y CSV para integración con Google Drive (`inventario.energycpy@gmail.com`). |
| **CLI & Runner** | `main.py` | Interfaz interactiva de consola para ejecutar simulaciones y generar reportes. |
| **Suite de Tests** | `tests/test_real_estate_suite.py` | Batería de 5 pruebas unitarias deterministas que validan aserciones numéricas con exit code 0. |

---

## 📊 3. Caso Testigo: Simulación de Escalamiento Patrimonial

Se ejecutó una simulación representativa para un inversor que posee un **departamento de 1 dormitorio en Alberdi Centro** y desea realizar un salto cualitativo hacia una propiedad de mayor categoría:

```text
1. Propiedad Inicial: Dpto 1 Dormitorio - Alberdi Centro
   • Valor de Mercado: USD 45,000 | Venta estimada: USD 42,750 (descuento habitual)
   • (-) Comisión CPI Córdoba (3%): USD 1,282
   • (-) Impuesto de Sellos Rentas Córdoba (DGR): USD 321
   • (-) Gastos Notariales y Certificados: USD 692
   • (=) Efectivo Neto Realizable en Venta: USD 40,455 (Fricción Total: 5.4%)

2. Poder de Compra:
   • Efectivo Neto de Venta: USD 40,455
   • (+) Aporte de Capital Propio: USD 15,000
   • 🎯 Poder de Compra Total: USD 55,455

3. Ranking de Salto (Trade-Up):
   [1] ✅ VIABLE | Score: 68.7/100 | Dpto 2 Dormitorios c/ Balcón Terraza - Alto Alberdi
       • Zona: Alberdi / Alto Alberdi (875 USD/m² vs Benchmark 1,020 USD/m²)
       • Costo Total de Adquisición (c/ CPI + Sellos + Escritura): USD 53,749 (Gap sobrante: USD 1,706)
       • Salto de Metros: +19.0 m² (+42% de superficie efectiva)
       • Salto de Renta Anual: +USD 638/año
       • Amortización de Fricciones: 71.7 meses con el mayor flujo generado.

4. Modelado Financiero de la Propiedad Adquirida:
   • Inversión Total: USD 60,102 (Adquisición + Fricciones)
   • Renta Tradicional: Ingreso Bruto USD 3,248/año | NOI Neto USD 2,140/año | CAP Rate Neto: 3.82% | TIR a 5 años: 5.61%
   • Renta Temporaria: Renta Bruta USD 3,640/año | Mayor desgaste y vacancia en esta tipología hace más aconsejable la Renta Tradicional.
```

---

## 📁 4. Archivos Generados para Google Drive y Descargas

- `data/cma_comparativo_cordoba.xlsx`: Matriz comparativa de todas las propiedades evaluadas con sus métricas y scores.
- `data/plan_escalamiento_patrimonial.xlsx`: Libro de trabajo con resumen del poder de compra y desglose de candidatos de salto.

---

## 🔗 5. Enlaces Relacionales
- **Ficha del Agente Rector**: `[[docs/Agentes/15-Experto-Inmobiliario-Bienes-Raices-Financiero|Agente 15]]`
- **Repositorio Local**: [`D:\Proyectos\real-estate-investment-intelligence`](file:///D:/Proyectos/real-estate-investment-intelligence)
- **Repositorio GitHub**: [`inventarioenergycpy/real-estate-investment-intelligence`](https://github.com/inventarioenergycpy/real-estate-investment-intelligence.git)
- **Tablero MOC Principal**: `[[00-Dashboard-MOC]]`

