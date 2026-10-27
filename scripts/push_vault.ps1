param(
    [string]$RepoPath = "D:\Proyectos\antigravity-agents-repository",
    [string]$Branch = "master",
    [string]$Passphrase = "mapache91"
)

$VaultPath = "D:\Proyectos\antigravity-agents-repository\config\token_vault.json"
if (!(Test-Path $VaultPath)) {
    Write-Host "Error: No existe el archivo de boveda $VaultPath"
    exit 1
}

$vault = Get-Content $VaultPath -Raw -Encoding UTF8 | ConvertFrom-Json
$sha = [System.Security.Cryptography.SHA256]::Create()
$key = $sha.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Passphrase))
$bytes = [Convert]::FromBase64String($vault.vault_data)
if ($bytes.Length -lt 17) {
    Write-Host "Error: Datos de boveda invalidos"
    exit 1
}

$iv = $bytes[0..15]
$encrypted = $bytes[16..($bytes.Length - 1)]
$aes = [System.Security.Cryptography.Aes]::Create()
$aes.Key = $key
$aes.IV = $iv
$decryptor = $aes.CreateDecryptor()
$decrypted = $decryptor.TransformFinalBlock($encrypted, 0, $encrypted.Length)
$token = [System.Text.Encoding]::UTF8.GetString($decrypted)

if ($token -and $token.StartsWith("ghp_")) {
    Write-Host "Token descifrado con exito. Ejecutando git push..."
    $originUrl = git -C $RepoPath remote get-url origin
    if ($originUrl -match "github\.com[/:](.+)") {
        $repoSlug = $matches[1]
        $remoteUrl = "https://" + $token + "@github.com/" + $repoSlug
        git -C $RepoPath push $remoteUrl $Branch
        if ($LASTEXITCODE -eq 0) {
            Write-Host ">>> Git push completado con EXITO en $RepoPath ($Branch)."
        } else {
            Write-Host ">>> Error en git push (Codigo $LASTEXITCODE)."
        }
    } else {
        Write-Host "Error: No se pudo determinar el slug de GitHub para $originUrl"
        exit 1
    }
} else {
    Write-Host "Error: No se pudo descifrar el token con la clave provista."
    exit 1
}
