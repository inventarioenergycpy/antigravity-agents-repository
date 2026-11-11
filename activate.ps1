# Script de activación rápida del entorno virtual .venv y toolchain
$nodeDir = "C:\Users\jidiaz\AppData\Local\Programs\nodejs"
if ((Test-Path $nodeDir) -and ($env:Path -notlike "*$nodeDir*")) {
    $env:Path = "$nodeDir;$env:Path"
}

if (-not $env:PROJ_DATA -and (Test-Path "C:\Program Files\QGIS 4.2.0\share\proj")) {
    $env:PROJ_DATA = "C:\Program Files\QGIS 4.2.0\share\proj"
    $env:PROJ_LIB = "C:\Program Files\QGIS 4.2.0\share\proj"
}

$venvActivate = Join-Path $PSScriptRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
    & $venvActivate
    Write-Host "✅ Entorno virtual .venv activado con éxito en Antigravity IDE." -ForegroundColor Green
    Write-Host "Python: $((Get-Command python).Source)" -ForegroundColor Cyan
    if (Get-Command node -ErrorAction SilentlyContinue) {
        Write-Host "Node: $(node -v) | npm: $(npm -v)" -ForegroundColor Yellow
    }
} else {
    Write-Warning "No se encontró el entorno virtual en $venvActivate"
}


