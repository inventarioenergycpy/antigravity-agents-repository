---
title: "Registro de Mejora: Creación de Proyecto Dedicado - Abastecimiento y Brokerage de Combustibles y Gas para Generadoras en el MEM"
tags:
  - #historial-mejoras
  - #proyecto-dedicado
  - #mem
  - #cammesa
  - #gas-natural
  - #combustibles
  - #decreto-450-2025
  - #res-se-400-2025
created: 2026-11-10
updated: 2026-11-10
---

# 📜 Registro de Mejora: Creación del Repositorio Dedicado 'abastecimiento-combustibles-gas-generadoras'

## 1. Contexto y Justificación
En el marco de la desregulación estructural del Mercado Eléctrico Mayorista (MEM) impulsada por el **Decreto PEN N.º 450/2025** y la **Resolución SE N.º 400/2025**, CAMMESA finaliza progresivamente su rol como compradora centralizada de combustibles para centrales térmicas.

Para capturar esta oportunidad comercial sin precedentes, se estructuró a través del Squad Ágil Multi-Agente (conducido por el PM Top-1 y los 3 Operadores en Top-2 con la experticia del [[docs/Agentes/09-Profesor-Experto-Mercado-Electrico|Profesor Experto en MEM]], [[docs/Agentes/01-Analista-Financiero|Analista Financiero]] y [[docs/Agentes/05-Asesor-Legal-Financiero|Asesor Legal]]) un nuevo repositorio dedicado bajo la organización **`inventarioenergycpy`**.

---

## 2. Artefactos y Entregables Implementados

1. **Nuevo Repositorio Local y Remoto**:
   - Repositorio GitHub: [`https://github.com/inventarioenergycpy/abastecimiento-combustibles-gas-generadoras`](https://github.com/inventarioenergycpy/abastecimiento-combustibles-gas-generadoras)
   - Directorio Local Físico: `E:\Proyectos\abastecimiento-combustibles-gas-generadoras` (en disco de alta capacidad con 71.5 GB libres).
   - Junction NTFS: `C:\Users\Usuario\.gemini\antigravity-ide\Proyectos\abastecimiento-combustibles-gas-generadoras`.
2. **Datasets y Parámetros Estructurados**:
   - `data/precios_combustibles_benchmark.json`: Precios PIST cuencas Neuquina/Austral/NOA, GNL Escobar, Gasoil Grado 2/3 y Fuel Oil N.º 6.
   - `data/matriz_logistica_transporte.json`: Tarifas troncales TGS/TGN/GPNK, flete camión cisterna ($0.095 USD/m³-km) y costos portuarios CIF en Dock Sud, Campana, San Nicolás y Bahía Blanca.
   - `data/directorio_generadoras_argentina.json`: Censo exhaustivo de 9 grupos generadores y 25+ centrales térmicas (> 14.700 MW) segmentadas por estatus Plan Gas.Ar vs mercado spot.
   - `data/registro_licitaciones_oferentes.json`: Registro de licitaciones CAMMESA, MEGSA y oferentes petroleros y traders.
   - `data/listado_generadoras_clasificado.csv`: Exportación tabular para Excel / Power BI.
3. **Scripts Cuantitativos Deterministas (Exit Code 0)**:
   - `scripts/analisis_mercado_precios.py`: Cálculo de Heat-Rates, Costo Variable de Producción (CVP) por tecnología y pool de ahorro anual (**USD 171,9M/año**).
   - `scripts/calculadora_logistica_flete.py`: Comparativa local vs. importado puerto (ahorro neto en muelle de **USD 66,50/m³** en Gasoil y **USD 29,80/Ton** en Fuel Oil).
   - `scripts/generador_informe_mercado.py`: Generador y exportador tabular.
4. **Documentación Técnica Integral (Bóveda Obsidian y Repositorio)**:
   - `docs/01-Estudio-Mercado-Precios-Combustibles.md`
   - `docs/02-Analisis-Logistica-Interna-Importacion.md`
   - `docs/03-Listado-Generadoras-PlanGas-Potenciales-Clientes.md`
   - `docs/04-Marco-Regulatorio-Decreto450-Res400-Oportunidad-Brokerage.md`
   - Ficha cruzada en central: `docs/Proyectos/2026-11-10_abastecimiento-combustibles-gas-generadoras.md`
   - Actualización de `docs/00-Dashboard-MOC.md`.

---

## 3. Respaldo Preventivo Verificado (.bak)
- Backup de `00-Dashboard-MOC.md` previo a la modificación:
  [`docs/Backups/2026-11-10_130300_00-Dashboard-MOC.md.bak`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Backups/2026-11-10_130300_00-Dashboard-MOC.md.bak)
