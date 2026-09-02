---
tipo: normativa
estado: vigente
sensibilidad: publica
tags:
  - normativa-epec
  - normativa
  - epec
  - facturacion
aliases:
  - Reglamento de facturación EPEC
  - Facturación y cobranza
  - Factor de potencia
---

# 🧾 Facturación y cobranza

> [!abstract] Qué es esto
> El corazón del "reglamento de facturación": emisión y pago de facturas, **mora y recargos**, ajuste por **factor de potencia** y corrección de **diferencias de facturación**. Estas son las reglas que un sistema comercial encoda como lógica de cálculo y de cobranza.

> [!tip] Reglas cuantificables (para desarrollo)
> | Regla | Valor | Fuente |
> |---|---|---|
> | Antelación mínima de la factura antes del vencimiento | **5 días corridos** | 2.4.1 |
> | Tope de la tasa de recargo por mora | ≤ **1,5×** la tasa del Banco de Córdoba (descuento de docs. a 30 días) | 2.4 |
> | Factor de potencia mínimo exigido (cos φ) | **0,95** | 2.2.5 |
> | cos φ que dispara emplazamiento a corregir (plazo 30 días) | < **0,50** | 2.2.5.2 |
> | Retroactividad máxima de reajuste por diferencias de facturación | **1 año** | 2.3.5 |
> | Plazo de intimación de pago por tarifa mal aplicada | **10 días corridos** | 2.3.5.1 |

## 📨 Facturas (2.4)

- El usuario **paga dentro del plazo** fijado en la factura. La falta de pago genera **mora automática** (sin interpelación judicial ni extrajudicial).
- La factura se remite al domicilio del suministro (o al que indique el titular) con **≥ 5 días corridos** de antelación al vencimiento (2.4.1).
- Si el usuario **no recibe** la factura, EPEC debe proveer vías para conocer importe y fechas; el usuario puede pedir **duplicado** en cualquier local comercial (2.4.2).
- La facturación debe ser **clara y completa**, con los datos exigidos legalmente. El **ERSEP** puede exigir más información (2.4.3).

## ⏱️ Mora y recargos

- **Mora automática** al vencimiento (2.4). Proceso de suspensión/interrupción por impago: ver [[Otorgamiento y obligaciones#Mora en el pago (2.2.8) — línea de tiempo]].
- **Tasa de recargo:** no puede superar **1,5 veces** la tasa del Banco de la Provincia de Córdoba para descuento de documentos a 30 días (2.4).
- Se suman los **gastos de notificación**.

## ⚙️ Factor de potencia (2.2.5)

El usuario debe mantener el **cos φ medio ≥ 0,95**. Si no:

### Recargo por bajo factor de potencia (2.2.5.1)
Para cos φ medio **< 0,95**, el importe de consumo (energía + potencia) se ajusta:

```
Importe ajustado = Importe facturado × 0,95 / (factor de potencia medio medido)
```

> [!example] Ejemplo
> cos φ medido = 0,90 → factor de ajuste = 0,95 / 0,90 ≈ **1,056** → recargo del ~5,6 % sobre consumo.

### cos φ crítico (2.2.5.2)
Si el cos φ medio **< 0,50**: EPEC **emplaza a corregir en ≤ 30 días**; vencido el plazo sin corrección → **suspensión** del suministro.

### Vigencia del ajuste (2.2.5.3)
- Con **medidor de reactiva instalado**: aplica desde la primera lectura posterior a su instalación (ídem para traslados por cambio de domicilio).
- Con **medición temporaria**: aplica desde ese período y se mantiene **hasta que el cliente corrija**, salvo nueva medición peor.
- La **corrección** la comunica el usuario fehacientemente; EPEC mide/comprueba dentro de **5 días hábiles**, con validez **desde la notificación**.

## 🔁 Diferencias de facturación (2.3.5)

> [!important] Retroactividad acotada a 1 año
> En ambos casos, el reajuste se calcula con la **tarifa vigente de cada período** desde el **inicio de la anormalidad** hasta el **reclamo del usuario o la constatación de EPEC (lo que sea anterior)**, con tope de **1 año** hacia atrás. Se suma, además, el período entre ese hito y la **normalización efectiva**.

### Por aplicación indebida de la tarifa (2.3.5.1)
| Caso | Efecto |
|---|---|
| Datos **inexactos del titular** → tarifa incorrecta → se facturó **de menos** | EPEC factura e **intima el pago** de la diferencia en **10 días corridos**. |
| EPEC aplicó tarifa **superior** / facturó de más por causa propia | EPEC **reintegra** lo percibido de más. |

### Por errores en la facturación (2.3.5.2)
Si EPEC facturó sumas mayores o menores por error, emite **notas de crédito o débito** por cada período, con la misma regla de retroactividad (tope **1 año**).

## 🚫 Efecto suspensivo (2.3.3)

> [!warning] Reclamar no frena el pago
> Los reclamos por importes, provisión de energía, cambio de medidor o aumento de potencia **no suspenden la obligación de pago** cuando la causa obedece a hechos **controvertidos por la empresa**.

## 🔗 Relacionado
- [[Medicion de consumos]] — cuando el error viene del medidor, el reajuste sale de ahí (fórmulas de corrección).
- [[Demandas de potencia]] — la demanda autorizada define escalas/precios del Cuadro Tarifario.
- [[Ilicitos y recupero de energia]] — recupero por hurto de energía (régimen propio, retroactivo 2 años).

---
- [[_index|← Normativa EPEC]] · [[Otorgamiento y obligaciones]] · [[Medicion de consumos]]
