---
tipo: indice
estado: vigente
sensibilidad: interna
tags:
  - reportes
  - moc
  - epec
aliases:
  - Reportes
  - Sitio de reportes
  - MOC Reportes
---

# 📰 Reportes — sitio interno de informes técnicos

> [!abstract] Qué es
> Sitio **estático** para publicar informes técnicos como páginas HTML y compartirlos
> por URL dentro de la red de EPEC. Sin backend ni base de datos: es una carpeta que
> se sirve. Nació para responder el [[Projects/sigec-explorer/_index\|expediente de la
> Coop. de Villa General Belgrano]] y quedó como canal permanente para los informes
> que se vayan pidiendo.

## 🎯 Para qué existe

Los informes se venían compartiendo como archivos sueltos por mail. El problema no
era el formato sino la **trazabilidad**: nadie sabía cuál era la última versión ni
dónde había quedado el que se mandó hace tres meses. Con una URL estable por informe,
el link que compartís hoy sigue apuntando a la versión vigente mañana.

## 🧭 Cómo se publica

- [[Convención de publicación]] — un reporte = una carpeta, reglas de slug, metadatos
  en `reporte.json`, informes autocontenidos. **Leer antes de agregar un informe.**
- [[Seguridad]] — qué contienen estos informes, por qué no se publican afuera y qué
  revisar antes de compartir una URL.

## ⚙️ Cómo funciona

Dos scripts, nada más:

| Script | Qué hace |
|---|---|
| `build.py` | Escanea `public/reporte/*/` y regenera `public/index.html` con la lista. Lee los metadatos de cada `reporte.json`. |
| `serve.py` | Sirve `public/` en la red interna con `http.server`. Manda `Cache-Control: no-store` para que una republicación se vea al recargar. |

```
reportes/
├── CLAUDE.md                 ← instrucciones para agentes (incluye mantener este vault)
├── README.md                 ← convención completa, paso a paso
├── build.py · serve.py
├── netlify.toml              ← config preparada, NO en uso (ver Seguridad)
└── public/                   ← el sitio
    ├── index.html            ← GENERADO por build.py
    └── reporte/<slug>/
        ├── index.html        ← el informe
        └── reporte.json      ← metadatos del índice
```

> [!warning] `public/index.html` es autogenerado
> Lo escribe `build.py` en cada corrida. Editarlo a mano se pierde. El contenido del
> índice se controla desde los `reporte.json` (regla de [[Fuentes de verdad]]).

## 🌐 Cómo se sirve hoy

Desde la PC del autor, en la red interna:

```
python serve.py            →  http://PC38301EC:8080/
```

Requiere una regla de firewall habilitada una sola vez (el comando está en el
`README.md` del repo) y que la PC quede encendida. **No hay hosting externo**: ver
[[Seguridad]] para el razonamiento.

## 📋 Reportes publicados

| Reporte | URL | Asunto | Estado |
|---|---|---|---|
| Coop. Villa General Belgrano | `/reporte/coop-villa-general-belgrano/` | Expte. 110.291/2024 — puntos frontera, mecánica de facturación y qué puede responderse | Listo para revisión |

## 🔖 Metadatos

| | |
|---|---|
| **Repo** | `d:\Usuarios\pberecibar\Desktop\proyectos\reportes` |
| **Stack** | Python 3 (solo stdlib) · HTML/CSS autocontenido · sin dependencias |
| **Hosting** | Red interna, servidor local. Sin hosting externo (ver [[Seguridad]]) |
| **Proyecto relacionado** | [[Projects/sigec-explorer/_index\|SIGEC Explorer]] — origen de los informes sobre `XXSIGEC` |
