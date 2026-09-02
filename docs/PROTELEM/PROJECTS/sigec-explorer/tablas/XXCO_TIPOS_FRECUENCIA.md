---
tipo: tabla
categoria: custom
owner: XXSIGEC
num_rows: 8
tags:
  - sigec-explorer
  - tabla
  - custom
aliases:
  - "XXCO_TIPOS_FRECUENCIA"
---

# 🔧 XXCO_TIPOS_FRECUENCIA

> Creada en Proyecto 270 - Para representar las Frecuencias de Lectura y Facturacion en un único lugar. Reemplaza Tipos_Facturacion la cual se convierte en Vista

**Filas estimadas:** 8

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `TFR_CODIGO` | VARCHAR2 | NO | 🔑 PK |
| `TFR_DESCRIPCION` | VARCHAR2 | YES |  |
| `TFR_FRECUENCIA` | NUMBER | NO |  |
| `TFR_DIAS` | NUMBER | YES |  |
| `TFR_MESES` | VARCHAR2 | YES |  |
