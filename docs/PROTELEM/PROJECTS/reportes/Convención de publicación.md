---
tipo: referencia
estado: vigente
sensibilidad: interna
tags:
  - reportes
  - referencia
aliases:
  - Convención de publicación
  - Cómo publicar un reporte
---

# 🧭 Convención de publicación

> [!abstract] Para qué
> Las reglas que hacen que el sitio de [[_index|Reportes]] se mantenga ordenado a
> medida que se agregan informes. La versión operativa —con los comandos— está en el
> `README.md` del repo; acá está el **por qué** de cada regla.

## 1. Un reporte es una carpeta, no un archivo

```
public/reporte/<slug>/index.html
        └────────┘
         esto es la URL
```

El HTML **siempre** se llama `index.html`. Es lo que hace que la dirección quede
`/reporte/<slug>/` en vez de `/reporte/<slug>/informe-completo.html`. Sin esto no hay
URLs limpias, porque el servidor sirve el `index.html` de un directorio por defecto.

## 2. El slug es la URL, y no se cambia

Minúsculas, guiones, sin acentos ni espacios. **Descriptivo del asunto**, no del
formato ni de la fecha ni de la versión.

| ✅ | ❌ | Por qué |
|---|---|---|
| `coop-villa-general-belgrano` | `Informe Final (2).html` | espacios y paréntesis rompen la URL |
| `energia-facturada-cordoba` | `reporte-2026-08-03` | la fecha no dice de qué se trata |
| `medidores-inteligentes` | `informe_coop_VGB_v3` | el versionado en el nombre garantiza links rotos |

> [!important] Una vez compartida, la URL es un compromiso
> Si el slug cambia, el link que mandaste deja de funcionar. **Para publicar una
> corrección se pisa el `index.html` de la misma carpeta**: la URL sigue siendo la
> misma y quien la tenga guardada ve la versión nueva.

## 3. Los metadatos van aparte, en `reporte.json`

```json
{
  "titulo": "Título que se ve en el índice",
  "descripcion": "Una o dos frases sobre qué resuelve el informe.",
  "area": "Comercial",
  "fecha": "2026-08-03",
  "estado": "Listo para revisión"
}
```

**Por qué separado del HTML:** los informes se regeneran. Si los metadatos vivieran
dentro del `index.html`, cada vez que se pisa el archivo habría que volver a
insertarlos y tarde o temprano se pierden. Con el JSON aparte, regenerar el informe
no toca el índice.

Si falta el archivo, `build.py` usa el `<title>` del HTML como título. `estado` es
texto libre; los valores en uso son `Borrador`, `Listo para revisión` y `Cerrado`.

## 4. El informe tiene que ser autocontenido

CSS, imágenes y todo embebido. **Cero recursos externos**: nada de CDN, fuentes de
Google ni imágenes enlazadas.

Tres razones concretas: la red de EPEC puede bloquear dominios externos; el mismo
archivo tiene que servir para la URL, para abrirlo desde el disco y para mandarlo
adjunto; y un informe que depende de un CDN deja de renderizar bien el día que ese
CDN cambia o desaparece.

## 5. El índice se genera, no se edita

`public/index.html` lo escribe `build.py` en cada corrida. Editarlo a mano se pierde.
La fuente de verdad del índice son los `reporte.json` — regla general de
[[Fuentes de verdad]].

## Flujo completo

1. Carpeta `public/reporte/<slug>/`
2. El HTML adentro, renombrado a `index.html`
3. Un `reporte.json` al lado
4. `python build.py`
5. `python serve.py` (si no está ya corriendo) y se comparte la URL

## Al agregar un reporte, actualizar acá

La tabla **Reportes publicados** del [[_index]] tiene que reflejar lo que está
publicado. Es lo primero que mira alguien que retoma el proyecto.
