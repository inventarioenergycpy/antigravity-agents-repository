---
tipo: indice
estado: vigente
sensibilidad: publica
tags:
  - normativa-epec
  - moc
  - epec
  - normativa
aliases:
  - MOC Normativa EPEC
  - Normativa y reglas de negocio EPEC
  - Reglamentación EPEC
  - Reglas de negocio EPEC
---

# ⚖️ Normativa y reglas de negocio EPEC — Cerebro del proyecto

> [!abstract] Qué es esto
> Corpus de **normativa y reglas de negocio de EPEC** que cualquier desarrollo debe respetar. No es una app: es la **fuente de verdad conceptual** de las reglas del negocio (facturación, suministro, medición, demandas, obras) que después se materializan en código en los proyectos comerciales.
>
> Arranca con el **Reglamento de Comercialización de la Energía Eléctrica**; está pensado para **crecer** con más reglamentos, resoluciones internas y reglas de empresa a medida que aparezcan.

> [!tip] Para un agente que va a desarrollar
> Antes de modelar o tocar lógica comercial (tarifas, mora, recupero, factor de potencia, demandas, contribuciones), **leé la nota de esta normativa que corresponda**. Estas reglas son el *porqué* de las tablas que ves en los sistemas comerciales; codificar sin conocerlas produce bugs de negocio silenciosos.

## 📖 Contenido

- [[Definiciones y glosario]] — vocabulario del reglamento: tipos de suministro, tensiones, actores, instalaciones, demandas y zonas. **Empezá acá** para fijar términos.
- [[Otorgamiento y obligaciones]] — requisitos para dar de alta un suministro, garantías, y las obligaciones del usuario (uso de la energía, mora, suspensión, límites de responsabilidad).
- [[Facturacion y cobranza]] — facturas, plazos, recargos por mora, **factor de potencia**, y diferencias de facturación (tarifa indebida / errores). El corazón del "reglamento de facturación".
- [[Medicion de consumos]] — qué pasa cuando el medidor falla: tolerancias por clase, fórmulas de corrección, medidor en vacío y estimación de consumos.
- [[Demandas de potencia]] — demandas contratadas, estacionales, aumentos y el tratamiento de los **excesos** sobre la demanda autorizada.
- [[Ilicitos y recupero de energia]] — apoderamiento ilícito de energía: retiro de medidor y cálculo del recupero (retroactivo 2 años + recargo).
- [[Obras y contribuciones financieras]] — quién paga las obras según zona/tensión, contribuciones financieras y su devolución, fraccionamientos urbanos.

## 🎯 Naturaleza y alcance

> [!info] Es un proyecto, pero su conocimiento es **transversal**
> Vive en `Projects/` por ser un cuerpo de documentación autónomo con su propio MOC, pero lo que documenta **aplica a varios proyectos**. Los proyectos de desarrollo lo **enlazan** en vez de duplicarlo. Cuando una regla concreta sea usada por 2+ proyectos, evaluá promover un resumen a [[Conocimiento compartido]] según la [[Convenciones#♻️ Regla de promoción a Shared|regla de promoción]].

**Proyectos que consumen estas reglas** (referencia, sin acoplarse a su interior):
- [[Projects/sigec-explorer/_index|SIGEC Explorer]] — el esquema `XXSIGEC` (documentos, tarifas, lecturas, recupero) es la materialización de estas reglas.
- [[Projects/plataforma-clientes/_index|Plataforma de Clientes]] — gestión de suministros y facturación de clientes.

## 🔖 Metadatos

| | |
|---|---|
| **Tipo de proyecto** | referencia / normativa (corpus de reglas de negocio) |
| **Fuente legal** | Decreto 1601/2016 · Resolución 79067 · mod. Decreto 674/18 · Resolución 80972 |
| **Órgano regulador** | ERSEP (Ente Regulador de los Servicios Públicos, Córdoba) |
| **Sensibilidad** | `publica` — reglamento publicado; sin datos de cliente ni secretos |
| **Material fuente** | `my-brain/inbox/reglamentacion-epec/` (staging; la verdad legal es el decreto) |

---
- [[Home|← Inicio del cerebro]] · Reglas: [[Convenciones]] · [[Modelo de seguridad]]
