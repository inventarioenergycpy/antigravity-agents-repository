---
title: "Copiloto Orquestador - Documentación de la Propuesta Operativa de Despliegue MI 2027 (Escenarios 14k vs. 21k u./mes, Balance Mono/Tri y 24 Temas Críticos)"
tags:
  - #ami
  - #epec
  - #licitacion-5573
  - #propuesta-2027
  - #escenarios-contratistas
  - #nansen
  - #clou
  - #trifasicos
  - #historial-mejoras
  - #copiloto-orquestador
  - #triple-qa
created: 2026-10-28
updated: 2026-10-28
---

# 📋 Copiloto Orquestador: Documentación Integral de la Propuesta de Despliegue MI 2027 (Licitación Pública N° 5573)

## 📌 Contexto y Requerimiento
A solicitud del usuario, el **Agente 11 (Copiloto Orquestador y Selector Dinámico de Habilidades)** procedió a procesar, estructurar y documentar exhaustivamente la propuesta técnica contenida en el informe oficial emitido el **28/10/2026**:
- **Documento Fuente**: [`docs/licitacion_5573/Propuesta-despliegue-MI-2027.pdf`](file:///D:/Proyectos/despliegue-medidores-inteligentes-ami/docs/licitacion_5573/Propuesta-despliegue-MI-2027.pdf) (10 páginas).
- **Nuevo Documento Oficial Creado**: [`docs/09_propuesta_despliegue_mi_2027_operativa_escenarios_contratistas.md`](file:///D:/Proyectos/despliegue-medidores-inteligentes-ami/docs/09_propuesta_despliegue_mi_2027_operativa_escenarios_contratistas.md).
- **Actualizaciones Complementarias**:
  - [`README.md`](file:///D:/Proyectos/despliegue-medidores-inteligentes-ami/README.md) del repositorio dedicado.
  - [`docs/PROTELEM/00-Indice-PROTELEM-EPEC.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/PROTELEM/00-Indice-PROTELEM-EPEC.md).
  - [`docs/00-Dashboard-MOC.md`](file:///D:/Proyectos/antigravity-agents-repository/docs/00-Dashboard-MOC.md).

---

## 🛡️ Resguardo Preventivo (Rollback Protection)
Antes de editar los archivos existentes, se generaron los backups correspondientes:
- `docs/Backups/2026-10-28_114930_README_despliegue_ami.md.bak`

---

## 🎯 Síntesis Técnica de la Propuesta Documentada

### 1. Pilares Operativos y Priorización Territorial
- **Córdoba Capital Primero (Zona A)**: Cupo bruto de 200.000 medidores (180.000 netos con reserva del 10%). Se prioriza la colocación de CLOU y se completa con NANSEN.
- **Interior 100% NANSEN**: Distritos 28 (Río Cuarto), 8 (Villa María), 18 (San Francisco) y 23 (Villa Allende) son exclusivamente Nansen y reciben el remanente de Capital.
- **Cooperativas (93.000 CLOU)**: Absorben el 100% de su cupo en marca CLOU (83.701 monofásicos + 9.300 trifásicos).
- **Diferimiento CLOU 4**: El lote de 75.000 u. (40.125 netas EPEC) disponible el 16/12/2027 se pasa formalmente a **2028**.
- **Stock de Seguridad Dinámico**: 3% inicial, +0,5% mensual hasta un techo del 10% (reserva final de 20.000 NANSEN y 10.700 CLOU).

### 2. Comparativa de Escenarios de Contratistas en Capital
| Indicador Clave | Escenario 2 Contratistas (14.000 u./m) | Escenario 3 Contratistas (21.000 u./m) |
| :--- | :---: | :---: |
| **Instalados a Dic-2027** | 163.000 medidores (Capital 136k, Interior 27k) | **207.000 medidores** (Capital 180k, Interior 27k) |
| **Finalización Capital (180k)** | **Abril 2028** (+5 meses) | **Noviembre 2027** (Dentro del año) |
| **NANSEN Usados en Capital** | 83.701 unidades | 119.429 unidades |
| **CLOU Usados en Capital** | 96.299 unidades | 60.571 unidades |
| **NANSEN Remanente Interior** | **96.299 unidades** (Termina Ago-28) | **60.571 unidades** (Termina Abr-28) |
| **Pico de Stock Nansen Almacén** | 152.571 unidades | 119.571 unidades |

### 3. Desbalance Estructural de Fases
- **Sobrante de Trifásicos**: Entran 80.000 u. brutas (70.700 netas para EPEC), pero la demanda real es del 9% en Capital y 11-14% en Interior. El cronograma sólo absorbe entre 23.597 (33%) y 28.141 (40%). Ni cambiando todos los trifásicos posibles de la provincia (46.933) se consumen.
- **Tensión en Monofásicos**: Entran 236.299 mono netos. Con 2 contratistas se exige el **105%** de lo disponible.

### 4. Pliego de las 24 Decisiones Estratégicas
Se desglosaron y estructuraron las 24 dudas operativas y normativas que deben ser laudadas por la Gerencia de Distribución y el Directorio de EPEC (discrepancia de lotes 5 vs. 7 en Nansen, demora de 21 días en CLOU 1, bache de stock en invierno 2027, destino de trifásicos, mezcla de cooperativas y habilitación de subestaciones con DCU comunicando).

---

## ⚖️ Validación Triple QA
- **QA 1 (Técnico)**: Estructuración exhaustiva en Markdown sin omisión de tablas, diagramas Mermaid ni datos numéricos del PDF fuente. Copia fiel resguardada en `docs/licitacion_5573/Propuesta-despliegue-MI-2027.pdf`.
- **QA 2 (Dominio)**: Conformidad estricta con la Licitación 5573, OPs 27131/32/33/34 y las directivas de catastro por plan.
- **QA 3 (UX)**: Hipervínculos cruzados funcionales con esquema `file:///`, navegación integrada en el MOC rector y respaldo preventivo asegurado.
