# Script de activación rápida del entorno virtual .venv
$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    & $venvActivate
    Write-Host "✅ Entorno virtual .venv activado con éxito en Antigravity IDE." -ForegroundColor Green
    Write-Host "Python: $((Get-Command python).Source)" -ForegroundColor Cyan
} else {
    Write-Warning "No se encontró el entorno virtual en $venvActivate"
}

