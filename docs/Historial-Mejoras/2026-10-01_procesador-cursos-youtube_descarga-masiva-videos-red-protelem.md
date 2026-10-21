---
title: "Descarga Masiva y Catalogación de Videos de Cursos Académicos a Red"
agente: "07-Procesador-Cursos-YouTube"
fecha: 2026-10-01
tags: ["#cursos", "#youtube", "#videos", "#protelem", "#descarga", "#ffmpeg", "#yt-dlp"]
---

# 🎬 Registro de Automatización: Descarga Masiva de Videos a Red PROTELEM

- **Agente Responsable**: [[docs/Agentes/07-Procesador-Cursos-YouTube|Agente 07: Procesador y Documentador de Cursos Académicos YouTube]]
- **Directorio Origen**: `docs/Cursos/` (Bóveda Obsidian)
- **Directorio Destino en Red**: `\\srvfs01\ProyectoTelemedicion\13-Documentacion_Tutoriales_Videos_Instaladores\cursos_videos_diplomaturas\`
- **Script de Automatización**: [`scripts/descargar_videos_cursos.py`](file:///D:/Usuarios/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/descargar_videos_cursos.py)
- **Motor de Multiplexión**: [`scripts/ffmpeg.exe`](file:///D:/Usuarios/jidiaz/.gemini/antigravity-ide/scratch/antigravity-agents-repository/scripts/ffmpeg.exe)
- **Total Almacenado en Red**: **69 videos en formato MP4 (25.97 GB)**

---

## 📊 Inventario Final de Videos Descargados por Módulo

| Módulo / Diplomatura | Videos Descargados | Estado | Destino en Servidor |
| :--- | :---: | :---: | :--- |
| **Diplomatura en Energía Eléctrica (UTN.FRSN)** | **40 / 40** | 100% Completo | `...\cursos_videos_diplomaturas\Diplomatura-Energia-Electrica\` |
| **Transición Energética - General / Lanzamiento** | **1 / 1** | 100% Completo | `...\cursos_videos_diplomaturas\Diplomatura-Transicion-Energetica\General\` |
| **Transición Energética - Módulo 03 (Almacenamiento)** | **5 / 5** | 100% Completo | `...\cursos_videos_diplomaturas\Diplomatura-Transicion-Energetica\Modulo-03-Almacenamiento\` |
| **Transición Energética - Módulo 04 (Transporte)** | **5 / 5** | 100% Completo | `...\cursos_videos_diplomaturas\Diplomatura-Transicion-Energetica\Modulo-04-Transporte-Energetico\` |
| **Transición Energética - Módulo 05 (Regulaciones)** | **12 / 12** | 100% Publicados | `...\cursos_videos_diplomaturas\Diplomatura-Transicion-Energetica\Modulo-05-Regulaciones\` |
| **Transición Energética - Módulo 06 (Beneficios y Políticas)** | **6 / 6** | 100% Completo | `...\cursos_videos_diplomaturas\Diplomatura-Transicion-Energetica\Modulo-06-Beneficios-y-Politicas\` |
| **TOTAL CONSOLIDADO** | **69 Videos** | **25.97 GB** | **\\srvfs01\ProyectoTelemedicion\...\cursos_videos_diplomaturas\** |

*Nota: La Clase 11 del Módulo 05 (`oRODR0edcqg`) corresponde a un evento de transmisión en vivo aún no emitido públicamente por el canal SomoslaSEU.*

---

## ⚙️ Características Técnicas del Pipeline de Descarga

1. **Deduplicación Automática**: Detección unívoca por `video_id` evitando descargas redundantes.
2. **Multiplexión MP4 de Alta Fidelidad**: Fusión automática de pistas de video 1080p/720p y audio AAC/M4A en contenedor MP4 nativo mediante FFmpeg.
3. **Staging Local & Transferencia Atómica**: Descarga intermedia en SSD local (`temp_video_staging/`) para máxima velocidad y traslado seguro al recurso de red sin bloqueos SMB.
4. **Reanudación / Skip Inteligente**: Verificación de archivos previamente completados en la carpeta de destino para ejecuciones incrementales.
