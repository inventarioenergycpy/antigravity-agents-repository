---
title: "Documento Técnico N° 08: Arquitectura de Gráficas Ejecutivas - Flujo Mensual de Medidores EPEC, Curvas Acumuladas y Balance de Stock con Escalas Niveladas"
tags:
  - #ami
  - #epec
  - #licitacion-5573
  - #graficas-ejecutivas
  - #balance-stock
  - #escalas-niveladas
  - #xlsxwriter
  - #spa-svg
created: 2026-10-27
updated: 2026-10-27
---

# 📊 Documento Técnico N° 08: Arquitectura de Gráficas Ejecutivas
## Flujo Mensual de Medidores EPEC, Curvas Acumuladas y Balance de Stock con Escalas Niveladas

> [!IMPORTANT]
> **Documento Oficial de Ingeniería y Sistemas N° 08 · `PROTELEM-EPEC`**  
> **Proyecto:** Despliegue Masivo de Medidores Inteligentes AMI (Licitación Pública N° 5573)  
> **Objetivo:** Establecer la especificación técnica, matemática y visual de la gráfica ejecutiva *"Curva de Instalación Acumulada, Entregas y Descenso de Stock Remanente (Instalación Sostenida y Déficit en Amarillo-Naranja)"*, su calibración de escalas en Excel nativo y en la aplicación web interactiva (SPA).

---

## 📌 1. Resumen Ejecutivo y Problemática Resuelta

Durante las simulaciones del despliegue provincial de medidores inteligentes (403.137 suministros censados vs. 307.000 medidores asignados a EPEC bajo Licitación 5573), se identificó la necesidad de un tablero gráfico que comunique de manera simultánea e inequívoca:

1. **El ritmo de ingreso físico de medidores a los almacenes de EPEC** (lotes contractuales de Sanxing y CLOU).
2. **El ritmo mensual de instalación en campo**, segregando Córdoba Capital (20.000 u./mes fijas por 10 meses) del Interior de la Provincia (9.233,5 u./mes sostenidas por 22 meses).
3. **La curva acumulada provincial de instalación** que asciende de $0$ a $403.137$ medidores.
4. **La disponibilidad neta de stock remanente en almacén**, evidenciando con total claridad el periodo de reserva positiva (verde) y el momento exacto del **quiebre de stock** donde la curva se sumerge en valores negativos (déficit en amarillo-naranja hasta $-96.137$ medidores).

---

## 📐 2. Arquitectura de Doble Eje Nivelado al Cero ($Y1$ y $Y2$)

Para evitar distorsiones visuales y permitir que las columnas mensuales convivan armónicamente con las curvas acumuladas y el stock negativo, se implementó un sistema de **cero compartido y nivelado** en la misma línea horizontal de la cuadrícula ($1/6$ de la altura gráfica).

```
[Eje Izquierdo Y1: Flujo Mensual]                   [Eje Derecho Y2: Acumulados y Stock]
 100.000 u./mes ------------------------------------- +500.000 u.
  80.000 u./mes ------------------------------------- +400.000 u.
  60.000 u./mes ------------------------------------- +300.000 u.
  40.000 u./mes ------------------------------------- +200.000 u.
  20.000 u./mes ------------------------------------- +100.000 u.
       0 u./mes =====================================        0 u. (Línea Base de Quiebre)
 -20.000 u./mes ------------------------------------- -100.000 u. (Zona de Déficit Negativo)
```

### Relación de Escalas:
* **Eje Izquierdo $Y1$ (Flujo Mensual: Ingresos e Instalación)**:
  * Rango: **$-20.000$ a $100.000$ medidores/mes** (amplitud total: $120.000$).
  * Unidad mayor: **$20.000$ u./mes** ($6$ intervalos iguales).
  * Posición del cero: $20.000 / 120.000 = \mathbf{16,67\% \ (1/6)}$.
  * Formato de número: `#,##0;;0` (oculta los valores negativos bajo el eje para mantener despejada la base).
* **Eje Derecho $Y2$ (Curvas Acumuladas y Stock Remanente)**:
  * Rango: **$-100.000$ a $500.000$ medidores** (amplitud total: $600.000$).
  * Unidad mayor: **$100.000$ medidores** ($6$ intervalos iguales).
  * Posición del cero: $100.000 / 600.000 = \mathbf{16,67\% \ (1/6)}$.
  * Formato de número: `#,##0` (permite visualizar nítidamente los valores negativos $-100.000$).

---

## 🎨 3. Definición de Series y Código Cromático

La gráfica combina un gráfico base de **columnas agrupadas** para los ritmos mensuales con un subgráfico de **líneas continuas** para las acumulaciones:

### A. Columnas (Eje Primario $Y1$ - Flujo Mensual)
1. **Ingreso Mes EPEC** (`#38bdf8` / Celeste vibrante con borde `#0284c7`):
   * Muestra el volumen físico entregado en Almacén Ferreyra cada mes.
   * Valores: Feb-27: 34.000 u.; Mar-27: 73.000 u.; Abr a Jun-27: 45.000 u./m; Jul-Ago: 0 u.; Sep-27: 41.500 u.; Oct-27: 23.500 u.; Nov-27 a Dic-28: 0 u.
2. **Instalación Capital Mensual** (`#8b5cf6` / Morado con borde `#7c3aed`):
   * Ritmo contractualmente establecido para Zona A: **20.000 medidores/mes** constantes durante 10 meses (Marzo a Diciembre 2027), alcanzando los 200.000 medidores previstos.
3. **Instalación Interior Mensual** (`#0ea5e9` / Azul Cian con borde `#0284c7`):
   * Ritmo proporcional sostenido para el Interior: **9.233,5 medidores/mes** durante todo el horizonte de 22 meses (Marzo 2027 a Diciembre 2028), completando el censo de 203.137 suministros.

### B. Líneas (Eje Secundario $Y2$ - Curvas Acumuladas y Stock)
4. **Instalación Total Provincial Acumulada** (`#2563eb` / Azul Royal, línea de 2.5 pt con marcadores cuadrados):
   * Comienza en 0 u. y asciende progresivamente hasta completar **403.137 medidores** en Diciembre 2028.
5. **Stock Remanente Positivo ($\ge 0$)** (`#10b981` / Verde Esmeralda, línea de 3.0 pt con marcadores circulares):
   * Refleja el saldo real disponible en almacén mientras hay existencia física.
   * Comienza en 34.000 u., alcanza su pico en Mayo-2027 (+125.066 u.) y se reduce a +5.431 u. en Enero-2028.
6. **Déficit Faltante ($< 0$)** (`#f59e0b` / `#ea580c` / Amarillo-Naranja con marcadores circulares):
   * Representa los suministros pendientes de medidor que carecen de cobertura física de stock bajo la Licitación 5573.
   * Se inicia exactamente en el **quiebre de Febrero 2028 (-3.802 u.)** y desciende mes a mes hasta acumular **-96.137 medidores faltantes**.

![Curva de Instalación Acumulada, Entregas y Descenso de Stock Remanente (Instalación Sostenida y Déficit en Amarillo-Naranja)](../assets/img/grafica_01_curva_acumulada_entregas_stock_remanente.png)

---

## 📋 4. Matriz Mensual Consolidada de Simulación (Feb-27 a Dic-28)

$$\text{Stock Remanente}_m = \text{Entregas Acumuladas}_m - \text{Instalación Provincial Acumulada}_m$$

| Periodo | Mes N° | Ingreso Mes EPEC (u.) | Stock Acum. Licitación (u.) | Inst. Capital Mes (u.) | Inst. Interior Mes (u.) | Inst. Total Mes (u.) | Inst. Total Acum. (u.) | Stock Remanente (u.) | Estado del Stock |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **2027-02** | — | **34.000** | 34.000 | 0 | 0 | 0 | 0 | **+34.000** | Acopio inicial en Almacén |
| **2027-03** | 1 | **73.000** | 107.000 | 20.000 | 9.233,5 | 29.233,5 | 29.233,5 | **+77.766,5** | Stock Fuerte (+77k) |
| **2027-04** | 2 | **45.000** | 152.000 | 20.000 | 9.233,5 | 29.233,5 | 58.467,0 | **+93.533,0** | Stock Fuerte (+93k) |
| **2027-05** | 3 | **45.000** | 197.000 | 20.000 | 9.233,5 | 29.233,5 | 87.700,5 | **+109.299,5** | Pico de Acopio (+109k) |
| **2027-06** | 4 | **45.000** | 242.000 | 20.000 | 9.233,5 | 29.233,5 | 116.934,0 | **+125.066,0** | **MÁXIMO HISTÓRICO (+125k)** |
| **2027-07** | 5 | **0** | 242.000 | 20.000 | 9.233,5 | 29.233,5 | 146.167,5 | **+95.832,5** | Receso invernal (consumo) |
| **2027-08** | 6 | **0** | 242.000 | 20.000 | 9.233,5 | 29.233,5 | 175.401,0 | **+66.599,0** | Receso invernal (consumo) |
| **2027-09** | 7 | **41.500** | 283.500 | 20.000 | 9.233,5 | 29.233,5 | 204.634,5 | **+78.865,5** | Ingreso Lote CLOU E2 |
| **2027-10** | 8 | **23.500** | 307.000 | 20.000 | 9.233,5 | 29.233,5 | 233.868,0 | **+73.132,0** | **TOPE LICITACIÓN (307.000 u.)** |
| **2027-11** | 9 | **0** | 307.000 | 20.000 | 9.233,5 | 29.233,5 | 263.101,5 | **+43.898,5** | Consumo sostenido |
| **2027-12** | 10 | **0** | 307.000 | 20.000 | 9.233,5 | 29.233,5 | 292.335,0 | **+14.665,0** | Cierre Zona A (200k instalados) |
| **2028-01** | 11 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 301.568,5 | **+5.431,5** | Remanente crítico de reserva |
| **2028-02** | 12 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 310.802,0 | <span style="color:#ea580c">**-3.802,0**</span> | ⚠️ **QUIEBRE FORMAL DE STOCK** |
| **2028-03** | 13 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 320.035,5 | <span style="color:#ea580c">**-13.035,5**</span> | Déficit creciente en Interior |
| **2028-04** | 14 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 329.269,0 | <span style="color:#ea580c">**-22.269,0**</span> | Déficit creciente en Interior |
| **2028-05** | 15 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 338.502,5 | <span style="color:#ea580c">**-31.502,5**</span> | Déficit creciente en Interior |
| **2028-06** | 16 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 347.736,0 | <span style="color:#ea580c">**-40.736,0**</span> | Déficit creciente en Interior |
| **2028-07** | 17 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 356.969,5 | <span style="color:#ea580c">**-49.969,5**</span> | Déficit creciente en Interior |
| **2028-08** | 18 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 366.203,0 | <span style="color:#ea580c">**-59.203,0**</span> | Déficit creciente en Interior |
| **2028-09** | 19 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 375.436,5 | <span style="color:#ea580c">**-68.436,5**</span> | Déficit creciente en Interior |
| **2028-10** | 20 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 384.670,0 | <span style="color:#ea580c">**-77.670,0**</span> | Déficit creciente en Interior |
| **2028-11** | 21 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 393.903,5 | <span style="color:#ea580c">**-86.903,5**</span> | Déficit creciente en Interior |
| **2028-12** | 22 | **0** | 307.000 | 0 | 9.233,5 | 9.233,5 | 403.137,0 | <span style="color:#ea580c">**-96.137,0**</span> | 🎯 **DÉFICIT FINAL (-96.137 u.)** |

---

## 🖼️ 5. Catálogo Completo de Gráficas Nativas Generadas desde el Modelo Excel (`Simulacion_Despliegue_AMI_EPEC_307k_Interior_22m.xlsx`)

El modelo analítico oficial incorpora un panel de **6 gráficas ejecutivas de alta resolución** exportadas directamente desde la hoja `Tablero y Gráficas` del libro Excel distribuible:

### Gráfica 1: Curva de Instalación Acumulada, Entregas y Descenso de Stock Remanente
> **Foco:** Balance consolidado provincial, visualización del quiebre en Febrero-2028 y proyección del déficit acumulado de -96.137 unidades en amarillo-naranja.
![Curva de Instalación Acumulada, Entregas y Descenso de Stock Remanente (Instalación Sostenida y Déficit en Amarillo-Naranja)](../assets/img/grafica_01_curva_acumulada_entregas_stock_remanente.png)

---

### Gráfica 2: Ritmo Mensual de Instalación: Zona A (Capital) vs. Interior
> **Foco:** Comparación directa de intensidades operativas: Zona A concentrada en 20.000 u./mes por 10 meses vs. Interior sostenido a 9.233,5 u./mes por 22 meses.
![Ritmo Mensual de Instalación: Zona A (Capital) vs. Interior](../assets/img/grafica_02_ritmo_mensual_zona_a_vs_interior.png)

---

### Gráfica 3: Interior: Ritmo Mensual Proporcional por Distrito (22 Meses Sostenido)
> **Foco:** Distribución equitativa distrital según peso censal: Río Cuarto (4.010 u/m), Villa María (2.876 u/m), San Francisco (1.672 u/m) y Villa Allende (675 u/m).
![Interior: Ritmo Mensual Proporcional por Distrito (22 Meses Sostenido)](../assets/img/grafica_03_interior_ritmo_mensual_proporcional_distritos.png)

---

### Gráfica 4: Interior: Curvas Acumuladas por Distrito (100% Cobertura Sostenida 22 Meses)
> **Foco:** Trayectoria acumulativa de medidores instalados por ciudad hasta completar los 203.137 suministros censados.
![Interior: Curvas Acumuladas por Distrito (100% Cobertura Sostenida 22 Meses)](../assets/img/grafica_04_interior_curvas_acumuladas_distritos.png)

---

### Gráfica 5: Zona A: Suministros Relevados vs. Pendientes de Relevamiento por Plan
> **Foco:** Auditoría censal en Córdoba Capital sobre 159.838 suministros: 96.796 relevados (60,56%) vs. 63.042 pendientes (39,44%), priorizando Plan 8 y Plan 17.
![Zona A: Suministros Relevados vs. Pendientes de Relevamiento por Plan](../assets/img/grafica_05_zona_a_relevados_vs_pendientes_por_plan.png)

---

### Gráfica 6: Zona A: Despliegue por Plan con Nueva Tecnología (CLOU: 8,6,17 | NANSEN: 18,19,12)
> **Foco:** Cronograma armónico mensual de 20.000 u./mes segregado por tecnología: CLOU (Planes 6, 8, 17) y NANSEN (Planes 18, 19, 12) + cuencas densas.
![Zona A: Despliegue por Plan con Nueva Tecnología (CLOU: 8,6,17 | NANSEN: 18,19,12)](../assets/img/grafica_06_zona_a_despliegue_por_plan_nueva_tecnologia.png)

---

## 🛠️ 6. Consideraciones Técnicas y Compatibilidad OpenXML (Excel)

Durante el diseño de la gráfica combinada en Python mediante la biblioteca `xlsxwriter`, se identificó una restricción crítica del esquema **OpenXML DrawingML**:

> [!WARNING]
> **Restricción OpenXML:** Microsoft Excel no permite que un gráfico de tipo `column` tenga series asignadas a un eje secundario (`'y2_axis': True`) si simultáneamente se combina (`combine()`) con un gráfico de tipo `line` que también utiliza `'y2_axis': True`. Esto genera un conflicto en los identificadores de eje (`<c:axId>`) que provoca un error irrecuperable al abrir el archivo en Excel.

### Solución Técnica Implementada:
1. **Gráfico Base (`chart_col`)**: Contiene **exclusivamente las tres series de columnas** (`Ingreso Mes EPEC`, `Inst. Capital Mensual`, `Inst. Interior Mensual`), asignadas todas al eje primario $Y1$ (rango $-20.000$ a $100.000$).
2. **Gráfico Superpuesto (`chart_line`)**: Contiene **las tres series de líneas** (`Inst. Total Provincial Acum.`, `Stock Positivo`, `Déficit Faltante`), asignadas todas al eje secundario $Y2$ (`'y2_axis': True`, rango $-100.000$ a $500.000$).
3. **Resultado**: Archivo OpenXML 100% estándar, compatible con todas las versiones de Microsoft Excel (2016, 2019, 2021, Office 365) y libre de advertencias de reparación.

---

## 🌐 7. Implementación en la Aplicación Web (SPA)

En la interfaz web interactiva (`app.js`, `index.html`, `style.css`), la gráfica se implementa mediante un elemento `<svg>` dinámico con las siguientes características:
* **Escala Vertical Nivelada**: Las funciones de transformación matemática `getYLine()` y `getColH()` mapean el cero exactamente en el $83,33\%$ de la altura disponible (`yZero = 352.5px`).
* **Columnas Clustered**: Cada mes dibuja 3 barras rectangulares de 8px de ancho, con gradientes SVG independientes (`#ingresoGradient`, `#capGradient`, `#intGradient`).
* **Detección Dinámica de Quiebre**: La función interpola el punto exacto donde la línea de stock remanente corta el cero entre Enero y Febrero 2028, renderizando el indicador circular `Quiebre (0 u.)`.
* **Tooltip Enriquecido**: Despliega en tiempo real al pasar el cursor el ingreso puntual del mes, las instalaciones y el saldo remanente con indicadores visuales de estado.

---

## 📂 8. Trazabilidad de Archivos y Versiones

| Recurso | Ruta en el Repositorio | Descripción |
| :--- | :--- | :--- |
| **Script Generador** | [`scripts/exportar_excel_simulacion_ami.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/despliegue-medidores-inteligentes-ami/scripts/exportar_excel_simulacion_ami.py) | Genera el libro Excel con fórmulas, formatos y gráficas nativas. |
| **Excel Oficial** | [`data/Simulacion_Despliegue_AMI_EPEC_307k_Interior_22m.xlsx`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/despliegue-medidores-inteligentes-ami/data/Simulacion_Despliegue_AMI_EPEC_307k_Interior_22m.xlsx) | Libro de cálculo oficial distribuible para gerencia y auditoría. |
| **Descarga Local** | [`C:\Users\jidiaz\Downloads\Simulacion_Despliegue_AMI_EPEC_307k_Interior_22m.xlsx`](file:///C:/Users/jidiaz/Downloads/Simulacion_Despliegue_AMI_EPEC_307k_Interior_22m.xlsx) | Copia directa en la carpeta de descargas del usuario. |
| **Lógica Web (JS)** | [`app.js`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/despliegue-medidores-inteligentes-ami/app.js) | Renderizado SVG interactivo de la gráfica ejecutiva. |
| **Estructura Web** | [`index.html`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/despliegue-medidores-inteligentes-ami/index.html) | Vista ejecutiva con mini-KPIs, controles y leyenda del tablero. |
| **Estilos Web** | [`style.css`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/despliegue-medidores-inteligentes-ami/style.css) | Tokens de diseño, gradientes y badges de estado. |
