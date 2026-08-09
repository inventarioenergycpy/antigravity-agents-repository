---
name: auto-documentacion-agente
description: Captura e incorpora correcciones o configuraciones confirmadas por el usuario para actualizar el SKILL.md del agente correspondiente y registrar el historial en la Bóveda de Obsidian.
---

# Habilidad: Auto-Documentación y Mejora Continua de Agentes

Esta habilidad se activa cuando el usuario solicita expresamente registrar o guardar una instrucción, configuración, corrección o preferencia que ha demostrado mejorar la calidad del agente.

## Flujo de Ejecución

1. **Identificar el Agente Afectado**:
   - Analizar a qué agente corresponde la mejora (`analista-financiero`, `ciencia-de-datos`, `desarrollador-web-showroom` u otro).

2. **Actualizar el `SKILL.md` del Agente**:
   - Editar `.agents/skills/<nombre-agente>/SKILL.md`.
   - Insertar la nueva regla o patrón dentro de la sección relevante del `SKILL.md` sin alterar las reglas base existentes.

3. **Registrar en la Bóveda de Obsidian**:
   - Crear una nueva nota de registro en `docs/Historial-Mejoras/` con el siguiente formato de nombre: `YYYY-MM-DD_<nombre-agente>_<breve-descripcion>.md`.
   - Usar la siguiente plantilla Markdown:

```markdown
---
type: historial-mejora
agente: "[[<nombre-agente>]]"
fecha: YYYY-MM-DD
tags:
  - #historial
  - #mejora
  - #configuracion
---

# Registro de Mejora: [<Nombre del Agente>]

## 📝 Descripción del Cambio
- **Contexto**: <Breve resumen de la interacción que originó la mejora>
- **Regla o Instrucción Agregada**:
  ```markdown
  <Texto exacto de la regla o patrón guardado>
  ```

## 🎯 Impacto y Beneficio
- <Explicación de cómo esta mejora incrementa la precisión, formato o calidad de respuesta del agente>

## 🔗 Referencias
- [[00-Dashboard-MOC]]
- [[<Nombre-Ficha-Agente-en-Docs>]]
```

4. **Confirmar al Usuario**:
   - Resumir de forma precisa y formal la mejora que se ha guardado en el archivo `SKILL.md` y mostrar el enlace a la nota creada en Obsidian.
