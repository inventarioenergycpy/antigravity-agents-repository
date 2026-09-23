---
tipo: glosario
estado: vigente
sensibilidad: publica
tags:
  - normativa-epec
  - glosario
  - epec
  - suministro
aliases:
  - Glosario del Reglamento EPEC
  - Definiciones de suministro
---

# 📖 Definiciones y glosario — Reglamento EPEC

> [!abstract] Qué es esto
> Vocabulario del **Capítulo 1** del Reglamento de Comercialización. Fija el significado de los términos que usa el resto de la normativa. Si un desarrollo modela "suministro", "demanda" o "zona", **estos son los significados canónicos**.

## 🔌 Tipos de suministro

```
Suministro
├── DEFINITIVO (permanente, cumple requisitos)
│   ├── Principal ── (variante) Estacional
│   ├── Auxiliar (solo si se corta el principal)
│   └── Condicional (permiso municipal "condicional"; interrumpible por autoridad)
└── TRANSITORIO (no permanente: obradores, móviles, ferias, eventos…)
```

| Término | Definición |
|---|---|
| **Suministro** | Provisión de energía eléctrica al usuario. |
| **Definitivo** | Servicio permanente; el titular cumplió todos los requisitos técnicos, legales, administrativos y económicos. |
| **Principal** | Suministro por el que se presta normalmente el servicio. |
| **Estacional** | Variante del principal cuyas demandas máximas varían en períodos del año preestablecidos (industria/comercio con estacionalidad). Ver [[Demandas de potencia#🗓️ Suministros estacionales (2.5.2)]]. |
| **Auxiliar** | Conexión que se usa **únicamente** cuando se interrumpe el principal. |
| **Condicional** | Permiso municipal "condicional"; mismas prerrogativas y obligaciones que el definitivo, con la única salvedad de que es **interrumpible por orden de la autoridad municipal**. También abarca los casos en que el suministro se otorga con **requisitos del definitivo aún pendientes** de cumplir, o con **documentación del usuario en análisis**: en ambos EPEC puede **interrumpirlo unilateralmente**. |
| **Transitorio** | Carácter no permanente: obradores de obra, conexiones móviles, circos/ferias/eventos. |

## ⚡ Tensiones normales y rangos de demanda

Servicio en corriente alterna de **50 Hz**.

| Nivel | Tensiones | Rango de demanda máxima |
|---|---|---|
| **Baja Tensión (BT)** | Monofásico 220 V · Trifásico 3×380/220 V | Monof. hasta 5 kW · Trif. hasta 300 kW |
| **Media Tensión (MT)** | 13.200 V y 33.000 V | desde 300 kW |
| **Alta Tensión (AT)** | 66.000 V y 132.000 V | desde 20 MW |

> [!note] EPEC decide el nivel
> El nivel/forma de conexión lo **fija EPEC**, independientemente de los límites. Si el solicitante prefiere un nivel fuera de rango, EPEC resuelve por conveniencia técnico-económica y las obras van a su cargo.

## 👤 Actores

| Término | Definición |
|---|---|
| **Solicitante** | Persona (física o jurídica) que **requiere** el suministro. |
| **Usuario** | Persona (física o jurídica) **titular** del suministro. La condición se adquiere **desde que EPEC conecta** el servicio. |

## 🧰 Instalaciones y puntos

| Término | Definición |
|---|---|
| **Derivación** | Conjunto de instalaciones que se adicionan al sistema para satisfacer un nuevo suministro. |
| **Punto de derivación** | Lugar donde se vincula el sistema preexistente con la derivación. |
| **Acometida** | Conductores y elementos desde la red de distribución hasta el **punto de medición**. Con varios suministros: una parte general + partes individuales. |
| **Conexión de la acometida** | Operación que energiza la acometida. |
| **Conexión del suministro** | Operación que energiza para el suministro (coincide con la de acometida si el suministro es individual). |
| **Punto de medición** | Lugar donde se mide la energía. |

## 📊 Demandas de potencia

| Término | Definición | Unidad |
|---|---|---|
| **Potencia instalada** | Suma de potencias nominales de todos los artefactos/motores instalados por el usuario. | kW |
| **Demanda máxima registrada** | Máximo valor medio de potencia entre dos lecturas, integrado en **15 minutos**. Puede ser "En Pico" o "Fuera de Pico" según el Cuadro Tarifario. | kW |
| **Demanda máxima autorizada** | Demanda máxima **convenida** entre EPEC y el usuario. Se desglosa en "En Pico" y "Fuera de Pico". | kW |

> [!info] Pico / Fuera de Pico
> Los horarios de Pico y Fuera de Pico los define el **Cuadro Tarifario** (documento aparte, no incluido en este reglamento). Tanto la demanda *registrada* como la *autorizada* se discriminan por banda horaria.

## 🗺️ Zonas de prestación

| Zona | Definición |
|---|---|
| **Dentro de zona (BT)** | Hasta **50 m** por vía pública entre el punto más próximo de la red de BT y el punto de medición. |
| **Dentro de zona (MT)** | Hasta **100 m** por vía pública entre el punto más próximo de la red de MT y el punto de medición. |
| **Fuera de zona** | Lo que exceda esos límites, y **todo suministro en Alta Tensión**. |

> [!tip] Por qué importa "dentro/fuera de zona"
> Determina **quién paga la obra** de conexión: dentro de zona la absorbe EPEC; fuera de zona el solicitante hace una contribución financiera reembolsable. Detalle en [[Obras y contribuciones financieras]].

---
- [[_index|← Normativa EPEC]] · [[Otorgamiento y obligaciones]] · [[Demandas de potencia]]
