@echo off
set "NODE_DIR=C:\Users\jidiaz\AppData\Local\Programs\nodejs"
if exist "%NODE_DIR%" (
    set "PATH=%NODE_DIR%;%PATH%"
)
if not defined PROJ_DATA (
    if exist "C:\Program Files\QGIS 4.2.0\share\proj" (
        set "PROJ_DATA=C:\Program Files\QGIS 4.2.0\share\proj"
        set "PROJ_LIB=C:\Program Files\QGIS 4.2.0\share\proj"
    )
)
set "VENV_ACTIVATE=%~dp0.venv\Scripts\activate.bat"
if exist "%VENV_ACTIVATE%" (
    call "%VENV_ACTIVATE%"
    echo [OK] Entorno virtual .venv activado con exito.
) else (
    echo [ERROR] No se encontro el entorno virtual en %VENV_ACTIVATE%
)


