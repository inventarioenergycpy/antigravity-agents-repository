# ==============================================================================
# Script: start.ps1
# Propósito: Menú Interactivo CLI para configuración y conexión Multi-PC
# Repositorio: inventarioenergycpy / inventario.energycpy@gmail.com
# ==============================================================================

function Show-Header {
    Clear-Host
    Write-Host "======================================================================" -ForegroundColor Cyan
    Write-Host " 🚀 MENÚ DE INICIO MULTI-PC - REPOSITORIO DE AGENTES (ANTIGRAVITY IDE)" -ForegroundColor Yellow
    Write-Host "======================================================================" -ForegroundColor Cyan
    Write-Host " Cuenta GitHub : inventarioenergycpy" -ForegroundColor Green
    Write-Host " Email Contacto: inventario.energycpy@gmail.com" -ForegroundColor Green
    Write-Host " Local Path    : $PSScriptRoot\.." -ForegroundColor Gray
    Write-Host "======================================================================" -ForegroundColor Cyan
    Write-Host ""
}

function Check-GitConfig {
    Write-Host "🔍 Verificando configuración de Git..." -ForegroundColor Yellow
    $gitUser = git config user.name
    $gitEmail = git config user.email

    if ([string]::IsNullOrEmpty($gitUser)) {
        Write-Host "  ➜ Estableciendo usuario Git: inventarioenergycpy" -ForegroundColor Gray
        git config user.name "inventarioenergycpy"
    } else {
        Write-Host "  ✔ Usuario Git: $gitUser" -ForegroundColor Green
    }

    if ([string]::IsNullOrEmpty($gitEmail)) {
        Write-Host "  ➜ Estableciendo email Git: inventario.energycpy@gmail.com" -ForegroundColor Gray
        git config user.email "inventario.energycpy@gmail.com"
    } else {
        Write-Host "  ✔ Email Git  : $gitEmail" -ForegroundColor Green
    }
}

function Sync-Repository {
    Write-Host "`n🔄 Sincronizando repositorio con GitHub..." -ForegroundColor Yellow
    try {
        git fetch origin
        $status = git status -sb
        Write-Host "Estado local: $status" -ForegroundColor Gray
        
        git pull --rebase origin main
        Write-Host "✔ Sincronización completada con éxito." -ForegroundColor Green
    } catch {
        Write-Host "⚠️ Ocurrió una advertencia durante la sincronización: $_" -ForegroundColor Red
    }
}

function Check-DownloadsPath {
    Write-Host "`n📁 Verificando carpeta local de Descargas..." -ForegroundColor Yellow
    $downloadsPath = Join-Path $env:USERPROFILE "Downloads"
    if (Test-Path $downloadsPath) {
        Write-Host "  ✔ Carpeta de Descargas detectada: $downloadsPath" -ForegroundColor Green
    } else {
        Write-Host "  ⚠️ No se encontró la carpeta predeterminada de Descargas." -ForegroundColor Red
    }
}

do {
    Show-Header
    Write-Host "Seleccione una opción:" -ForegroundColor White
    Write-Host " 1. Verificar sesión Git y Credenciales" -ForegroundColor Cyan
    Write-Host " 2. Sincronizar Repositorio (Pull/Push desde GitHub)" -ForegroundColor Cyan
    Write-Host " 3. Verificar Entorno Local y Ruta de Descargas" -ForegroundColor Cyan
    Write-Host " 4. Inicializar Entorno Completo (setup_environment.ps1)" -ForegroundColor Cyan
    Write-Host " 0. Salir" -ForegroundColor Red
    Write-Host ""
    $choice = Read-Host "Opción [0-4]"

    switch ($choice) {
        "1" {
            Check-GitConfig
            Pause
        }
        "2" {
            Sync-Repository
            Pause
        }
        "3" {
            Check-DownloadsPath
            Pause
        }
        "4" {
            & "$PSScriptRoot\setup_environment.ps1"
            Pause
        }
        "0" {
            Write-Host "`n¡Hasta luego! Entorno de agentes listo." -ForegroundColor Green
        }
        default {
            Write-Host "Opción no válida. Intente de nuevo." -ForegroundColor Red
            Start-Sleep -Seconds 1
        }
    }
} while ($choice -ne "0")
