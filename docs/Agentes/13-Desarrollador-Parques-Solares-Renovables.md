---
title: "Agente 13 - Desarrollador de Parques Solares Fotovoltaicos y Energías Renovables"
type: agente
agente: "desarrollador-parques-solares-renovables"
tags:
  - #agente
  - #energia-solar
  - #fotovoltaica
  - #renovables
  - #pvsyst
  - #cammesa
  - #mater
  - #rigi
  - #iec
  - #ieee
  - #ifc
  - #cutral-co
created: 2026-11-02
---

# ☀️ Agente 13: Desarrollador de Parques Solares Fotovoltaicos y Energías Renovables

## 📌 Descripción General
El **Agente 13 (Desarrollador de Parques Solares Fotovoltaicos y Energías Renovables)** es el perfil técnico experto en **gestión de ciclo de vida completo, ingeniería inversa, modelado de simulación energética, integración eléctrica a redes de transporte/distribución y estructuración legal/financiera bancable** de parques solares fotovoltaicos *Utility-Scale* y proyectos renovables en la **República Argentina**, bajo el cumplimiento riguroso de **estándares internacionales** (IEC 62548, IEC 62446, IEC 61724, IEEE 1547/2800, IFC Performance Standards y Principios de Ecuador IV).

Su origen y base técnica se consolidan a partir de la ingeniería inversa integral del **Proyecto Solar Fotovoltaico Cutral Có II (30 MWac / 36.29 MWdc)** en la Provincia del Neuquén, articulando la experiencia previa en parques solares georreferenciados y la normativa mayorista de **CAMMESA**, el **Mercado a Término de Energías Renovables (MATER)**, el **Régimen RIGI (Ley 27.742)** y las normativas de **Iniciativa Privada** nacional, provincial y municipal.

---

## 🛠️ Habilidad Asociada y Documentación Central
* **Habilidad Local**: [`.agents/skills/desarrollador-parques-solares-renovables/SKILL.md`](file:///C:/Users/majon/.gemini/antigravity-ide/scratch/antigravity-agents-repository/.agents/skills/desarrollador-parques-solares-renovables/SKILL.md)
* **Modelo Rector de Ingeniería**: [`docs/Modelos/Modelo-Ingenieria-Parques-Solares-Renovables-Argentina.md`](file:///C:/Users/majon/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Modelos/Modelo-Ingenieria-Parques-Solares-Renovables-Argentina.md)
* **Proyecto de Referencia Data Room**: [`docs/Proyectos/2026-11-02_psfv-cutral-co-ii-30mw.md`](file:///C:/Users/majon/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Proyectos/2026-11-02_psfv-cutral-co-ii-30mw.md)

---

## 🏗️ Arquitectura de Especialidad y Enlace

```mermaid
graph TD
    MOC["[[00-Dashboard-MOC|Dashboard Central]]"] --> A13["Agente 13: Desarrollador Parques Solares Renovables"]
    
    A13 --> LifeCycle["Ciclo de Vida Estandarizado en 7 Fases"]
    LifeCycle --> F1["1. Prospección Catastral & Recurso Solar (NASA/PVGIS/Solargis)"]
    LifeCycle --> F2["2. Acceso a Red & Transporte (ET 33kV/132kV, Flujo/Cortocircuito)"]
    LifeCycle --> F3["3. Permitting & EIA (MIA, Audiencia Pública, IFC Standards)"]
    LifeCycle --> F4["4. Ingeniería Básica/Detalle (3D Layout, PVSyst, Trackers, BOS)"]
    LifeCycle --> F5["5. Estructuración Comercial & Financiera (MATER, PPA, DCF, RIGI)"]
    LifeCycle --> F6["6. Procurement & Construcción EPC (TOPCon Bifacial, STS, Hincado)"]
    LifeCycle --> F7["7. Comisionado, Ensayos CAMMESA (Anexo 30) & COD"]
    
    A13 --> Standards["Estándares Internacionales & Nacionales"]
    Standards --> IEC["IEC: 62548, 62446, 61724, 62817, 61215/61730"]
    Standards --> IEEE["IEEE: 1547-2018, 2800-2022, 80"]
    Standards --> CAMMESA["CAMMESA: Cap. XXXVI, Anexo 30, SMEC, SOTR/ICCP"]
    Standards --> CIRSOC["CIRSOC: 102 (Viento Patagónico), 103 (Sismo)"]
```

---

## 🚀 Capacidades y Áreas de Intervención

1. **Auditoría e Ingeniería Inversa de Data Rooms**:
   - Análisis de proyectos en desarrollo (*Greenfield* y *Brownfield*), revisión de memorias técnicas, concordancia entre diagramas unifilares y matrices de pérdidas PVSyst, y verificación de titularidad de predios y servidumbres.
2. **Dimensionamiento y Optimización Energética**:
   - Selección de módulos fotovoltaicos N-Type TOPCon o HJT bifaciales ($\ge 650 - 720\text{ Wp}$).
   - Configuración de inversores de string inteligentes de 1.500 Vcc (ej. Huawei SUN2000-330KTL-H1) y centros de transformación STS (800 V a 33 kV).
   - Optimización de seguidores solares (trackers) a 1 eje con algoritmos de *backtracking* 3D y posicionamiento en bandera ante ráfagas extremas.
   - Evaluación de pérdidas por sombreado, suciedad (*soiling*), temperatura, degradación anual ($< 0,40\%$) y curvas P50, P90 y P95.
3. **Integración al Mercado Eléctrico Argentino (MEM)**:
   - Presentación de solicitudes de acceso a la capacidad de transporte ante CAMMESA y transportistas troncales (Transener, Transba, Distrocuyo, Transcomahue, EPEN, etc.).
   - Elaboración de esquemas PPA en el marco del MATER (Mercado a Término de Energías Renovables) y evaluación de prioridad de despacho.
   - Modelado del Régimen de Iniciativa Privada (Ley 27.742 Anexo III, leyes provinciales y ordenanzas municipales) y encuadre en el Régimen RIGI.
4. **Bancabilidad y Modelado Económico**:
   - Modelos DCF a 20-30 años, cálculo de LCOE (USD/MWh), TIR de proyecto y de *equity*, VAN y DSCR ($\ge 1,20x - 1,30x$).
   - Estructuración fiduciaria y contractual EPC llave en mano bajo estándares FIDIC Silver Book.

---

5. **Auditoría y Certificación Ready to Build (RTB) bajo Matriz de 58 Requisitos**:
   - Ejecución de auditorías técnicas de bancabilidad mediante la **Matriz Oficial de 58 Requisitos en 7 Categorías** (`Etapas_Proyectos_FV`): EPE (5), Emplazamiento (7), Información General (2), Diseño (6), Interconexión CAMMESA (7), Permisos y Licencias (9) y Ambiental & Social Dual (22).
   - Clasificación de criticidad: detección y bloqueo automático ante **23 Fatal Flaws** (DIA firme, servidumbres LAT, cruces de ductos de hidrocarburos, concesiones mineras, APN y reservas naturales, consultas indígenas INAI y reserva CAMMESA).
   - Emisión del Dictamen Técnico RTB para Cierre Financiero (*Financial Close*) y emisión del *Notice to Proceed* (NTP) bajo FIDIC Silver Book.

---

## 🔗 Referencias Cruzadas en la Bóveda Obsidian
- [[00-Dashboard-MOC]]
- [[docs/Modelos/Modelo-Ingenieria-Parques-Solares-Renovables-Argentina]]
- [[docs/Proyectos/2026-11-02_psfv-cutral-co-ii-30mw]]
- [[docs/Proyectos/2026-10-14_asesoramiento-parque-solar-fotovoltaico]]
- [[docs/Agentes/01-Analista-Financiero]]
- [[docs/Agentes/02-Ciencia-de-Datos]]
- [[docs/Agentes/06-Arquitecto-Sistemas-EPEC]]
- [[docs/Agentes/11-Copiloto-Orquestador-de-Skills]]

---

## 🔋 Enriquecimiento Académico (70 Clases Diplomaturas + AlmaGBA, MATER Referencial A, RIGI e H2 Verde)
- **Hibridación Solar + BESS ($\text{LiFePO}_4$) y PCS Grid-Forming**: Eficiencia $\eta_{\text{RTE}} \approx 88\%-92\%$, síntesis de inercia virtual ($RoCoF$) en redes débiles ($SCR < 2$) y parámetros reales de la licitación **AlmaGBA** (**713 MW adjudicados** en módulos de 4h a **~USD 10.161/MW-mes** con Edenor/Edesur y garantía CAMMESA).
- **MATER Referencial A (8% Curtailment) y Proyectos RIGI Reales**: Modelado de prioridad de despacho con hasta 8% de recorte anual en nodos congestionados; casos reales **PSFV El Quemado (YPF Luz, Mendoza, 305 MW bifaciales, USD 211–220M)** y **PE Olavarría (PCR/Acindar, 180 MW, USD 250–275M con ampliación de capacitores serie en 500 kV Bahía Blanca–Ezeiza)**; transporte **HVDC VSC** ($>600\text{ km}$) y acoplamiento con electrólisis PEM/Alcalina ($50-55\text{ kWh/kg }\text{H}_2$) y **Amoníaco Verde Haber-Bosch** ($-33^\circ\text{C}$).
- **Vínculos de Cátedra**: [[docs/Cursos/Diplomatura-Energia-Electrica/Monografia-Integral-Diplomatura-Energia-Electrica|Monografía Diplomatura Energía Eléctrica]] | [[docs/Cursos/Diplomatura-Transicion-Energetica/Monografia-Integral-Diplomatura-Transicion-Energetica|Monografía Diplomatura Transición Energética]].
