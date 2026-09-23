---
tipo: tabla
categoria: base
owner: XXSIGEC
num_rows: 29
tags:
  - sigec-explorer
  - tabla
  - base
aliases:
  - "DIS_DOCS_"
---

# 📋 DIS_DOCS_

**Filas estimadas:** 29

## Columnas

| Columna | Tipo | Null | Rol |
|---|---|---|---|
| `DOCUMENT_ID` | NUMBER | NO | 🔑 PK |
| `OWNER` | VARCHAR2 | NO |  |
| `DOCUMENT_NAME` | VARCHAR2 | NO |  |
| `COMMENTS` | VARCHAR2 | YES |  |
| `CREATE_DATE` | DATE | NO |  |
| `MODIFIED_DATE` | DATE | YES |  |
| `MODIFIED_BY` | VARCHAR2 | YES |  |
| `DOC_LENGTH` | NUMBER | NO |  |
| `DOCUMENT` | LONG RAW | YES |  |
| `BATCH` | NUMBER | YES |  |
