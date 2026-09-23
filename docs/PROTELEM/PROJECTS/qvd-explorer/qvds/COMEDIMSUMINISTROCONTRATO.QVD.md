---
tipo: qvd
estado: vigente
conexion: QS_GERENCIA_COMERCIAL
carpeta: raiz
num_campos: 60
scraped: 2026-07-16
tags:
  - qvd-explorer
  - qvd
---

# 📦 COMEDIMSUMINISTROCONTRATO.QVD

> [!info] Ficha autogenerada por `qs-scrapping`
> No editar a mano: se sobreescribe en cada corrida. Comentario humano va en
> [[Catálogo]] o en notas propias del proyecto.

**Conexión:** QS_GERENCIA_COMERCIAL · **Carpeta:** raiz · **Scrapeado:** 2026-07-16

## Campos

| Campo                          | Tipo inferido | Ejemplos                                                                           |
| ------------------------------ | ------------- | ---------------------------------------------------------------------------------- |
| `ID_SUMINISTRO_CONTRATO`       | integer       | 92305101 · 92307501 · 92460301 · 92638601 · 92703001                               |
| `CODIGO_SUMINISTRO`            | integer       | 923051 · 923075 · 924603 · 926386 · 927030                                         |
| `NRO_CONTRATO`                 | integer       | 1                                                                                  |
| `ID_CLIENTE`                   | integer       | 63511 · 932539 · 935168 · 938054 · 938979                                          |
| `SUMINISTRO_DIRECCION`         | text          | · VILLA DALCAR · BARRIO BANDA NORTE · SARMIENTO · LABORDE                          |
| `SUMINISTRO_CALLE`             | text          | JUJUY · CRIO CONSIGLI NORTE · HONDURAS · GOETHE · RIVADAVIA                        |
| `SUMINISTRO_NRO_CALLE`         | integer       | 655 · 557 · 690 · 2214 · 742                                                       |
| `SUMINISTRO_PISO`              | unknown       |                                                                                    |
| `SUMINISTRO_DEPTO`             | unknown       |                                                                                    |
| `CODIGO_RUTA`                  | integer       | 364271 · 283361 · 283461 · 11210 · 123332                                          |
| `TIPO_FACTURACION`             | text          | M · B                                                                              |
| `CODIGO_GUDI`                  | unknown       |                                                                                    |
| `CONDICION_SUBSIDIO_ACTUAL`    | text          | SSE · SN1 · SN2 ·                                                                  |
| `ID_TARIFA_BASE`               | integer       | 240 · 140                                                                          |
| `ID_CLASE`                     | integer       | 1                                                                                  |
| `ID_TENSION`                   | integer       | 1                                                                                  |
| `GRUPO_CONTRATO`               | text          | CC                                                                                 |
| `GRUPO_FACTURACION`            | text          | 42G1 · 33FA · 34FA · 12A · 33C2                                                    |
| `FECHA_INICIO_CONTRATO`        | integer       | 36431 · 36430 · 36447 · 34698 · 36472                                              |
| `FECHA_FIN_CONTRATO`           | integer       | 45721 · 42692 ·  · 42124                                                           |
| `ID_LOCALIDAD_OIM`             | integer       | 7050 · 6000 · 1000 · 3300                                                          |
| `ID_GRUPO_LECTURA`             | integer       | 42 · 33 · 34 · 12                                                                  |
| `ESTADO_ACTUAL_CONTRATO`       | text          | C · V                                                                              |
| `ID_ENTE`                      | integer       | 5000                                                                               |
| `ID_SUCURSAL`                  | integer       | 36 · 28 · 1 · 12                                                                   |
| `ID_BARRIO`                    | integer       | 77674 · 50049 · 50006 · 121 · 120003300                                            |
| `ID_CONDICION_IVA`             | integer       | 1 · 5                                                                              |
| `CONDICION_IVA_DESCRIPCION`    | text          | RI- Resp.Inscripto c/Ret. · CF- Consumidor Final                                   |
| `CONDICION_INTIMACION`         | flag          | S                                                                                  |
| `CONDICION_CORTE`              | flag          | S                                                                                  |
| `CONDICION_RETIRO`             | flag          | S                                                                                  |
| `FACTURA_DIGITAL`              | flag          | N                                                                                  |
| `ID_CIIU`                      | integer       | 999999                                                                             |
| `CIIU_DESCRIPCION`             | text          | Sin definir                                                                        |
| `ID_RUTA_LECTURA`              | integer       | 7791 · 5223 · 5276 · 735 · 2459                                                    |
| `ID_SUMINISTRO_CONTRATO_PADRE` | unknown       |                                                                                    |
| `LATITUD`                      | decimal       | -32,6917483333 · -33,1028809801 · -33,10016443 · -31,430112842122 · -33,1585777857 |
| `LONGITUD`                     | decimal       | -62,0987833333 · -64,3669039331 · -64,31629405 · -64,155993885344 · -62,8502895229 |
| `SUBESTACION`                  | integer       | · 0593 · 4641                                                                      |
| `SEA`                          | text          | MJUARE · RIOCUA · LASHIG · SUR · IVERDE                                            |
| `DISTRIBUIDOR`                 | text          | 13_HOSPITAL_3 · 13_DISTRI60 · 13_DISTRI31 · 13_ESCORIAL · 33_PASCANAS_1            |
| `TELEMEDIBLE`                  | text          | NO TELEMEDIBLE · NANSEN                                                            |
| `ID_EQUIPO_ACTUAL`             | integer       | · 71058447 · 838743                                                                |
| `DEM_PICO_CONT`                | integer       | 5                                                                                  |
| `DEM_F_PICO_CONT`              | integer       | 5                                                                                  |
| `ID_EDIFICIO`                  | unknown       |                                                                                    |
| `SITUACION_INCORE`             | text          | NO ACT                                                                             |
| `ORDEN_LECTURA`                | integer       | 92 · 351 · 196 · 59 · 115                                                          |
| `ORIGEN_GEO`                   | text          | GPS_L · MAS                                                                        |
| `TIENE_GARANTE`                | flag          | N · S                                                                              |
| `ESTADO_ACTUAL_SERVICIO`       | text          | FR · SN                                                                            |
| `ALICUOTA_OIM_ACTUAL`          | decimal       | 9,26 · 10 · 9,9 · 11,06                                                            |
| `ID_MEDIO_PAGO`                | text          | PA · TV                                                                            |
| `MEDIO_PAGO`                   | text          | Bancos y Entidades habilitadas · Tarjeta VISA, Cuenta N.:                          |
| `ID_CATEGORIA_ING_BRUTOS`      | integer       | 31 ·                                                                               |
| `CATEGORIA_ING_BRUTOS`         | text          | Alicuota unica 6% ·                                                                |
| `TIPO_OIM`                     | text          | A                                                                                  |
| `TIPO_OIM_DESCRIPCION`         | text          | Grupo A - de practica                                                              |
| `ID_TIPO_SERVICIO_CONTRATADO`  | text          | DE · CO                                                                            |
| `TIPO_SERVICIO_CONTRATADO`     | text          | Definitivo · Condicional                                                           |

---
- [[_index|← QVD Explorer]] · [[Catálogo]]
