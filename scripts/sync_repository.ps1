# ==============================================================================
# Script: sync_repository.ps1
# Propósito: Sincronizar automáticamente la Bóveda de Obsidian y Skills con GitHub
# ==============================================================================

Write-Host "🔄 Iniciando sincronización bidireccional..." -ForegroundColor Yellow

$repoPath = Resolve-Path "$PSScriptRoot\.."
Set-Location $repoPath

# Pull cambios remotos
Write-Host "📥 Descargando cambios remotos (git pull)..." -ForegroundColor Cyan
git pull origin master --rebase

# Ver cambios locales
$status = git status --porcelain
if ($status) {
    Write-Host "📦 Se detectaron cambios locales en habilidades u Obsidian:" -ForegroundColor Yellow
    Write-Host $status -ForegroundColor Gray
    
    $commitMsg = "auto-sync: Actualización de habilidades e historial Obsidian ($(Get-Date -Format 'yyyy-MM-dd HH:mm'))"
    git add .
    git commit -m $commitMsg
    
    Write-Host "📤 Enviando cambios a GitHub (git push)..." -ForegroundColor Cyan
    git push origin master
    Write-Host "✔ Repositorio sincronizado exitosamente." -ForegroundColor Green
} else {
    Write-Host "✔ No hay cambios locales pendientes de subir." -ForegroundColor Green
}
