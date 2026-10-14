---
title: "Ficha Técnica: Asesoramiento para Parque Solar Fotovoltaico Georreferenciado"
proyecto: "asesoramiento-parque-solar-fotovoltaico"
fecha: 2026-10-14
agente: "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]] & [[docs/Agentes/01-Analista-Financiero|Analista Financiero]] & [[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
cliente: "SFERCO RUDY DELFINA"
suministro: 3091044
contrato: "0309104402"
tarifa: "Residencial T1 (TCL 140) Trifásica"
ubicacion: "Barrio El Terrón Lote 454, Villa Allende, Córdoba"
georreferencia: "-31.25194° S, -64.29087° O"
repositorio_remoto: "https://github.com/protelemepec-coder/asesoramiento-parque-solar-fotovoltaico"
cuenta_objetivo: "https://github.com/inventarioenergycpy/asesoramiento-parque-solar-fotovoltaico"
tags:
  - #proyecto
  - #energia-solar
  - #fotovoltaica
  - #growatt
  - #sigec
  - #nasa-power
  - #villa-allende
  - #sferco
---

# ☀️ Proyecto Dedicado: Asesoramiento para Parque Solar Fotovoltaico
### Simulador Georreferenciado, Análisis por Fecha de Lectura SIGEC y Modelos Comerciales Growatt

- **Repositorio Remoto Oficial**: [`https://github.com/protelemepec-coder/asesoramiento-parque-solar-fotovoltaico`](https://github.com/protelemepec-coder/asesoramiento-parque-solar-fotovoltaico) *(Transferencia en curso hacia `inventarioenergycpy`)*
- **Directorio Local de Trabajo**: [`D:\Proyectos\asesoramiento-parque-solar-fotovoltaico`](file:///D:/Proyectos/asesoramiento-parque-solar-fotovoltaico) / [`C:\Users\jidiaz\.gemini\antigravity-ide\scratch\asesoramiento-parque-solar-fotovoltaico`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/asesoramiento-parque-solar-fotovoltaico)

---

## 🎯 1. Resumen Ejecutivo y Alcance
El proyecto proporciona un entorno autónomo y reproducible para:
1. **Extracción Automatizada de Datos Comerciales**: Conexión a la base de datos de **Oracle / XXSIGEC** de EPEC para extraer la información cadastral, contrato y las 10 últimas lecturas efectivas del medidor trifásico `9039488` entre el **22/10/2025 y el 19/08/2026** (33.178 kWh acumulados en 298 días).
2. **Georreferenciación Satelital Solar**: Incorporación de la serie horaria y mensual de radiación solar **NASA POWER** (`ALLSKY_SFC_SW_DWN`) para la celda de Villa Allende / Córdoba (-31.25°, -64.29°), calculando el **HSP ponderado día a día** entre las fechas exactas de lectura del medidor.
3. **Simulador Fotovoltaico con Restricción Práctica de Coincidencia (46%)**:
   - Modelado del balance energético donde el **autoconsumo directo en tiempo real** se limita al 46% máximo de la generación solar.
   - El restante **54%** se inyecta a la red de distribución de EPEC bajo el marco de la **Ley Nacional 27.424 y Ley Provincial 10.604 de Usuario-Generador**.
4. **Comparativa de Modelos Comerciales Growatt**:
   - Evaluación técnica de la gama trifásica: **Growatt MOD (6 kW, 8 kW, 10 kW, 12 kW)** y **Growatt MID (15 kW)** con módulos TOPCon monocristalinos de 580 Wp.
5. **Presupuestación Bimonetaria Llave en Mano**: Estructuración del presupuesto en dólares (USD) y pesos argentinos (ARS) tomando como referencia oficial la cotización billete vendedor del Banco Nación Argentina ($ 1.535,00).

---

## 📊 2. Tabla Comparativa de Modelos Growatt (Período 298 Días)

| Modelo Inversor Growatt | Potencia AC / DC | Paneles (580W) | Área Techo (m²) | Generación Solar (kWh) | Autoconsumo (46%) (kWh) | Inyección Red (54%) (kWh) | Cobertura Gen / Consumo | Presupuesto Llave en Mano (USD) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Growatt MOD 6KTL3-X** | 6 kW / 6,38 kWp | 11 | 28,6 m² | 7.766 | 3.572 | 4.194 | **23,4%** | USD 5.900 |
| **Growatt MOD 8KTL3-X** | 8 kW / 8,70 kWp | 15 | 39,0 m² | 10.594 | 4.873 | 5.721 | **31,9%** | USD 7.200 |
| **Growatt MOD 10KTL3-X ⭐ (Óptimo)** | **10 kW / 10,44 kWp** | **18** | **46,8 m²** | **12.713** | **5.848** | **6.865** | **38,3%** | **USD 8.500** |
| **Growatt MOD 12KTL3-X** | 12 kW / 12,76 kWp | 22 | 57,2 m² | 15.538 | 7.147 | 8.390 | **46,8%** | USD 9.900 |
| **Growatt MID 15KTL3-X** | 15 kW / 15,08 kWp | 26 | 67,6 m² | 18.363 | 8.447 | 9.916 | **55,3%** | USD 11.800 |

---

## 📁 3. Componentes y Entregables del Repositorio Dedicado

- `README.md`: Memoria ejecutiva, parámetros de diseño y guía CLI.
- `scripts/simulador_solar.py`: Motor matemático interactivo con CLI (`--modelo`, `--pr`, `--coincidencia`).
- `scripts/descargar_lecturas_sigec.py`: Conector nativo de extracción en Oracle EPEC.
- `data/lecturas_sigec_3091044.json` y `.csv`: Base de datos histórica con los 10 registros de lecturas.
- `data/radiacion_cordoba_nasa_power.json`: Matriz de irradiancia satelital de la NASA.
- `docs/01-Marco-Normativo-y-Regulacion-EPEC.md`: Leyes 27.424 y 10.604, ERSeP, medidor bidireccional.
- `docs/02-Base-Radiacion-Solar-NASA-POWER.md`: Irradiación solar y algoritmo de ponderación temporal.
- `docs/03-Analisis-Consumo-Suministro-3091044.md`: Ficha técnica de cliente, contrato y estacionalidad.
- `docs/04-Simulador-Modelos-Growatt.md`: Fichas técnicas de inversores trifásicos Growatt MOD y MID.
- `docs/05-Presupuesto-Tecnico-Comercial.md`: Presupuesto llave en mano con cómputo y garantías.
