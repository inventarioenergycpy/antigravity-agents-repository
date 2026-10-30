# Directivas y Reglas Globales de Agentes - Antigravity IDE

## 1. Identificación y Credenciales del Entorno
- **Cuenta de GitHub Principal**: inventarioenergycpy
- **Organización de Proyectos EPEC**: PROTELEM-EPEC (https://github.com/PROTELEM-EPEC) y repositorios satélites en protelemepec-coder.
- **Correo de Contacto / Google Drive**: inventario.energycpy@gmail.com
- **Forma de Autenticación**: Registro directo asociado a la cuenta de Gmail y credenciales PAT / SSH para las organizaciones de GitHub.
---

## 2. Propósito del Repositorio y Política de Almacenamiento

### A. Repositorio Central de Agentes (`antigravity-agents-repository`)
- **Regla Estricta**: Este repositorio está destinado **100% exclusivamente a la documentación de agentes, habilidades (`.agents/skills/`), reglas globales (`.agents/AGENTS.md`), respaldos (`docs/Backups/`) y la Bóveda de Obsidian (`docs/`)**.
- No debe contener código fuente final ni prototipos pesados de proyectos individuales.

### B. Informes y Documentos de Google Workspace
- **Regla**: Todos los informes, análisis financieros, presentaciones ejecutivas y planillas creadas en Google Workspace (Docs, Slides, Sheets) se almacenan en el **Google Drive** de `inventario.energycpy@gmail.com`.

### C. Entregables Locales de Trabajo Directo
- **Regla**: Entregables temporales, scripts de un solo uso o borradores de Power BI Project (`.pbip`) se depositan en la carpeta local de **Descargas del Sistema** (`%USERPROFILE%\Downloads`).

---

## 3. Creación de Nuevos Perfiles de Agentes Futuros

Para incorporar un nuevo perfil de agente al repositorio:
1. Crear el directorio de la habilidad en `.agents/skills/<nombre-nuevo-agente>/SKILL.md` con su YAML frontmatter y pautas operativas.
2. Crear la ficha técnica legible en Obsidian dentro de `docs/Agentes/<Nombre-Nuevo-Agente>.md`.
3. Actualizar el tablero principal `docs/00-Dashboard-MOC.md` agregando el nuevo agente al diagrama Mermaid y a la lista relacional.

---

## 4. Protocolo Obligatorio de Backup, Histórico y Rollback

Cuando el usuario apruebe o solicite guardar una mejora (ej. *"guarda esta mejora"*, *"actualiza este agente"*), se activará el siguiente protocolo estricto:

### Paso 1: Backup Preventivo (Rollback Protection)
- **ANTES** de aplicar cualquier cambio en `SKILL.md`, crear una copia exacta de respaldo de la versión actual en la carpeta:
  - `docs/Backups/YYYY-MM-DD_HHmmss_<nombre-agente>_SKILL.md.bak`

### Paso 2: Aplicación del Cambio
- Actualizar `.agents/skills/<nombre-agente>/SKILL.md` incorporando la nueva pauta o corrección.

### Paso 3: Registro Histórico en Obsidian
- Crear una entrada detallada de la mejora en `docs/Historial-Mejoras/YYYY-MM-DD_<nombre-agente>_<descripcion>.md` especificando contexto, regla agregada, impacto y enlace al archivo de backup creado.

### Paso 4: Reversión / Rollback (En caso de requerirse)
- Si el usuario solicita revertir un cambio (ej. *"haz un rollback al agente"*, *"restaura la versión anterior de este agente"*), invocar la habilidad `.agents/skills/rollback-agente/SKILL.md` para restaurar desde `docs/Backups/` el archivo `.bak` seleccionado.

---

## 5. Integración y Sincronización con la Bóveda de Obsidian

- La raíz del repositorio actúa como Bóveda de Obsidian (Opción A).
- Toda documentación creada o modificada debe incluir metadatos YAML frontmatter y enlaces relacionales (`[[00-Dashboard-MOC]]`, `[[docs/Backups/]]`, `[[docs/Proyectos/]]`, `[[docs/Cursos/00-Indice-General-Cursos]]`, etc.).
- **Protocolo Oficial de Sincronización**: La bóveda cuenta con el plugin nativo `obsidian-git` pre-configurado para ejecutar auto-pull al arranque y auto-push cada 10 minutos contra `origin/master`. Ver guía completa y parámetros en [`docs/Protocolo-Sincronizacion-Obsidian-GitHub.md`](file:///C:/Users/Usuario/.gemini/antigravity-ide/scratch/antigravity-agents-repository/docs/Protocolo-Sincronizacion-Obsidian-GitHub.md).

---

## 6. Protocolo Multi-Repositorio: Creación de Repositorios Dedicados por Proyecto

Cada vez que un agente desarrolle un nuevo proyecto (página web showroom, aplicación de análisis de datos, modelo financiero dinámico u otro sistema) cuya naturaleza sea distinta a los anteriores:

1. **Parametrización del Nuevo Repositorio**:
   - Inicializar una nueva carpeta local independiente (ej. D:\Proyectos\<nombre-proyecto> o en el scratchpad del disco activo).
   - Crear y vincular el repositorio remoto en GitHub bajo la organización que corresponda:
     - https://github.com/inventarioenergycpy/<nombre-proyecto-kebab-case>.git (Proyectos generales, financieros, showrooms y ciencia de datos).
     - https://github.com/PROTELEM-EPEC/<nombre-proyecto-kebab-case>.git o protelemepec-coder (Proyectos específicos de EPEC, Facturación SIGEC, Dashboards Comerciales y Telemedición).

2. **Estructura Interna del Repositorio de Proyecto**:
   - `README.md`: Descripción ejecutiva del proyecto, objetivos y enlace a su despliegue (ej. GitHub Pages).
   - `docs/`: Documentación técnica puntual del proyecto y notas de arquitectura.
   - `src/` o raíz del proyecto: Código fuente ejecutable, componentes e interfaz.
   - `assets/`: Recursos gráficos e imágenes URL-safe.

3. **Registro Cruzado en la Bóveda Central (`antigravity-agents-repository`)**:
   - Crear una nota de registro en `docs/Proyectos/YYYY-MM-DD_<nombre-proyecto>.md` especificando:
     - Nombre del proyecto y objetivo.
     - Agente responsable del desarrollo.
     - Enlace al repositorio de GitHub creado (`https://github.com/inventarioenergycpy/<nombre-proyecto>`).
     - Enlace al despliegue o demo activa.
   - Actualizar el índice general en `docs/00-Dashboard-MOC.md` en la sección `[[Proyectos/|Proyectos Desarrollados]]`.

---

## 7. Protocolo de Acceso Concurrente a Entornos de Red (UNC / `\\srvfs01`) y Recursos Online: Snapshot Local de Mínima Interferencia

### A. Principio Rector de Concurrencia Compartida
En las carpetas de red compartidas (UNC como `\\srvfs01\ProyectoTelemedicion`, carpetas de facturación `Control_de_Gestion\DEPARTAMENTO FACTURACION`, etc.) u orígenes online, los archivos (Excel `.xlsx`/`.xls`, proyectos Power BI `.pbip`, videos MP4 de cátedra, etc.) son utilizados concurrentemente por múltiples trabajadores. 

**REGLA ESTRICTA**: Queda terminantemente prohibido abrir, parsear o procesar archivos directamente sobre la ruta de red durante tiempos prolongados (Pandas, OpenCV `cv2.VideoCapture`, DuckDB, PySpark o scripts analíticos). Retener el *file handle* sobre el servidor SMB genera bloqueos de uso compartido (`Sharing Violation` / Código 32) que impiden a otros usuarios abrir o guardar sus planillas en Excel.

### B. Procedimiento Operativo Obligatorio (Pipeline de Snapshot Local)
Cada vez que una acción operativa o una habilidad requiera consultar un archivo de red u online:

1. **Localización Inmediata y Mínima Interferencia**:
   - Localizar el archivo de red e iniciar de forma inmediata su snapshot local hacia la carpeta:  
     `data/network_cache/<nombre-origen>/<subcarpetas>/<archivo>` (excluida del control de versiones en `.gitignore`).
2. **Caché Inteligente (Delta Cache)**:
   - Comparar previamente tamaño (`st_size`) y fecha/hora de modificación (`st_mtime`).
   - Si el archivo ya existe localmente y no ha cambiado en la red, **reutilizar de inmediato la copia local** (tiempo de interferencia de red = **0 milisegundos**).
3. **Copia en Streaming No Bloqueante**:
   - Si el archivo es nuevo o fue modificado en la red, transferir una copia binaria en bloques (buffer de 4 MB a 8 MB) preservando atributos de fecha con `shutil.copystat` / `os.utime`.
   - **Liberar y cerrar el handle de red en milisegundos** tan pronto finaliza la copia, dejando el recurso 100% disponible para el resto del personal.
4. **Procesamiento Exclusivamente Local**:
   - Todo análisis tabular, extracción de texto, cómputo estadístico o visión artificial de cuadros debe ejecutarse **única y exclusivamente sobre la copia local** en `data/network_cache/`.
5. **Estrictamente Solo Lectura (Snapshot de Análisis)**:
   - Los agentes jamás deben escribir, sobrescribir ni modificar directamente el archivo original en la red compartida, garantizando la indemnidad total de los datos corporativos.
6. **Módulo de Soporte Oficial**:
   - Emplear la utilidad estándar [`scripts/network_snapshot.py`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/network_snapshot.py) invocando `get_local_snapshot(remote_path)`.

---

## 8. Protocolo de Consultas Seguras a Bases de Datos (Oracle y Motores Relacionales/NoSQL): Pacing, Retardos Obligatorios (Throttling) y Protección contra Sobrecarga

### A. Principio Rector de No-Saturación de Servidores de Base de Datos
En entornos corporativos y de producción (como el cluster Oracle RAC `epec2-scan2.epec.net / PRODEBS_SEE`, esquemas `XXSIGEC`, o cualquier motor SQL/NoSQL corporativo), las bases de datos atienden transacciones en tiempo real de facturación, usuarios comerciales y cuadrillas de terreno.

**REGLA ESTRICTA**: Queda terminantemente prohibido disparar ráfagas continuas de consultas en bucle (*hammering* / *loop flooding*), queries masivas sin paginar o barridos no particionados sin retardo.

### B. Retardo Preventivo Inter-Consulta Obligatorio (Pacing / Throttle Delay)
Toda ejecución de consultas iterativas, por lotes o en bucles sobre bases de datos DEBE incorporar obligatoriamente una pausa controlada entre cada consulta individual o bloque:
1. **Rango Operativo Estandarizado**: Mínimo **300 ms a 1.000 ms** (0,3 s a 1,0 s) de retardo entre lotes / queries en scripts Python (`time.sleep(0.5)` o equivalente en otros lenguajes).
2. **Consultas Masivas / Lotes Grandes**: Si cada consulta extrae $\ge 500$ registros o involucra joins pesados (ej. `DOCUMENTOS`, `ITEMS`, `AUDITORIA_CAMMESA`), elevar el retardo a **1.000 ms - 2.000 ms** (1 s - 2 s) entre chunks para permitir al motor de base de datos desocupar buffers y CPU.

### C. Estrategia de Loteado Óptimo (Chunking Controlado $\le 500$ - $900$ elementos)
1. Particionar siempre cláusulas `IN (...)` en lotes de tamaño máximo recomendado de **500 a 900 elementos** (evita la limitación `ORA-01795` de Oracle y reduce el número total de llamadas a la base de datos).
2. Aplicar el retardo de pacing al finalizar cada lote antes de abrir la siguiente solicitud.

### D. Aislamiento Transaccional y Modo Solo Lectura
1. Abrir la sesión inmediatamente con `cur.execute("SET TRANSACTION READ ONLY")` (o equivalente en el motor correspondiente) para garantizar snapshot isolation determinista y evitar bloqueos en tablas transaccionales.
2. Cerrar explícitamente cursores y conexiones en bloques `finally:` o context managers `with conn:` al terminar la extracción, liberando recursos del pool de conexiones.

### E. Backoff Exponencial y Detección de Fricción
Si se detecta lentitud inusual en la respuesta, bloqueos temporales o advertencias de contención (`ORA-01013`, timeouts de socket, latencia $\ge 2.000$ ms), el agente debe aplicar backoff exponencial duplicando el retardo (ej. $0,5\text{s} \to 1\text{s} \to 2\text{s} \to 4\text{s}$) e informar al usuario antes de reintentar.
