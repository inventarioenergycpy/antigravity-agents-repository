---
fecha: 2026-08-12
agente: desarrollador-web-showroom
tipo_mejora: Buenas Prácticas Oficiales de GitHub & Almacenamiento Híbrido
backup_asociado: "[[docs/Backups/2026-08-12_004050_desarrollador-web-showroom_SKILL.md.bak]]"
---

# 🚀 Registro de Mejora Continua: Incorporación de Buenas Prácticas de GitHub para Desarrollo Web

## 📋 Contexto de la Mejora
A solicitud del usuario, se actualizó la definición operativa del agente **Desarrollador Web Showroom** para incorporar explícitamente las **buenas prácticas recomendadas por GitHub** en el desarrollo, optimización de activos multimedia, gestión de cuotas de almacenamiento y despliegue continuo en GitHub Pages.

---

## ⚙️ Reglas y Pautas Oficiales de GitHub Incorporadas al Agente

1. **Gestión Estricta de Cuotas de Almacenamiento**:
   - Monitorear que el tamaño total del repositorio se mantenga muy por debajo de **1 GB** (límite recomendado) y ningún archivo supere **100 MB** (límite máximo estricto por archivo en GitHub).

2. **Estrategia de Almacenamiento Híbrido (GitHub + Google Drive)**:
   - **Activos Livianos (`< 25 MB`)**: Código HTML/CSS/JS, imágenes de diapositivas optimizadas a 150 DPI y PDFs livianos alojados en el repositorio (`showroom-web/assets/`).
   - **Activos Pesados (`> 25 MB`)**: Videos corporativos 4K/HD, modelos 3D o PDFs voluminosos alojados en la cuenta oficial de **Google Drive** (`inventario.energycpy@gmail.com`) e integrados mediante enlaces directos en el showroom.

3. **Nombrado de Archivos URL-Safe**:
   - Obligatoriedad de nombrar todos los archivos y carpetas sin espacios dobles, tildes ni caracteres especiales (`snake_case` o `kebab-case`) para prevenir errores de codificación HTTP/404 en navegadores móviles.

4. **Compatibilidad Dual de URL para GitHub Pages**:
   - Mantenimiento de un archivo `index.html` en la raíz del repositorio con redirección semántica instantánea a `showroom-web/` para garantizar la funcionalidad tanto en la raíz como en subcarpetas.

5. **Validación Pre-Deployment mediante Suite Automatizada**:
   - Verificación obligatoria de responsividad móvil/PC (17 pruebas) y presencia de activos antes de realizar `git push origin master`.

---

## 📈 Impacto en el Sistema
- **Eficiencia**: Optimización constante del consumo de ancho de banda y cuota de disco en GitHub Pages.
- **Seguridad**: Respaldo preventivo guardado en `[[docs/Backups/2026-08-12_004050_desarrollador-web-showroom_SKILL.md.bak]]`.
- **Escalabilidad**: Garantiza que el Showroom pueda crecer para albergar decenas de futuros proyectos de inversión sin superar nunca los límites de GitHub.

---
*Enlace relacional: [[00-Dashboard-MOC]]*
