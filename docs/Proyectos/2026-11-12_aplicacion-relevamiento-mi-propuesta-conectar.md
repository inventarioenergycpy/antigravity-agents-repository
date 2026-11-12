---
title: "Auditoría de Alcance Técnico: App Relevamiento de Medidores Inteligentes EPEC (Propuesta CONECTAR GD-654 vs. PET Versión 4)"
tags:
  - #protelem
  - #epec
  - #conectar
  - #relevamiento
  - #catastro
  - #ami
  - #auditoria
  - #sigec
created: 2026-11-12
updated: 2026-11-12
responsable: "Javier Ignacio Diaz"
proyecto_local: "D:\\Proyectos\\aplicacion-relevamiento-mi-propuesta-conectar"
pliego_referencia: "PET SERVICIOS RELEVAMIENTO CATASTRAL - Versión 4"
item_evaluado: "Prestación N° 5: Relevamiento de punto de medición (~20.000 u./mes)"
---

# 📱 Auditoría de Alcance Técnico: App Relevamiento de Medidores Inteligentes EPEC (Propuesta CONECTAR GD-654 vs. PET V4)

Ficha técnica del proyecto dedicado `aplicacion-relevamiento-mi-propuesta-conectar`, que documenta la auditoría realizada sobre la propuesta técnica de **Grupo CONECTAR** (*Alexis Meneses - GD-654*) para la construcción de la aplicación de relevamiento de medidores en baja tensión de EPEC frente a las exigencias del **PET Versión 4 (Ítem 5)**.

---

## 🏢 1. Datos de Identificación y Contexto

- **Repositorio Local Dedicado**: `D:\Proyectos\aplicacion-relevamiento-mi-propuesta-conectar`
- **Pliego Técnico Oficial**: [PET SERVICIOS RELEVAMIENTO CATASTRAL.pdf](file:///D:/Proyectos/aplicacion-relevamiento-mi-propuesta-conectar/resources/PET%20SERVICIOS%20RELEVAMIENTO%20CATASTRAL.pdf) *(Gerencia Comercial EPEC - Versión 4)*.
- **Propuesta Evaluada**: [Propuesta_CONECTAR_Informe_Tecnico_Alcance_App_Medidores_EPEC.pdf](file:///D:/Proyectos/aplicacion-relevamiento-mi-propuesta-conectar/resources/Propuesta_CONECTAR_Informe_Tecnico_Alcance_App_Medidores_EPEC.pdf) *(Jira GD-654 - Grupo CONECTAR Sistemas & IT)*.
- **Comunicación Formal**: Enviada por Javier Ignacio Díaz el 12 de noviembre de 2026 a la supervisión técnica de EPEC (Matías Ramírez, Santiago Munge, Nicolás Dib, Pedro Berecibar).

---

## 🎯 2. Alcance Contractual Evaluado: Prestación N° 5 (Ítem 5)

> *"Relevamiento de punto de medición, corresponde a operativo de relevamiento masivo por polígonos de sectores ya relevados y con sus datos catastrales validados, debiendo registrar el estado del punto de medición con su acometida, estado, novedades, riesgo eléctrico, etc. En toda la Provincia."*
> - **Volumen mensual indicativo**: 20.000 relevamientos/mes (55% del valor de la Unidad de Servicio Equivalente - U.S.E.).

---

## ⚖️ 3. Las 7 Observaciones Críticas y Desvíos Detectados

```mermaid
graph TD
    Audit["Auditoría Integral Ítem 5"] --> P1["1. Cronograma\n(CONECTAR 18-24 Dic vs. Acordado 1 Dic / Pruebas 15-30 Nov)"]
    Audit --> P2["2. Navegación SET\n(Obligatorio selector de Subestación en cabecera de la App)"]
    Audit --> P3["3. Web Service vs Excel\n(Pliego exige API. Se documentan links vigentes de fotos)"]
    Audit --> P4["4. Novedades y Riesgo\n(ST, PE, VC, FF, IN, OB y 8 rubros comerciales obligatorios)"]
    Audit --> P5["5. Régimen de Fotos\n(5 fotos obligatorias y máscara JPG del Anexo I)"]
    Audit --> P6["6. SLA 72 hs\n(Cuello de botella en resolución manual de duplicados)"]
    Audit --> P7["7. Resguardo de Fotos\n(PET exige resguardo permanente. Migración estratégica a SIGEC)"]
```

### Síntesis de los 7 Puntos:

1. **Desfasaje en el Cronograma y Fechas de Entrega**:
   - CONECTAR propone entrega del 18 al 24 de diciembre (6 a 7 semanas).
   - El compromiso técnico y operativo exige **pruebas del 15 al 30 de noviembre** y **salida a producción el 1 de diciembre**.
2. **Organización y Navegación de la App por Subestación (SET)**:
   - El relevamiento se estructura por el polígono de BT de cada SET. La App debe incorporar en su pantalla principal un selector de SET para visualizar y filtrar los medidores y parcelas correspondientes.
3. **Exclusión del Servicio Web de Entrega a EPEC (Entrega solo por Excel)**:
   - CONECTAR excluye el Web Service de entrega. El pliego (Anexo I) define la sincronización vía API.
   - **Formato Actual de Consulta de Fotos en Producción**:
     - *Medidor*: `https://relevamientoEpec:R3l3v4m13nt02021@rest.grupoconectar.com/Relevamiento/Ws/getFotoMedidor/id/<REL_ID>`
     - *Acometida*: `https://relevamientoEpec:R3l3v4m13nt02021@rest.grupoconectar.com/Relevamiento/Ws/getFotoMedidor/id/<REL_ID>/nov/ACOMETIDA`
     - *Tapa*: `https://relevamientoEpec:R3l3v4m13nt02021@rest.grupoconectar.com/Relevamiento/Ws/getFotoMedidor/id/<REL_ID>/nov/TAPA`
4. **Novedades Incompletas y Falta de Banderas de Riesgo Eléctrico / Fraude**:
   - Falta tipificar en el formulario móvil los códigos normativos: `ST` (tapa), `PE` (pilar electrificado / riesgo), `VC` (verificación de categoría), `FF` (fraude), `IN` (interno), `OB` (obstáculo), así como las banderas booleanas de seguridad y los **8 rubros comerciales**.
5. **Régimen y Nomenclatura Fotográfica (Anexo I, Punto 5)**:
   - El PET exige 5 tomas obligatorias (*Puerta, Acometida, Pilar, Tapa y Medidor*) con la máscara:  
     $$\text{<ID\_EMPRESA>-<ID\_SINC>-<ID\_PUNTO><ID\_RELEV><NRO\_IMG>.jpg}$$
6. **SLA de Rendición a 72 hs y Gestión de Duplicados**:
   - La resolución de duplicados delegada exclusivamente al verificador web puede retrasar el cumplimiento del plazo máximo de 72 horas.
7. **Duración del Almacenaje de Fotos**:
   - El PET fija resguardo permanente (*"garantizar que no sean eliminadas"*). Se sugiere coordinar la migración de las fotos activas (desde abril de 2023) hacia los servidores de EPEC para vincularlas a los ordenativos de **Oracle SIGEC**.

---

## 📂 4. Enlaces y Documentación en el Repositorio del Proyecto

- Repositorio Local: [aplicacion-relevamiento-mi-propuesta-conectar](file:///D:/Proyectos/aplicacion-relevamiento-mi-propuesta-conectar/README.md)
- Registro de Correo Oficial: [2026-11-12_comunicacion_oficial_observaciones_epec.md](file:///D:/Proyectos/aplicacion-relevamiento-mi-propuesta-conectar/docs/2026-11-12_comunicacion_oficial_observaciones_epec.md)
- Matriz Detallada de Conformidad: [matriz_conformidad_pet_v4_vs_conectar_gd654.md](file:///D:/Proyectos/aplicacion-relevamiento-mi-propuesta-conectar/docs/matriz_conformidad_pet_v4_vs_conectar_gd654.md)
- Pliego PET Oficial: [PET SERVICIOS RELEVAMIENTO CATASTRAL.pdf](file:///D:/Proyectos/aplicacion-relevamiento-mi-propuesta-conectar/resources/PET%20SERVICIOS%20RELEVAMIENTO%20CATASTRAL.pdf)
- Propuesta Técnica CONECTAR: [Propuesta_CONECTAR_Informe_Tecnico_Alcance_App_Medidores_EPEC.pdf](file:///D:/Proyectos/aplicacion-relevamiento-mi-propuesta-conectar/resources/Propuesta_CONECTAR_Informe_Tecnico_Alcance_App_Medidores_EPEC.pdf)
