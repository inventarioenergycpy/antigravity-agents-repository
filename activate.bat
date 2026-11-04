@echo off
set "VENV_ACTIVATE=%~dp0.venv\Scripts\activate.bat"
if exist "%VENV_ACTIVATE%" (
    call "%VENV_ACTIVATE%"
    echo [OK] Entorno virtual .venv activado con exito.
) else (
    echo [ERROR] No se encontro el entorno virtual en %VENV_ACTIVATE%
)

