---
title: "Configuración Segura de Credenciales y Bóveda Cifrada GitHub PAT"
tags:
  - #credenciales
  - #seguridad
  - #github-pat
  - #despliegue
  - #boveda-segura
created: 2026-08-23
actualizado: 2026-08-27
---

# 🔐 Configuración Segura de Credenciales y Bóveda Cifrada GitHub

Este documento describe el protocolo de resguardo, cifrado y desbloqueo seguro de las credenciales de GitHub para la automatización de despliegues, creación de repositorios y sincronización de cambios en la cuenta `inventarioenergycpy`.

---

## 📌 Datos de la Bóveda de Seguridad Activa

- **Usuario GitHub**: `inventarioenergycpy`
- **Correo Oficial**: `inventario.energycpy@gmail.com`
- **Tipo de Credencial**: Personal Access Token Clásico (PAT) con permisos `repo` y `workflow`.
- **Mecanismo de Resguardo**: Bóveda cifrada en estándar AES-256 (`config/token_vault.json`).
- **Clave Maestra de Desbloqueo**: `mapache91`
- **Límite de Intentos de Seguridad**: **5 intentos consecutivos**.

---

## 🛡️ Reglas y Protocolo de Ejecución

### 1. Desbloqueo Obligatorio por Clave Maestra
* **Solo se puede utilizar el token para aplicar cambios, sincronizar o desplegar en GitHub si se introduce la clave de seguridad:** `mapache91`.
* El token no reside en texto plano en repositorios públicos; se almacena cifrado con AES-256 en `config/token_vault.json`.
* Los scripts automatizados ([`desplegar_todo.bat`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/dashboard-gestion-intermediacion/desplegar_todo.bat), [`publish.bat`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/dashboard-gestion-intermediacion/publish.bat) y [`scripts/vault_manager.ps1`](file:///C:/Users/jidiaz/.gemini/antigravity-ide/scratch/dashboard-gestion-intermediacion/scripts/vault_manager.ps1)) solicitan la clave interactiva antes de proceder.

### 2. Sistema de 5 Intentos de Seguridad
1. El usuario dispone de **hasta 5 intentos** para ingresar la clave correcta.
2. Tras cada intento fallido, el sistema muestra una advertencia con la cantidad de intentos restantes.
3. Si la clave ingresada es correcta, el token se descifra en memoria y la subida/despliegue a GitHub se ejecuta con éxito.

### 3. Protocolo de Bloqueo y Contingencia (Si se agotan los 5 intentos)
Si se ingresa una clave incorrecta 5 veces consecutivas:
1. La ejecución se cancela y se bloquea inmediatamente por seguridad.
2. El sistema muestra y abre automáticamente el enlace oficial para generar un nuevo token en GitHub:  
   👉 **[Generar Nuevo Token Clásico en GitHub (Pre-configurado con permisos repo/workflow)](https://github.com/settings/tokens/new?description=Antigravity+Deploy&scopes=repo,workflow)**
3. **Pasos para reanudar:**
   - Hacer clic en **"Generate token"** en la página abierta de GitHub.
   - Copiar el nuevo código (`ghp_...`).
   - Pegarlo directamente en el chat de **Antigravity** para que el asistente reconfigure la bóveda segura con la clave `mapache91` y reanude los despliegues.

---

## 📂 Archivos del Sistema de Bóveda
- `config/token_vault.json`: Archivo de bóveda con carga útil cifrada en AES-256.
- `scripts/vault_manager.ps1`: Motor de cifrado, descifrado, conteo de intentos y enlace de recuperación.
- `desplegar_todo.bat` / `publish.bat`: Scripts de un clic con integración de desbloqueo seguro.
