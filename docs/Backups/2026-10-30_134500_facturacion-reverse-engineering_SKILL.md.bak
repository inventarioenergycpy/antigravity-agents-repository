---
name: facturacion-reverse-engineering
description: Ingeniero Especialista en Reverse Engineering de Facturación EPEC, simulación tarifaria SIGEC, descomposición cuadro a cuadro, tributos y cotejo punto a punto contra Oracle 19c. Incluye protocolo mandatorio de sincronización con el repositorio upstream PROTELEM-EPEC/facturacion-reverse-engineering para garantizar exactitud a perpetuidad.
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

---

## 📚 Documentación Técnica de Enlace

* **Repositorio Dedicado**: [PROTELEM-EPEC/facturacion-reverse-engineering](https://github.com/PROTELEM-EPEC/facturacion-reverse-engineering)
* **Recorrido del Modelo**: [`docs/modelo_facturacion_sigec.md`](file:///D:/Proyectos/facturacion-reverse-engineering/docs/modelo_facturacion_sigec.md)
* **Glosario de 31 Tablas SIGEC**: [`docs/glosario_tablas.md`](file:///D:/Proyectos/facturacion-reverse-engineering/docs/glosario_tablas.md)
* **Suite de Consultas SQL (A a M)**: [`docs/modelo_factura_documentado.sql`](file:///D:/Proyectos/facturacion-reverse-engineering/docs/modelo_factura_documentado.sql)
* **Ficha de Agente en Obsidian**: `[[docs/Agentes/12-Especialista-Facturacion-Reverse-Engineering]]`
