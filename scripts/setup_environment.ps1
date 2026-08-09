# ==============================================================================
# Script: setup_environment.ps1
# Propósito: Inicializar el entorno en un nuevo PC para Antigravity IDE y Obsidian
# ==============================================================================

Write-Host "⚙️ Configurando entorno local..." -ForegroundColor Yellow

# Configurar Git
git config --global user.name "inventarioenergycpy"
git config --global user.email "inventario.energycpy@gmail.com"

# Asegurar carpeta de Descargas
$downloadsFolder = Join-Path $env:USERPROFILE "Downloads"
if (-not (Test-Path $downloadsFolder)) {
    New-Item -ItemType Directory -Path $downloadsFolder | Out-Null
}

Write-Host "✔ Entorno configurado correctamente." -ForegroundColor Green
Write-Host "  - Usuario Git: inventarioenergycpy" -ForegroundColor Gray
Write-Host "  - Ruta Descargas: $downloadsFolder" -ForegroundColor Gray
