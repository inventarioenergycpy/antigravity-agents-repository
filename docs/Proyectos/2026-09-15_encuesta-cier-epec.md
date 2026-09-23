---
type: proyecto
proyecto: "Encuesta de Satisfacción CIER EPEC-AR (2025 - 2026)"
agente_responsable: "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos & BI EPEC]]"
repositorio_github: "https://github.com/inventarioenergycpy/encuesta-cier-epec"
despliegue_url: "https://inventarioenergycpy.github.io/encuesta-cier-epec/"
fecha_creacion: 2026-09-15
muestra_auditada: "N = 1.250 encuestas residenciales (625 en 2025 y 625 en 2026)"
error_muestral: "+/- 3.92% (Confianza 95%)"
tags:
  - #proyecto
  - #ciencia-de-datos
  - #satisfaccion-cliente
  - #cier
  - #epec
  - #iscal
  - #benchmark-500k
  - #dashboard
---

# Proyecto: Encuesta de Satisfacción CIER EPEC-AR (2025 - 2026)

## 📌 Resumen Ejecutivo
Estudio integral de satisfacción de clientes residenciales y benchmarking de distribución eléctrica basado en las auditorías anuales de la **Comisión de Integración Energética Regional (CIER)** para la **Empresa Provincial de Energía de Córdoba (EPEC)**.

Comprende el procesamiento, estandarización y modelado de microdatos ($N = 1.250$ registros), catálogos y diccionarios de variables, comparativas interanuales de índices macro (`ISCAL`, `IAC`, `IECP`, `IICP`, `IAOP`), comparativas competitivas contra distribuidoras de Gran Porte (>500.000 clientes) y el despliegue de un **Dashboard Interactivo SPA**.

---

## 🔗 Enlaces y Repositorio Dedicado
- **Repositorio Central (inventarioenergycpy)**: [https://github.com/inventarioenergycpy/encuesta-cier-epec](https://github.com/inventarioenergycpy/encuesta-cier-epec)
- **Repositorio Réplica (PROTELEM-EPEC)**: [https://github.com/PROTELEM-EPEC/encuesta-cier-epec](https://github.com/PROTELEM-EPEC/encuesta-cier-epec)
- **Repositorio Personal (protelemepec-coder)**: [https://github.com/protelemepec-coder/encuesta-cier-epec](https://github.com/protelemepec-coder/encuesta-cier-epec)
- **Live Dashboard (protelemepec-coder Pages)**: [https://protelemepec-coder.github.io/encuesta-cier-epec/](https://protelemepec-coder.github.io/encuesta-cier-epec/)
- **Live Dashboard (GitHub Pages)**: [https://inventarioenergycpy.github.io/encuesta-cier-epec/](https://inventarioenergycpy.github.io/encuesta-cier-epec/)
- **Ubicación Local del Proyecto**: `D:\Proyectos\encuesta_cier` (enlazado a `%USERPROFILE%\.gemini\antigravity-ide\scratch\encuesta_cier`)

---

## 📊 Matriz de Indicadores Clave y Evolución Interanual

```
Escala CIER: 0 (Pésimo) a 100 (Excelente)
IAOP: Índice de Aprovechamiento de Oportunidades Positivas
```

| Indicador Macro | EPEC 2025 | EPEC 2026 | Variación IAOP | Benchmark >500k (2026) | Diagnóstico y Posicionamiento |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **ISCAL Global (Calidad Percibida)** | **63,69** | **65,96** | **+3,56%** | 70,15 | 📈 Reducción de brecha con el promedio regional |
| **Aprobación del Cliente (IAC)** | **75,68** | **77,60** | **+2,54%** | 78,50 | 🟢 A 0,90 pts del Promedio Regional |
| **Excelencia en Calidad (IECP - Notas 9-10)** | **21,61%** | **27,15%** | **+25,65%** | 32,50% | 🚀 +5,54% promotores netos ganados |
| **Insatisfacción (IICP - Notas 1-4)** | **17,66%** | **15,19%** | **-13,97%** | 13,20% | 📉 Disminución favorable de detractores |

---

## ⚡ Pilares de Desempeño por Áreas de Servicio

1. **Suministro de Energía (78,48 pts | Superior al Promedio Regional):**
   - **Continuidad del Servicio (85,92 pts vs. 84,30 pts)**: Fortaleza líder regional (+1,62 pts sobre el promedio >500k).
   - **Calidad y Nivel de Tensión (77,40 pts vs. 76,20 pts)**: Percepción sobresaliente sin fluctuaciones bruscas.
2. **Canales de Pago y Digitalización (89,20 pts | Nivel Clase Mundial):**
   - Atributo de mayor puntuación absoluta en toda la evaluación.
3. **Compromiso Socioambiental (63,46 pts | +12,70% IAOP):**
   - Crecimiento acelerado superando el benchmark promedio regional (63,20 pts).
4. **Información y Comunicación (52,03 pts | +11,99% IAOP):**
   - Dimensión de mayor dinamismo y aceleración (+5,57 puntos brutos ganados respecto a 2025).

---

## 📂 Artefactos y Componentes del Proyecto
- `data/processed/microdata_epec_2025_2026.xlsx`: Base de microdatos unificada ($N=1.250$ encuestas x 120+ atributos).
- `data/processed/diccionario_unificado.xlsx`: Diccionario formal de variables y etiquetas CIER.
- `data/processed/comparativo_distribuidores_500k.xlsx`: Matriz de benchmarking para distribuidoras de gran porte.
- `docs/resumen_ejecutivo_indices.md`: Análisis exhaustivo de índices y notas promedio por atributo.
- `docs/comparativo_distribuidores_500k.md`: Diagnóstico competitivo regional.
- `index.html`, `app.js`, `style.css`, `data_bundle.js`: Dashboard directivo interactivo.
