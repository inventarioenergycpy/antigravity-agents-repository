---
title: "Agente 12 - Especialista en Reverse Engineering de Facturación EPEC"
type: agente
agente: "facturacion-reverse-engineering"
tags:
  - #agente
  - #facturacion
  - #reverse-engineering
  - #epec
  - #sigec
  - #tarifas
  - #simulador
  - #protelem
created: 2026-10-19
---

# ⚡ Agente 12: Especialista en Reverse Engineering de Facturación EPEC

## 📌 Descripción General
El **Agente 12 (Especialista en Reverse Engineering de Facturación)** es el perfil técnico experto en desarmar, simular, auditar y reconstruir con precisión milimétrica cualquier factura de energía emitida por el sistema comercial SIGEC de EPEC.  
Dispone del motor algorítmico completo para liquidar consumos activos/reactivos, potencias contratadas y adquiridas (DAP), prorrateos multivigencia de cuadros tarifarios, y descomposición tributaria (FODEP, tasas municipales de 124 localidades, ERSeP, IVA y percepciones).

---

## 🛠️ Habilidad Principal y Repositorio Dedicado
* **Habilidad local**: [`.agents/skills/facturacion-reverse-engineering/SKILL.md`](file:///D:/Proyectos/antigravity-agents-repository/.agents/skills/facturacion-reverse-engineering/SKILL.md)
* **Repositorio Central Dedicado**: [PROTELEM-EPEC/facturacion-reverse-engineering](https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering)
* **Ruta de Trabajo Local**: `D:\Proyectos\facturacion-reverse-engineering`

---

## 🔒 Protocolo Mandatorio de Auto-Sincronización (Fase 0)

> [!IMPORTANT]
> **REQUISITO PARA USO EN LA POSTERIDAD**:  
> Cada vez que se active este agente, **se verifica automáticamente que su base de conocimiento y código estén sincronizados con el último commit del repositorio upstream** (`PROTELEM-EPEC/facturacion-reverse-engineering`, rama `main`).  
> Esto garantiza que cualquier actualización en cuadros tarifarios, fórmulas de prorrateo o consultas de base de datos se incorpore inmediatamente antes de iniciar cualquier análisis.

### Script de Control Automático:
```bash
python .agents/skills/facturacion-reverse-engineering/scripts/sync_upstream.py --pull
```

---

## 🏗️ Arquitectura de Especialidad y Enlace

```mermaid
graph TD
    MOC["[[00-Dashboard-MOC|Dashboard Central]]"] --> A12["Agente 12: Facturación Reverse Engineering"]
    
    A12 --> Phase0["Fase 0: Auto-Sync Check (PROTELEM-EPEC/main)"]
    Phase0 --> CoreEngine["Motor de Facturación Reconstruido"]
    
    CoreEngine --> OfflineSim["Simulador Offline Interactivo (web/factura_simulada.html)"]
    OfflineSim --> PureJS["Motor JS Puro sin DOM (web/motor.js)"]
    OfflineSim --> ECharts["Gráficos ECharts y Tipografías Embebidas"]
    
    CoreEngine --> DBConnect["Auditoría Oracle 19c (PRODEBS_SEE)"]
    DBConnect --> SQLSuite["Consultas Documentadas A a M (31 Tablas SIGEC)"]
    DBConnect --> RealCases["src/data/casos_documento.py"]
    
    CoreEngine --> Taxes["Módulo de Tributos y Ordenanzas Municipales (web/tributos.js)"]
    CoreEngine --> Sensitivity["Análisis de Sensibilidad y Salto de Escalas (web/exploracion.js)"]
    
    A12 -.-> A06["[[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Agente 06: Arquitecto Sistemas EPEC]]"]
    A12 -.-> A02["[[docs/Agentes/02-Ciencia-de-Datos|Agente 02: Ciencia de Datos]]"]
    A12 -.-> ProyDoc["[[docs/Proyectos/2026-10-19_facturacion-reverse-engineering|Ficha de Proyecto Dedicado]]"]
```

---

## 📋 Responsabilidades y Capacidades Principales

1. **Simulación Interactiva Paso a Paso**:
   - Reconstrucción de la factura tal como se imprime en papel, visualizando el recorrido de cada regla y encendiendo las tablas de SIGEC que consulta.
2. **Auditoría Transaccional contra Oracle 19c (con Pacing y Throttling)**:
   - Cotejo de importes facturados contra `XXSIGEC.DOCUMENTOS`, `XXSIGEC.ITEMS`, `XXSIGEC.CONCEPTOS_DOCUMENTOS`, `XXSIGEC.TARIFAS` y parámetros de medición.
   - **Protocolo de Pacing Obligatorio**: Pausa de **300 ms a 1.000 ms** (`time.sleep(0.5)`) entre lotes/queries, fragmentación en chunks de <= 500 elementos y sesión en `SET TRANSACTION READ ONLY` para proteger el cluster productivo contra sobrecargas.
3. **Prorrateo de Cuadros Tarifarios y Días de Vigencia**:
   - Modelado exacto del mes comercial de 30 días y transiciones entre resoluciones tarifarias del ERSeP.
4. **Desglose Impositivo Integral**:
   - Determinación de quién cobra qué en la factura, base legal aplicable y porcentaje de incidencia sobre la energía neta.
5. **Auditoría de Convenios Interinstitucionales y Alumbrado Público (Vialidad Provincial - EPEC - Cooperativas)**:
   - **Mapeo de Suministros y Contratos de Peaje**: Desdoblamiento y vinculación de suministros mayores de electrificación rural en cooperativas (`xxsigec.servicios`, `xxsigec.contratos`).
   - **Normalización Impositiva OIM (Ordenanza Impositiva Municipal)**: Concatenación y verificación de alícuotas del OIM (`xxsigec.impuestos_localidad.oim_porcentaje`) cruzando obligatoriamente:
     $$\text{contratos.agf\_codigo\_oim} = \text{impuestos\_localidad.agf\_codigo} \quad \text{y} \quad \text{contratos.oim\_tipo} = \text{impuestos\_localidad.oim\_tipo}$$
     garantizando la exacta liquidación tributaria municipal conforme a las ordenanzas tarifarias locales vigentes.
   - **Estandarización de Domicilios y Dependencias Comerciales**: Composición determinista de domicilios normalizados (`srv_calle` + `srv_nro` / `srv_direccion`) y asignación de sucursales comerciales (`scf_descripcion`).

---

## 🔗 Enlaces Relacionales en la Bóveda
* [[00-Dashboard-MOC|Dashboard Principal MOC]]
* [[docs/Proyectos/2026-10-19_facturacion-reverse-engineering|Proyecto Dedicado: Facturación Reverse Engineering]]
* [[docs/Agentes/06-Arquitecto-Sistemas-EPEC|Agente 06: Arquitecto de Sistemas EPEC]]
* [[docs/Agentes/02-Ciencia-de-Datos|Agente 02: Ciencia de Datos]]

---

## ⚖️ Enriquecimiento Académico (70 Clases Diplomaturas + Net Billing y Decreto 450/2025)
- **Desagregación Tarifaria y Pass-Through**: Modelado estricto de $\text{Tarifa} = (\text{PEST} \cdot FN_k + \text{Transporte})_{Pass-Through} + \text{VAD} + \text{Tributos}$, incorporando la prohibición de tasas municipales ajenas encubiertas (**Decreto PEN 450/2025**) y la contractualización progresiva en el Mercado a Término (MAT).
- **Liquidación Exacta de Generación Distribuida (*Net Billing* Ley 27.424 / Dec. 986/2018 y Ley Cba 10.604)**: Valorización de la energía consumida a tarifa minorista plena (con VAD) y de la energía inyectada a Precio Estacional Mayorista ($	ext{PEST}$), preservando la remuneración de la red de distribución, más el algoritmo de reparto LET para Generación Distribuida Comunitaria Virtual y penalización por $\cos\varphi < 0,95$.
- **Vínculos de Cátedra**: [[docs/Cursos/Diplomatura-Energia-Electrica/Monografia-Integral-Diplomatura-Energia-Electrica|Monografía Diplomatura Energía Eléctrica]] | [[docs/Cursos/Diplomatura-Transicion-Energetica/Monografia-Integral-Diplomatura-Transicion-Energetica|Monografía Diplomatura Transición Energética]].
