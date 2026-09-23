---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 492
tags:
  - sigec-explorer
  - tabla
  - base
  - documentada/negocio
aliases:
  - "ENTES"
---

# 📋 ENTES

> [!info] Significado de negocio
> Organismos/entes públicos y clientes institucionales (PK MIN_CODIGO, 492 filas). Columnas: MIN_DESCRIPCION (ej. 'Municipalidad La Falda', 'Dispensarios', 'Escuelas'), TMI_CODIGO (tipo de ente → TIPOS_ENTE). El prefijo MIN_ es de esta tabla. Se enlaza desde CONTRATOS.MIN_CODIGO y PERSONAS.MIN_CODIGO (esta última suele venir NULL).

**Filas estimadas:** 492

## Columnas

| Columna | Tipo | Null | Rol | Significado |
|---|---|---|---|---|
| `MIN_CODIGO` | VARCHAR2 | NO | 🔑 PK | Código de ente/organismo (PK de ENTES; prefijo MIN_ = ENTES). Presente en CONTRATOS y PERSONAS. Une un contrato/persona con su organismo público (Municipalidad, escuela, etc.). |
| `MIN_DESCRIPCION` | VARCHAR2 | YES |  |  |
| `MIN_GRUPO` | VARCHAR2 | YES |  |  |
| `MIN_DIRECCION` | VARCHAR2 | YES |  |  |
| `AGF_CODIGO` | NUMBER | NO |  | Área geográfica de facturación (PK de AREAS_GEOGRAFICAS; AGF_NOMBRE, AGF_TIPO). SERVICIOS.AGF_CODIGO apunta al nivel ZL (zona-localidad). Localidad = este campo. Córdoba capital = AGF_CODIGO 1000 (ZL 'CORDOBA'). |
| `MIN_C_POSTAL` | NUMBER | YES |  |  |
| `MIN_CODIGO1` | VARCHAR2 | YES |  |  |
| `TMI_CODIGO` | VARCHAR2 | YES |  | Tipo de ente (PK de TIPOS_ENTE, en ENTES): 1 Nacional, 2 Provincial, 3 Municipal, 4 Cooperativas, 5 Particulares, 6 Prov. No Autárq., 7 EPEC, 8 Barrios. Se guarda como VARCHAR ('1'...'8'). |
| `MIN_DEFINICION_CONTABLE` | VARCHAR2 | YES |  |  |

## Tablas que referencian esta tabla

- [[PERSONAS]] via `MIN_CODIGO`
