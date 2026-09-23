---
title: "Registro de Mejora: Sinónimos de Medición, Patrón Último Medidor y Mapeo de Distritos SUCURSALES"
tags:
  - #historial-mejoras
  - #ciencia-de-datos
  - #sigec-explorer
  - #sucursales
  - #equipos
  - #distritos
fecha: 2026-09-23
agente_responsable: ciencia-de-datos
backup_referencia: "[[docs/Backups/2026-09-23_133300_ciencia-de-datos_SKILL.md.bak]]"
---

# Registro de Mejora: Sinónimos de Medición, Patrón Último Medidor y Mapeo de Distritos SUCURSALES

- **Fecha**: 2026-09-23
- **Agente Afectado**: `ciencia-de-datos`
- **Archivo de Backup Preventivo**: `docs/Backups/2026-09-23_133300_ciencia-de-datos_SKILL.md.bak`

---

## 1. Contexto y Objetivos
Se formalizaron reglas semánticas y resoluciones de negocio indispensables para el Motor Text-to-SQL y consultas sobre el esquema `XXSIGEC`:
1. **Sinónimos de Medidores**: Definir formalmente que *"Medidores Activos"* es equivalente a *"Medidores instalados"* / *"Medidor instalado"*.
2. **Patrón 'Último Medidor Instalado por Suministro'**: Estandarizar la consulta analítica para obtener el equipo con fecha de instalación más reciente por suministro (`srv_codigo`), considerando casos activos y retirados.
3. **Mapeo de Sectores y Distritos con la Tabla `SUCURSALES`**: Documentar la equivalencia de campos para `SECTOR_ORIGEN` / `SECTOR_DESTINO` y distritos territoriales.

---

## 2. Reglas y Mapeos Incorporados

### A. Reglas de Medidores (`xxsigec.equipos`)
- **Filtro de Medidor Activo / Instalado**: `eqp_estado IS NULL`.
- **Último Medidor Instalado**:
  ```sql
  WITH ultimo_medidor AS (
      SELECT 
          srv_codigo,
          ste_numero,
          ste_tipo,
          eqp_fecha_instal,
          eqp_fecha_retiro,
          eqp_estado,
          ROW_NUMBER() OVER (
              PARTITION BY srv_codigo 
              ORDER BY eqp_fecha_instal DESC NULLS LAST, eqp_orden DESC
          ) AS rn
      FROM xxsigec.equipos
  )
  SELECT * FROM ultimo_medidor WHERE rn = 1;
  ```

### B. Mapeo de Distritos y Sectores (`xxsigec.sucursales` & `xxsigec.areas_geograficas`)
| Concepto de Negocio | Tabla y Columna Origen | Descripción / Observaciones |
| :--- | :--- | :--- |
| **Número de Distrito** | `xxsigec.sucursales[scf_codigo]` | Clave primaria de la sucursal/distrito |
| **Nombre del Distrito** | `xxsigec.sucursales[scf_descripcion]` | Descripción de la sucursal/distrito |
| **Zona del Distrito / Suministro** | `xxsigec.sucursales[zon_codigo]` | Clave foránea a `xxsigec.zonas` |
| **Localidad del Distrito** | `xxsigec.areas_geograficas[agf_nombre]` | Vía `sucursales.agf_codigo = areas_geograficas.agf_codigo` |
| **Sectores Origen / Destino** | `xxsigec.sucursales` | Enlace para transferencias o movimientos de sectores |

---

## 3. Artefactos y Fichas Actualizadas
- `.agents/skills/ciencia-de-datos/SKILL.md`
- `docs/Agentes/02-Ciencia-de-Datos.md`
- `docs/PROTELEM/PROJECTS/sigec-explorer/tablas/SUCURSALES.md`
- `docs/PROTELEM/PROJECTS/sigec-explorer/tablas/EQUIPOS.md`
- `docs/00-Dashboard-MOC.md`
