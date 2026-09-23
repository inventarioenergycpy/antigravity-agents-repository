---
tipo: seguridad
estado: vigente
sensibilidad: interna
tags:
  - sistema-epec-oracle
  - seguridad
  - licitacion
aliases:
  - Seguridad Sistema EPEC Oracle
---

# 🔒 Seguridad — Sistema EPEC Oracle

> [!abstract] Qué es esto
> Clasificación de datos **de este proyecto**. Complementa el [[Modelo de seguridad]] global. El rasgo que lo distingue de los demás proyectos del cerebro: acá no hay datos de clientes ni credenciales, pero sí **material de una licitación en curso**, que es sensible por otra vía.

## Clasificación de datos (default del proyecto: `interna`)

| Sensibilidad | Qué cae acá | Ejemplos en este proyecto |
|---|---|---|
| `confidencial` | Posición negociadora de EPEC y datos comerciales de los oferentes antes de la adjudicación | Precios por componente y por etapa (PRETECO cloud vs. híbrida, ESC Partners, OPEN), comparativas de costos, análisis de afinidad Oracle vs. OPEN, motivos internos de recorte de requerimientos |
| `interna` | El corpus funcional y su gobernanza | Requerimientos del Anexo I, alcance del pliego, responsables por sector, deuda técnica detectada, preguntas abiertas |
| `publica` | Genérico y sin riesgo | Método de trabajo del wiki, patrón de base de conocimiento mantenida por LLM |

## Regla propia: el material sensible no se copia acá

> [!warning] La licitación no está adjudicada
> Los precios de los proveedores, las comparativas de propuestas y el análisis de sesgo del pliego hacia un producto **viven en la carpeta de red y se quedan ahí**. El vault los referencia por su ubicación — nunca transcribe cifras, totales ni conclusiones comparativas.

Motivo doble: el [[Fuentes de verdad|principio de fuente única]] (el dato vive en su corpus, la nota lo explica y enlaza) y el hecho de que un número de una licitación abierta, sacado de contexto y sin fecha, es a la vez inexacto y comprometedor.

Si en algún momento hace falta razonar sobre costos, se hace en el staging local
(`my-brain\projects\sistema-epec-oracle\analisis\`), que es efímero, no en el vault.

## PII / datos sensibles

Este proyecto **no maneja datos de clientes reales**: el corpus son especificaciones funcionales, no bases de datos. No hay suministros, DNI ni direcciones.

Sí hay **nombres de personas y sectores** en la hoja de responsables por funcionalidad del Anexo de marzo. No se transcriben al vault: se referencia el artículo `wiki/gobernanza/responsables-por-funcionalidad.md` de la fuente.

## Secretos

No aplica: el proyecto no tiene credenciales, conexiones ni tokens. El acceso a la fuente es por permisos de red sobre `\\srvfs01`.

## Reglas del proyecto

1. **La carpeta de red es de solo lectura.** Ver [[Fuentes de información]]. No se escribe nada ahí, ni siquiera archivos temporales.
2. **Nada de cifras de la licitación en el vault** ni en notas compartidas.
3. **Ningún nombre propio de contacto** se transcribe desde el Anexo.
4. **Nada de este proyecto se promueve a `Shared/`** mientras la licitación esté abierta — y si algún día se promueve, será solo el método de trabajo (el patrón de wiki mantenido por LLM), nunca el contenido del pliego. Ver [[Convenciones#Regla de promoción a Shared]].

---
- Global: [[Modelo de seguridad]] · [[_index|← MOC]]
