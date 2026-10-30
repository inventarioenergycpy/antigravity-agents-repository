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
        
        git pull --rebase origin master
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

function Show-SquadInfo {
    Write-Host "`n🤖 ARQUITECTURA MULTI-AGENTE ADAPTATIVA (SQUAD DE 4 AGENTES - TOP-2 GEMINI)" -ForegroundColor Yellow
    Write-Host " ----------------------------------------------------------------------" -ForegroundColor Gray
    Write-Host " • Fase 0 (Armado)      : Evalúa modelos Gemini en config. más alta (Mejor a Peor)" -ForegroundColor Magenta
    Write-Host " • Project Manager (PM) : Top-1 Gemini disponible (Clarificación, WBS & Arbitraje)" -ForegroundColor White
    Write-Host " • Operador 1 (Core)    : Top-2 Gemini disponible (Algoritmos / Datos / Código)" -ForegroundColor Cyan
    Write-Host " • Operador 2 (Dominio) : Top-2 Gemini disponible (Normativa EPEC / SIGEC / Legal)" -ForegroundColor Cyan
    Write-Host " • Operador 3 (QA & UX) : Top-2 Gemini disponible (Validación, Tests & Replicabilidad)" -ForegroundColor Cyan
    Write-Host " • Protocolo de Validación: TRIPLE QA (Técnico -> Dominio -> UX/Replicabilidad)" -ForegroundColor Green
    Write-Host " • Protocolo Rector     : docs/Protocolo-Arquitectura-Multi-Agente-PM-Operadores.md" -ForegroundColor Gray
    Write-Host " ----------------------------------------------------------------------" -ForegroundColor Gray
    Write-Host " 12 Agentes Especialistas disponibles en .agents/skills/ y docs/Agentes/" -ForegroundColor Yellow
}

function Copy-PromptInicio {
    Write-Host "`n📋 Copiando Prompt Maestro de Inicio Rápido al Portapapeles..." -ForegroundColor Yellow
    $promptFile = Join-Path $PSScriptRoot "..\PROMPT_INICIO_RAPIDO.md"
    if (Test-Path $promptFile) {
        $content = Get-Content $promptFile -Raw
        # Extraer el bloque de código
        if ($content -match '(?s)```text\r?\n(.*?)\r?\n```') {
            $promptText = $matches[1]
            Set-Clipboard -Value $promptText
            Write-Host "  ✔ ¡Prompt copiado con éxito al Portapapeles! Listo para pegar en Antigravity IDE." -ForegroundColor Green
        } else {
            Set-Clipboard -Value $content
            Write-Host "  ✔ Archivo copiado al Portapapeles." -ForegroundColor Green
        }
    } else {
        Write-Host "  ⚠️ No se encontró el archivo PROMPT_INICIO_RAPIDO.md." -ForegroundColor Red
    }
}

do {
    Show-Header
    Write-Host "Seleccione una opción:" -ForegroundColor White
    Write-Host " 1. Verificar sesión Git y Credenciales" -ForegroundColor Cyan
    Write-Host " 2. Sincronizar Repositorio (Pull/Push desde GitHub)" -ForegroundColor Cyan
    Write-Host " 3. Verificar Entorno Local y Ruta de Descargas" -ForegroundColor Cyan
    Write-Host " 4. Inicializar Entorno Completo (setup_environment.ps1)" -ForegroundColor Cyan
    Write-Host " 5. Ver Arquitectura Multi-Agente Squad de 4 y Roles (Top-2 Gemini)" -ForegroundColor Cyan
    Write-Host " 6. Copiar Prompt Maestro de Inicio Rápido al Portapapeles" -ForegroundColor Cyan
    Write-Host " 0. Salir" -ForegroundColor Red
    Write-Host ""
    $choice = Read-Host "Opción [0-6]"

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
        "5" {
            Show-SquadInfo
            Pause
        }
        "6" {
            Copy-PromptInicio
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
