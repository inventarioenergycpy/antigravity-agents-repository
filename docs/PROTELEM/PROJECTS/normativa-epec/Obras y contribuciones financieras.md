---
tipo: normativa
estado: vigente
sensibilidad: publica
tags:
  - normativa-epec
  - normativa
  - epec
  - obras
aliases:
  - Contribuciones financieras
  - Obras de conexión
  - Fraccionamientos urbanos
---

# 🏗️ Obras y contribuciones financieras

> [!abstract] Qué es esto
> **Capítulo 3** del Reglamento: quién paga las obras para otorgar o ampliar un suministro según **zona y tensión**, cómo se **reembolsan** las contribuciones financieras, y el régimen de **fraccionamientos urbanos**. La lógica de "dentro/fuera de zona" viene de [[Definiciones y glosario#🗺️ Zonas de prestación]].

> [!tip] Reglas cuantificables (para desarrollo)
> | Regla | Valor | Fuente |
> |---|---|---|
> | Crédito mensual de devolución de contribución | **1/30** del valor de la obra | 3.4 |
> | Duración del reembolso | **30 meses** o hasta agotar la contribución (lo que ocurra primero) | 3.4 |
> | Ventana para que un nuevo suministro herede reembolsos pendientes | **30 días** desde la baja/retiro | 3.7 |
> | Umbral de dispersión para obra de EPEC en loteos preexistentes | **< 17** (km MT+BT)/MVA | 3.10.03 |

## 🔌 Quién paga la obra según tensión y zona

| Suministro | Regla |
|---|---|
| **BT definitivo (3.1)** | Dentro de zona: obra a cargo de **EPEC** (líneas + capacidad de transformación). Fuera de zona: el solicitante aporta **contribución financiera** por la distancia excedente, reembolsable (3.4). Si EPEC elige alimentar desde un punto no óptimo, el costo en exceso es de EPEC. |
| **MT definitivo (3.2)** | Igual que 3.1, pero midiendo distancias contra la red de **Media Tensión**. |
| **AT definitivo (3.3)** | El solicitante aporta contribución financiera por el **costo total** de la obra, reembolsable (3.4). |
| **Transitorios / auxiliares (3.8)** | El usuario se hace cargo del **costo total** de las obras. |

## 💵 Devolución de contribuciones financieras (3.4)

Se devuelven como **créditos en la facturación** del suministro:

| Tipo de suministro | Crédito mensual |
|---|---|
| **Sin facturación de potencia (3.4 a)** | **1/30** del valor de la obra por mes, sin superar el neto facturado por EPEC, durante **30 meses** o hasta agotar la contribución. |
| **Con facturación de potencia (3.4 b)** | **1/30** del valor de la obra × (demanda máxima autorizada del mes / demanda para la que se hizo la obra); tope = neto de energía + demanda. Se corta a los **30 meses** o al igualar el valor de la obra. |

> [!warning] Saldo no recuperado se pierde
> Vencidos los **30 meses**, el usuario **no tiene derecho** a acreditación sobre el importe no recuperado. Los créditos arrancan en la primera facturación posterior a la habilitación (rige 3.7).

## ⬆️ Incremento de demandas contratadas (3.5)
Siempre "dentro de zona", **salvo**:
- **a)** que implique **cambio de nivel de tensión** → se tramita como 3.2 o 3.3 según el nuevo nivel;
- **b)** que exista una obra previa con contribución financiera y **no hayan pasado 30 meses** desde que empezó el reintegro → si el incremento exige obras nuevas, las paga el usuario.

## 🔧 Ejecución de obras por el solicitante (3.6)
EPEC y el usuario acuerdan el plazo (discrepancias las resuelve el **ERSEP**).

- **Dentro de zona (3.6.1):** se comparan el **presupuesto de EPEC** (precios de Licitación Pública) y el del **solicitante** (rubricado por profesional del Colegio de Ingenieros) y se elige el **menor** — pero el "menor" fija la **base del reembolso**, **no quién ejecuta** la obra:
    - Si el presupuesto menor es el del **solicitante** → éste ejecuta y se le reembolsa **a su presupuesto**.
    - Si el presupuesto menor es el de **EPEC** → el solicitante **conserva dos opciones y no pierde el derecho a ejecutar**: **(a)** ejecuta él la obra, pero el reembolso se calcula al **precio de Licitación de EPEC** (el menor); o **(b)** **EPEC ejecuta** y el solicitante **aporta una contribución**.

    En ambos casos el reembolso es un **crédito sobre el neto de energía y demanda** de los suministros vinculados, **redeterminado** por variación de costos (Dto. 800/2016): sin nuevas actualizaciones durante los primeros 12 meses de devolución, redeterminando el remanente cada 12 meses.
- **Fuera de zona / AT nuevos (3.6.2):** el monto (el menor entre presupuesto de EPEC por licitación y de tercero) de las obras que EPEC evita realizar se reembolsa con el mecanismo de 3.6.1; luego, la parte que el usuario debía contribuir financieramente se reembolsa según 3.4.

> [!info] Marco legal de los presupuestos
> Ley 8614 (Obras Públicas provincial) + Dto. 4757/77, Dto. 418/86 (Pliego General para obras por terceros por cuenta y orden de EPEC) y Dto. 800/2016 (redeterminación de precios). EPEC puede fijar topes por concepto.

## 🔄 Reembolsos pendientes ante cambio/baja (3.7)
- **Cambio de titularidad con continuidad:** los créditos siguen aplicándose al suministro a nombre del **nuevo titular**.
- **Nueva solicitud dentro de 30 días** de la baja/retiro: los créditos continúan en el nuevo suministro.
- **Más de 30 días:** tanto el usuario dado de baja como el nuevo titular **pierden** el derecho al monto pendiente.
- El saldo reconocido al nuevo titular se aplica **previa deducción** de toda deuda del titular anterior (en éste u otros suministros).

## 🏘️ Equipos especiales y fraccionamientos

- **Equipos especiales (3.9):** si equipos del usuario (rayos X, tomógrafos, compresores de GNC, etc.) obligan a sobredimensionar, el **sobredimensionamiento lo paga el usuario**.
- **Fraccionamientos urbanos (3.10):** el propietario construye a su cargo y **dona a EPEC** el sistema eléctrico (líneas primarias, subestaciones, líneas secundarias) previo al otorgamiento. Debe presentar documentación para aprobación del proyecto (3.10.02).

### Loteos preexistentes sin red (3.10.03)
EPEC puede hacer la obra por su cuenta (según partida presupuestaria) si la **dispersión** cumple:

```
Dispersión = (km línea MT + km línea BT) / MVA solicitados < 17
```

Si la dispersión **≥ 17**, el costo total se reparte:

```
A cargo de EPEC     = (17 / Dispersión) × Costo Total Obra
A cargo de usuarios = (1 − 17 / Dispersión) × Costo Total Obra
```

*(MVA solicitados = potencia aparente usada para dimensionar la subestación MT/BT.)*

## ⚖️ Cierre del reglamento
- **Resolución de controversias:** las situaciones no previstas o de interpretación las resuelve el **ERSEP**.
- **Cláusula transitoria:** el reglamento aplica a trámites iniciados **después** de su aprobación; los anteriores se rigen por la normativa previa.

---
- [[_index|← Normativa EPEC]] · [[Definiciones y glosario]] · [[Demandas de potencia]]
