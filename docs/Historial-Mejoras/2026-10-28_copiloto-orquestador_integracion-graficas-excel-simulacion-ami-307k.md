---
title: "Copiloto Orquestador - Actualización de Gráficas de Simulación AMI 307k (Etiquetas de Datos dLbls, Layout Ajustado y Sincronización)"
tags:
  - #ami
  - #epec
  - #licitacion-5573
  - #graficas-ejecutivas
  - #data-labels
  - #excel
  - #historial-mejoras
  - #copiloto-orquestador
  - #triple-qa
created: 2026-10-28
updated: 2026-10-28
---

# 📈 Copiloto Orquestador: Actualización de Gráficas de Simulación AMI 307k con Etiquetas Numéricas Directas

## 📌 Contexto de la Actualización
El usuario realizó ajustes visuales y analíticos avanzados sobre las gráficas nativas en Microsoft Excel, guardando la versión perfeccionada en [`Simulacion_Despliegue_AMI_EPEC_307k.xlsx`](file:///D:/Proyectos/despliegue-medidores-inteligentes-ami/data/Simulacion_Despliegue_AMI_EPEC_307k.xlsx) y exportando el testimonio metrológico en [`curva entregas de med MI.pdf`](file:///D:/Usuarios/jidiaz/Downloads/curva%20entregas%20de%20med%20MI.pdf).

### Principales Modificaciones Detectadas en las Gráficas:
1. **Etiquetas de Datos Directas (`dLbls`)**:
   - Se activaron etiquetas numéricas directas sobre las barras de entrega de medidores (Feb: 34.000, Mar: 73.000, Abr a Jun: 45.000, Sep: 41.500, Oct: 23.500).
   - Se habilitaron etiquetas de stock remanente positivo sobre los hitos de acopio (+34k, +77.7k, +93.5k, +109.3k, pico de +125.066 u., +5.432 u. en Enero 2028).
   - Se rotularon explícitamente los valores de déficit en la zona de agotamiento (-3.802 u. en Feb-28, -13.036 u., hasta el cierre de -96.137 u. en Dic-28).
2. **Re-escalado y Proporciones de Gráficos 1, 2 y 6**:
   - Ajuste de espaciado entre series, tamaños de fuentes en títulos y ejes secundarios sin solapamientos.
3. **Sincronización Multi-Directorio**:
   - Se replicó el archivo actualizado en `data/` y en las rutas de descarga `%USERPROFILE%\Downloads` bajo ambas nomenclaturas (`Simulacion_Despliegue_AMI_EPEC_307k.xlsx` y `Simulacion_Despliegue_AMI_EPEC_307k_Interior_22m.xlsx`).

---

## 🛡️ Resguardos Preventivos (Backups)
Se consolidaron copias exactas en la bóveda de resguardo del Hub Central:
- `docs/Backups/2026-10-28_075217_*.bak` (Línea base previa).
- `docs/Backups/2026-10-28_080815_*.bak` (Línea base con integración completa de gráficas con etiquetas de datos).

---

## 🎨 Catálogo de Assets PNG Re-Exportados en Ultra-Resolución

| Gráfica | Archivo PNG | Nueva Resolución | Peso | Características Visuales Incorporadas |
| :-: | :--- | :---: | :---: | :--- |
| **1** | `grafica_01_curva_acumulada_entregas_stock_remanente.png` | $1404 \times 487$ | 48.2 KB | Etiquetas numéricas directas en entregas, stock remanente y déficit amarillo-naranja. |
| **2** | `grafica_02_ritmo_mensual_zona_a_vs_interior.png` | $1029 \times 525$ | 10.3 KB | Columnas agrupadas con comparativa de ritmos 20k vs. 9.2k u./m. |
| **3** | `grafica_03_interior_ritmo_mensual_proporcional_distritos.png` | $1029 \times 525$ | 17.7 KB | Desglose distrital mensual proporcional para los 4 distritos del Interior. |
| **4** | `grafica_04_interior_curvas_acumuladas_distritos.png` | $1029 \times 525$ | 32.3 KB | Trayectorias acumuladas distritales continuas hacia los 203.137 suministros. |
| **5** | `grafica_05_zona_a_relevados_vs_pendientes_por_plan.png` | $1029 \times 525$ | 8.0 KB | Barras de balance censal en Capital (Plan 8 virgen 99,7% vs. Plan 18/19 listos). |
| **6** | `grafica_06_zona_a_despliegue_por_plan_nueva_tecnologia.png` | $1029 \times 525$ | 31.8 KB | Despliegue mensual por tecnología CLOU (8, 6, 17) y NANSEN (18, 19, 12). |

---

## ⚖️ Verificación Triple QA
- **QA 1 (Técnico)**: Re-exportación limpia a 1404x487 px; etiquetas de datos legibles al 100% sin solapamientos; legacy copy `grafica_flujo_mensual_epec_balance_stock.png` sincronizada.
- **QA 2 (Dominio)**: Conciliación centavo a centavo y unidad a unidad entre la curva PDF (`curva entregas de med MI.pdf`), el libro Excel y los cuadros de la documentación.
- **QA 3 (UX/Usabilidad)**: Trazabilidad total de enlaces y previsualización inmediata en Obsidian y GitHub.
