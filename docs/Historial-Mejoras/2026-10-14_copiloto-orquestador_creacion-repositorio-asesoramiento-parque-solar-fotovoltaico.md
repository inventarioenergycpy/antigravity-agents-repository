---
title: "Creación de Repositorio Dedicado: asesoramiento-parque-solar-fotovoltaico"
fecha: 2026-10-14
agente: "[[docs/Agentes/11-Copiloto-Orquestador-de-Skills|Copiloto Orquestador]] & [[docs/Agentes/01-Analista-Financiero|Analista Financiero]] & [[docs/Agentes/02-Ciencia-de-Datos|Ciencia de Datos]]"
tipo: "nuevo_repositorio"
repositorio_remoto: "https://github.com/protelemepec-coder/asesoramiento-parque-solar-fotovoltaico"
cuenta_objetivo: "https://github.com/inventarioenergycpy/asesoramiento-parque-solar-fotovoltaico"
tags:
  - #historial-mejoras
  - #copiloto-orquestador
  - #energia-solar
  - #growatt
  - #sigec
  - #nasa-power
  - #sferco
---

# Registro de Mejora: Repositorio Dedicado `asesoramiento-parque-solar-fotovoltaico`

## 📝 Contexto y Solicitud
El usuario solicitó emplear el **Agente 11 (Copiloto Orquestador)** para investigar en las habilidades y repositorios de **PROTELEM** la información necesaria para construir un **simulador de energía solar fotovoltaica** georreferenciado con base de datos de radiación satelital en Argentina (NASA POWER). Con los datos del cliente `SFERCO RUDY DELFINA` (Barrio El Terrón, Lote 454, Villa Allende), se requirió extraer en el sistema comercial **Oracle / XXSIGEC** el número de suministro (`3091044`), descargar el historial de lecturas reales desde noviembre de 2025, organizar los consumos por **Fecha de Lectura** (en vez del período facturado), simular el dimensionamiento de la instalación considerando los modelos comerciales de inversores trifásicos de la marca **Growatt** y aplicar la premisa operativa de que la coincidencia de consumo y generación solar no supera el **46%** en un caso práctico. Finalmente, se solicitó documentar y resguardar todo el proyecto en un nuevo repositorio Git dedicado.

## 🛠️ Acciones Realizadas

1. **Investigación y Descubrimiento en PROTELEM**:
   - Localización en `facturacion-reverse-engineering` del motor de evaluación solar (`evaluacion_solar.md`), la base de radiación satelital NASA POWER (`datos/radiacion.json`) y el esquema de consulta de lecturas (`query/caso_referencia_lecturas.sql`).

2. **Consulta y Descarga en Base de Datos Oracle / XXSIGEC**:
   - Conexión al ERP comercial de EPEC y detección del suministro `3091044` (Contrato `0309104402`, Cliente `6000840`, CUIT `27-45696222-5`, medidor trifásico activo `9039488`).
   - Descarga de las 10 lecturas consecutivas registradas entre el **22/10/2025 y el 19/08/2026**, acumulando **33.178 kWh** en 298 días efectivos.

3. **Simulación Matemática Georreferenciada por Fecha de Lectura**:
   - Ponderación diaria del HSP de NASA POWER (media 4,92 a 5,07 kWh/m²/día) para cada rango exacto entre tomas de medidor.
   - Aplicación del 46% de autoconsumo simultáneo y 54% de inyección excedente a la red de EPEC bajo el marco de la Ley 27.424 / Ley 10.604.
   - Evaluación comparativa de 5 modelos comerciales trifásicos Growatt (MOD 6K, 8K, 10K, 12K y MID 15K).

4. **Creación y Publicación del Repositorio Dedicado en GitHub**:
   - Repositorio: [`https://github.com/protelemepec-coder/asesoramiento-parque-solar-fotovoltaico`](https://github.com/protelemepec-coder/asesoramiento-parque-solar-fotovoltaico) (iniciada transferencia a `inventarioenergycpy`).
   - Directorio local: `D:\Proyectos\asesoramiento-parque-solar-fotovoltaico` y enlace Junction en el scratchpad del IDE.
   - Estructura completa: `README.md`, `data/` (JSON y CSV de lecturas y radiación), `scripts/` (`simulador_solar.py` con interfaz CLI y `descargar_lecturas_sigec.py`), y `docs/` con 5 notas técnicas modulares.

5. **Registro Cruzado en la Bóveda Central (`antigravity-agents-repository`)**:
   - Ficha técnica en `docs/Proyectos/2026-10-14_asesoramiento-parque-solar-fotovoltaico.md`.
   - Actualización del tablero principal `docs/00-Dashboard-MOC.md` e índice de proyectos `docs/Proyectos/README.md`.
