# 🏛️ Registro de Decisión y Mejora: Incorporación de Planes 14 y 15 (Centro Subterráneo) al Plan de Despliegue AMI

**Fecha de Registro:** 28 de Octubre de 2026, 14:40 ART  
**Agente Responsable:** Agente 11 (Copiloto Orquestador y Selector Dinámico de Habilidades)  
**Proyecto Asociado:** Despliegue de Medidores Inteligentes AMI - EPEC (Licitación Pública 5573)  
**Repositorios Impactados:**
- `D:\Proyectos\despliegue-medidores-inteligentes-ami`
- `D:\Proyectos\antigravity-agents-repository`

---

## 🎯 1. Contexto y Directiva del Usuario

En el marco de la planificación operativa 2027 para la instalación masiva de medidores inteligentes en Córdoba Capital y el Interior provincial, se analizó inicialmente la postergación de los planes del área central debido a su complejidad constructiva.

El usuario instruyó expresamente:
> *"Considerar los Planes 14 y 15 (Centro) por más que sean subterráneos pero con la salvedad que son subterráneos. Documentar y guardar todo lo aprendido."*

---

## 🗺️ 2. Diagnóstico Técnico y Datos Censales de Planes 14 y 15

| Métrica | Plan 14 (Microcentro) | Plan 15 (Macrocentro) | Total Consolidado Centro |
| :--- | :---: | :---: | :---: |
| **Suministros Posibles Cambios** | **25.010** | **23.710** | **48.720** |
| **Monofásicos Directos** | 22.152 (88,57%) | 20.229 (85,32%) | **42.381 (86,99%)** |
| **Trifásicos Directos** | **2.858 (11,43%)** | **3.481 (14,68%)** | **6.339 (13,01%)** |
| **Medidores Inteligentes Preexistentes** | 8 | 8 | 16 |
| **Cartografía SET en GIS** | Sin SET dibujadas | Sin SET dibujadas | Pendiente de digitalización |
| **Lote Tecnológico Planificado** | CLOU E4 | CLOU E4 | **CLOU E4 (~75k u.) + Módem GPRS** |

---

## ⚡ 3. Las 5 Salvedades Operativas y Técnicas de la Red Subterránea

### Salvedad 1: Infraestructura de Cámaras y Espacios Confinados
- **Realidad de Campo**: El Centro de Córdoba no posee tendidos aéreos de baja tensión sobre postes. La distribución opera en cámaras subterráneas de hormigón bajo calzada y acera, conductos y sótanos comerciales.
- **Protocolo Requerido**: Las cuadrillas instaladoras convencionales no están autorizadas a ingresar a cámaras subterráneas. Se requiere:
  - Personal certificado en **Seguridad para Trabajos en Espacios Confinados**.
  - Equipos de detección de gases múltiple ($O_2, CO, H_2S, LEL$).
  - Equipos de ventilación forzada y bombas de achique para cámaras anegadas.
  - Consignación y corte programado coordinado con la Guardia de Mantenimiento de Redes Subterráneas de EPEC.

### Salvedad 2: Propagación de Frecuencia PLC y Antenas Uplink Remotas
- **Realidad de Campo**: Los cables subterráneos armados poseen blindaje metálico y discurren bajo losas de hormigón que atenúan severamente las señales PLC (PRIME / G3).
- **Protocolo Requerido**:
  - Los concentradores de datos (DCU) deben montarse dentro de la cámara, requiriendo **cableado coaxial y antenas remotas externas** llevadas hacia conductos de ventilación, respiraderos o cajas a nivel rasante de vereda para garantizar comunicación celular 4G/GPRS con el sistema central.
  - En galerías comerciales y subsuelos con alta atenuación, se debe optar por medidores inteligentes de conexión directa con **módem celular punto a punto (GPRS / NB-IoT)**.

### Salvedad 3: Absorción Masiva del Excedente de Medidores Trifásicos (6.339 u.)
- **Dilema Resuelto**: En la Licitación 5573 entran **70.700 medidores trifásicos netos para EPEC**, pero los planes periféricos aéreos de Capital (9% trifásicos) y el Interior (11-14%) dejaban entre 42.000 y 47.000 medidores trifásicos sin destino claro.
- **Solución Estratégica**: Planes 14 y 15 presentan **6.339 suministros comerciales trifásicos directos** (13,0% del total, concentrando el **24,2% de todos los trifásicos de la Capital**). La consideración de estos planes ofrece la vía de escape natural para absorber el stock trifásico de la licitación.

### Salvedad 4: Prerrequisito Excluyente de Cartografía GIS
- **Condición Previa**: No es posible enviar cuadrillas de catastro o relevamiento a ciegas en el Centro. La Gerencia de Planificación / Topografía GIS debe dibujar y georreferenciar primero las subestaciones transformadoras (SET) subterráneas, centros de distribución y derivaciones hacia tableros generales de edificios de propiedad horizontal.

### Salvedad 5: Sincronización Temporal con Lote CLOU E4
- **Cronograma**: El lote CLOU E4 (75.000 unidades) llega al almacén central el **16 de Diciembre de 2027**. Con el periodo de Verificación Primitiva (VP de 20 días), queda plenamente liberado a inicios de 2028.
- **Articulación**: La inclusión de los Planes 14 y 15 encaja como la continuación natural e inmediata tras finalizar los planes aéreos prioritarios (19, 6, 18, 17, 12, 8).

---

## 📂 4. Documentos Actualizados

1. **`docs/09_propuesta_despliegue_mi_2027_operativa_escenarios_contratistas.md`**:
   - Tabla 3.B actualizada: Planes 14 y 15 pasan de "Excluidos" a "CONSIDERADOS con Salvedad Subterránea".
   - Subsección 3.C incorporada con el detalle técnico de las 5 salvedades.
   - Puntos 10 y 16 reformulados ratificando la directiva.
2. **`docs/07_simulacion_epec_307k_cooperativas_97k_prioridades_interior.md`**:
   - Sección 10 incorporada con el análisis estratégico del destino de CLOU E4 y balanceo de trifásicos.
3. **`README.md` (Proyecto Despliegue AMI)**:
   - Punto 7 del Diagnóstico de Planes actualizado con la salvedad subterránea.
   - Punto 6 de la Propuesta Operativa agregado formalmente.
4. **`docs/00-Dashboard-MOC.md`**:
   - Registro en el tablero de control de la Bóveda de Agentes.

---

## 🔒 5. Trazabilidad y Backups
Se generaron copias de seguridad previas en:
- `docs/Backups/2026-10-28_143600_07_simulacion_epec_307k_cooperativas_97k_prioridades_interior.md.bak`
- `docs/Backups/2026-10-28_143600_09_propuesta_despliegue_mi_2027_operativa_escenarios_contratistas.md.bak`
- `docs/Backups/2026-10-28_143600_README_despliegue_ami.md.bak`
