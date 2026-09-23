---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 103
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "SECTORES"
---

# 📋 SECTORES

> [!info] Significado de negocio
> Areas organizativas de EPEC (103 filas, arbol por SEC_CODIGO_PADRE). Contiene los tres sectores de esta frontera: FRAU 'Fraude e Ilicitos' (padre COM), LEGALES 'Legales' (padre NULL, raiz) y COBJUDIC 'Cobranzas Judiciales' (padre ADM). SEC_TIPO='SX' marca TERCEROS EXTERNOS: CONECTAR SRL, COOP. DE LYF, EMA, IEMCO, INGENIA, LOZA, ROWING, NAXOS, TECNORED.

**Filas estimadas:** 103

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `SEC_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `SEC_DESCRIPCION` | VARCHAR2 | NO |  |
| `SEC_TIPO` | VARCHAR2 | NO |  |
| `SEC_CODIGO_PADRE` | VARCHAR2 | YES | 🔗 → [[SECTORES]] |

## FK declaradas → otras tablas

- **AOR_PERTENECIENTE_A**: `SEC_CODIGO_PADRE` → [[SECTORES]] (`SEC_CODIGO`)

## Tablas que referencian esta tabla

- [[INTERFAZ_MED_ORD]] via `SEC_CODIGO`
- [[ORDENATIVOS]] via `SEC_CODIGO_DESTINO`
- [[SECTORES]] via `SEC_CODIGO_PADRE`
- [[USUARIOS]] via `SEC_CODIGO`
- [[XXCO_LOTE_EQUIPO]] via `SEC_CODIGO_ASIGNADO`, `SEC_CODIGO_CREACION`
- [[XXCO_MOTIVOS_RECLAMOS]] via `SEC_CODIGO_DESTINO`
- [[XXCO_MOVIMIENTOS_EQUIPOS]] via `SEC_CODIGO_ASIGNADO`
- [[XXCO_SECTORES_EQUIPOS]] via `SEC_CODIGO_DESTINO`, `SEC_CODIGO_ORIGEN`
