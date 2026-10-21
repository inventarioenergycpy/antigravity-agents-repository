# Registro de Mejora: Metodología de Control, Auditoría y Zonificación Comercial de Suministros Eléctricos de Vialidad Provincial
**Fecha:** 2026-10-02  
**Agente Responsable:** 02 - Ciencia de Datos & 06 - Arquitecto de Sistemas EPEC  
**Categoría:** Auditoría Comercial / Oracle 19c XXSIGEC / SUAF / Zonificación Territorial EPEC  

---

### 1. Descripción del Requerimiento
Implementación de un protocolo estandarizado de auditoría y cruce de datos para los suministros de energía eléctrica facturados a través de SUAF y Cooperativas del Interior para la **Dirección Provincial de Vialidad (DPV)**, integrando la base de datos comercial en vivo de EPEC (`XXSIGEC` en Oracle 19c / `PRODEBS_SEE`).

### 2. Acciones Ejecutadas
1. **Conexión Directa Oracle 19c (`XXSIGEC`)**:
   - Conexión Thick Mode vía `oracledb` utilizando el cliente Oracle 19c en `C:\app\client\product\19.0.0\client_2\bin`.
   - Cruce automatizado de tablas: `SERVICIOS`, `CONTRATOS`, `PERSONAS`, `SUCURSALES`, `ZONAS`, `MEDIDORES_INSTALADOS` y `AREAS_GEOGRAFICAS`.
2. **Auditoría de Titularidad y Ente**:
   - Validación algorítmica de código de ente (`min_codigo = '02'`) y número de cliente (`prs_numero = 336080`).
   - Identificación de 28 suministros confirmados de DPV (25 en SUAF y 3 en No cargados SUAF) y 45 suministros asignados a otros entes gubernamentales.
3. **Zonificación Comercial Oficial EPEC (`zon_codigo`)**:
   - Incorporación de la letra de Zona Oficial EPEC (**A a I**) en todas las hojas del libro Excel:
     - `EPEC - SUAF` (42 suministros)
     - `EPEC - No cargados SUAF` (31 suministros)
     - `coop. vialidad` (157 filas jerárquicas con 26 cooperativas y todas las obras viales).
4. **Conservación de Atributos Críticos**:
   - Preservación completa de las columnas `NOMBRE INMUEBLE` y `Nro CLIENTE` en la hoja `coop. vialidad`.
5. **Generación de Entregables**:
   - `Cooperativas -EPEC_Auditado_Vialidad_Provincial.xlsx` actualizado en rutas `D:\Usuarios\jidiaz\Downloads\` y `C:\Users\jidiaz\Downloads\`.
   - Documento metodológico y consultas SQL replicables.

### 3. Impacto Operativo
- **Trazabilidad Total**: Cada suministro cuenta con su ID físico, número de contrato descompuesto, número de medidor activo, tarifa, sucursal EPEC y zona comercial.
- **Saneamiento Administrativo**: Base depurada para tramitar regularizaciones y altas en el sistema SUAF ante la Secretaría General y Ministerio de Finanzas.
- **Homogeneidad Tarifaria**: Agrupamiento de Cooperativas y EPEC por las 9 Zonas Comerciales de la Provincia de Córdoba.
