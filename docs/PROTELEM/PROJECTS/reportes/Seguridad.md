---
tipo: seguridad
estado: vigente
sensibilidad: interna
tags:
  - reportes
  - seguridad
aliases:
  - Seguridad Reportes
  - Sensibilidad de los reportes
---

# 🔒 Seguridad y sensibilidad de los reportes

> [!abstract] Para qué
> Qué contienen los informes que publica [[_index|Reportes]], por qué hoy **no** se
> alojan afuera, y qué revisar antes de compartir una URL. Complementa el
> [[Modelo de seguridad]] general de la bóveda.

## Default de sensibilidad

> [!warning] Todo reporte es `interna` salvo que se declare lo contrario
> Los informes de este sitio se arman sobre datos de producción. Salen del ámbito de
> EPEC solo con decisión explícita de quien corresponda.

## Qué contienen estos informes

Un informe típico de este sitio incluye:

- **Números de expediente administrativo** en trámite.
- **Identificadores reales de clientes**: suministros, contratos, medidores, personas.
- **Razones sociales** de clientes y de terceros (otras cooperativas, organismos).
- **SQL contra esquemas de producción**, con nombres de tablas y columnas de SIGEC.
- **Observaciones de control interno** — circuitos administrativos, trazabilidad de
  cargas, procedimientos que no se están cumpliendo.

Los dos últimos son los que más pesan. El SQL expone la estructura interna del sistema
comercial, y las observaciones de control pueden tener consecuencias si circulan fuera
del canal correcto.

> [!tip] Referirse a áreas, no a personas
> Los informes nombran **áreas** ("el área Comercial carga la energía"), nunca usuarios
> ni personas. La auditoría del sistema sí guarda usuarios, pero eso queda en la
> bitácora técnica del repo de origen, no en el informe publicado. Mantener esa
> separación: hace que el informe sea sobre el proceso y no sobre alguien.

## Por qué no hay hosting externo

Se evaluó **Netlify** (agosto 2026) y se descartó por una razón concreta:

> En el plan gratuito de Netlify los sitios son **públicos en internet**. Cualquiera
> con la URL entra, sin usuario ni contraseña. La protección por contraseña es
> función de plan pago.

El `netlify.toml` quedó en el repo con headers de seguridad y `X-Robots-Tag: noindex`
preparados, **pero sin usar**. Conviene tener presente que `noindex` **no es control
de acceso**: evita que lo levante un buscador, no que lo lea alguien que tenga el link.

Si en algún momento se retoma la idea, las salidas razonables son:

1. Plan pago con protección por contraseña.
2. Publicar afuera una versión recortada, sin anexo técnico ni identificadores.
3. **La mejor**: pedirle a Sistemas un servidor web interno donde alojar `public/`.
   Es lo mismo que hoy pero puertas adentro y sin depender de una PC encendida.

## Cómo se sirve hoy

Servidor local en la red interna (`serve.py`, puerto 8080). El acceso queda limitado
por la propia red: desde afuera de EPEC no se ve, y está bien que así sea.

Limitaciones asumidas: **no hay autenticación** —quien esté en la red y tenga la URL
entra— y la disponibilidad depende de que la PC esté encendida con el proceso
corriendo. Para informes que se leen una vez antes de una reunión, alcanza.

## Antes de compartir una URL

1. ¿El informe nombra personas? Debería hablar de áreas.
2. ¿El anexo técnico hace falta para este destinatario, o alcanza con las conclusiones?
3. ¿A quién le estás pasando el link y por qué canal?
4. Si el informe toca a un **tercero** (otra cooperativa, otro organismo), ¿corresponde
   que ese dato circule?
