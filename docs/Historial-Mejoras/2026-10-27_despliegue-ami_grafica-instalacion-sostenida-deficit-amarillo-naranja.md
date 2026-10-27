---
title: "Actualización de Gráficas: Curva de Instalación Acumulada vs. Descenso de Stock Remanente con Instalación Sostenida y Déficit en Amarillo-Naranja"
tags:
  - #ami
  - #epec
  - #licitacion-5573
  - #graficas
  - #simulacion-22m
  - #interior
  - #deficit-stock
  - #historial-mejoras
created: 2026-10-27
updated: 2026-10-27
---

# 📈 Actualización de Gráficas: Curva de Instalación Acumulada vs. Descenso de Stock Remanente

## 📌 Contexto y Requerimiento
A solicitud del usuario, se implementaron mejoras estructurales en la gráfica principal y en el motor de simulación del proyecto **Despliegue de Medidores Inteligentes AMI (Licitación N° 5573 / Res. 0653/2026)**:
1. **Columnas Separadas de Instalación Mensual**: Desglose explícito en barras verticales lado a lado para la instalación mensual de **Capital (Zona A)** y del **Interior**.
2. **Sostenimiento de la Instalación en el Interior**: No detener la instalación al agotarse la cuota inicial de 107.000 medidores en Febrero 2028. Mantener el ritmo proporcional de **9.233,5 medidores/mes** durante los 22 meses completos (Marzo 2027 a Diciembre 2028) hasta cubrir el **100% de los suministros censados del Interior (203.137 u.)**.
3. **Resaltado de Stock Negativo en Amarillo-Naranja**: Marcar el stock remanente que desciende por debajo de cero con valores negativos y formato visual en **amarillo-naranja (`#f59e0b` / `#ea580c`)**, señalizando el quiebre de stock en Febrero 2028 (-3.802 u.) y el déficit acumulado final de **-96.137 medidores**.

---

## 🛠️ Modificaciones Realizadas

### 1. Motor de Simulación y Exportador Excel (`scripts/exportar_excel_simulacion_ami.py`)
- **Lógica de Sostenimiento**: Se eliminó la detención de obra en el Interior. El ritmo mensual de 9.233,5 u./m se ejecuta ininterrumpidamente durante los 22 meses.
- **Cómputo de Déficit**:
  - Mes 11 (Ene-2028): Stock remanente positivo de **+5.431,5 u.**
  - Mes 12 (Feb-2028): Quiebre de stock, remanente pasa a **-3.802,0 u.**
  - Mes 22 (Dic-2028): Conclusión del censo completo del Interior (**203.137 u.**), acumulando un déficit final de **-96.137 u.**
- **Gráfico Combinado (Combo Chart)**:
  - `chart_col` (Columnas): Instalación Capital Mensual (Morado `#8b5cf6`) e Instalación Interior Mensual (Azul `#0ea5e9`).
  - `chart_line` (Líneas sobre eje secundario `y2_axis`): Instalación Total Provincial Acumulada (Azul `#2563eb`) y Stock Remanente en Almacén (**Amarillo-Naranja `#f59e0b`** con marcadores circulares y línea que desciende hasta el cuadrante negativo).
- **Estilos de Celda**: Se creó `f_td_deficit_amber` para colorear en fondo ámbar (`#fef3c7`) y texto amarillo-naranja oscuro (`#b45309`) los números negativos de stock en todas las hojas.
- **Generación de Archivos**:
  - `data/Simulacion_Despliegue_AMI_EPEC_307k_Interior_22m.xlsx`
  - `C:\Users\jidiaz\Downloads\Simulacion_Despliegue_AMI_EPEC_307k_Interior_22m.xlsx`
  - `data/simulacion_sostenida_capital_interior_22m.json`
  - `data/simulacion_proporcional_interior_22m.json`

### 2. Tablero Interactivo Web SPA (`index.html`, `app.js`, `style.css`)
- **Nueva Pestaña**: Se agregó `tab-grafica-stock` con navegación en sidebar (*"📈 Curva Instalación vs. Stock"*).
- **Visualizador SVG / Canvas de Alta Definición**:
  - Gráfica combinada con columnas para Capital e Interior lado a lado.
  - Sombreado de advertencia en degradado amarillo-naranja para la **Zona de Déficit ($Y < 0$)**.
  - Línea punteada ámbar en el nivel $Y = 0$ indicando el hito de quiebre en Febrero 2028.
  - Línea de stock remanente en amarillo-naranja con callout interactivo en `-96.137 u.`
  - Tooltip reactivo con microdatos al pasar el mouse por cada periodo.
- **Tabla Mensual Sincronizada**: Formateo con badge ámbar para todas las filas con déficit de stock.
- **Botón de Descarga**: Acceso directo al archivo Excel oficial.

---

## 🛡️ Validación en 3 Instancias de QA (Multi-Perspective QA)

| Instancia | Criterio Evaluado | Resultado |
| :--- | :--- | :---: |
| **Instancia 1: QA Técnico & Algorítmico** | • Ejecución exitosa de `scripts/exportar_excel_simulacion_ami.py` (exit code 0).<br>• Cero errores de sintaxis en `app.js`, `index.html` y `style.css`.<br>• Consistencia matemática estricta: $200.000 + 203.137 = 403.137$ u. instaladas; $307.000 - 403.137 = -96.137$ u. remanentes. | **APROBADO (PASS)** |
| **Instancia 2: QA de Negocio & Dominio EPEC** | • Conformidad con la Licitación N° 5573 / Res. 0653/2026 (400k licitados, 307k EPEC, 93k Cooperativas).<br>• Censo exacto del Interior verificado: Río Cuarto (88.224), Villa María (63.282), San Francisco (36.776), Villa Allende (14.855) = 203.137 suministros.<br>• Identificación fehaciente del mes de quiebre (Feb-2028) para planificación licitatoria temprana. | **APROBADO (PASS)** |
| **Instancia 3: QA de Usabilidad & UX** | • Columnas separadas de Capital e Interior con alto contraste visual (morado vs. azul/cian).<br>• Stock remanente negativo destacado en color amarillo-naranja con sombreado de zona y badges claros.<br>• Tooltips interactivos y descarga directa del archivo Excel tanto localmente como en `Downloads/`. | **APROBADO (PASS)** |

---

## 💾 Backups Preventivos Generados
- `docs/Backups/2026-10-27_113500_exportar_excel_simulacion_ami.py.bak`
- `docs/Backups/2026-10-27_114300_index.html.bak`
- `docs/Backups/2026-10-27_114400_style.css.bak`
- `docs/Backups/2026-10-27_114500_app.js.bak`
