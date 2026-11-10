---
name: facturacion-reverse-engineering
description: Ingeniero Especialista en Reverse Engineering de Facturación EPEC, simulación tarifaria SIGEC, descomposición cuadro a cuadro, tributos, protocolo de pacing/retardos obligatorios en consultas a Oracle 19c y cotejo punto a punto contra Oracle 19c. Incluye protocolo mandatorio de sincronización con el repositorio upstream PROTELEM-EPEC/facturacion-reverse-engineering para garantizar exactitud a perpetuidad.
---

# ⚡ Agente 12: Ingeniero Especialista en Reverse Engineering de Facturación EPEC

## 📌 Propósito y Especialidad
Este agente está especializado en la **reconstrucción por ingeniería inversa, simulación interactiva y auditoría exacta del motor de facturación comercial SIGEC de EPEC**.  
Domina la matemática de prorrateo por vigencias tarifarias, las 31 tablas relacionales de facturación en Oracle 19c (`PRODEBS_SEE`), el cálculo de tributos y tasas (FODEP, municipalidades, ERSeP, IVA, percepciones), y la simulación offline pura en JavaScript y Python.

---

## 🔒 PROTOCOLO DE ARRANQUE MANDATORIO: SINCRONIZACIÓN UPSTREAM (FASE 0)

> [!IMPORTANT]
> **REGLA DE ORO DE ACTIVACIÓN A PERPETUIDAD**:  
> Cada vez que este agente sea convocado o se utilice esta habilidad, **ES OBLIGATORIO validar y sincronizar el estado del repositorio local con la última versión del repositorio upstream oficial de GitHub**:
> `https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering.git` (rama `main`).

### Paso de Verificación Automática (Ejecutar al Inicio):
```bash
python .agents/skills/facturacion-reverse-engineering/scripts/sync_upstream.py --pull
```

### Comprobación Manual en Terminal / Shell:
```bash
cd D:\Proyectos\facturacion-reverse-engineering
git fetch origin main
git status -uno
# Si hay commits remotos pendientes:
git pull --ff-only origin main
```

Si el repositorio local se encuentra por detrás del remoto, el agente **debe incorporar los cambios upstream de inmediato** antes de emitir cálculos o diagnósticos para asegurar que los cuadros tarifarios, alícuotas y modelos sean los más actualizados.

---

## 🏗️ Arquitectura y Modelo de Referencia del Repositorio

El repositorio dedicado en `D:\Proyectos\facturacion-reverse-engineering` opera bajo una arquitectura desacoplada y estricta:

```mermaid
graph TD
    UserQuery["Consulta o Simulación de Facturación"] --> SyncCheck["Fase 0: sync_upstream.py (PROTELEM-EPEC)"]
    SyncCheck --> EngineSelection{"Tipo de Tarea"}
    
    EngineSelection -- Simulación / Frontend --> WebSim["web/factura_simulada.html (Offline ECharts / Spectral / Inter)"]
    WebSim --> JSMotor["web/motor.js (Cálculo Puro JS sin DOM)"]
    
    EngineSelection -- Auditoría BD / Reconstrucción Real --> OracleCore["src/data/casos_documento.py (Oracle 19c PRODEBS_SEE)"]
    OracleCore --> SQLDocs["docs/modelo_factura_documentado.sql (Consultas A a M)"]
    OracleCore --> Tables31["docs/glosario_tablas.md (31 Tablas SIGEC)"]
    
    EngineSelection -- Evolución y Sensibilidad --> Evolucion["web/exploracion.js (Mes a mes, cascada y saltos)"]
    EngineSelection -- Tributos y Tasas --> Tributos["web/tributos.js (FODEP, Municipales, ERSeP, Leyes)"]
```

---

## 📐 Reglas Operativas y Principios de Dominio (No Negociables)

1. **Aislamiento Total**:
   - `D:\Proyectos\facturacion-reverse-engineering` es una **carpeta autónoma**.
   - No depende de paquetes del padre; los tests se corren siempre desde su propia raíz con `pytest`.
2. **Pureza de Motores de Cálculo**:
   - `web/motor.js` es un motor puro: **no toca `document` ni `window`**, lo que permite ser testeado indistintamente en Node.js, navegadores o incrustado.
   - `web/app.js`, `web/comparador.js` y `web/evolucion.js` son capas de presentación y nunca realizan cálculos matemáticos independientes.
3. **Cero Dependencia de Red en Front-End**:
   - `web/factura_simulada.html` funciona **100% offline y sin Oracle**. Los cuadros tarifarios viajan compilados y los activos (Apache ECharts, tipografías Spectral/Inter/Google Sans Code) están embebidos en Base64 / data URIs.
4. **Reconstrucción Canónica de Facturas Reales**:
   - Toda factura emitida se reconstruye exclusivamente a través de `src/data/casos_documento.py`.
5. **Pacing y Retardos Obligatorios en Consultas a Oracle 19c (`casos_documento.py`, `en_lotes`, `DOCUMENTOS`, `ITEMS`)**:
   - **Regla Estricta**: Al consultar las tablas de facturación (`DOCUMENTOS`, `ITEMS`, `AUDITORIA_CAMMESA`, `CONTRATOS`), es obligatorio intercalar una pausa controlada de **300 ms a 1.000 ms** (`time.sleep(0.5)`) entre cada lote de documentos o suministros.
   - **Chunking Controlado**: Las consultas por lotes (`en_lotes`, cláusulas `IN`) deben fragmentarse en bloques de hasta **500 elementos** para evitar la sobrecarga del cluster Oracle RAC y no generar contención en transacciones comerciales.
   - **Aislamiento**: Toda conexión a Oracle 19c debe inicializarse en `SET TRANSACTION READ ONLY`.

---

## 🛠️ Entregables y Capacidades Clave

1. **Reconstrucción y Simulación de Facturas Emitidas**:
   - Desarmado de cabecera, potencias (DAP), consumos por bandas horarias (Pico, Resto, Valle), energía activa/reactiva y factores de potencia ($\cos \varphi$).
2. **Prorrateo de Cuadros Tarifarios Multivigencia**:
   - Aplicación exacta de la regla de prorrateo por días de vigencia según el mes comercial estándar de 30 días o calendario real.
3. **Auditoría de Tributos, Ordenanzas y Percepciones**:
   - Determinación precisa de bases imponibles y alícuotas de las 124 municipalidades de Córdoba, fondos provinciales (FODEP) y resoluciones ERSeP.
4. **Análisis de Sensibilidad y Salto de Escalas**:
   - Identificación del costo marginal del próximo kWh y detección del umbral de escalón de cascada tarifaria.
5. **Auditoría de Convenios Interinstitucionales y Alumbrado Público (Vialidad Provincial - EPEC - Cooperativas)**:
   - **Mapeo de Suministros y Contratos de Peaje**: Desdoblamiento y vinculación de suministros mayores de electrificación rural en cooperativas (`xxsigec.servicios`, `xxsigec.contratos`).
   - **Normalización Impositiva OIM (Ordenanza Impositiva Municipal)**: Concatenación y verificación de alícuotas del OIM (`xxsigec.impuestos_localidad.oim_porcentaje`) cruzando obligatoriamente:
     $$\text{contratos.agf\_codigo\_oim} = \text{impuestos\_localidad.agf\_codigo} \quad \text{y} \quad \text{contratos.oim\_tipo} = \text{impuestos\_localidad.oim\_tipo}$$
     garantizando la exacta liquidación tributaria municipal conforme a las ordenanzas tarifarias locales vigentes.
   - **Estandarización de Domicilios y Dependencias Comerciales**: Composición determinista de domicilios normalizados (`srv_calle` + `srv_nro` / `srv_direccion`) y asignación de sucursales comerciales (`scf_descripcion`).

---

## ⚖️ 5. Fundamentos Tarifarios y Regulatorios de las Diplomaturas y Reforma MEM 2025–2026

En articulación con las 70 clases de las Diplomaturas (IDE-UTN.FRSN y SomoslaSEU), el motor de ingeniería inversa de facturación EPEC incorpora los siguientes principios regulatorios y ecuaciones de liquidación:

### 1. Ecuación Canónica de Desagregación Tarifaria, Factor de Nodo y Pass-Through
$$\text{Tarifa Final Usuario} = \underbrace{\left(\text{PEST} \times FN_k\right) + \text{Peaje de Transporte AT/MT}}_{\text{Pass-Through Puro (Margen Comercial = 0)}} + \underbrace{\text{VAD (CAPEX + OPEX + Pérdidas Reconocidas)}}_{\text{Retribución Propia de la Distribuidora}} + \text{Carga Tributaria}$$
- **Pass-Through Neutro**: El Precio Estacional de la Energía y Potencia en el MEM ($\text{PEST}$, afectado por el Factor de Nodo $FN_k$) y los cargos de transporte se trasladan al usuario final exactamente al costo mayorista facturado por CAMMESA, sin recargo ni margen comercial para la distribuidora.
- **Intangibilidad de la Factura Eléctrica (Decreto PEN N.º 450/2025 y Res. SE N.º 400/2025)**: Prohibición regulatoria de incluir en la factura eléctrica tasas municipales ajenas al servicio eléctrico o cargos locales encubiertos, exigiendo desglose transparente de abastecimiento MEM, transporte, VAD e impuestos de ley.
- **Contractualización en el Mercado a Término (MAT)**: Bajo el Decreto 450/2025, la distribuidora incorpora progresivamente precios de contratos bilaterales a término en su mix de costo de abastecimiento trasladable a tarifa.

### 2. Liquidación de Generación Distribuida bajo Esquema *Net Billing* (Ley 27.424 / Dec. 986/2018 y Ley Córdoba 10.604)
- **Diferencia Estructural entre *Net Billing* y *Net Metering***: En Argentina rige estrictamente el **Balance Neto de Facturación (*Net Billing*)**, nunca la compensación física 1:1 de kWh (*Net Metering*):
  $$\text{Importe Neto antes de Impuestos} = \left(E_{\text{consumida red}} \times T_{\text{minorista plena}}\right) - \left(E_{\text{inyectada red}} \times P_{\text{inyección PEST}}\right) + \text{Cargos Fijos / Potencia VAD}$$
  - La energía demandada desde la red ($E_{\text{consumida red}}$) se valoriza a la **tarifa minorista plena** del cuadro tarifario (que incluye PEST + Transporte + VAD).
  - La energía excedente inyectada a la red ($E_{\text{inyectada red}}$) se remunera exclusivamente al **Precio Estacional Mayorista ($\text{PEST}$)** de compra de la distribuidora en el MEM (discriminado por bandas Pico, Resto y Valle cuando existe medición telemedida de cuatro cuadrantes), garantizando que el Usuario-Generador retribuya íntegramente el **VAD** por el uso bidireccional de la red física de distribución.
- **Generación Distribuida Comunitaria Virtual y Algoritmo de Reparto LET**: Liquidación de créditos de energía inyectada por un parque solar comunitario remoto asignados porcentualmente a múltiples suministros asociados dentro del área de concesión de EPEC, descontando el crédito valorizado a tarifa de inyección sobre el bloque de energía de cada factura individual.

### 3. Penalización por Bajo Factor de Potencia ($\cos\varphi$) y Excesos de Capacidad
- **Umbral Normativo de Energía Reactiva**:
  $$\cos\varphi = \frac{P}{\sqrt{P^2 + Q^2}} \ge 0,95 \quad \Longleftrightarrow \quad \tan\varphi = \frac{E_{\text{reactiva}}}{E_{\text{activa}}} \le 0,329$$
  Cuando el factor de potencia medio mensual o de banda cae por debajo del umbral reglamentario, el motor aplica el recargo porcentual escalonado sobre el importe de energía activa o facturación de energía reactiva excedente, incentivando la instalación de bancos de capacitores automáticos.

---

## 📚 Documentación Técnica de Enlace

* **Repositorio Dedicado**: [PROTELEM-EPEC/facturacion-reverse-engineering](https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering)
* **Recorrido del Modelo**: [`docs/modelo_facturacion_sigec.md`](file:///D:/Proyectos/facturacion-reverse-engineering/docs/modelo_facturacion_sigec.md)
* **Glosario de 31 Tablas SIGEC**: [`docs/glosario_tablas.md`](file:///D:/Proyectos/facturacion-reverse-engineering/docs/glosario_tablas.md)
* **Suite de Consultas SQL (A a M)**: [`docs/modelo_factura_documentado.sql`](file:///D:/Proyectos/facturacion-reverse-engineering/docs/modelo_factura_documentado.sql)
* **Tratados Académicos**: `[[docs/Cursos/Diplomatura-Energia-Electrica/Monografia-Integral-Diplomatura-Energia-Electrica]]` y `[[docs/Cursos/Diplomatura-Transicion-Energetica/Monografia-Integral-Diplomatura-Transicion-Energetica]]`
* **Ficha de Agente en Obsidian**: `[[docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering]]`
