---
title: "Configuración Segura de Credenciales y GitHub PAT"
tags:
  - #credenciales
  - #seguridad
  - #github-pat
  - #despliegue
created: 2026-08-23
---

# 🔐 Configuración de Credenciales y Autenticación GitHub

Este documento describe el protocolo y almacenamiento seguro de las credenciales de GitHub para la automatización de despliegues, creación de repositorios y sincronización en la cuenta `inventarioenergycpy`.

---

## 📌 Datos de Configuración Activa

- **Usuario GitHub**: `inventarioenergycpy`
- **Correo Electrónico**: `inventario.energycpy@gmail.com`
- **Tipo de Credencial**: Personal Access Token Clásico (PAT) con permisos `repo` y `workflow`.
- **Ubicaciones de Almacenamiento Local (Protegidas por `.gitignore`)**:
  - `~/.env` (Directorio raíz del usuario `%USERPROFILE%\.env`)
  - `antigravity-agents-repository/.env`
  - `dashboard-gestion-intermediacion/.env`
  - **Windows Credential Manager / Git Credential Manager**: Aprobado y almacenado de forma persistente para operaciones de Git en consola y scripts.

---

## 🛡️ Reglas Estrictas de Seguridad

1. **Nunca versionar Tokens en Git**:
   - Todo archivo `.env`, `.key`, `.pem` o token está explícitamente ignorado en `.gitignore`.
2. **Carga Automática en Scripts**:
   - Los scripts y asistentes cargan las variables `GITHUB_USER` y `GITHUB_TOKEN` directamente desde las variables de entorno o desde `%USERPROFILE%\.env`.
3. **Flujo de Despliegues**:
   - Las operaciones de creación remota y subida se ejecutan sin prompts interactivos gracias a la persistencia en el Administrador de Credenciales de Windows.
