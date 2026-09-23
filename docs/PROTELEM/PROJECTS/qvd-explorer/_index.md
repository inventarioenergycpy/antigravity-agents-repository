---
tipo: indice
estado: vigente
sensibilidad: interna
tags:
  - qvd-explorer
  - moc
aliases:
  - QVD Explorer
---

# 📦 QVD Explorer — diccionario de QVDs de Qlik Sense

> [!abstract] Qué es
> Diccionario de los **505 QVD** accesibles desde el Editor de carga de datos de
> Qlik Sense (EPEC): columnas, tipo inferido y ejemplos. Insumo para migrar los
> tableros de Power BI y para el agente que cruza QVD ↔ SIGEC.

> [!warning] Colección autogenerada
> Las fichas de `qvds/` las genera el repo `qs-scrapping`
> (`d:\Usuarios\pberecibar\Desktop\proyectos\qs-scrapping`, comando
> `python main.py vault`) y se **sobreescriben** en cada corrida. No editarlas a mano;
> el comentario humano va en [[Catálogo]] o en notas propias. La fuente de verdad es
> `data/output/qvd_dictionary.json` del repo (regla de [[Fuentes de verdad]]).

- [[Catálogo]] — índice navegable de todos los QVD, con match SIGEC.
- [[Seguridad]] — sensibilidad de la colección (default **confidencial**: los ejemplos
  traen datos reales de clientes).
- Relación con Oracle: [[Projects/sigec-explorer/_index\|SIGEC Explorer]] — cada ficha
  de QVD enlaza sus tablas de origen candidatas.

*Última regeneración: 2026-07-17.*

---
- [[Home|← Inicio]]
