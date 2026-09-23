---
tipo: normativa
estado: vigente
sensibilidad: publica
tags:
  - normativa-epec
  - normativa
  - epec
  - demanda
aliases:
  - Demandas máximas contratadas
  - Excesos de demanda
---

# 📊 Demandas de potencia

> [!abstract] Qué es esto
> **Artículo 2.5** del Reglamento: cómo se contrata la demanda máxima, su vigencia, los suministros estacionales y —lo más sensible para facturación— el tratamiento de los **excesos** sobre la demanda autorizada. Los términos base están en [[Definiciones y glosario#📊 Demandas de potencia]].

> [!tip] Reglas cuantificables (para desarrollo)
> | Regla | Valor | Fuente |
> |---|---|---|
> | Vigencia mínima de una demanda máxima autorizada | **12 meses** consecutivos | 2.5.1 |
> | Duración mínima del período de mayor demanda (estacional) | **4 meses** | 2.5.2 |
> | Piso del período de menor demanda (estacional) | ≥ **30 %** del período de máxima | 2.5.2 |
> | Umbral de exceso sostenido que dispara emplazamiento | > **1,10×** la autorizada, **3 meses** consecutivos | 2.5.4 |
> | Plazo para ajustar tras el emplazamiento | **15 días corridos** | 2.5.4 |
> | Denuncia de exceso imputable a EPEC | dentro de **48 h hábiles** | 2.5.5 |

## 🤝 Demandas máximas contratadas (2.5.1)
Antes de iniciar el suministro se conviene la **demanda máxima autorizada "En Pico"** y **"Fuera de Pico"**. Cada valor es válido para facturación (a los precios de las categorías/escalas del Cuadro Tarifario) por un período **≥ 12 meses** consecutivos, salvo que antes ocurra un aumento (2.5.3) o un exceso sostenido (2.5.4).

## 🗓️ Suministros estacionales (2.5.2)
Aplica a la tarifa de **Grandes Consumos**.
- Período de **mayor** demanda: **≥ 4 meses**, acordado con el usuario.
- Período de **menor** demanda: **≥ 30 %** de la demanda del período de máxima (y no menor al límite de la tarifa del período de máxima).
- Los excesos dentro de un período se cobran según las nuevas demandas verificadas, por el tiempo que reste del período estacional.

## ⬆️ Aumentos de demanda (2.5.3)
Si el usuario necesita más demanda que la convenida, la **solicita previamente**. Acordada, la nueva demanda máxima autorizada reemplaza a la anterior desde que se pone a disposición, y rige **≥ 12 meses** consecutivos (salvo estacionales).

## ⚠️ Excesos sobre la demanda autorizada (2.5.4)

El usuario **no puede** usar (ni EPEC está obligada a suministrar) potencias superiores a las autorizadas cuando pongan en riesgo las instalaciones o la calidad del servicio → previa notificación, EPEC puede **suspender**. El usuario responde por los daños causados por el exceso.

> [!warning] Reencuadre automático por exceso sostenido
> Si la **demanda registrada > 1,10 × la autorizada** durante **3 meses consecutivos**, EPEC emplaza a ajustar en **15 días corridos**. Si el usuario no cumple, EPEC puede tomar como **nueva demanda autorizada** (en pico y/o fuera de pico) el **valor registrado en el último exceso**, válido para facturación por **≥ 12 meses** desde el mes siguiente al último exceso.

> [!danger] Casos de borde — lectura estricta del 2.5.4
> - **Magnitud sin duración no basta:** un exceso de gran magnitud pero breve (ej. **1,15× durante solo 2 meses**) **no** habilita el reencuadre ni siquiera para emplazar. El requisito es **> 1,10× durante 3 meses _consecutivos_**; si un mes intermedio vuelve a la normalidad, el conteo se corta y hay que empezar de cero.
> - **Se fija el valor del _último_ exceso, no el primero ni el más alto:** aun cumpliéndose los 3 meses, la nueva demanda autorizada es la **registrada en el último exceso** que originó la intimación — nunca "el pico del primer mes".
> - **Aun sin reencuadre subsisten dos potestades** (párrafos 1–2 del 2.5.4): si el exceso pone en riesgo instalaciones o calidad de servicio, EPEC puede **suspender** (previa notificación), y el usuario **responde por los daños** causados por el exceso. "No corresponde reencuadre" **no** equivale a "EPEC no puede hacer nada".

Sin perjuicio de tratamientos particulares del Cuadro Tarifario y de eventuales períodos de prueba autorizados por EPEC.

## 🟢 Excesos imputables a EPEC (2.5.5)
**No** se aplican las reglas de exceso cuando la mayor demanda se debió a **causa imputable a EPEC** (interrupciones u otras), con constancias técnicas de la perturbación y **denuncia del usuario dentro de 48 h hábiles**.

## 🔚 Utilización y baja (2.5.6 / 2.5.7)
- El usuario tiene derecho a las demandas autorizadas **hasta el retiro del equipo de medición** (2.5.6).
- Si prescinde del suministro (o EPEC lo retira por incumplimiento) **antes de 12 meses** de fijados los valores de demanda: solo puede volver a pedir el servicio tras **≥ 1 año** del retiro; en su defecto, EPEC puede exigir que abone las demandas máximas autorizadas (pico y fuera de pico) que hubiera correspondido facturar mientras el servicio estuvo retirado (2.5.7).

---
- [[_index|← Normativa EPEC]] · [[Definiciones y glosario]] · [[Facturacion y cobranza]]
