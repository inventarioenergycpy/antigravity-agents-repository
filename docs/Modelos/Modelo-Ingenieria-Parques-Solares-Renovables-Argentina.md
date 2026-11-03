---
title: "Modelo Maestro de Ingeniería para Parques Solares Fotovoltaicos y Energías Renovables en Argentina"
tipo: "modelo-ingenieria"
fecha: 2026-11-02
autor: "[[docs/Agentes/13-Desarrollador-Parques-Solares-Renovables|Desarrollador Parques Solares Renovables]] & Squad de Ingeniería Reversa"
estandares_internacionales:
  - "IEC 62548 (PV Array Design)"
  - "IEC 62446-1/2 (Testing & Commissioning)"
  - "IEC 61724-1/2/3 (Performance Monitoring & PR)"
  - "IEC 62817 (Tracker Qualification)"
  - "IEEE 1547-2018 / IEEE 2800-2022 (Grid Interconnection & IBR)"
  - "IEEE 80 (Substation Grounding)"
  - "IFC Performance Standards (1-8) & Equator Principles IV"
  - "DNV GL / NREL Bankability Guidelines"
normativa_argentina:
  - "CAMMESA Los Procedimientos (Capítulo XXXVI y Anexo 30)"
  - "Resolución MEyM 281-E/2017 & SE 330/2023 (MATER)"
  - "Ley 27.191 (Régimen de Fomento Renovables & FODER)"
  - "Ley 27.742 (Ley Bases - RIGI & Iniciativa Privada Anexo III)"
  - "INPRES-CIRSOC 103 (Diseño Sismorresistente)"
  - "CIRSOC 102 (Acción del Viento)"
  - "AEA 90364-7-712 (Instalaciones Fotovoltaicas)"
tags:
  - #modelo-ingenieria
  - #ingenieria-inversa
  - #energia-solar
  - #renovables
  - #iec
  - #ieee
  - #cammesa
  - #mater
  - #rigi
  - #iniciativa-privada
  - #argentina
---

# ⚡ Modelo Maestro de Ingeniería para Parques Solares Fotovoltaicos y Energías Renovables en Argentina
### Guía Técnica, Regulatoria y de Bancabilidad bajo Estándares Internacionales (IEC / IEEE / IFC) y Normativa Nacional (CAMMESA / RIGI / MATER)

---

## 🧭 1. Fundamentos y Enfoque de Ingeniería Inversa

Este modelo sintetiza los aprendizajes técnicos, jurídicos y económicos obtenidos a partir de la **ingeniería inversa de proyectos reales de gran escala en Argentina** (como el **PSFV Cutral Có II de 30 MWac / 36.29 MWdc**, y parques de referencia nacional como Cauchari, Altiplano, Zonda y Ullum), extrapolando una **metodología sistemática, reproducible y bancable** para desarrollar cualquier proyecto renovable fotovoltaico en el territorio argentino, desde la prospección inicial hasta su operación comercial y despacho en el Mercado Eléctrico Mayorista (MEM).

```mermaid
flowchart TD
    subgraph "CICLO DE VIDA INTEGRAL DEL PROYECTO RENOVABLE (7 FASES)"
        F1["Fase I: Prospección, Tierra & Recurso Solar\n(GIS, Tierras, GHI/DNI NASA/Solargis, CIRSOC)"] --> F2["Fase II: Capacidad de Transporte & Red Eléctrica\n(Barra ET, Estudios de Flujo, CAMMESA/Transener)"]
        F2 --> F3["Fase III: Permitting, Impacto Ambiental & Social\n(EIA/MIA, Audiencia Pública, IFC Standards, Tierras)"]
        F3 --> F4["Fase IV: Ingeniería Básica & Detalle\n(3D Layout, PVSyst, DC/AC 1.2-1.3, Trackers, BOS 33kV/132kV)"]
        F4 --> F5["Fase V: Estructuración Comercial, PPA & Finanzas\n(MATER, PPA Privado, DCF, LCOE, RIGI Ley 27.742)"]
        F5 --> F6["Fase VI: Provisión (Procurement) & Construcción EPC\n(Módulos TOPCon, Inversores, Hincado, Obra Eléctrica)"]
        F6 --> F7["Fase VII: Comisionado, Ensayos CAMMESA & COD\n(IEC 62446, Anexo 30 CAMMESA, SMEC/SOTR, COD)"]
    end
```

---

## 🌐 2. Matriz de Estándares Internacionales de Cumplimiento Obligatorio

Para que un parque solar sea apto para financiamiento internacional (*Project Finance* sin recurso con agencias como BID Invest, IFC, CAF, DFC o banca comercial internacional), el diseño debe alinearse con la siguiente suite de normas:

### 2.1. Normas IEC (International Electrotechnical Commission)
1. **IEC 62548 (Diseño de Matrices Fotovoltaicas)**:
   - Requisitos de aislamiento, seccionamiento en CC, protecciones contra sobrecorriente (fusibles gPV), descargadores de sobretensión (SPD Tipo I+II), y cálculo de corrientes máximas de cortocircuito ($I_{sc} \times 1,25$).
2. **IEC 62446-1 y IEC 62446-2 (Ensayos de Puesta en Marcha, Inspección y O&M)**:
   - **Categoría 1**: Continuidad de conductores de puesta a tierra y equipotencial, polaridad de strings, tensión a circuito abierto ($V_{oc}$), corriente de cortocircuito ($I_{sc}$), y resistencia de aislamiento en seco y húmedo ($R_{iso} \ge 1\text{ M}\Omega$ a 1.000/1.500 Vcc).
   - **Categoría 2**: Trazado de curvas I-V (corriente-voltaje) para cada string y termografía infrarroja (IR) aérea o manual para detección de *hot spots* y diodos en bypass abiertos.
3. **IEC 61724-1, -2 y -3 (Monitoreo de Rendimiento y Performance Ratio - PR)**:
   - Clasificación de estaciones meteorológicas en sitio (Clase A de alta precisión: piranómetros secundarios de patrón, termorresistencias PT100 para temperatura de módulo, anemómetros sónicos y pluviómetros/soiling stations).
   - Cálculo del **Performance Ratio Corregido por Temperatura ($PR_{corr}$)** para descartar variaciones estacionales ajenas a la degradación física.
4. **IEC 62817 (Calificación de Seguidores Solares - Trackers)**:
   - Resistencia a la fatiga por torsión y deflexión por viento, ciclos de vida acelerados (mínimo 25 años equivalentes), y prueba de posicionamiento de emergencia ante ráfagas extremas (*Aeroelastic Instability / Galloping*).
5. **IEC 61215 e IEC 61730 (Calificación y Seguridad de Módulos Fotovoltaicos)**:
   - Ensayos de durabilidad térmica (-40°C a +85°C), granizo (impacto de bolas de hielo de 25-35 mm), resistencia mecánica a carga de nieve/viento (2.400 Pa / 5.400 Pa) y aislamiento eléctrico a 1.500 Vcc.

### 2.2. Normas IEEE (Institute of Electrical and Electronics Engineers)
1. **IEEE 1547-2018 / IEEE 2800-2022 (Interconexión a Redes de Potencia de Recursos Basados en Inversores - IBR)**:
   - **Capacidad de Soporte ante Huecos de Tensión (Fault / Low Voltage Ride-Through - LVRT)**: El parque debe permanecer conectado y aportar corriente reactiva durante fallas en la red de transporte sin disparar protecciones.
   - **Control de Potencia Activa y Reactiva**: Capacidad de responder a variaciones de frecuencia ($P(f)$ - estatismo de $2\%$ a $5\%$) y control dinámico de tensión en barras mediante regulación $Q(V)$ en cuatro cuadrantes ($\cos \varphi = \pm 0,90$).
2. **IEEE 80 (Seguridad en Puesta a Tierra de Subestaciones de CA)**:
   - Cálculo determinista de tensiones de paso y de contacto (*Step and Touch Voltages*) en la subestación elevadora y centros de transformación, verificando que los valores calculados no superen los umbrales de fibrilación ventricular humana.

### 2.3. Criterios de Sostenibilidad y Bancabilidad (IFC & Principios de Ecuador IV)
1. **Normas de Desempeño Ambiental y Social de la IFC (1 a 8)**:
   - Evaluación y gestión de riesgos socioambientales (ND 1), condiciones laborales y transición justa (ND 2), eficiencia del uso de recursos y prevención de la contaminación (ND 3), salud y seguridad de la comunidad (ND 4), adquisición de tierras y reasentamiento involuntario (ND 5), conservación de la biodiversidad (ND 6), pueblos indígenas (ND 7), y patrimonio cultural / hallazgos arqueológicos (ND 8).
2. **Informe de Bancabilidad de Rendimiento Energético (DNV GL / NREL)**:
   - Exigencia de evaluación independiente de rendimiento energético (*Independent Engineer Report*) con análisis de incertidumbre global ($< 6\%$) y curvas de probabilidad de excedencia P50, P90 y P95 para el dimensionamiento del ratio de cobertura de deuda (DSCR $\ge 1,20x - 1,30x$).

---

## 🇦🇷 3. Marco Normativo, Regulatorio y Tarifario Específico de Argentina

### 3.1. Procedimientos y Códigos de Red de CAMMESA
El ingreso al Mercado Eléctrico Mayorista (MEM) como Agente Generador Renovable se rige por:
1. **Capítulo XXXVI de Los Procedimientos**:
   - Solicitud de Ingreso y Habilitación Comercial como Agente Generador / Cogenerador Renovable.
   - Presentación del Proyecto de Detalle de Interconexión y Estudio de Acceso a la Capacidad de Transporte Eléctrico.
2. **Anexo 30 de CAMMESA (Ensayos de Puesta en Servicio y Comisionado)**:
   - Medición de potencia neta inyectada al Sistema Argentino de Interconexión (SADI).
   - Verificación de la curva $P-Q$ del generador en bornes y límites de inyección de reactivos.
   - Ensayos de respuesta de frecuencia y control de rampas de subida/bajada ($\text{MW/min}$).
3. **Sistemas Obligatorios de Medición y Telecontrol**:
   - **SMEC (Sistema de Medición Comercial)**: Medidores de energía activa y reactiva de clase 0.2s redundantes (principal y respaldo), sincronizados por GPS, con conexión vía módem satelital o fibra óptica IP al sistema central de CAMMESA.
   - **SOTR (Sistema de Operación en Tiempo Real)**: Telemetría obligatoria mediante protocolo ICCP (TASE.2) o DNP3/IEC 60870-5-104 reportando en tiempo real tensión, corriente, potencia activa, reactiva, frecuencia, estado de interruptores y variables meteorológicas (irradiancia y viento).

### 3.2. Régimen del Mercado a Término de Energías Renovables (MATER)
- Regulado por la **Resolución MEyM 281-E/2017** y **Resolución SE 330/2023**:
  - Permite a los generadores renovables suscribir contratos privados de compraventa de energía (PPA) bilaterales y libremente pactados en dólares (USD/MWh) con Grandes Usuarios del MEM (GUMAs y GUMEs con demanda media anual $\ge 300\text{ kW}$).
  - Asignación trimestral de **Prioridad de Despacho** administrada por CAMMESA:
    - *Prioridad Tipo A*: Capacidad de transporte firme y plena en el corredor eléctrico.
    - *Prioridad Tipo B / Referencial (Curtailment aceptado)*: Asignación supeditada a recortes de generación programados ante congestión de red, requiriendo análisis de costo-beneficio del vertido energético (*curtailment loss* $\le 3\% - 8\%$).

### 3.3. Estructuras de Contratación: Iniciativa Privada (IP) y Régimen RIGI
1. **Régimen de Iniciativa Privada (Nacional Ley 27.742 / Provincias / Municipios)**:
   - **Fase de Propuesta**: Presentación formal no vinculante que acredite viabilidad técnica, económica y ambiental, solvencia patrimonial y principio estricto de **riesgo empresario** (sin garantías directas de repago estatal).
   - **Declaración de Interés Público**: Aprobación por parte de la autoridad ejecutiva o legislativa (ordenanza/decreto), convocando a licitación pública.
   - **Preferencia del Iniciador**: Derecho de preferencia ante igualdad de ofertas (margen del $5\%$) o derecho a mejorar oferta (*mejora de postura*) si la oferta externa es hasta un $15\% - 20\%$ más conveniente.
2. **Régimen de Incentivo para Grandes Inversiones (RIGI - Ley 27.742)**:
   - Aplicable a proyectos energéticos con inversión computable en bienes de capital y obras de infraestructura elegibles:
     - **Estabilidad Fiscal a 30 años**: Inalterabilidad de alícuotas de Ganancias (tasa reducida del $25\%$), amortización acelerada de bienes de capital y devolución anticipada de IVA en créditos fiscales dentro de los 3 meses.
     - **Exenciones Aduaneras**: Arancel de importación del $0\%$ para bienes de capital, módulos solares, inversores, trackers y repuestos nuevos.
     - **Libre Disponibilidad de Divisas**: Exención progresiva de la obligación de liquidación de divisas de exportación y libre remesa de dividendos al exterior.

### 3.4. Normativa Geotécnica y Estructural Argentina
- **INPRES-CIRSOC 103 (Reglamento Argentino para Construcciones Sismorresistentes)**: Zonificación de amenaza sísmica (Zona 0 muy reducida a Zona 4 muy elevada). Exige cálculo de fundaciones de centros de transformación, pórticos de subestación y estructuras de hincado según espectro de respuesta del sitio.
- **CIRSOC 102 (Acción del Viento sobre las Construcciones)**: Prescripción indispensable en la Patagonia y Cuyo, donde ráfagas sostenidas de viento obligan a recalcular los coeficientes de presión de forma ($C_p$) sobre las superficies inclinadas de los módulos y verificar el torque dinámico sobre los ejes de los seguidores (*aeroelastic torsional flutter*).

---

## 🛠️ 4. Metodología de Diseño en 7 Fases Operativas

### Fase I: Prospección, Terreno & Evaluación de Recurso Solar
1. **Criterios de Land Scouting**:
   - Ratio de superficie territorial: **$1,3\text{ a }1,6\text{ hectáreas por MWac}$** para plantas con seguidores monofila 1P o 2P.
   - Pendientes topográficas: Idealmente $\le 2\% - 3\%$ (máximo $5\%$ en sentido Norte-Sur para evitar cortes/rellenos en trackers).
   - Disponibilidad jurídica: Dominio privado con título perfecto, usufructo público municipal/provincial a largo plazo ($\ge 30\text{ años}$) o servidumbre minera/industrial.
2. **Modelado Satelital del Recurso**:
   - Extracción de series históricas de irradiancia horizontal global (GHI), directa normal (DNI) y difusa (DHI) de fuentes combinadas: **NASA POWER, PVGIS 5.3, Solargis y Meteonorm 8.2**.
   - Generación de serie horaria típica TMY (Typical Meteorological Year).

### Fase II: Conexión Eléctrica & Capacidad de Evacuación (Grid Interconnection)
1. **Identificación del Punto de Conexión (POI)**:
   - Distancia al nodo: Líneas de evacuación en 33 kV para potencias hasta 30-40 MWac (distancias $< 10-15\text{ km}$); subestaciones dedicadas elevadoras 33/132 kV para proyectos $\ge 50\text{ MWac}$.
2. **Estudios de Red Eléctrica Requeridos por CAMMESA / Distribuidor**:
   - **Flujo de Potencia en Régimen Permanente**: Verificación de sobrecargas térmicas en líneas y transformadores bajo escenarios de máxima generación solar y mínima demanda local.
   - **Cálculo de Cortocircuito (IEC 60909)**: Determinación de la potencia de cortocircuito trifásica y monofásica en la barra para especificar el poder de corte del *switchgear* (ej. 25 kA / 31,5 kA).
   - **Estabilidad Transitoria y Dinámica**: Modelado de inversores IBR (Grid-following / Grid-forming) en software PSS/E o DigSILENT PowerFactory.

### Fase III: Permitting, Impacto Socioambiental & Factibilidad
1. **Manifiesto de Impacto Ambiental (MIA / EIA)**:
   - Línea de base ambiental (flora, fauna, avifauna esteparia/andina, hidrología superficial y escorrentías).
   - Plan de Gestión Ambiental y Social (PGAS): Manejo de residuos de obra, supresión de polvo en caminos y desmantelamiento/cierre.
   - Audiencia Pública obligatoria y Declaración de Impacto Ambiental (DIA) emitida por la autoridad provincial.
2. **Permisos Sectoriales**:
   - Dirección Provincial de Recursos Hídricos (autorización de cruces de cauces y escorrentías aluvionales).
   - Vialidad Nacional / Provincial (permisos de acceso sobre rutas nacionales, ej. RN 22, RN 40).
   - Dirección de Patrimonio Cultural y Arqueológico (monitoreo paleontológico/arqueológico previo al movimiento de suelos).

### Fase IV: Ingeniería Básica, Simulación 3D & Ingeniería de Detalle
1. **Selección Óptima de Componentes**:
   - **Módulos Fotovoltaicos**: Monocristalinos N-Type TOPCon o HJT bifaciales de gran formato ($\ge 650 - 720\text{ Wp}$), factor de bifacialidad $\ge 80\%$, encapsulante POE/EVA con vidrio doble (dual glass) para resistencia mecánica y degradación mínima ($< 0,40\%/\text{año}$).
   - **Inversores**: Inversores de string de alta potencia ($300\text{ a }350\text{ kWac}$ a 800 Vca) con 6 a 12 MPPTs independientes, facilitando la modularidad, reposición rápida y reducción de cajas de combinación (combiner boxes).
   - **Seguidores (Trackers)**: Seguidores solares a 1 eje horizontal (N-S) con accionamiento descentralizado o multitorque, con algoritmo de *backtracking* 3D (para compensar irregularidades del terreno) y ganancia bifacial optimizada.
2. **Dimensionamiento y Ratios de Diseño**:
   - **DC/AC Ratio**: Típicamente entre **$1,18\text{ y }1,30$** en Argentina (permite aplanar la curva de generación al mediodía y maximizar la inyección en horas tempranas y tardías, compensando el *clipping loss* con mayor volumen total anual).
   - **Ground Coverage Ratio (GCR)**: Típicamente entre **$0,28\text{ y }0,38$** (Pitch entre 6 y 8 metros para seguidores 2P).
   - **Pérdidas Óhmicas de Cableado**: $\le 1,2\%$ en corriente continua y $\le 1,0\%$ en corriente alterna hasta el centro de transformación.
3. **Centros de Transformación (Power Stations / STS)**:
   - Configuración compacta exterior sobre *skid* de hormigón o contenedor metálico, integrando transformador elevador BT/MT (800 V / 33 kV) con aceite dieléctrico biodegradable o mineral, celdas de media tensión aisladas en SF6 o aire comprimido, transformador de servicios auxiliares y UPS.

### Fase V: Estructuración Comercial, PPA & Modelo Financiero (Bancabilidad)
1. **Estructura de Ingresos**:
   - PPA Privado a Largo Plazo (10 a 20 años) con tarifa fija en USD/MWh o indexada por CPI americano.
   - PPA con Distribuidoras Locales / Municipales con precio sostén de garantía.
   - Despacho spot en el MEM (remuneración base por energía entregada y potencia disponible).
2. **Métricas Financieras del Modelo DCF (Flujo de Fondos Descontado)**:
   - **CAPEX Típico Utility-Scale Argentina**: $650.000\text{ a }820.000\text{ USD / MWdc}$ (incluyendo conexión en 33 kV).
   - **OPEX de Referencia**: $9.500\text{ a }14.000\text{ USD / MWdc / año}$ (incluye O&M preventivo/correctivo, seguros todo riesgo, canon de tierra, peajes y gestión administrativa).
   - **LCOE (Levelized Cost of Electricity)**: $32\text{ a }45\text{ USD / MWh}$ (en regiones de excelente recurso solar como Cuyo, NOA y Patagonia Norte).
   - **DSCR (Debt Service Coverage Ratio)**: Mínimo $1,20x$ sobre escenario P90.

### Fase VI: Provisión (Procurement) & Construcción EPC
1. **Estrategia Contractual**:
   - Contrato EPC Llave en Mano (*Turnkey EPC*) con cláusulas FIDIC Silver Book (EPC/Turnkey Contract), penalidades por mora (*Liquidated Damages - LDs*) y garantías de rendimiento (*Performance Guarantees*).
2. **Ensayos de Suelos y Pruebas de Hincado (Pull-Out Tests)**:
   - Ensayos geotécnicos de hincabilidad y pruebas de tracción vertical (*pull-out*) y esfuerzo lateral sobre perfiles de acero C/H para determinar la profundidad óptima de hincado sin requerir zapatas de hormigón.
3. **Logística y Cadena de Suministro**:
   - Despacho marítimo en contenedores high-cube, internación aduanera bajo régimen RIGI/Renovables, transporte terrestre carretero con sobredimensión para transformadores y trackers, y acopio seguro en obrador perimetrado.

### Fase VII: Testing, Comisionado, Ensayos CAMMESA & Operación (COD)
1. **Ensayos Pre-Operativos (Cold & Hot Commissioning)**:
   - Verificación de rigidez dieléctrica, apriete de torques mecánicos, calibración de sensores de viento y comunicación SCADA.
2. **Protocolo de Ensayos CAMMESA (Anexo 30)**:
   - Coordinación con el Centro de Control Regional (Comahue, Cuyo, NOA, etc.).
   - Pruebas de estatismo, rampa de carga, verificación de corte por sobretensión/subtensión y energización bajo carga.
3. **Firma del Acta de Habilitación Comercial (COD)**:
   - Emisión de la autorización formal de despacho por CAMMESA y la Secretaría de Energía, habilitando la facturación comercial de la energía generada.

---

---

## 🏗️ 5. Protocolo de Auditoría y Certificación de Estado Ready to Build (RTB)

Para que un parque solar fotovoltaico alcance el estado **Ready to Build (RTB)** —momento en el cual los riesgos de desarrollo han sido mitigados al 100%, se logra el Cierre Financiero (*Financial Close*) y se emite la orden de inicio (*Notice to Proceed - NTP*) al contratista EPC—, el agente debe auditar y verificar el cumplimiento estricto de la **Matriz Maestra de 58 Requisitos en 7 Categorías** (procedente de la norma de desarrollo bancable `Etapas_Proyectos_FV`):

```mermaid
graph TD
    subgraph "COMPUERTA DE MADUREZ: READY TO BUILD (RTB) - 58 REQUISITOS"
        C1["1. EPE: Producción de Energía (5 ítems)<br>.pan, .ond, TMY satelital, PVSyst congelado"] --> RTB{"Compuerta RTB<br>100% De-risked"}
        C2["2. Emplazamiento & Sitio (7 ítems)<br>LIDAR <=0.5m, Pull-out tests, Hidrología 100a"] --> RTB
        C3["3. Información General (2 ítems)<br>KMZ planta + KMZ traza línea evacuación LAT"] --> RTB
        C4["4. Diseño & BOS (6 ítems)<br>Layout 3D, SLD 1.500V/33kV/132kV, Viento CIRSOC 102"] --> RTB
        C5["5. Interconexión Eléctrica (7 ítems)<br>Acceso CAMMESA, Garantías bancarias, Curva S, POI ET"] --> RTB
        C6["6. Permisos & Licencias (9 ítems)<br>Contrato usufructo >=25a, Cruces DNV, Building Permit"] --> RTB
        C7["7. Ambiental & Social Dual (22 ítems)<br>DIA Planta + DIA LAT, No interferencia ductos/minería, INAI"] --> RTB
    end
    
    RTB --> FC["🏁 Cierre Financiero (Financial Close)"]
    FC --> NTP["🚀 Notice to Proceed (NTP) / EPC Turnkey (FIDIC Silver Book)"]
```

### 📋 5.1 Matriz Maestra de Due Diligence y Compuertas RTB (58 Requisitos Oficiales)

| Id | Categoría | Requisito Documental Auditado | Criticidad | Ente Emisor / Regulador | Criterio de Aprobación Bancable |
| :-: | :--- | :--- | :---: | :--- | :--- |
| **1** | **EPE** | Archivo `.pan`, PV module data file (PVsyst format) | **Alta** | Fabricante Tier-1 / PVSyst | Curvas I-V, coeficientes térmicos y bifacialidad calibrados. |
| **2** | **EPE** | Archivo `.ond`, Inverter data file (PVsyst format) | **Alta** | Fabricante Tier-1 / PVSyst | Rangos MPPT, curvas de eficiencia europea y límites de tensión. |
| **3** | **EPE** | TMY o datos meteorológicos satelitales duales | 🚨 **Fatal Flaw** | Solargis / PVGIS / Meteonorm | Serie horaria multianual representativa; incertidumbre global $\le 6\%$. |
| **4** | **EPE** | Estudios previos / existentes del recurso solar | **Media** | Desarrollador / Consultor | Comparativa histórica de bases de radiación GHI y DNI. |
| **5** | **EPE** | Configuración eléctrica (DC/AC ratio, strings) | **Alta** | Ingeniería Básica | Ratio DC/AC optimizado (1.20 - 1.25); pérdidas de string $< 1,5\%$. |
| **6** | **Emplazamiento** | Reporte de estudio topográfico de sitio | **Alta** | Agrimensura Profesional | Memoria técnica con puntos GPS georreferenciados en POSGAR/WGS84. |
| **7** | **Emplazamiento** | Topografía detallada (CAD/GIS/DEM) | 🚨 **Fatal Flaw** | Agrimensor / LIDAR | Curvas de nivel $\le 0,5\text{ m}$; pendientes del predio $\le 2\% - 3\%$. |
| **8** | **Emplazamiento** | Diseño de drenajes y escorrentías | **Alta** | Hidráulica / Obras Viales | Zanjas perimetrales y badenes dimensionados para lluvia crítica. |
| **9** | **Emplazamiento** | Estudio hidrológico de cuenca de aporte | 🚨 **Fatal Flaw** | Hidrólogo / DPA / HEC-HMS | Caudales pico calculados para período de retorno T = 100 años. |
| **10** | **Emplazamiento** | Estudio de inundabilidad (mancha de inundación) | 🚨 **Fatal Flaw** | Hidrólogo / HEC-RAS | Verificación de cota de implantación por encima de crecida centenaria. |
| **11** | **Emplazamiento** | Pruebas de carga en sitio (*pull-out tests*) | 🚨 **Fatal Flaw** | Laboratorio Geotécnico | Ensayos de tracción vertical y lateral sobre perfiles hincados. |
| **12** | **Emplazamiento** | Estudio geotécnico (calicatas y resistividad) | 🚨 **Fatal Flaw** | Geotecnista Certificado | Perfil estratigráfico, agresividad de cloruros/sulfatos y resistividad. |
| **13** | **Info General** | `.kmz` del proyecto (predio parque solar) | 🚨 **Fatal Flaw** | SIG / Proyectista | Polígono georreferenciado WGS84 del loteo y superficie total. |
| **14** | **Info General** | `.kmz` de la ruta de la línea de transmisión (LAT) | 🚨 **Fatal Flaw** | SIG / Proyectista | Traza vectorial WGS84 de la línea de evacuación hasta la ET. |
| **15** | **Diseño** | Plano de implantación general (*layout* 3D) | 🚨 **Fatal Flaw** | Ingeniería Básica | Disposición de trackers, pitch, separación de filas y viales. |
| **16** | **Diseño** | Diagrama unifilar (Single Line Diagram - SLD) | 🚨 **Fatal Flaw** | Ingeniería Eléctrica | Esquema unifilar completo en 1.500 Vcc, 33 kV y 132 kV. |
| **17** | **Diseño** | Otros documentos de ingeniería básica (MDL / DPP) | **Alta** | EPC / Proyectista | Lista Maestra de Documentos emitida y congelada para construcción. |
| **18** | **Diseño** | Validaciones estructurales o de carga (viento/sismo) | 🚨 **Fatal Flaw** | Calculista Estructural | Memoria de cálculo bajo CIRSOC 102 (viento) e INPRES-CIRSOC 103 (sismo). |
| **19** | **Diseño** | Planos y dibujos constructivos | **Alta** | EPC / Proyectista | Planos de fundaciones, zanjas de MT, salas de control y cercado. |
| **20** | **Diseño** | Diseños y cálculos de servicios auxiliares (SCADA/Meteo) | **Alta** | Automatización / Control | Estación meteorológica Clase A (IEC 61724-1), CCTV y telemetría. |
| **21** | **Interconexión** | Acuerdos de interconexión con transportista/distribuidora | 🚨 **Fatal Flaw** | Transportista / EPEC / EPEN | Convenio técnico-económico de conexión al SADI formalizado. |
| **22** | **Interconexión** | Estudios de interconexión eléctrica aprobados | 🚨 **Fatal Flaw** | Especialista Eléctrico / CAMMESA | Flujo de potencia, cortocircuito IEC 60909 y estabilidad PSS/E. |
| **23** | **Interconexión** | Informes periódicos de avance a la CAMMESA | **Alta** | Desarrollador / PMO | Reportes de cumplimiento de hitos de desarrollo según Los Procedimientos. |
| **24** | **Interconexión** | Garantías bancarias de reserva de transporte | 🚨 **Fatal Flaw** | Banco Emisor / CAMMESA | Boletas de garantía vigentes para respaldar la asignación MATER. |
| **25** | **Interconexión** | Aprobación de reserva de capacidad CAMMESA | 🚨 **Fatal Flaw** | CAMMESA / Sec. Energía | Asignación de Prioridad de Despacho (Res. 281-E/17 o SE 330/23). |
| **26** | **Interconexión** | Curva S entregada a la CAMMESA | **Alta** | Planificador / PMO | Cronograma físico-financiero comprometido de obras e hitos. |
| **27** | **Interconexión** | Estudio de disponibilidad de espacio en ET (POI) | 🚨 **Fatal Flaw** | Transportista / Dueño de ET | Factibilidad de celda de reserva o ampliación física en la ET. |
| **28** | **Permisos** | Contratos de arrendamiento / usufructo notarial | 🚨 **Fatal Flaw** | Escribano / Registro Propiedad | Contrato notarial registrado por plazo $\ge 25-30$ años. |
| **29** | **Permisos** | Certificados de tradición y libertad (dominio) | 🚨 **Fatal Flaw** | Registro de la Propiedad | Título perfecto libre de embargos, gravámenes o hipotecas. |
| **30** | **Permisos** | Licencia de construcción (*Building Permit*) | 🚨 **Fatal Flaw** | Municipio Local | Permiso municipal de obras civiles y habilitación de radicación. |
| **31** | **Permisos** | Permisos de DNV para cruce con línea de transmisión | **Alta** | Dirección Nacional de Vialidad | Permiso formal de cruce aéreo/subterráneo de rutas nacionales. |
| **32** | **Permisos** | Permiso de cruce en rutas concesionadas / autopistas | **Alta** | Órgano Control Concesiones | Autorización específica con empresa concesionaria vial. |
| **33** | **Permisos** | Permisos de cruce y ocupación municipal para LAT | **Alta** | Municipios atravesados | Permiso de uso de banquinas y vías comunales para la traza. |
| **34** | **Permisos** | Servidumbres o permisos de ocupación pública para LAT | 🚨 **Fatal Flaw** | Escribanía / Catastro | Franja de servidumbre de electroducto constituida e inscripta. |
| **35** | **Permisos** | Certificado de compatibilidad de uso de suelo | **Alta** | Planeamiento Urbano | Certificado de aptitud de uso industrial / generación renovable. |
| **36** | **Permisos** | Aprobaciones aeronáuticas (ANAC) | **Alta** | ANAC | Dictamen de no afectación de conos de aproximación ni deslumbramiento. |
| **37** | **Ambiental/Social** | Interferencias con hidrocarburos: proyecto parque | 🚨 **Fatal Flaw** | Sec. Energía / Operadoras | Libre de gasoductos, oleoductos y pozos activos en el polígono. |
| **38** | **Ambiental/Social** | Interferencias con hidrocarburos: línea transmisión | 🚨 **Fatal Flaw** | Transportadoras de Gas/Petróleo | Acuerdos de cruce y distancias mínimas de seguridad con ductos. |
| **39** | **Ambiental/Social** | Interferencias con minería: proyecto parque | 🚨 **Fatal Flaw** | Dirección Prov. de Minería | Libre de concesiones mineras, cateos o pedimentos en el predio. |
| **40** | **Ambiental/Social** | Interferencias con minería: línea de transmisión | **Alta** | Dirección Prov. de Minería | No afectación de derechos mineros vigentes a lo largo de la LAT. |
| **41** | **Ambiental/Social** | Licencia ambiental del proyecto (EIA + DIA) | 🚨 **Fatal Flaw** | Autoridad Ambiental Prov. | Declaración de Impacto Ambiental (DIA) firme para la planta. |
| **42** | **Ambiental/Social** | Licencia ambiental de la línea de transmisión (LAT) | 🚨 **Fatal Flaw** | Autoridad Ambiental Prov. | Declaración de Impacto Ambiental (DIA) firme para la línea. |
| **43** | **Ambiental/Social** | Plan de Manejo Ambiental (PMA) | **Alta** | Autoridad Ambiental | Programas de monitoreo, mitigación y gestión de residuos. |
| **44** | **Ambiental/Social** | Certificado de presencia de comunidades étnicas | 🚨 **Fatal Flaw** | INAI / Asuntos Indígenas | Certificado oficial negativo o identificación de comunidades. |
| **45** | **Ambiental/Social** | Consultas previas con comunidades indígenas | 🚨 **Fatal Flaw** | INAI / Comunidades | Cumplimiento del Convenio 169 de la OIT sin litigios pendientes. |
| **46** | **Ambiental/Social** | Socializaciones con la comunidad y Audiencia Pública | **Alta** | Autoridad Ambiental / Municipio | Audiencia pública cumplida sin objeciones sustantivas. |
| **47** | **Ambiental/Social** | Consultas de procesos de restitución de tierras | **Alta** | Registro de Tierras / Justicia | Certificado de ausencia de reclamos territoriales en trámite. |
| **48** | **Ambiental/Social** | Permiso de aprovechamiento forestal: proyecto parque | **Alta** | Dirección de Bosques Nativos | Autorización de desmonte / tala / poda selectiva en el predio. |
| **49** | **Ambiental/Social** | Permiso de aprovechamiento forestal: línea transmisión | **Alta** | Dirección de Bosques Nativos | Permiso de apertura de picada / franja de seguridad de la LAT. |
| **50** | **Ambiental/Social** | Plan de compensación biótica: planta solar | **Alta** | Autoridad Ambiental | Plan de reforestación o enriquecimiento de flora nativa. |
| **51** | **Ambiental/Social** | Plan de compensación biótica: línea transmisión | **Alta** | Autoridad Ambiental | Plan de restauración de corredores ecológicos afectados. |
| **52** | **Ambiental/Social** | Aprobación del programa de arqueología preventiva | **Alta** | Patrimonio Cultural Prov. | Protocolo de preservación y hallazgos fortuitos aprobado. |
| **53** | **Ambiental/Social** | Aprobación del proyecto de prospección arqueológica | **Alta** | Patrimonio Cultural Prov. | Campaña en terreno con dictamen de no afectación patrimonial. |
| **54** | **Ambiental/Social** | Permiso de ocupación de cauce: proyecto parque | **Alta** | Recursos Hídricos / DPA | Permiso de cruce o intervención de cauces temporarios. |
| **55** | **Ambiental/Social** | Permiso de ocupación de cauce: línea transmisión | **Alta** | Recursos Hídricos / DPA | Autorización de tendido aéreo/subterráneo sobre cauces hídricos. |
| **56** | **Ambiental/Social** | Interferencia con áreas de reserva nacional (APN) | 🚨 **Fatal Flaw** | Parques Nacionales | Certificado de no superposición con Parques/Reservas Nacionales. |
| **57** | **Ambiental/Social** | Interferencia con áreas de reserva provincial y local | 🚨 **Fatal Flaw** | Dirección de Áreas Protegidas | No afectación de reservas naturales provinciales o municipales. |
| **58** | **Ambiental/Social** | Interferencia con ecosistemas estratégicos (RAMSAR/AICA) | 🚨 **Fatal Flaw** | Secretaría de Ambiente | Compatibilidad y no afectación de humedales o sitios RAMSAR. |

---

### 🚦 5.2 Protocolo de Dictamen RTB y Clasificación de Riesgos

El agente emitirá uno de los tres dictámenes formales tras auditar los 58 ítems:

1. **APROBADO RTB (100% De-risked / Bankable)**:
   - Cumplimiento del 100% de los **23 ítems calificados como Fatal Flaw**.
   - Al menos el 90% de los ítems de criticidad Alta resueltos y los restantes con cronograma contractual mitigado en el contrato EPC.
2. **CONDICIONADO A FINANCIAL CLOSE (CP-FC)**:
   - Los Fatal Flaws principales están aprobados (DIA, CAMMESA, Terreno), pero restan emitir boletas de garantía de transporte, pólizas de caución o permisos de cruce vial DNV en fase final de tramitación administrativa.
3. **RECHAZADO / NO RTB (Fatal Flaws Activos)**:
   - Cualquier incumplimiento en: DIA ambiental provincial, superposición no autorizada con ductos de hidrocarburos o áreas protegidas (APN), falta de titularidad perfecta del predio, o ausencia de capacidad firme asignada por CAMMESA.

---

## 📋 6. Checklist Maestro de Auditoría para Nuevos Proyectos Solares

| Eje de Evaluación | Ítems Obligatorios a Verificar | Criterio de Aprobación Bancable |
| :--- | :--- | :--- |
| **1. Recurso & Sitio** | • Coordenadas WGS 84 y archivo KMZ.<br>• Estudio de pendientes topográficas $< 3\%$.<br>• Base satelital dual (PVGIS + Meteonorm / Solargis).<br>• Estudio de riesgo sísmico (INPRES-CIRSOC 103) y viento (CIRSOC 102). | P50 / P90 con incertidumbre global $\le 6\%$. Terreno sin zonas inundables ni escorrentías activas. |
| **2. Red Eléctrica** | • Distancia a la Estación Transformadora más cercana.<br>• Tensión de evacuación (33 kV o 132 kV).<br>• Capacidad disponible de transporte confirmada por CAMMESA/Transportista.<br>• Disponibilidad de campo o celda de reserva en la ET. | Nota formal de la transportista/distribuidora o prioridad de despacho MATER asignada sin riesgo de congestión severa. |
| **3. Ingeniería** | • Simulación PVSyst versión $\ge 7.4$ u $8.x$ con archivo `.PAN` y `.OND`.<br>• Módulos Tier-1 BloombergNEF con certificación IEC 61215/61730.<br>• Inversores con certificación IEEE 1547 / IEC 62109.<br>• Trackers con certificación IEC 62817 y posición de bandera automática.<br>• Balance Balance of System (BOS) con caída óhmica $< 1,5\%$. | Performance Ratio (PR) Año 1 entre $80\%$ y $85\%$. Pérdida por suciedad modelada con ciclo de limpieza local. |
| **4. Legal & Tierras** | • Título de propiedad o contrato de arrendamiento/usufructo $\ge 25 - 30$ años inscripto en el Registro de la Propiedad Inmueble.<br>• Permisos de cruce de caminos y servidumbres de electroducto.<br>• En proyectos públicos: Ordenanza o Decreto de Iniciativa Privada formalmente protocolizado. | Libre de gravámenes, hipotecas o embargos. Aprobación municipal/provincial con fuerza de ley. |
| **5. Ambiental** | • Estudio de Impacto Ambiental (EIA) aprobado con Declaración de Impacto Ambiental (DIA).<br>• Audiencia pública realizada.<br>• Cumplimiento de las 8 Normas de Desempeño de la IFC. | Cero afectación crítica de hábitats protegidos o comunidades sin consulta previa informada. |
| **6. Comercial** | • Contrato PPA firmado o Carta de Intención de compra del $100\%$ de la energía.<br>• Matriz de precio USD/MWh garantizado o contrato MATER indexado.<br>• Mecanismo de despacho y asunción de riesgo de desvíos (CAMMESA). | Riesgo de cobro mitigado por garante de primera línea (GUMA/GUME solvente o distribuidora con fideicomiso). |

---

## 🔗 Referencias Cruzadas en la Bóveda Obsidian
- [[00-Dashboard-MOC]]
- [[docs/Agentes/13-Desarrollador-Parques-Solares-Renovables]]
- [[docs/Proyectos/2026-11-02_psfv-cutral-co-ii-30mw]]
- [[docs/Proyectos/2026-10-14_asesoramiento-parque-solar-fotovoltaico]]
- [[docs/Agentes/01-Analista-Financiero]]
- [[docs/Agentes/02-Ciencia-de-Datos]]
- [[docs/Agentes/06-Arquitecto-Sistemas-EPEC]]
- [[docs/Agentes/11-Copiloto-Orquestador-de-Skills]]

