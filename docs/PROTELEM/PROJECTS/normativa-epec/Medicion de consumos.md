---
tipo: normativa
estado: vigente
sensibilidad: publica
tags:
  - normativa-epec
  - normativa
  - epec
  - medicion
aliases:
  - Inconvenientes en la medición
  - Corrección y estimación de consumos
---

# 📐 Medición de consumos

> [!abstract] Qué es esto
> **Artículo 2.3.4** del Reglamento: qué hace EPEC cuando el medidor **no registra el consumo real** — tolerancias por clase, fórmulas de corrección y estimación de consumos. Estas reglas generan **notas de crédito/débito** y son la base de cualquier lógica de recálculo de lecturas.

> [!tip] Reglas cuantificables (para desarrollo)
> | Umbral / regla | Valor | Fuente |
> |---|---|---|
> | Tolerancia medidor **Clase 1** al 10 % de I nominal | ± 3 % | 2.3.4.1 a) |
> | Tolerancia medidor **Clase 1** al 100 % de I nominal | ± 2 % | 2.3.4.1 a) |
> | Tolerancia medidor **Clase 2** al 10 % de I nominal | ± 5 % | 2.3.4.1 b) |
> | Tolerancia medidor **Clase 2** al 100 % de I nominal | ± 3 % | 2.3.4.1 b) |
> | Ventana de reajuste por error de medición | último **bimestre** facturado previo al reclamo + días hasta el cambio | 2.3.4.1 |
> | Base de estimación por medidor defectuoso | promedio de los **últimos 6 meses** | 2.3.4.5 |

## 🎯 Tolerancias por clase (2.3.4.1)

Se **reemplaza el medidor** cuando el error (adelanto o atraso) supera:

| Clase | Al 10 % de la corriente nominal | Al 100 % de la corriente nominal |
|---|---|---|
| **Clase 1** | > 3 % | > 2 % |
| **Clase 2** | > 5 % | > 3 % |

Superados los límites **al 100 % de carga**, se emite **Nota de Crédito o Débito** por el reajuste sobre el **último bimestre** facturado previo al reclamo (o a la solicitud de inspección de EPEC, lo que sea anterior) más los días hasta el cambio, considerando **solo el error al 100 %** y aplicando las fórmulas de 2.3.4.3.

## 🔢 Fórmulas de corrección (2.3.4.3)

Consumo corregido a partir del registro del medidor y su error medido:

```
Medidor ADELANTADO:  Consumo = Registro × 100 / (100 + error%)
Medidor en ATRASO:   Consumo = Registro × 100 / (100 − error%)
```

## 🧮 Casos particulares

| Caso | Tratamiento |
|---|---|
| **Equipos electrónicos (2.3.4.2)** | Si medidor / TT / TC exceden el error de clase, se reemplaza el componente y se **recalculan** energía activa, reactiva, demandas y factor de potencia (fórmulas 2.3.4.3). Reajuste sobre el **último mes** facturado + días hasta el cambio. Cambiar el factor de potencia reajusta lo facturado por energía activa y demanda. |
| **Medidor girando en vacío (2.3.4.4)** | Se asienta la demanda instantánea en vacío × horas del último bimestre + horas hasta el reemplazo → **Nota de Crédito** a favor del cliente. |
| **Anormalidad sin consumo fehaciente (2.3.4.5)** | Se **estima** por promedio de los **últimos 6 meses**. Si el servicio es **estacional**, se usa la misma época de años anteriores. Sin antecedentes suficientes: EPEC ajusta con consumos futuros o datos del usuario. |
| **Pérdidas en instalación de EPEC (2.3.4.6)** | Los consumos en exceso por pérdidas dentro de instalaciones responsabilidad de EPEC se reconocen aplicando 2.3.4.5. |

> [!info] Conexión con facturación
> El resultado de estas correcciones se materializa como **Notas de Crédito/Débito** en la cuenta del usuario. Las diferencias por **tarifa mal aplicada o error administrativo** (no por el medidor) siguen otra vía: ver [[Facturacion y cobranza#🔁 Diferencias de facturación (2.3.5)]].

---
- [[_index|← Normativa EPEC]] · [[Facturacion y cobranza]] · [[Demandas de potencia]]
