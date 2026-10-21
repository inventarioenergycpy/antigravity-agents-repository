---
type: proyecto
proyecto: "Plan Maestro de Despliegue de Medidores Inteligentes AMI y Concentradores PLC"
agente_responsable: "[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Arquitecto de Sistemas EPEC]]"
agentes_colaboradores:
  - "[[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos & BI EPEC]]"
  - "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]]"
repositorio_github: "https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami"
ubicacion_local: "D:\\Proyectos\\despliegue-medidores-inteligentes-ami"
fecha_creacion: 2026-10-21
licitacion_origen: "Licitación Pública N° 5573 / Resolución N° 0653/2026"
volumen_total: "400.000 Medidores (200k Sanxing + 200k CLOU) + 6.000 Concentradores PLC + 188.000 USE"
tags:
  - #proyecto
  - #telemedicion
  - #ami
  - #epec
  - #protelem
  - #subestaciones
  - #plc
  - #sanxing
  - #clou
  - #nansen
---

# ⚡ Proyecto: Plan Maestro de Despliegue de Medidores Inteligentes AMI & Concentradores PLC (EPEC)

## 📌 Resumen Ejecutivo
Planificación estratégica, simulación de curva de stock físico con **Verificación Primitiva (`VP 20d`)**, gobernanza de compatibilidad en **Subestaciones Transformadoras (`SET OK`)** y despliegue operativo en campo para **400.000 medidores inteligentes**, **6.000 concentradores de baja tensión** y **188.000 USE de mano de obra** adjudicados en la Licitación Pública N° 5573.

---

## 🔗 Repositorio Dedicado y Enlaces
* **Repositorio Central (PROTELEM-EPEC)**: [https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami](https://github.com/PROTELEM-EPEC/despliegue-medidores-inteligentes-ami)
* **Ruta de Trabajo Local**: `D:\Proyectos\despliegue-medidores-inteligentes-ami`
* **Vínculo Scratchpad**: `C:\Users\jidiaz\.gemini\antigravity-ide\scratch\despliegue-medidores-inteligentes-ami`

---

## 📑 1. Contratos y Órdenes de Provisión Adjudicadas
1. **OP 27131 - SANFORD GLOBAL TRADE LLC**: USD 11.688.100 (160.000 Monofásicos + 40.000 Trifásicos + 3.000 Concentradores PLC).
2. **OP 27133 - NICEMA S.A.**: USD 11.688.100 (160.000 Monofásicos + 40.000 Trifásicos + 3.000 Concentradores PLC).
3. **OP 27132 - ROWING S.A.**: $10.583.507.000 ARS (94.000 USE mano de obra e instalación).
4. **OP 27134 - CONECTAR S.R.L.**: $10.583.507.000 ARS (94.000 USE mano de obra e instalación).

---

## 📅 2. Cronograma de Disponibilidad Real en Campo (`Disp.`)

Conforme a la **Resolución 247/2019 de la Secretaría de Comercio**, todo lote ingresado debe cumplir los **20 días de Verificación Primitiva (VP)** antes de salir a campo:

| Lote / Marca | Cantidad | Días Contractuales | Verificación Primitiva | Disponibilidad Real (`Disp.`) | Destino Asignado |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Sanxing E1** | **34.000** | 120 d | VP 20 d | **18/02/2027** | Arranque: Plan 18 (Capital) + San Francisco Lote 1 |
| **Sanxing E2** | **31.000** | 148 d | VP 20 d | **18/03/2027** | Cierre Distrito San Francisco (28.000 totales) |
| **CLOU E1** | **42.000** | 155 d | VP 20 d | **25/03/2027** | Arranque CLOU: Plan 6 (Continuidad con Plan 4) |
| **Sanxing E3** | **45.000** | 176 d | VP 20 d | **15/04/2027** | Plan 17 (Zona Aérea) + extensiones |
| **Sanxing E4** | **45.000** | 211 d | VP 20 d | **20/05/2027** | Distrito Río Cuarto (13.000 puntos) |
| **Sanxing E5** | **45.000** | 239 d | VP 20 d | **17/06/2027** | Distrito Villa María (6.000 puntos) + Cierre 100% Sanxing |
| **CLOU E2** | **41.500** | 330 d | VP 20 d | **16/09/2027** | Plan 8 (Post-relevamiento acometidas) |
| **CLOU E3** | **41.500** | 351 d | VP 20 d | **07/10/2027** | Plan 12 + Villa Allende (800) |
| **CLOU E4** | **75.000** | 421 d | VP 20 d | **16/12/2027** | Zona Centro Subterránea (Planes 14 y 15 GPRS) + Cierre Licitación |

---

## 🗺️ 3. Distribución Territorial y Compatibilidad por Subestación
* **Directiva de Oro**: Toda instalación requiere que la subestación asociada figure en estado **"SET OK"** (concentrador montado y comunicando con Headend).
* **Plan 19 (Capital)**: Preservar cuenca tecnológica de casi **10.000 Nansen preexistentes**.
* **Plan 6 (Capital)**: Asignación **CLOU** por colindancia y continuidad con Plan 4.
* **Plan 18 (Capital)**: Asignación **SANXING** para absorber la primera entrega de Febrero 2027.
* **San Francisco (Interior)**: Asignación masiva en bloque a **SANXING** (28.000 puntos).
* **Río Cuarto y Villa María**: Programados para el segundo trimestre de 2027 con Sanxing.

---

## 📂 Componentes del Proyecto
* `README.md`: Memoria técnica maestra.
* `index.html`, `style.css`, `app.js`: Tablero SPA ejecutivo interactivo.
* `data/`: Datasets JSON estructurados de entregas y diagnóstico territorial.
* `docs/`: 4 informes de ingeniería (análisis de licitación, protocolo SET, compatibilidad y cuadrillas) y pliegos PDF.
* `assets/img/`: Cartografía GIS de planes Zona A y diagrama Gantt de entregas.
